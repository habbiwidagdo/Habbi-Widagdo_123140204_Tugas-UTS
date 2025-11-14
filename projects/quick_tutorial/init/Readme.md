Analysis
Di langkah ini saya belajar bagaimana Pyramid memisahkan configuration dari code, dan bagaimana .ini berperan besar untuk mengatur aplikasi tanpa harus mengutak-atik kode Python setiap saat.
1. .ini digunakan untuk mem-boot aplikasi
pserve development.ini --reload, maka pserve membaca [app:main], menemukan use = egg:tutorial, lalu mencari entry point tutorial:main di setup.py.
2. Entry point di setup.py sebagai "petunjuk" lokasi WSGI app
Pyramid mengenali bahwa fungsi main() dalam package tutorial adalah pembuat aplikasi.
3. Kode startup dipindah ke tutorial/__init__.py
Di sini fungsi main() berisi:
- inisialisasi Configurator
- definisi route dan view
- membuat WSGI app
4. .ini juga mengatur server WSGI & logging
- [server:main] menentukan server apa yang dipakai dan portnya (di sini Waitress).
- Logging juga dikonfigurasi lewat .ini, yang membuat output konsol rapi.
5. --reload sangat membantu dev
Ketika file Python atau .ini berubah, server otomatis restart.
Tidak perlu manual stop–start.

Extra Credit
1. Ya, sangat bisa.
Sama seperti di langkah sebelumnya, kita bisa membuat konfigurator, membuat WSGI app, dan menjalankan Waitress hanya lewat Python code.
2. Bisa, Biasanya dipakai untuk:
- development.ini (debug on, toolbar aktif, logging verbose)
- production.ini (debug off, logging minim, konfigurasi server berbeda)
- testing.ini (setting khusus untuk unit/functional test)
3. Karena dalam Python, ketika kita menulis: tutorial:main
4. **settings adalah keyword arguments dictionary unpacking. ** berarti semua pasangan key=value dimasukkan ke dalam satu dictionary bernama settings.