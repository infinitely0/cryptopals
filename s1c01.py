import base64


def hex_to_base64(hex_string):
    b16 = bytes.fromhex(hex_string)
    b64 = base64.b64encode(b16)

    return b64


if __name__ == "__main__":
    hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206" \
                 "120706f69736f6e6f7573206d757368726f6f6d"

    b64 = hex_to_base64(hex_string)
    assert b64.decode() == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29" \
                           "ub3VzIG11c2hyb29t"

    b64_string = base64.b64decode(b64)
    print(b64_string.decode())
