# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


def del_some_words(some_str):

    some_str=tuple(filter( lambda x: "абв" not in x , _str.split() ))
    return " " .join(some_str)



_str = "Напишите прогуабв программу ,абв удаляющую из текста тексабвта все слова, содержащие ""абв""."
result_str = del_some_words(_str)
print (result_str)