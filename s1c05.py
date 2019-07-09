def repeating_key_xor(block, key):
    xor = []
    for idx, c in enumerate(block):
        xor.append(c ^ key.encode()[idx % len(key)])

    return bytes(xor)


if __name__ == "__main__":
    plaintext = "Burning 'em, if you ain't quick and nimble" \
                "I go crazy when I hear a cymbal"

    key = "ICE"

    xor = repeating_key_xor(plaintext.encode(), key)

    assert xor.hex() == "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d" \
                        "63343c2a26226324272765272a282b2f200063222663263b22" \
                        "3f30633221262b690a652126243b632469203c24212425"
