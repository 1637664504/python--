#!/usr/bin/python3
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

#增
tinydict['address']="ShenZhen"

#改
tinydict['Age'] = 8               # 更新 Age
tinydict['School'] = "菜鸟教程"  # 添加信息

#删
tinydict.pop('Class')
#del tinydict['Name'] # 删除键 'Name'
#tinydict.clear()     # 清空字典

#查
tinydict['Age']
print ("tinydict['Name']: ", tinydict['Name'])