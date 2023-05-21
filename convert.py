def text_to_bits(text, encoding='utf-8', errors='replace'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, string_encode_main):
    for item in range(0, len(bits), 8):
        my_char = bits[item:item + 8]
        print(my_char, end=' ')
    print(end='\n')

    binary_int = int(bits, 2)
    byte_number = binary_int.bit_length() + 8 // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    result = binary_array.decode()

    first_letter_word = string_encode_main[0]
    index = result.find(first_letter_word)
    if index != -1:
        result_string = result[index:]
        return result_string
