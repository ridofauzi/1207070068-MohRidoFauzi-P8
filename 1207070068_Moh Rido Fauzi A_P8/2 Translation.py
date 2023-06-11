import cv2 as cv  # Mengimpor library OpenCV dengan alias cv. Ini memungkinkan kita untuk menggunakan fungsi-fungsi OpenCV dengan memanggil cv daripada cv2.
import numpy as np  # Mengimpor library NumPy dengan alias np. NumPy digunakan untuk operasi matriks dan array multidimensi.
import matplotlib.pyplot as plt  # Mengimpor modul pyplot dari library matplotlib dengan alias plt. pyplot digunakan untuk membuat plot dan menampilkan gambar.

image = cv.imread('dog.jpg')  # Membaca gambar dengan nama file 'LUKISAN.jpg' menggunakan fungsi cv.imread dari OpenCV. Gambar tersebut disimpan dalam variabel image.

h, w = image.shape[:2]  # Menggunakan atribut shape pada image untuk mendapatkan dimensi tinggi dan lebar gambar. [0:2] mengambil elemen pertama dan kedua dari atribut shape, yaitu tinggi dan lebar.

half_height, half_width = h // 4, w // 8  # Menghitung setengah tinggi dan setengah lebar gambar dengan membagi tinggi (h) dengan 4 dan lebar (w) dengan 8 menggunakan operator pembagian bulat //.

transition_matrix = np.float32([[1, 0, half_width], [0, 1, half_height]])  # Membuat matriks transformasi menggunakan np.float32. Matriks ini digunakan untuk menerapkan translasi pada gambar. Nilai 1 pada posisi (0, 0) dan (1, 1) menunjukkan tidak ada perubahan pada sumbu x dan y. Nilai half_width dan half_height pada posisi (0, 2) dan (1, 2) menentukan seberapa jauh translasi dilakukan.

img_transition = cv.warpAffine(image, transition_matrix, (w, h))  # Menggunakan fungsi cv.warpAffine untuk menerapkan transformasi translasi pada gambar menggunakan matriks transformasi transition_matrix. Parameter kedua adalah matriks transformasi, dan parameter ketiga adalah ukuran gambar hasil.

plt.imshow(cv.cvtColor(img_transition, cv.COLOR_BGR2RGB))  # Menampilkan gambar hasil translasi menggunakan plt.imshow. Karena image memiliki format warna BGR, kita perlu mengonversinya ke format RGB menggunakan cv.cvtColor agar tampilan warna gambar benar.

plt.title("Translation")  # Memberikan judul "Translation" pada gambar.

plt.show()  # Menampilkan plot dengan judul dan gambar hasil translasi yang telah ditentukan.
