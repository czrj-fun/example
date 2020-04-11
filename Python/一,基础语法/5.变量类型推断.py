 # 整型变量
variate1 = 100
 # 浮点型  
variate2 = 1000.0   
 # 字符串  
variate3 = "runoob"  
 # 布尔
variate4 = True

# 字典
scores = {'语文': 89, '数学': 92, '英语': 93}  
# 列表
lists = ['Google', 'Runoob', 1997, 2000];
# 元组 相比较列表，元组数组不可修改
tup = ('Google', 'Runoob', 1997, 2000)

print('--variate1的类型是',type(variate1))
print('--variate2的类型是',type(variate2))
print('--variate3的类型是',type(variate3))
print('--variate4的类型是',type(variate4))
print('--scores的类型是',type(scores))
print('--list的类型是',type(lists))
print('--tup的类型是',type(tup))

print('--variate1的类型是',isinstance(variate1,int))
print('--variate2的类型是',isinstance(variate2,float))
print('--variate3的类型是',isinstance(variate3,str))
print('--variate4的类型是',isinstance(variate4,bool))
print('--scores的类型是',isinstance(scores,dict))
print('--list的类型是',isinstance(lists,list))
print('--tup的类型是',isinstance(tup,tuple))