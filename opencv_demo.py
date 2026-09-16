# --- 保存为 opencv_demo.py 文件执行 ---
import cv2
img = cv2 .imread('photo.jpg')                     # 读取图片
gray = cv2 .cvtColor(img, cv2 .COLOR_BGR2GRAY)      # 灰度化
resized = cv2 .resize(img, (224, 224))             # 缩放到固定尺寸
rotated = cv2 .rotate(img, cv2 .ROTATE_90_CLOCKWISE) # 旋转90度
edges = cv2 .Canny(gray, 100, 200)                 # 边缘检测（Canny算法）
cv2 .imwrite('gray.jpg', gray)                     # 保存结果
cv2 .imwrite('edges.jpg', edges)
cv2.imwrite('rotated.jpg', rotated)