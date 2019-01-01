from CaesarCipher import CaesarCipher
from VigenereCipher import VigenereCipher

if __name__ == "__main__":
    print("Cryptography")
    cc_encoded = CaesarCipher.encode('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.')
    print('Ceaser cipher encoded: ', cc_encoded)
    cc_decoded = CaesarCipher.decode(cc_encoded)
    print('Ceaser cipher decoded: ', cc_decoded)

    key = 'verysecrectkey'
    vc_encoded = VigenereCipher.encode('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', key)
    print('Vigenere cipher encoded: ', vc_encoded)
    vc_decoded = VigenereCipher.decode(vc_encoded, key)
    print('Vigenere cipher decoded: ', vc_decoded)

