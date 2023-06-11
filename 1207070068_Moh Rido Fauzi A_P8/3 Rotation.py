import cv2 as cv  # Mengimpor library OpenCV dengan alias cv. Ini memungkinkan kita untuk menggunakan fungsi-fungsi OpenCV dengan memanggil cv daripada cv2.
import numpy as np  # Mengimpor library NumPy dengan alias np. NumPy digunakan untuk operasi matriks dan array multidimensi.
import matplotlib.pyplot as plt  # Mengimpor modul pyplot dari library matplotlib dengan alias plt. pyplot digunakan untuk membuat plot dan menampilkan gambar.

image = cv.imread("dog.jpg")  # Membaca gambar dengan nama file "kucing.jpg" menggunakan fungsi cv.imread dari OpenCV. Gambar tersebut disimpan dalam variabel image.

h, w = image.shape[:2]  # Menggunakan atribut shape pada image untuk mendapatkan dimensi tinggi dan lebar gambar. [0:2] mengambil elemen pertama dan kedua dari atribut shape, yaitu tinggi dan lebar.

rotation_matrix = cv.getRotationMatrix2D((w / 2, h / 2), -180, 0.5)  # Membuat matriks rotasi menggunakan cv.getRotationMatrix2D. Titik tengah rotasi adalah (w / 2, h / 2). Sudut rotasi adalah -180 derajat (rotasi searah jarum jam sebesar 180 derajat). Skala adalah 0.5.

rotated_image = cv.warpAffine(image, rotation_matrix, (w, h))  # Menggunakan fungsi cv.warpAffine untuk menerapkan transformasi rotasi pada gambar menggunakan matriks transformasi rotation_matrix. Parameter kedua adalah matriks transformasi, dan parameter ketiga adalah ukuran gambar hasil.

plt.imshow(cv.cvtColor(rotated_image, cv.COLOR_BGR2RGB))  # Menampilkan gambar hasil rotasi menggunakan plt.imshow. Karena image memiliki format warna BGR, kita perlu mengonversinya ke format RGB menggunakan cv.cvtColor agar tampilan warna gambar benar.

plt.title("Rotation")  # Memberikan judul "Rotation" pada gambar.

plt.show()  # Menampilkan plot dengan judul dan gambar hasil rotasi yang telah ditentukan.
