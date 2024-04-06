import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 计算y值
y = [num**3 for num in x]

# 计算一阶差分
diff = [y[i] - y[i-1] for i in range(1, len(y))]

# calculate second difference
diff2 = [diff[i] - diff[i-1] for i in range(1, len(diff))]

diff3 = [diff2[i] - diff2[i-1] for i in range(1, len(diff2))]
# 绘制一阶差分图形
plt.plot(diff3)

# 添加标题和坐标轴标签
plt.title("First Difference of y = x^2")
plt.xlabel("Index")
plt.ylabel("Difference")

# 显示图形
plt.show()
