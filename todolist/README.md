### Tugas 4 - Shafa Aleyda Tsabitah (2106634534)\_PBP F

##### [Link Aplikasi Heroku](http://tugaspbpshafa.herokuapp.com/todolist)
#
#### Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?

CSRF token merupakan token unik, rahasia, dan tidak dapat diprediksi yang di-generate oleh aplikasi dari pihak server dan dikirimkan kepada klien bersamaan dengan HTTP request yang diminta oleh klien. 

Server akan menolak request dari klien apabila tidak terdapat token atau token yang diberikan invalid. CSRF berfungsi untuk mencegah serangan CSRF. 
Apabila tidak terdapat potongan kode pada elemen form, akan tampil halaman seperti berikut. 

![CSRF error](todolist/csrf_error.png)

Request yang diminta oleh klien akan ditolak oleh server karena tidak terdapat CSRF token pada elemen form di halaman html form. 

#### Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.

Elemen form dapat dibuat secara manual tanpa menggunakan generator form.as_table. Implementasi secara manual dilakukan dengan elemen HTML input yang dapat menghasilkan input-field untuk text input. 

#### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Server akan menerima HTTP request berupa path HTML form yang akan dikunjungi oleh klien. Server kemudian akan mencari fungsi views.py pada urls.py yang dapat menangani request tersebut. Request kemudian akan diarahkan ke fungsi pada views.py yang sesuai, dimana pada kasus ini fungsi views.py tersebut adalah fungsi form yang menerima parameter request. Pada fungsi form, request akan di-render menjadi sebuah halaman HTML yang berisi form. 

Setelah klien mengisi data pada form yang telah disediakan, maka fungsi form akan memvalidasi method dari request serta data hasil pengisian pada form . Apabila method dari request dan data pengisian pada form sudah valid, maka data pada form akan disimpan ke django database dengan command form_reference.save(). 

Pada halaman html utama yang akan menampilkan judul task, deskripsi task, dan tanggal pembuatan task, data tersebut akan diperoleh dari database yang sama dengan fungsi show_todolist pada views.py. Fungsi show_todolist kemudian akan memetakan data terhadap context yang sesuai pada template HTML. 

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

- Implementasi form registrasi, login, logout

Implementasi form registrasi, login, dan logout diawali dengan membuat tiga fungsi yang masing-masing berfungsi untuk menerima request untuk selanjutnya di-render menjadi form registrasi, login, maupun logout. Selanjutnya, dilakukan pemetaan routing terhadap masing-masing fungsi pada module urls.py. 

Halaman html untuk login dan register dibuat dengan elemen form sehingga dapat menerima response data dari klien. Elemen form tersebut memiliki atribut method berupa post sehingga form-data akan dikirimkan sebagai HTTP post transaction. Form-data kemudian akan masuk ke database dan klien akan diarahkan ke halaman selanjutnya yang sesuai dengan ketentuan yang ditetapkan. 

Halaman utama todolist dengan username pengguna, tombol tambah task baru, tombol logout, tabel berisi tanggal pembuatan task, judul task, dan deskripsi task

Tombol tambah task baru dan tombol logout diimplementasikan dengan menggunakan class button pada HTML yang dilengkapi dengan hyperlink menuju halaman HTML selanjutnya. Selanjutnya, data pada tabel diperoleh dengan user.todolist.all sehingga yang akan ditampilkan pada setiap user sesuai dengan data yang tersimpan pada setiap usernya. 

Judul task dan deskripsi task diperoleh dari data-form yang dimasukkan oleh user, sedangkan untuk tanggal pembuatan task menggunakan atribut auto_add_now pada model Date Field untuk model date dari task. 

- Halaman form untuk pembuatan task 

Mulanya, model akan didaftarkan pada site admin sehingga model dapat dikenali. Form untuk pembuatan task diimplementasikan dengan menggunakan ModelForm pada class TaskForm yang terdapat pada module forms.py. Pada class TaskForm diimplementasikan class Meta serta fields dari model Task yang akan diimplementasikan menggunakan form. 

Selanjutnya, request HTTP berupa path menuju form akan diimplementasikan pada fungsi form yang terdapat di views.py. Routing dari fungsi form dipetakan pada module urls.py. Halaman HTML dari pembuatan task kemudian diimplementasikan menggunakan elemen form.

- Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.
![dummy1](todolist/pengguna1_tugas3.png)
![dummy2](todolist/pengguna2_tugas4.png)
