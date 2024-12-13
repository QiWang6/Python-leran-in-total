# @Time: 2024/10/16 
# @Author: Qi Wang
# @File: test1
# @Project: Python-leran-in-total
# @Quelle:

# 模拟数据库中的数据
'''items = [{"name": f"Item {i}"} for i in range(100)]  # 模拟 100 条数据
for i in range(100):
    print(items[i], end='\n')'''
'''
import matplotlib.pylab as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Plot')
plt.show()'''

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

fig = plt.figure()
gs = gridspec.GridSpec(2, 2)  # 创建一个 2x2 的网格布局

ax1 = fig.add_subplot(gs[0, 0])  # 第 1 行第 1 列
ax2 = fig.add_subplot(gs[0, 1])  # 第 1 行第 2 列
ax3 = fig.add_subplot(gs[1, :])  # 第 2 行占据所有列

ax1.set_title("Subplot 1")
ax2.set_title("Subplot 2")
ax3.set_title("Subplot 3")

plt.tight_layout()
plt.show()



