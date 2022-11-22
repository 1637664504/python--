thisset = set(("Google", "Runoob", "Taobao"))

#增
thisset.add("ali")
thisset.update({1,3}) #可以是列表，元组，字典

#删
thisset.remove("Taobao")
thisset.discard("Facebook")		#无元素,不报错

#判断
"Runoob" in thisset
#True
"Facebook" in thisset
#False