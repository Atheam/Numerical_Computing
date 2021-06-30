import numpy as np
from PIL import Image
from numpy.linalg import svd,norm
import matplotlib.pyplot as plt

#loading image
filename = "lena512.bmp"
img = np.asarray(Image.open(filename))

#result matrix using k singular values
def get_k_values(img,k):
    U,S,V = svd(img)
    I = np.zeros((U.shape[0],V.shape[0]))
    for i in range(k):
        I += np.outer(U[:,i],V[i]) * S[i] 
    return I

k_values = [8,16,32,128,256,512]
diff = []
for k in k_values:
    #getting compressed img
    compressed_matrix = get_k_values(img, k)
    #calculting difference img matrix
    difference_matrix = np.subtract(img, compressed_matrix)

    compressed_img = Image.fromarray(compressed_matrix).convert("RGB")
    compressed_img.save("./imgs/compressed_lena" + str(k) + ".jpg")

    difference_img = Image.fromarray(difference_matrix).convert("RGB")
    difference_img.save("./imgs/difference_lane" + str(k) +".jpg")

    diff.append(norm(np.subtract(img, compressed_matrix)))

plt.plot(k_values,diff)
plt.show()

