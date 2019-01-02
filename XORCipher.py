import string


class XORCipher:
    @staticmethod
    def encode(text: string, key: string) -> object:
        encoded_text = ''
        text_bin = ''.join(map(bin, bytearray(text, 'utf8')))
        text_bin = text_bin.replace('0b', '')

        key_bin = ''.join(map(bin, bytearray(key, 'utf8')))
        key_bin = key_bin.replace('0b', '')

        for x in range(len(text_bin)):
            encoded_text += str(XORCipher.__xor(text_bin[x], key_bin[x % len(key_bin)]))

        return encoded_text

    @staticmethod
    def __xor(a, b):
        return int(bool(a) ^ bool(b))

