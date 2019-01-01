import string


class CaesarCipher:
    @staticmethod
    def encode(text: string, shift: int = 13) -> object:
        encoded_text = ''
        alphabet = string.ascii_lowercase
        for letter in text.lower():
            if alphabet.find(letter) < 0:
                encoded_text += letter
            else:
                x = alphabet.find(letter)
                encoded_text += alphabet[(x + shift) % len(alphabet)]
        return encoded_text
    
    @staticmethod
    def decode(text: string, shift: int = 13) -> object:
        decoded_text = ''
        alphabet = string.ascii_lowercase
        for letter in text.lower():
            if alphabet.find(letter) < 0:
                decoded_text += letter
            else:
                y = alphabet.find(letter)
                decoded_text += alphabet[(y - shift) % len(alphabet)]
        return decoded_text

