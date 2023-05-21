import datetime
import numpy as np


def generate_private_key_from_file(sigma_main, width_main, height_main, L):
    now_time = datetime.datetime.now()
    np.random.seed(int(now_time.time().strftime('%f')) % 2 ** 32)

    x = np.random.randint(sigma_main + 1, width_main - sigma_main - 1, L)
    y = np.random.randint(sigma_main + 1, height_main - sigma_main - 1, L)
    key = np.column_stack([x, y])

    f = open('file_key/file_name_key', 'w')
    for i in key:
        f.write(str(i[0]) + " " + str(i[1]) + " ")
    f.close()
