#  Created by avivyh on 31/05/22.
#  Copyright © 2022  avivyh. All rights reserved.




import cv2
import numpy as np

img = cv2.imread('IMAGEMTESTE.jpg', cv2.IMREAD_COLOR)

cv2.namedWindow('Exibindo Imagem!')

cv2.imshow('Exibindo Imagem!', img)

cv2.waitKey()

