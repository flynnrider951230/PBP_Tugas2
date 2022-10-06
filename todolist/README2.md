### Tugas 5 - Shafa Aleyda Tsabitah (2106634534)\_PBP F

##### [Link Aplikasi Heroku](http://tugaspbpshafa.herokuapp.com/todolist)
#

#### Perbedaan dari inline, internal, dan external CSS dan kelebihan serta kekurangan masing-masing style 

Internal CSS merupakan jenis pemakaian CSS yang ditulis di dalam tag <style>. Tag <style> diletakkan pada bagian tag <head> dari halaman HTML. Internal CSS digunakan apabila pada satu halaman HTML ingin dibuat style yang unik dibandingkan dengan halaman HTML lainnya. 

Inline CSS merupakan jenis pemakaian CSS yang digunakan pada elemen. Atribut style ditambahkan pada tag pembuka dari suatu elemen. Inline CSS digunakan apabila ingin menambahkan style tertentu pada elemen yang spesifik. 

External CSS merupakan jenis pemakaian CSS yang mengacu pada file CSS secara utuh yang terletak diluar dokumen halaman HTML. Apabila ingin menggunakan metode external CSS, maka pada halaman HTML perlu disertakan tag link yang berisi referensi ke file CSS yang akan digunakan. 

| Internal CSS | Inline CSS | External CSS |
| -------------| -------------| :-------------:|
| Apabila terjadi perubahan, maka dampak perubahan hanya berpengaruh pada satu halaman HTML saja | Dapat dengan mudah mengatur perubahan style pada satu elemen | enulisan kode pada halaman HTML terlihat lebih teratur |
| Class dan id pada elemen dapat digunakan pada pemakaian internal CSS | Perbaikan kode menjadi lebih cepat | Waktu loading laman HTML menjadi lebih cepat |
| | Request HTTP akan menjadi lebih kecil dan waktu load website menjadi lebih cepat | File CSS dapat digunakan pada lebih dari satu halaman website sekaligus sehingga dapat mengurangi pengulangan pembuatan kode | 
  
| Internal CSS | Inline CSS | External CSS |
| -------------| -------------| :-------------:|
| Kurang efisien apabila penggunaan CSS ingin digunakan pada lebih dari satu file HTML | Kurang efisien | Potensi kegagalan dalam pemanggilan file CSS |
| Performa website akan menurun karena setiap laman website memiliki CSS yang berbeda-beda dan akan menyebabkan loading ulang  | Berpotensi terjadinya banyak pengulangan dari kode yang sama untuk setiap elemennya | Tidak praktis untuk mengatur perubahan pada elemen yang sifatnya minor |
| | Kode pada laman HTML relatif tidak rapih  | |
  
#### Tag HTML 5
- <.a> digunakan untuk membuat hyperlink
- <.b> bold style
- <.body> body dari dokumen
- <.br> line break
- <.div> membuat divisi atau section pada dokumen 
- <.form> membuat HTML form yang menerima input user 
- <.head> bagian head dari dokumen 
- <.h1> … <.h6> heading HTML
- <.img> menampilkan gambar
- <.input> mengatur input 
- <.link> hubungan antara dokumen dengan file eksternal 
- <.p> paragraf 
- <.style> menambahkan CSS internal 
- <.table> menampilkan tabel 
- <.title> judul halaman HTML 
- <.u> underline style
  
#### Tipe-tipe CSS Selector 
**CSS Universal Selector** memilih semua elemen yang terdapat pada halaman HTML 

**CSS Element Selector (Type Selector)** memilih semua elemen dengan tipe yang sama 

**CSS ID Selector** memilih seluruh elemen dengan ID yang sama. Developer sebelumnya harus mendeklarasikan ID yang akan digunakan pada elemen-elemen halaman HTML. 

**CSS Class Selector** digunakan untuk memilih elemen-elemen pada class yang sama. Pemakaiannya didahului oleh .nama_kelas {. . . }

**CSS Attribute Selector** digunakan untuk memiliki elemen yang memiliki attribute elemen serta value dari atribut yang sama. 

#### Implementasi Checklist
Sebelum memulai, saya menambahkan CDN bootstrap pada halaman base.html sehingga pada aplikasi dapat diimplementasikan bootstrap. 
  
  Mulanya, pada halaman todolist saya mengimplementasikan kelas cards dari Bootstrap untuk setiap satu task. Cards disusun baris per baris dan panjang cards mengikuti panjang kolom. 
  
  Pada setiap cards, ditampilkan jenis task yang akan dilakukan, tanggal pembuatan task, deskripsi dari task dan checkbox untuk menandakan bahwa task sudah diselesaikan. Keterangan dari task dan checkbox dipisahkan berdasarkan kolom pada setiap cardnya. 
  
  Selain itu, saya juga menambahkan kelas navbar pada bagian atas halaman HTML yang tertulis nama aplikasi, tombol yang mengarahkan ke halaman untuk menambahkan task baru dan tombol untuk logout.  Pada halaman login, registrasi dan penambahan task, saya meletakkan form-form yang menerima input pada card. Card diposisikan pada tengah halaman menggunakan bantuan beberapa class. Dengan CSS, saya memodifikasi tampilan card. 


