#!/usr/bin/env python3

import base64
import argparse
import os
import sys

VERSION = "1.1.0"

def print_help():
    print(f"""
yaml2hs v{VERSION} - Convert base64 YAML keys to hidden service key files

Usage:
  yaml2hs.py [OPTIONS]

Options:
  -i, --interactive           Prompt for keys interactively
  -p, --public KEY            Base64-encoded hs_ed25519_public_key
  -s, --secret KEY            Base64-encoded hs_ed25519_secret_key
  -o, --output DIR            Output directory (default: ./keys)
  -q, --quiet                 Suppress success messages
  -v, --version               Show script version
  -h, --help                  Show this help message and exit

Examples:
  yaml2hs.py --interactive
  yaml2hs.py -p "<pub>" -s "<sec>" -o mykeys
""")

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-i", "--interactive", action="store_true")
    parser.add_argument("-p", "--public")
    parser.add_argument("-s", "--secret")
    parser.add_argument("-o", "--output", default="keys")
    parser.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("-v", "--version", action="store_true")
    parser.add_argument("-h", "--help", action="store_true")
    args = parser.parse_args()

    if args.help:
        print_help()
        sys.exit(0)

    if args.version:
        print(f"yaml2hs version {VERSION}")
        sys.exit(0)

    if not args.interactive and not (args.public and args.secret):
        print_help()
        sys.exit(1)

    if args.interactive:
        print("\n=== Hidden Service Key Import (interactive mode) ===\n")
        pub_b64 = input("Enter the base64-encoded hs_ed25519_public_key:\n> ").strip()
        sec_b64 = input("\nEnter the base64-encoded hs_ed25519_secret_key:\n> ").strip()
    else:
        pub_b64 = args.public.strip()
        sec_b64 = args.secret.strip()

    try:
        pub_bytes = base64.b64decode(pub_b64)
        sec_bytes = base64.b64decode(sec_b64)
    except base64.binascii.Error as e:
        print(f"\nError decoding base64: {e}")
        sys.exit(1)

    os.makedirs(args.output, exist_ok=True)
    pub_path = os.path.join(args.output, "hs_ed25519_public_key")
    sec_path = os.path.join(args.output, "hs_ed25519_secret_key")

    with open(pub_path, "wb") as f:
        f.write(pub_bytes)
    with open(sec_path, "wb") as f:
        f.write(sec_bytes)

    if not args.quiet:
        print(f"\nKey files written to: {args.output}/")

if __name__ == "__main__":
    main()
