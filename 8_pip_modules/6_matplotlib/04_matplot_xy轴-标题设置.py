#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
squares =[1,4,9,25]

#fig 图, axes x轴
fig,axes = plt.subplots()
axes.plot(squares,linewidth=2)
axes.set_title('Squares line',fontsize=24)
axes.set_xlabel('value',fontsize=12)
axes.set_ylabel('squares',fontsize=12)
axes.tick_params(axis='both',labelsize=14)
plt.show()