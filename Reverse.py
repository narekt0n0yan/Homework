a=[5,6,7,8,9,10]
for i in range(len(a)//2):
    (a[i], a[-i-1]) = (a[-i-1], a[i])

print(a)