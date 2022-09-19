# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def encoding_rle(data):
    encode = ""
    var_char = ""
    count = 1
    for char in data:
        if char != var_char:
            if var_char:
                encode += str(count) + var_char
            count = 1
            var_char = char
        else:
            count += 1
    encode += str(count) + var_char

    return encode

def decoding_rle(data):
    decode = ""
    count = ""
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ""
    return decode

print( encoding_rle("AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE"))
print(decoding_rle("6A1F2D7C1A17E"))
