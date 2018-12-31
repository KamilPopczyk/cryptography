import string


class CaesarCipher:

    @staticmethod
    def encode(text: string, shift: int = 13) -> object:
        encoded_text = ''
        alphabet = string.ascii_lowercase
        for letter in text.lower():
            if letter is ' ':
                encoded_text += ' '
            else:
                x = alphabet.find(letter)
                encoded_text += alphabet[(x + shift) % len(alphabet)]
        return encoded_text
    
    @staticmethod
    def decode(text: string, shift: int = 13) -> object:
        decoded_text = ''
        alphabet = string.ascii_lowercase
        for letter in text.lower():
            if letter is ' ':
                decoded_text += ' '
            else:
                y = alphabet.find(letter)
                decoded_text += alphabet[(y - shift) % len(alphabet)]
        return decoded_text

