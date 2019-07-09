import string

from s1c02 import hex_xor

FREQUENCIES = {
    "e": 0.12702, "t": 0.09056, "a": 0.08167, "o": 0.07507, "i": 0.06966,
    "n": 0.06749, "s": 0.06327, "h": 0.06094, "r": 0.05987, "d": 0.04253,
    "l": 0.04025, "c": 0.02782, "u": 0.02758, "m": 0.02406, "w": 0.02360,
    "f": 0.02228, "g": 0.02015, "y": 0.01974, "p": 0.01929, "b": 0.01492,
    "v": 0.00978, "k": 0.00772, "j": 0.00153, "x": 0.00150, "q": 0.00095,
    "z": 0.00074, " ": 0.19181
}


def gen_key(char, length):
    as_hex = format(ord(char), "x")
    key = as_hex

    for i in range(length):
        key += as_hex

    return key


def score(plaintext):
    score = 0
    total = 0

    for char in plaintext.lower():
        if char in FREQUENCIES:
            score += FREQUENCIES[char]
        total += 1

    return score / total


if __name__ == "__main__":
    s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    best_score = 0
    best_string = ""

    for char in string.ascii_letters:
        key = gen_key(char, len(bytes.fromhex(s)))
        xor = hex_xor(s, key)

        decoded = xor.decode()
        value = score(decoded)

        if value > best_score:
            best_score = value
            best_string = decoded

    print(best_string)
