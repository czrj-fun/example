lists = [1,2,3,4,5,6,7,8,9]

for x in lists:
    if x == 3:
        print('哈哈，break可以停掉整个for循环')
        break
    else:
        print(x)


for x in lists:
    if x == 3:
        print('wc，continue只能让for停止一次')
        continue
    else:
        print(x)