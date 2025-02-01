# Дана строка, содержащая по крайней мере один символ пробела. Вывести подстроку,
# расположенную между первым и последним пробелом исходной строки. Если
# строка содержит только один пробел, то вывести пустую строку.
sptr = "p sfnf mgfnfgm fkgj fgjkgju r"
probel1 = sptr.index(' ')
possprobel =len(sptr) - sptr[::-1].index(" ")
if probel1 == possprobel:
    print("")
else:
    print(sptr[probel1:possprobel])