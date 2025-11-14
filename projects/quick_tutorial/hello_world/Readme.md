Analysis
Pada tahap pertama ini saya belajar bagaimana menjalankan aplikasi Pyramid yang paling sederhana, bahkan hanya dalam satu file Python. Tujuannya supaya saya benar-benar memahami apa yang terjadi “di balik layar” sebelum masuk ke struktur project yang lebih besar.
1. if __name__ == '__main__': (titik mulai program)
2. Configurator sebagai pusat pengaturan aplikasi
3. View function menghasilkan Response
4. Waitress menjalankan aplikasi WSGI
5. Pyramid bisa sangat sederhana maupun sangat besar

Extra Credit
1. Why do we do this: print('Incoming request') ...instead of: print 'Incoming request'
- Sintaks print '...' adalah gaya Python 2.
- Pyramid (dan ekosistem modern) menggunakan Python 3, sehingga yang benar adalah fungsi print('...').
- Jika saya memakai cara Python 2, Python 3 akan langsung error.
2. What happens if you return a string of HTML? A sequence of integers?
- Pyramid/Python 3 mengharapkan Response atau sesuatu yang bisa diadopsi menjadi body HTTP dengan encoding tertentu.
- Web server tidak tahu cara mengubah angka menjadi payload HTTP. WSGI mengharuskan body berupa bytestring iterable, bukan integer.
3. Put something invalid, such as print xyz, in the view function. Kill your python app.py with ctrl-C and restart, then reload your browser. See the exception in the console?
Saat server dijalankan ulang dan saya mengakses browser, Python akan langsung menampilkan traceback di terminal karena:
- xyz tidak didefinisikan (NameError).
- Error terjadi sebelum view mengembalikan Response.
Ini menunjukkan bahwa semua error Python biasa langsung terlihat di console ketika kita menjalankan aplikasi dengan python app.py.
4. The GI in WSGI stands for "Gateway Interface". What web standard is this modelled after?
WSGI pada dasarnya adalah versi modern, lebih efisien, dan lebih Pythonic dari CGI.
CGI dulu digunakan untuk menjalankan skrip server-side (perl, python, dll), tapi lambat karena harus membuat proses baru untuk tiap request.