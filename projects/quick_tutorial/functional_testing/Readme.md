Analysis
Pada tahap ini, implementasi pengujian fungsional end-to-end menggunakan WebTest telah berhasil diselesaikan. Hasilnya mengkonfirmasi bahwa metode pengujian ini dapat dieksekusi secara bersamaan dengan unit test standar (melalui pytest), di mana semua keluaran laporannya terkonsolidasi secara rapi.

Extra Credit – Kenapa functional test pakai b''
karena res.body mengembalikan data dalam bentuk bytes, bukan string biasa. Kalau saya pakai string tanpa b'', perbandingan akan error karena tipe data tidak cocok.