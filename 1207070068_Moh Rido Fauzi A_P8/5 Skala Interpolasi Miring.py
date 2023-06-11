import cv2 as cv  # Mengimpor library OpenCV dengan alias cv. Ini memungkinkan kita untuk menggunakan fungsi-fungsi OpenCV dengan memanggil cv daripada cv2.
import numpy as np  # Mengimpor library NumPy dengan alias np. NumPy digunakan untuk operasi matriks dan array multidimensi.
import matplotlib.pyplot as plt  # Mengimpor modul pyplot dari library matplotlib dengan alias plt. pyplot digunakan untuk membuat plot dan menampilkan gambar.

image = cv.imread("dog.jpg")  # Membaca gambar dengan nama file "kucing.jpg" menggunakan fungsi cv.imread dari OpenCV. Gambar tersebut disimpan dalam variabel image.

fig, ax = plt.subplots(1, 3, figsize=(16, 8))  # Membuat subplots dengan 1 baris dan 3 kolom, dengan ukuran total gambar (figsize) sebesar (16, 8). Subplots ini akan menampilkan 3 gambar.

# Gambar pertama: Skala dengan interpolasi linear
image_scaled = cv.resize(image, None, fx=0.15, fy=0.15)  # Mengubah ukuran gambar menjadi 0.15 kali ukuran aslinya menggunakan fungsi cv.resize. Interpolasi yang digunakan adalah interpolasi linear.
ax[0].imshow(cv.cvtColor(image_scaled, cv.COLOR_BGR2RGB))  # Menampilkan gambar hasil skala menggunakan plt.imshow. Karena image memiliki format warna BGR, kita perlu mengonversinya ke format RGB menggunakan cv.cvtColor agar tampilan warna gambar benar.
ax[0].set_title("Linear Interpolation Scale")  # Memberikan judul "Linear Interpolation Scale" pada gambar pertama.

# Gambar kedua: Skala dengan interpolasi kubik
image_scaled_2 = cv.resize(image, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)  # Mengubah ukuran gambar menjadi 2 kali ukuran aslinya menggunakan fungsi cv.resize. Interpolasi yang digunakan adalah interpolasi kubik.
ax[1].imshow(cv.cvtColor(image_scaled_2, cv.COLOR_BGR2RGB))  # Menampilkan gambar hasil skala menggunakan plt.imshow. Karena image memiliki format warna BGR, kita perlu mengonversinya ke format RGB menggunakan cv.cvtColor agar tampilan warna gambar benar.
ax[1].set_title("Cubic Interpolation Scale")  # Memberikan judul "Cubic Interpolation Scale" pada gambar kedua.

# Gambar ketiga: Skala dengan interpolasi area (skewed)
image_scaled_3 = cv.resize(image, (200, 400), interpolation=cv.INTER_AREA)  # Mengubah ukuran gambar menjadi (200, 400) piksel menggunakan fungsi cv.resize. Interpolasi yang digunakan adalah interpolasi area.
ax[2].imshow(cv.cvtColor(image_scaled_3, cv.COLOR_BGR2RGB))  # Menampilkan gambar hasil skala menggunakan plt.imshow. Karena image memiliki format warna BGR, kita perlu mengonversinya ke format RGB menggunakan cv.cvtColor agar tampilan warna gambar benar.
ax[2].set_title("Skewed Interpolation Scale")  # Memberikan judul "Skewed Interpolation Scale" pada gambar ketiga.

plt.show()  # Menampilkan plot dengan ketiga gambar yang telah ditentukan.
