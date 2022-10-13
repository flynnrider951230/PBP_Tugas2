### Tugas 6 - Shafa Aleyda Tsabitah (2106634534)\_PBP F

#### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming 

Asynchronous programming merupakan jenis programming yang tidak terikat terhadap input dan output. Hal ini berarti asynchronous programming tidak menjalankan program secara berurutan (sequential). Request pada asynchronous dijalankan secara bersamaan dan paralel. Apabila terdapat request yang gagal, hal tersebut tidak berpengaruh terhadap request lainnya. 

Keuntungan dari implementasi asynchronous programming 
- Meningkatkan user-experience
- Meningkatkan volume request yang dapat diterima oleh server 

Kelemahan dari implementasi asynchronous programming 
- Kompleks dalam pengembangannya
- Jumlah request yang berlebihan dapat menyebabkan aplikasi berjalan lebih lambat 

Synchronous programming merupakan jenis programming yang terikat terhadap pemetaan operasi I/O sehingga operasi harus diselesaikan terlebih dahulu agar operasi yang lain dapat dijalankan. 

Keuntungan dari implementasi synchronous programming 
- Lebih sederhana dalam pengembangannya 
- Lebih mudah ‘terbaca’ oleh search engines 

Kelemahan dari implementasi synchronous programming 
- Memiliki waktu loading time yang lebih lama dibandingkan dengan asynchronous programming 
- Memerlukan resource yang besar 

#### Event-Driven Programming 

Event-driven programming merupakan metode penulisan program yang memiliki respon terhadap suatu kejadian(event). Event dapat dipicu oleh user ataupun faktor lainnya. Bagian yang merespon terhadap event tersebut dikenal sebagai event handlers. 

#### Penerapan Asynchronous Programming pada AJAX

AJAX memungkinkan web app dan browsers untuk menerima dan mengirimkan data dari server secara asinkronus. Implementasi AJAX pada browsers dan web app tidak lagi memerlukan aktivitas refresh halaman secara keseluruhan agar dapat menampilkan data yang telah diubah. Hal tersebut dapat terjadi karena bagian untuk menampilkan data serta bagian untuk melakukan proses pengiriman/pertukaran saling terpisah.

#### Bagaimana cara kamu implementasi checklist di atas

Cara saya untuk mengimplementasikan checklist di atas dimulai dengan mebuat fungsi baru pada views.py yang bernama show_todolist_json untuk mengembalikan data models dengan format json. Hal tersebut dilakukan dengan menserialisasi objek data pada models terlebih dahulu. Kemudian, pada urls.py saya membuat routing terhadap fungsi show_todolist_json agar fungsi dapat diakses. Saya kemudian membuat copy html page todolist.html dengan nama todolist_ajax.html dengan menghapus beberapa bagian dan menambahkan script ajax dan bootstrap pada bagian head. Saya kemudian membuat fungsi baru pada views.py yang berfungsi untuk memetakan request ke halaman todolist_ajax.html. Fungsi baru tersebut juga sekaligus saya buat routingnya pada urls.py. Selanjutnya, saya memulai prosedur AJAX get untuk melakukan request terhadap data yang bersesuain. AJAX get dilakukan sembari melakukan iterasi pada setiap data pada yang tersimpan di file JSON dengan memanfaatkan keyname dari value data tersebut. AJAX post kemudian turut saya implementasikan untuk memetakan data pada data cell table yang bersesuaian. Selanjutnya, saya mengimplementasikan form pada modal dan membuat fungsi yang baru yang menerima request untuk membuat task baru pada form tersebut serta routingnya. 
