# 循环本质就是在满足某种条件的前提下多次执行指定的代码

number = 10
# 如果 number 大于零 则满足循环条件  否则不满足直接结束程序
while number > 0:
    print(number)
    number -= 1

number = 10
while number > 0:
    print('我在执行循环')
    number -= 1
else:
    print('循环结束了')

# while死循环 也就是条件永远是满足的成立的
number = 10
while number == 10:
    print('我是死循环，永远不会停止')

