import string

from s1c03 import gen_key, hex_xor, score

if __name__ == "__main__":
    f = open("4.txt", "r")

    best_score = 0
    best_string = ""

    for line in f.readlines():
        line = line.rstrip('\n')

        for char in string.printable:
            key = gen_key(char, len(bytes.fromhex(line)))

            try:
                xor = hex_xor(line, key)
            except ValueError as e:
                continue

            decoded = xor.decode("ISO-8859-1")
            value = score(decoded)

            if value > best_score:
                best_score = value
                best_string = decoded

    print(best_string)
