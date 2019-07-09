def hex_xor(hex1, hex2):
    b1 = bytes.fromhex(hex1)
    b2 = bytes.fromhex(hex2)

    xor = []
    for x, y in zip(b1, b2):
        xor.append(x ^ y)

    return bytes(xor)


if __name__ == "__main__":
    s1 = "1c0111001f010100061a024b53535009181c"
    s2 = "686974207468652062756c6c277320657965"
    xor = hex_xor(s1, s2)

    assert xor.hex() == "746865206b696420646f6e277420706c6179"

    print(xor.decode())
