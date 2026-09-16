# --- 保存为 numpy_demo.py 文件执行 ---
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape) # (2, 3) —— 2行3列
print(arr.reshape(3, 2)) # 变形为3行2列
print(arr[:, 1:]) # 切片：所有行，第1列及之后（冒号表示“所有”）
# 广播机制：形状不同的数组自动补齐
print(arr + np.array([10, 20, 30])) # 每行加不同的值
