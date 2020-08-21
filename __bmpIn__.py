import binascii
import sys
from __decrypt__ import mainf as dec


def fo(a):
    i = 0
    while i ** 2 < len(a):
        i += 32
    return i


def str_byte(a):
    res = str("")
    byte = ["0", "0", "0", "0", "0000"]
    while a >= 4096:
        if ((byte[2] != "a") or (byte[2] != "b") or (byte[2] != "c") or (byte[2] != "d") or (byte[2] != "e") or (
                byte[2] != "9")):
            byte[2] = str(int(byte[2]) + 1)
        else:
            if (byte[2] == "9"):
                byte[2] = "a"
            elif (byte[2] == "a"):
                byte[2] = "b"
            elif (byte[2] == "b"):
                byte[2] = "c"
            elif (byte[2] == "c"):
                byte[2] = "d"
            elif (byte[2] == "d"):
                byte[2] = "e"
            elif (byte[2] == "e"):
                byte[2] = "f"
        a -= 4096
    while a >= 256:
        if ((byte[3] != "a") or (byte[3] != "b") or (byte[3] != "c") or (byte[3] != "d") or (byte[3] != "e") or (
                byte[3] != "9")):
            byte[3] = str(int(byte[3]) + 1)
        else:
            if (byte[3] == "9"):
                byte[3] = "a"
            elif (byte[3] == "a"):
                byte[3] = "b"
            elif (byte[3] == "b"):
                byte[3] = "c"
            elif (byte[3] == "c"):
                byte[3] = "d"
            elif (byte[3] == "d"):
                byte[3] = "e"
            elif (byte[3] == "e"):
                byte[3] = "f"
        a -= 256
    while a >= 16:
        if ((byte[0] != "a") or (byte[0] != "b") or (byte[0] != "c") or (byte[0] != "d") or (byte[0] != "e") or (
                byte[0] != "9")):
            byte[0] = str(int(byte[0]) + 1)
        else:
            if (byte[0] == "9"):
                byte[0] = "a"
            elif (byte[0] == "a"):
                byte[0] = "b"
            elif (byte[0] == "b"):
                byte[0] = "c"
            elif (byte[0] == "c"):
                byte[0] = "d"
            elif (byte[0] == "d"):
                byte[0] = "e"
            elif (byte[0] == "e"):
                byte[0] = "f"
        a -= 16
    while a >= 1:
        if ((byte[1] != "a") or (byte[1] != "b") or (byte[1] != "c") or (byte[1] != "d") or (byte[1] != "e") or (
                byte[1] != "9")):
            byte[1] = str(int(byte[1]) + 1)
        else:
            if (byte[1] == "9"):
                byte[1] = "a"
            elif (byte[1] == "a"):
                byte[1] = "b"
            elif (byte[1] == "b"):
                byte[1] = "c"
            elif (byte[1] == "c"):
                byte[1] = "d"
            elif (byte[1] == "d"):
                byte[1] = "e"
            elif (byte[1] == "e"):
                byte[1] = "f"
        a -= 1
    res = byte[0] + byte[1] + byte[2] + byte[3] + byte[4]
    return res


def mainI(path_text, keyword, file_res_name):
    if (keyword.__contains__(".bmp")):
        keyword = dec(keyword, "fabcd", False, 0)
        if (keyword == ""):
            keyword = "0"
        key_3 = ""
        alph16_base = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        for i in keyword:
            if (alph16_base.__contains__(i)):
                key_3 += i
        keyword = key_3
        keyword = keyword.strip()
    alph16_base = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    alph16_mode = []
    for i in keyword:
        alph16_base.remove(i)
        alph16_mode.append(i)
    alph16_mode += alph16_base
    alph16_base = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    file_text = open(path_text, mode='r', encoding="utf-8")
    text = str("")
    for i in file_text:
        text += i
    file_text.close()
    text = str.encode(text).hex()
    llen = fo(text)
    k = 0
    text_mode = text
    text = ""
    for i in text_mode:
        for ii in alph16_base:
            if (i == ii):
                text += alph16_mode[alph16_base.index(i)]
                break
    bmp_len = str_byte(llen)
    bmp_width = bmp_len
    bmp_base = str(
        "424d7e000000000000003e00000028000000" + bmp_len + bmp_width + "0100010000000000400000000000000000000000000000000000000000000000ffffff00")
    result = bmp_base + text
    count = llen * llen / 4
    while len(text) / 2 < count:
        count -= 1
        result += alph16_mode[alph16_base.index("2")] + alph16_mode[alph16_base.index("0")]
    file_bmp = open(file_res_name, "wb")
    for i in range(int(len(result))):
        if (i % 2 == 0):
            try:
                file_bmp.write(binascii.unhexlify(result[i:i + 2]))
            except UnicodeEncodeError:
                print("Unknown symbol, skip")
                file_bmp.write(binascii.unhexlify("23"))
    file_bmp.close()
