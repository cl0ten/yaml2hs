# yaml2hs

**yaml2hs** is a small Python utility to convert base64-encoded hidden service keys (from [`mkp224o`](https://github.com/cl0ten/mkp224o) YAML output) into anon or tor compatible `hs_ed25519_public_key` and `hs_ed25519_secret_key` files.

Useful for `.anon` and `.onion` hidden services.

---
## Installation

No installation needed. 
(Requires **Python 3**)


Clone the repository
```bash
git clone https://github.com/cl0ten/yaml2hs.git
```

Enter the yaml2hs directory
```bash
cd yaml2hs
```

## Usage

### Interactive mode

```bash
python3 yaml2hs.py --interactive
```
Prompts for base64 keys from YAML and writes them to the `./keys` directory.

### Direct input

```bash
python3 yaml2hs.py -p "<base64_public_key>" -s "<base64_secret_key>" -o output_dir
```

### Command options

```
  -i, --interactive           Prompt for keys interactively
  -p, --public KEY            Base64-encoded hs_ed25519_public_key
  -s, --secret KEY            Base64-encoded hs_ed25519_secret_key
  -o, --output DIR            Output directory (default: ./keys)
  -q, --quiet                 Suppress success messages
  -v, --version               Show script version
  -h, --help                  Show this help message and exit
```

## Example YAML from `mkp224o`
```
---
hostname: clotencxpheajcfrsfc44███████████████████████████████████.anon
hs_ed25519_public_key: PT0gZWQyNTUxOXYxLXB1YmxpYzogdHlwZTAgPT0AAAAL...==
hs_ed25519_secret_key: PT0gZWQyNTUxOXYxLXNlY3JldDogdHlwZTAgPT0AAAAo...==
```
Use the `public_key` and `secret_key` fields from the `mkp224o` tool in this script.

## Output

The script creates two files:
* hs_ed25519_public_key
* hs_ed25519_secret_key

Place them in the appropriate hidden service directory (For example `/var/lib/tor/hidden_service/` or `/var/lib/anon/hidden_service/`) and restart the service to generate a `hostname` file containing your address.
