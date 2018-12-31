from CaesarCipher import CaesarCipher

if __name__ == "__main__":
    print("Cryptography")
    c = CaesarCipher.encode('Kamil  f', 2)
    print(c)
    d = CaesarCipher.decode(c, 2)
    print(d)