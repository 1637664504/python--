import matplotlib.pyplot as plt
#公式生成 数列
a=[2*x for x in range(1,10)]
b=[pow(x,2) for x in range(1,10) ]

fig,axes = plt.subplots()
axes.plot(a)
axes.plot(b)
plt.show()