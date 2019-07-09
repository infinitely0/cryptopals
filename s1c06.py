import base64
import string

from s1c03 import score
from s1c05 import repeating_key_xor


def hemming_distance(bytes1, bytes2):
    str1 = "".join(map(bin_str, bytes1))
    str2 = "".join(map(bin_str, bytes2))

    return sum(x != y for x, y in zip(str1, str2))


def bin_str(b):
    return str(bin(b)).replace("b", "0").rjust(9, "0")


def to_blocks(byte_array, block_size):
    blocks = []
    i = 0
    while i < len(byte_array):
        blocks.append(byte_array[i:i + block_size])
        i += block_size

    return blocks


def transpose(blocks, nth):
    trans = []
    for block in blocks:
        try:
            trans.append(block[nth])
        except IndexError as e:
            break
    return trans


def single_char_xor(block, char):
    xor = []
    for x in block:
        xor.append(x ^ ord(char))
    return bytes(xor)


def find_single_char_xor_key(block):
    best_score = 0
    best_key = ""

    for char in string.printable:
        xor = single_char_xor(block, char)
        decoded = xor.decode("utf-8")
        value = score(decoded)

        if value > best_score:
            best_score = value
            best_key = char

    return best_key


if __name__ == "__main__":
    b1 = "this is a test".encode()
    b2 = "wokka wokka!!!".encode()

    assert hemming_distance(b1, b2) == 37

    f = open("6.txt", "r")
    text = f.read()
    decoded = base64.b64decode(text)

    distances = {}
    for keysize in range(2, 50):
        blocks = to_blocks(decoded, keysize)

        i = 0
        sum_distances = 0
        while i < len(blocks) - 1:
            b1 = blocks[i]
            i += 1
            b2 = blocks[i]

            sum_distances += hemming_distance(b1, b2) / keysize

        distances[keysize] = sum_distances / len(blocks)

    best_keysizes = sorted(distances, key=distances.get)[:3]

    keys = []
    for keysize in best_keysizes:
        key = ""
        blocks = to_blocks(decoded, keysize)
        for i in range(0, keysize):
            transposed = transpose(blocks, i)
            key += find_single_char_xor_key(transposed)

        keys.append(key)

    best_score = 0
    best_key = ""
    best_plaintext = ""
    for key in keys:
        plaintext = repeating_key_xor(decoded, key).decode("utf-8")
        value = score(plaintext)
        if value > best_score:
            best_score = value
            best_key = key
            best_plaintext = plaintext

    print(best_key)
    print(best_plaintext)
