a = ["123","33211","12321","13531","112233"]

"""----------------part 1-------------------"""
b = []
for i in range(len(a)):
        if a[i]==a[i][::-1]:
                b.append(a[i])
print(b)

"""----------------part 2-------------------"""
c = [each for each in a if each == each[::-1]]
print(c)

"""
part 1 以及 part 2 实现相同效果，本例中寻找列表中“回文数”
part 2使用技巧  [pression for ... in ... (if ...)
                          for ... in ... (if ...)
                          for ... in ... (if ...)]

"""
