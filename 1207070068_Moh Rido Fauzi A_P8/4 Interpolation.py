import mahotas as mh  # Mengimpor library mahotas. Mahotas adalah library untuk pemrosesan gambar dan analisis citra.
import numpy as np  # Mengimpor library NumPy. NumPy digunakan untuk operasi matriks dan array multidimensi.
from pylab import imshow, show  # Mengimpor fungsi imshow dan show dari modul pylab. Fungsi ini digunakan untuk menampilkan gambar.

regions = np.zeros((8, 8), bool)  # Membuat matriks berukuran 8x8 dengan nilai boolean False.
regions[:3, :3] = 1  # Mengubah nilai bagian atas kiri matriks menjadi True.
regions[6:, 6:] = 1  # Mengubah nilai bagian bawah kanan matriks menjadi True.

labeled, nr_objects = mh.label(regions)  # Melabeli wilayah-wilayah pada matriks menggunakan fungsi mh.label dari library mahotas. Mengembalikan gambar hasil labeling dan jumlah objek yang terdeteksi.

imshow(labeled, interpolation='nearest')  # Menampilkan gambar hasil labeling dengan menggunakan fungsi imshow dari pylab.
show()  # Menampilkan plot dengan gambar hasil labeling.

labeled, nr_objects = mh.label(regions, np.ones((3, 3), bool))  # Melabeli wilayah-wilayah pada matriks menggunakan kernel 3x3 yang terdiri dari nilai boolean True. Mengembalikan gambar hasil labeling dan jumlah objek yang terdeteksi.

sizes = mh.labeled.labeled_size(labeled)  # Menghitung ukuran (luas) dari setiap objek dalam gambar menggunakan fungsi mh.labeled.labeled_size dari library mahotas.
print('Background size:', sizes[0])  # Menampilkan ukuran latar belakang (objek dengan label 0) dari gambar hasil labeling.
print('Size of first region:', sizes[1])  # Menampilkan ukuran (luas) dari objek pertama dalam gambar hasil labeling.

array = np.random.random_sample(regions.shape)  # Membuat matriks acak dengan ukuran yang sama dengan matriks regions.
sums = mh.labeled_sum(array, labeled)  # Menghitung jumlah piksel yang terdapat dalam setiap objek dalam gambar menggunakan fungsi mh.labeled_sum dari library mahotas.
print('Sum of first region:', sums[1])  # Menampilkan jumlah piksel dalam objek pertama dalam gambar hasil labeling.
