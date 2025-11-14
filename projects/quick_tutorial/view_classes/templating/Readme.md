Analysis
Pada tahap ini, saya mengubah struktur view dari fungsi bebas menjadi class-based views agar kode lebih terorganisir.
Dua view (home dan hello) sekarang menjadi method dalam satu kelas TutorialViews.
Dengan pendekatan ini, saya bisa mengelompokkan view yang berhubungan dan juga menaruh konfigurasi umum (seperti renderer='home.pt') di tingkat kelas menggunakan @view_defaults.
Hasil pengujian menunjukkan semua tes tetap lolos tanpa error, artinya fungsionalitas masih sama, tapi struktur kode jadi lebih rapi dan mudah dikembangkan.

Extra Credit
- Kenapa pakai view class? Karena beberapa view bisa berbagi logika atau data yang sama, jadi lebih efisien kalau dikelompokkan ke dalam satu class.
- Perubahan di test case: Karena view sekarang berupa class, di test saya harus membuat instance dulu (inst = TutorialViews(request)) sebelum memanggil method-nya (inst.home()).