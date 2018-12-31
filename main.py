from CaesarCipher import CaesarCipher

if __name__ == "__main__":
    print("Cryptography")
    c = CaesarCipher.encode('Apple')
    print(c)
    d = CaesarCipher.decode(c)
    print(d)
