import string
from math import sqrt


class MatrixCipher:
    @staticmethod
    def encode(text: string) -> object:
        matrix_d, text = MatrixCipher.__basic(text)
        # ['A', 'l', 'a', ' ']
        # ['m', 'a', ' ', 'k']
        # ['o', 't', 'a', ' ']
        # [' ', ' ', ' ', ' ']
        encoded_text = ''
        for x in range(matrix_d):
            for i in range(matrix_d):
                encoded_text += text[x + matrix_d*i]
        return encoded_text

    @staticmethod
    def decode(text: string) -> object:
        matrix_d, text = MatrixCipher.__basic(text)

        decoded_text = ''
        for x in range(matrix_d):
            for i in range(matrix_d):
                decoded_text += text[x + matrix_d * i]
        return decoded_text

    @staticmethod
    def __basic(text: string):
        matrix_d = int(len(text))
        while int(sqrt(matrix_d)) != sqrt(matrix_d):
            matrix_d += 1
        for i in range(matrix_d - len(text)):
            text += ' '
        matrix_d = int(sqrt(matrix_d))
        return matrix_d, text




