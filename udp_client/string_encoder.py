from character_encoder import CharacterEncoder


class StringEncoder(object):
    def __init__(self, height=16, space_width=1):
        self.character_encoder = CharacterEncoder(height)
        self.space_width = space_width

    def _build_space(self):
        return [[False for y in range(self.character_encoder.height)] for x in range(self.space_width)]

    def _build_bit_pattern(self, string):
        encoded_string = []
        for character in string:
            encoded_character = self.character_encoder.build_bit_pattern(character)
            encoded_string.extend(encoded_character)
            encoded_string.extend(self._build_space())
        return encoded_string

    def encode_string(self, string):
        bit_pattern = self._build_bit_pattern(string)
        return self.character_encoder.encode_bit_pattern(bit_pattern)


if __name__ == "__main__":
    string_encoder = StringEncoder()
    encoded_string = string_encoder.encode_string("ABBA ABBA")
    print(encoded_string)
