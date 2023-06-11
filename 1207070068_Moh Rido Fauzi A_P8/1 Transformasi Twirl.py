import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.transform import swirl

# Membaca gambar JPG
image = cv2.imread('LUKISAN.jpg', cv2.IMREAD_GRAYSCALE)

# Mengkonversi tipe data gambar menjadi float
image_float = image.astype(np.float32) / 255.0

# Melakukan operasi swirl pada gambar
swirled = swirl(image_float, rotation=0, strength=10, radius=120)

# Menampilkan gambar asli dan hasil swirl
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3), sharex=True, sharey=True)

# Menampilkan gambar asli
ax0.imshow(image, cmap='gray')
ax0.axis('off')
ax0.set_title('Gambar Asli')

# Menampilkan gambar hasil swirl
ax1.imshow(swirled, cmap='gray')
ax1.axis('off')
ax1.set_title('Gambar Swirl')

plt.show()
