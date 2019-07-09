from s1c06 import to_blocks
from s1c07 import decrypt

if __name__ == "__main__":
    f = open("8.txt", "r")

    ECB_ciphertext = None
    most_duplicates = 0

    for line in f.readlines():
        ciphertext = bytes.fromhex(line.rstrip())
        blocks = to_blocks(ciphertext, 16)
        duplicates = len(blocks) - len(set(blocks))

        if (duplicates > most_duplicates):
            most_duplicates = duplicates
            ECB_ciphertext = ciphertext

    print(ECB_ciphertext)
