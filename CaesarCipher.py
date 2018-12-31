import string


class CesarCipher:
    def test(self):
        print(string.ascii_lowercase)

    @staticmethod
    def encode(text: string, shift: int) -> object:
        encoded_text = ''
        for letter in text.lower():
            x = string.ascii_lowercase.find(letter)
            encoded_text += string.ascii_lowercase[(x + shift) % len(string.ascii_lowercase)]

        print(encoded_text)