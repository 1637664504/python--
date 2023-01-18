import matplotlib.pyplot as plt
ax_x=[1,2,3,4,5]
ax_y=[1,4,9,16,25]


#fig 图, axes x轴
fig,axes = plt.subplots()
axes.plot(ax_x,ax_y,linewidth=3)
plt.show()