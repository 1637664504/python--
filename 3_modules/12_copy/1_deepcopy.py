# 推荐使用vscode 查看栈的变化过程

import copy
a=[1,2,3,4,[5,6]]
a1=a
a2=copy.copy(a)
a3=copy.deepcopy(a)

a1[1]=11
a2[2]=22
a3[3]=33

print(id(a),"a ",a)
print(id(a1),"a1 ",a1)
print(id(a2),"a2 ",a2)
print(id(a3),"a3 ",a3)

#子 class修改
a1[4][0]=1
a2[4][0]=2
#a,a1,a2 的[5,6] 指向同一个地址

a3[4][0]=3
print("a ",a)
print("a1 ",a1)
print("a2 ",a2)
print("a3 ",a3)

# 结论:
# deepcopy() 拷贝子class/数据结构