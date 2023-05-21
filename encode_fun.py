from convert import text_to_bits
from PIL import Image, ImageDraw


def encode_to_BMP(file_name, v, str, sigma_main, K=5):
    encode_bit = text_to_bits(str)
    img = Image.open(file_name)
    img.load()
    draw = ImageDraw.Draw(img)
    brightness = [0.299, 0.587, 0.114]
    f = open('file_key/file_name_key', 'r')
    key = f.readline().split(' ')
    print(f'Length of key: {len(key)}')
    f.close()
    j = 0
    for z in encode_bit:
        for k in range(0, K):
            if 2 * j + 1 >= len(key):
                break
            x = int(key[2 * j])
            y = int(key[2 * j + 1])
            j += 2
            red = img.getpixel((x, y))[0]
            green = img.getpixel((x, y))[1]
            blue = img.getpixel((x, y))[2]
            sum1 = 0
            sum2 = 0
            for i in range(1, sigma_main + 1):
                sum1 += img.getpixel((x + i, y))[2] + img.getpixel((x - i, y))[2]
                sum2 += img.getpixel((x, y + i))[2] + img.getpixel((x, y - i))[2]
            b_prog = (sum1 + sum2) / (4 * sigma_main)
            lambda_xy = brightness[0] * red + brightness[1] * green + brightness[2] * blue
            msg = blue
            if (msg - b_prog) * (2 * int(z) - 1) <= 0:
                msg = round(blue + (2 * int(z) - 1) * v * lambda_xy)
            if (msg - b_prog) * (2 * int(z) - 1) <= 0 or abs(blue - b_prog) < v * lambda_xy:
                msg = round(blue + (2 * int(z) - 1) * (v * lambda_xy + abs(blue - b_prog)))
            if msg > 255:
                msg = 255
            elif msg < 0:
                msg = 0
            draw.point((x, y), (red, green, msg))
            k += 1
        if 2 * j + 1 >= len(key):
            break

    new_file_name = file_name.split('.')[0] + "_last_version.bmp"
    img.save(new_file_name, "BMP")
    print('Embedding is done')
