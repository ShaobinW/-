a = ["123","33211","12321","13531","112233"]
b = []
for i in range(len(a)):
        if a[i]==a[i][::-1]:
                b.append(a[i])
print(b)

c = [each for each in a if each == each[::-1]]
print(c)
