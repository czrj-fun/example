'''
基本数据类型包括：
    Number（数字）
    String（字符串）
    Boolean（布尔类型）
    List（列表）
    Tuple（元组）
    Set（集合）
    Dictionary（字典）
其中 
不可变数据:Number（数字）、String（字符串）、Tuple（元组）
可变数据:List（列表）、Dictionary（字典）、Set（集合）
'''

# python是根据数据类型推断变量类型

 # 整型变量
variate1 = 100         
print(variate1)

 # 浮点型变量
variate2 = 1000.0      
print(variate2)

 # 字符串
variate3 = "runoob"    
print(variate3)
# 布尔
variate4 = True
print(variate4)

# 字典
scores = {'语文': 89, '数学': 92, '英语': 93}  
# 输出字典所有内容
print(scores) 
# 输出字典某一个内容
print(scores['语文']) 
# 列表
list = ['Google', 'Runoob', 1997, 2000];
# 根据列表索引输出内容
print(list[1])
# 根据列表索引输出指定范围的内容 包含开头不包含结尾
print(list[1:4])
# 修改列表中指定索引的数据
list[1] = 100;
print(list)
# 元组 相比较列表，元组数组不可修改
tup = ('Google', 'Runoob', 1997, 2000)
# 根据索引输出元组中指定内容
print(tup[1])
# 指定索引范围，包含开头，不包含结尾
print(tup[1:4])