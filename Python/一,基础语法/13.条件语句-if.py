# 条件语句
boo = True

# 第一种句型,如果boo成立的话 则执行输出语句
if boo:
    print("boo是:",boo)

# 第二种句型，如果boo成立的话，输出A，如果不成立，输出B
boo = False
if boo:
    print('A')
else:
    print('B')

# 第三种句型 多条件联合判断
#   其中 elif 可以存在多个  else和if只能存在一个 if必须存在且只有一个
boo = 10

if boo == 11:
    print("boo是",boo)
elif boo == 12:
    print("boo是",boo)
else:
    print("boo是",boo)