# Дана строка, содержащая по крайней мере один символ пробела. Вывести подстроку,
# расположенную между первым и последним пробелом исходной строки. Если
# строка содержит только один пробел, то вывести пустую строку.
sptr = "p sju r"
probel1 = sptr.index(' ')
count_probel = sptr.count(" ")
probel2 = sptr.index(' ',count_probel)
if probel1 == probel2:
    print("")
else:
    print(sptr[probel1:probel2])