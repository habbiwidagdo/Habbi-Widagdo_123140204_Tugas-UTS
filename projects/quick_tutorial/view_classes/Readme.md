Analysis
Pada tahap ini, saya belajar bagaimana cara mengubah view function biasa menjadi sebuah view class di Pyramid. Tujuannya bukan menambah fitur baru, tapi lebih ke menata struktur kode supaya rapi dan scalable kalau nanti aplikasinya makin besar.

Awalnya semua view yang saya buat berdiri sendiri sebagai fungsi. Tapi ketika beberapa view punya hubungan atau memakai konfigurasi yang sama (misalnya templatenya sama), lebih masuk akal kalau digabung dalam satu kelas. Dengan begitu:
- view-view tersebut lebih terorganisir,
- konfigurasi yang berulang bisa dipusatkan di @view_defaults,
- dan kita bisa menyimpan state atau helper melalui __init__.

Perubahan paling besar ternyata ada di bagian unit test. Karena sekarang view bukan fungsi bebas lagi, saya harus membuat instance dari kelas view (TutorialViews(request)) sebelum memanggil metodenya. Sisanya tetap sama seperti sebelumnya. Setelah itu semua test berjalan normal (4 passed) dan aplikasi tetap bisa dijalankan seperti biasa.