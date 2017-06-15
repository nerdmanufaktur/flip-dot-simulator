import character_encodings

import binascii


class CharacterEncoder(object):
    def __init__(self, height=16):
        self.height = height

    def _build_bit_pattern(self, character):
        visual_pattern = character_encodings.character_dict[character]
        width = len(visual_pattern[0])
        bit_pattern = [[False for y in range(self.height)] for x in range(width)]
        for x in range(width):
            for y in range(len(visual_pattern[x])):
                if visual_pattern[x][y] != character_encodings.zero_character:
                    bit_pattern[x][y] = True
        return bit_pattern

    @staticmethod
    def binify(long_int):
        """
        Encode a long integer as bytes.
        https://stackoverflow.com/a/4670889

        :param long_int: long integer
        :return: binary encoding
        """
        h = hex(long_int)[2:].rstrip("L")
        return binascii.unhexlify("0" * (32 - len(h)) + h)

    def _encode_bit_pattern(self, bit_pattern):
        binary = 0
        for x in range(len(bit_pattern)):
            for y in range(self.height):
                binary = binary << 1
                if bit_pattern[x][y]:
                    binary += 1
        return CharacterEncoder.binify(binary)

    def encode_character(self, character):
        bit_pattern = self._build_bit_pattern(character)
        return self._encode_bit_pattern(bit_pattern)


if __name__ == "__main__":
    character_encoder = CharacterEncoder()
    binary = character_encoder.encode_character("A")
    print(binary)
