# 迭代器主要的作用就是访问集合

# 迭代器演示代码
# 定义一个集合
list=[1,2,3,4]
# 使用集合创建一个迭代器对象
it = iter(list)
# 每次调用next，都会从迭代器中取出一个值
print (next(it))
print (next(it))
print (next(it))
print (next(it))


# 生成器主要作用是生成测试数据
# 生成器演示代码
L = [x * x for x in range(10)]
for x in L:
    print(x)
