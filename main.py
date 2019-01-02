from CaesarCipher import CaesarCipher
from VigenereCipher import VigenereCipher
from MatrixCipher import MatrixCipher
from AtBashCipher import AtBashCipher
from XORCipher import XORCipher

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

    mc_encoded = MatrixCipher.encode('Ala ma kota')
    mc_decoded = MatrixCipher.decode(mc_encoded)
    print('Matrix cipher encoded: ', mc_encoded)
    print('Matrix cipher decoded: ', mc_decoded)

    atc_encoded = AtBashCipher.encode('Ala ma kota')
    atc_decoded = AtBashCipher.decode(atc_encoded)
    print('AtBash cipher encoded: ', atc_encoded)
    print('AtBash cipher decoded: ', atc_decoded)

    XORCipher.encode('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore', key)


