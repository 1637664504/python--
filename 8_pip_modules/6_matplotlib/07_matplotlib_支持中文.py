#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib import font_manager
#查询支持的中文字符集: fc-list :lang=zh
font = font_manager.FontProperties(fname="/usr/share/fonts/truetype/wqy/wqy-microhei.ttc")
# plt.rcParams['font.sans-serif']=['wqy-microhei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
squares =[1,4,9,25]

#fig 图, axes x轴
fig,axes = plt.subplots()
axes.plot(squares,linewidth=2)
axes.set_title('平方数',fontsize=24,fontproperties=font)
axes.set_xlabel('值',fontsize=12,fontproperties=font)
axes.set_ylabel('平方',fontsize=12,fontproperties=font)
axes.tick_params(axis='both',labelsize=14)
plt.show()