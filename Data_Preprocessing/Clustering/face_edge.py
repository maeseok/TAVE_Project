import cv2
import numpy as np
import imutils
from google.colab.patches import cv2_imshow

imagepath='/content/jg.jpg'
src=cv2.imread(imagepath,cv2.IMREAD_GRAYSCALE)
imagepath2='/content/image.jpg'
src2=cv2.imread(imagepath2,cv2.IMREAD_GRAYSCALE)

edges=cv2.Canny(src,90,120)
edges2=cv2.Canny(src2,90,120)

#모폴로지 연산으로 깔끔하게 테두리 따기
#흑백 invert하기

cv2_imshow(src)
cv2_imshow(edges)
cv2_imshow(src2)
cv2_imshow(edges2)
cv2.waitKey()
cv2.destroyAllWindows()