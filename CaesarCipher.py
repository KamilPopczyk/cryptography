import string


class CaesarCipher:
    def test(self):
        print(string.ascii_lowercase)

    @staticmethod
    def encode(text: string, shift: int) -> object:
        encoded_text = ''
        alphabet = string.ascii_lowercase
        for letter in text.lower():
            if letter is ' ':
                encoded_text += ' '
            else:
                x = alphabet.find(letter)
                encoded_text += alphabet[(x + shift) % len(alphabet)]
        return encoded_text

