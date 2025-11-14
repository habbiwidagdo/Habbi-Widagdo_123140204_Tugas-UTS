Analysis
Di modul ini, terdapat hal yang di pelajari diantaranya:
1. Route home yang otomatis redirect ke /plain pakai HTTPFound.
2. Route plain yang menampilkan nama dari query parameter, kalau ga ada nama dikasih default 'No Name Provided'.
Atur content_type sama body di response. Unit test ngecek logika redirect dan response body, sementara functional test ngecek di app beneran. Jadi gampang nge-test redirect, ambil data dari URL, dan ngubah response tanpa ribet.

Extra Credit
Iya, sebenarnya kita bisa memakai raise maupun return untuk HTTPFound.
Perbedaan utamanya:
- return = mengembalikan response sebagai hasil normal.
- raise = memicu mekanisme exception yang Pyramid tangani untuk menghasilkan response redirect.