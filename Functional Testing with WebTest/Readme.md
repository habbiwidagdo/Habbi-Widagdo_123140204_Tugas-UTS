Analysis:
Pada langkah ini, saya telah berhasil mengimplementasikan functional testing (pengujian fungsional) end-to-end ke dalam proyek saya menggunakan pustaka webtest.

Prosesnya dimulai dengan menambahkan webtest sebagai dependensi pengembangan (development dependency) di dalam file setup.py, di bawah kunci extras_require={'dev': ...}. Saya kemudian menginstal dependensi baru ini menggunakan perintah pip install -e ".[dev]", yang memastikan webtest dan pytest tersedia di virtual environment saya.

Selanjutnya, saya memperluas file tutorial/tests.py dengan menambahkan class tes baru bernama TutorialFunctionalTests. Berbeda dengan TutorialViewTests yang merupakan unit test murni, class ini dirancang untuk menguji aplikasi secara fungsional.

Di dalam metode setUp untuk TutorialFunctionalTests, saya melakukan langkah-langkah kunci berikut:
1. Mengimpor entry point main dari aplikasi saya (from tutorial import main).
2. Membuat instansi aplikasi WSGI dengan memanggil app = main({}).
3. Membungkus instansi aplikasi app tersebut dengan webtest.TestApp. Objek self.testapp inilah yang menjadi antarmuka saya untuk berinteraksi dengan aplikasi.

TestApp dari webtest secara cerdas mensimulasikan permintaan HTTP ke aplikasi WSGI tanpa perlu menjalankan server HTTP yang sesungguhnya. Ini memungkinkan tes berjalan dengan sangat cepat.

Pada metode tes test_hello_world yang baru, saya menggunakan self.testapp.get('/', status=200). Perintah ini mensimulasikan peramban (browser) yang membuat permintaan GET ke path root (/) dan sekaligus menegaskan (assert) bahwa respons yang diterima memiliki status kode HTTP 200 (OK).

Poin terpenting adalah asserter (penegasan) berikutnya: self.assertIn(b'<h1>Hello World!</h1>', res.body). Di sini, saya tidak lagi menguji view callable secara terisolasi. Sebaliknya, saya memeriksa res.body, yang merupakan isi (payload) mentah dari respons HTTP yang disimulasikan. Saya memastikan bahwa fragmen HTML <h1>Hello World!</h1> benar-benar ada di dalam respons yang dikirimkan.

Ketika saya menjalankan pytest tutorial/tests.py -q, kedua tes (satu unit test lama dan satu functional test baru) berhasil dijalankan (..). Ini menunjukkan bahwa pendekatan webtest terintegrasi mulus dengan pytest.

Extra Credit:
Tes fungsional saya menggunakan literal b'' (misalnya b'<h1>Hello World!</h1>') karena saya membandingkannya dengan atribut res.body dari objek respons webtest.

Atribut res.body mewakili payload HTTP mentah (raw HTTP payload) yang dikirimkan oleh aplikasi. Protokol HTTP pada dasarnya mentransmisikan aliran bytes, bukan string teks (Unicode).