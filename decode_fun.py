from convert import text_from_bits
from PIL import Image


def decode_from_img(quatity_bits, sigma_main, string_encode_main, K=6):
    global b
    decode_bit_str = ""
    img_encoding = Image.open('Image/landscape_last_version.bmp')
    img_encoding.load()
    width_encode = img_encoding.size[0]
    height_encode = img_encoding.size[1]
    f = open('file_key/file_name_key', 'r')
    key = f.readline().split(" ")
    f.close()
    j = 0
    delta = 0
    for n in range(0, quatity_bits):
        n += 1
        for k in range(0, K):
            if 2 * j + 1 >= len(key) or n == quatity_bits:
                len_d = (len(decode_bit_str) // 16) * 16
                print(f'my string {decode_bit_str}')
                print(f'length string {len(decode_bit_str)}')
                return text_from_bits(decode_bit_str, string_encode_main)

            x = int(key[2 * j])
            y = int(key[2 * j + 1])
            if x > width_encode - sigma_main or y > height_encode - sigma_main:
                len_d = (len(decode_bit_str) // 16) * 16
                return text_from_bits(decode_bit_str[0:len_d])
            b = img_encoding.getpixel((x, y))[2]
            sum1 = 0
            sum2 = 0
            for i in range(1, sigma_main + 1):
                sum1 += img_encoding.getpixel((x + i, y))[2] + img_encoding.getpixel((x - i, y))[2]
                sum2 += img_encoding.getpixel((x, y + i))[2] + img_encoding.getpixel((x, y - i))[2]

            b_prog = (sum1 + sum2) / (4 * sigma_main)
            delta = b - b_prog
            j += 2
        if delta < 0 or b == 0:
            decode_bit_str += '0'
        elif delta > 0 or b == 255:
            decode_bit_str += '1'
