lists = [1,2,3,4,5,6,7,8,9]

# 第一种句型
for x in lists:
    print(x)

# 第二种句型
for y in lists:
    print(y)
else:
    print('for循环结束了...')    

# 第三种句型 自动生成list并且开始循环
for z in range(1,3):
    print(z)

# 第四种句型 自动生成list并且指定长度
for k in range(2):
    print(k)

# 第五种句型
for m in lists:
    if m == 2:
        print('是2')
    else:
        print('不是2')