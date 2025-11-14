Analysis
Pada langkah ini saya belajar dasar penggunaan unit test di Python untuk memastikan bahwa setiap bagian kecil dari kode saya bekerja seperti yang diharapkan. Pyramid sendiri sangat mendukung testing, dan bahkan menyediakan helper seperti pyramid.testing untuk memudahkan membuat konfigurasi dummy serta request dummy.

Saya menggunakan pytest sebagai test runner karena lebih simpel, outputnya rapi, dan sudah jadi standar de facto di komunitas Python.

Dalam contoh ini, saya membuat satu test sederhana yang:
1. Memanggil view hello_world.
2. Membuat request palsu menggunakan testing.DummyRequest().
3. Menguji apakah status code dari response adalah 200.

Extra Credit
1. Jika saya ganti menjadi self.assertEqual(response.status_code, 404) Maka pytest akan error. Outputnya akan bilang:
2. Jika saya ganti menjadi x = not_defined_variable Lalu menjalankan pytest, maka error akan langsung muncul di terminal tanpa saya harus membuka browser. Ini menghemat waktu debugging dan memberi feedback sangat jelas.
3. Misal:
from pyramid.response import Response
def hello_world(request):
    return Response('Hi', status=404)
Saat saya menjalankan pytest, maka nilai status akan berubah jadi 404 dan test harus disesuaikan. Testing membantu memastikan kontrak kode (misalnya "view ini harus mengembalikan 200 OK") tetap konsisten.
4. self.assertIn(b'<h1>Hello</h1>', response.body)
Karena response.body adalah bytes, string HTML yang dicari juga harus dalam bentuk bytes (b'').
5. Karena:
- Import bisa memicu efek samping (misalnya konfigurasi Pyramid di-load, modul dijalankan, atau view memanggil sesuatu).
- Dengan meng-import di dalam test, setiap test terisolasi dan tidak saling mempengaruhi.
- Ini menjaga test tetap benar-benar “unit”, sehingga hanya kode yang relevan yang berjalan dalam lingkup test tersebut.
