import string


class VigenereCipher:
    @staticmethod
    def encode(text: string, key: string) -> object:
        alphabet = string.ascii_lowercase
        encoded_text = ''
        text = text.lower()
        key = key.lower()

        for x in range(len(text)):
            if alphabet.find(text[x]) < 0:
                encoded_text += text[x]
            else:
                encoded_text += alphabet[(alphabet.find(text[x]) + alphabet.find(key[x % len(key)])) % len(alphabet)]
        return encoded_text

    @staticmethod
    def decode(text: string, key: string) -> object:
        alphabet = string.ascii_lowercase
        decoded_text = ''
        text = text.lower()
        key = key.lower()

        for x in range(len(text)):
            if alphabet.find(text[x]) < 0:
                decoded_text += text[x]
            else:
                decoded_text += alphabet[(alphabet.find(text[x]) - alphabet.find(key[x % len(key)])) % len(alphabet)]
        return decoded_text
