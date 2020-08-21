import binascii
from __decrypt__ import mainf


def mainI(path, keyword, file_res_name):
    if (keyword.__contains__(".bmp")):
        key_2 = mainf(keyword, "fabcd", False, 0)
        if (key_2 == ""):
            key_2 = "0"
        key_3 = ""
        alph16_base = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        for i in key_2:
            if (alph16_base.__contains__(i)):
                key_3 += i
        key_2 = key_3
        key_2 = key_2.strip()
        mainf(path, key_2, True, file_res_name)
    else:
        mainf(path, keyword, True, file_res_name)
