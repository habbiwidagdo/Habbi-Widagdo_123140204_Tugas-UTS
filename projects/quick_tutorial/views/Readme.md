Analysis
Pada tahap ini saya belajar mengorganisir view di Pyramid dengan cara yang lebih rapi. Sebelumnya, semua hal dicampur dalam satu file: fungsi view, konfigurasi route, dan inisialisasi aplikasi (WSGI app). Walaupun itu berfungsi, tapi untuk aplikasi yang lebih besar struktur seperti itu bakal cepat berantakan.

Di langkah ini, saya memisahkan views ke file terpisah (views.py) dan membiarkan Pyramid men-scan file tersebut untuk menemukan dekorator @view_config. Mulai dari sini, konfigurasi view dilakukan secara deklaratif, bukan lagi imperatif seperti sebelumnya.

Extra Credit
1. Tanda titik di depan .views berarti relative import terhadap package saat ini. Kalau ditulis tanpa titik ('views'), Pyramid akan mencari modul bernama views dari root package Python, bukan dari package aplikasi saat ini.
2. Karena dalam pengujian web, isi respons biasanya lebih panjang atau memiliki konten tambahan yang tidak kita pedulikan.