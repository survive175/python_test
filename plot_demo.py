# --- 保存为 plot_demo.py 文件执行 ---
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(4)                    # 4组实验
acc = [0.85, 0.88, 0.90, 0.92]      # Method A的精度
acc_b = [0.80, 0.83, 0.86, 0.88]    # Method B的精度
plt.bar (x - 0.2, acc, width=0.4, label='Ours')
plt.bar (x + 0.2, acc_b, width=0.4, label='Baseline')
plt.xlabel('Dataset splits')        # 横轴标签
plt.ylabel('Accuracy (%)')          # 纵轴标签
plt.legend()                        # 显示图例
plt.savefig('ablation.png', dpi=300, bbox_inches='tight')  # 保存为高分辨率图
print("图片已保存为 ablation.png")
