import binascii


def mainf(path, keyword, sw, file_name):
    alph16_base = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    alph16_mode = []
    for i in keyword:
        alph16_base.remove(i)
        alph16_mode.append(i)
    alph16_mode += alph16_base
    alph16_base = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    text_hex = str("")
    try:
        f = open(path, "rb")
        b = f.read(1)
        while True:
            b = f.read(1)
            if b == b'':
                break
            text_hex += b.hex()
        f.close()
    except IOError:
        print('error')
    text_hex = text_hex[122:]
    text_mode = text_hex
    text_hex = ""
    for i in text_mode:
        for ii in alph16_mode:
            if (i == ii):
                text_hex += alph16_base[alph16_mode.index(i)]
                break
    text_bytes = binascii.unhexlify(text_hex)
    if sw:
        f = open(str(file_name), "w", encoding="utf-8")
        f.write(text_bytes.decode("utf-8"))
        f.close()
        return text_bytes.decode("utf-8")
    else:
        code = text_bytes.decode("utf-8")
        return code
