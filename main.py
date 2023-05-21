from PIL import Image
from generate_key import generate_private_key_from_file
from encode_fun import encode_to_BMP
from decode_fun import decode_from_img


if __name__ == '__main__':
    string_encode = 'Smagin Danila'
    my_file_name = 'Image/landscape.bmp'
    img = Image.open('Image/landscape.bmp')
    width = img.size[0]
    height = img.size[1]
    sigma = 3

    print(f'Value of sigma equal {sigma}, width equal {width},'
          f' height equal {height}')
    generate_private_key_from_file(sigma, width, height, 5000)
    encode_to_BMP(my_file_name, 0.1, string_encode, sigma, 6)
    encode_string = decode_from_img(len(string_encode) * 8 + 1,
                                    sigma, string_encode)
    print(encode_string)
