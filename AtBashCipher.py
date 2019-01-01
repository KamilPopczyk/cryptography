import string


class AtBashCipher:
    @staticmethod
    def encode(text: string) -> object:
        encoded_text = ''
        alphabet = string.ascii_lowercase
        for letter in text.lower():
            if alphabet.find(letter) < 0:
                encoded_text += letter
            else:
                x = alphabet.find(letter) + 1
                encoded_text += alphabet[-x]
        return encoded_text

    @staticmethod
    def decode(text: string) -> object:
        return AtBashCipher.encode(text)