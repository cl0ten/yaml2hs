import base64

# replace with keys from mkp224o yaml output 
# (example: mkp224o test -n 1 -v -y)
pub_b64 = "<yaml_ed25519_public_key>"
sec_b64 = "<yaml_ed25519_secret_key>"

# base64 decode and write files
pub_bytes = base64.b64decode(pub_b64)
sec_bytes = base64.b64decode(sec_b64)

with open("hs_ed25519_public_key", "wb") as f:
    f.write(pub_bytes)

with open("hs_ed25519_secret_key", "wb") as f:
    f.write(sec_bytes)

print("Key files written: hs_ed25519_public_key, hs_ed25519_secret_key")
