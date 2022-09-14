### Tugas 2 - Shafa Aleyda Tsabitah (2106634534)\_PBP F

## [Link Aplikasi Heroku](http://pbpshafa.herokuapp.com/katalog/)

### Bagan Request Client Django Web App beserta Responsenya & Kaitan antara urls.py, views.py, models.py, dan berkas html

![Bagan Request Client Django Web App & Response](bagan_tugas_2.jpg)

**Model**

Model akan berperan sebagai *interface* atau tampilan dari data. Model bertanggung jawab dalam memelihara data. Satu model (model class) dipetakan ke satu tabel *database*. *Field* data pada Model akan dipetakan oleh Django ke *field* data sesuai yang ada di *database*. 

Manipulasi data seperti *create, read, update,* dan *delete* (CRUD) data dapat dilakukan pada *database* dengan menggunakan *command* khusus yang dikenal dengan SQL. 

**View**

View merupakan bagian dari user *interface* yang berfungsi untuk menerima ***web request* dan mengembalikan *web response***. Eksekusi dari *business logic* juga merupakan salah satu fungsi dari View. *Response* yang diberikan dapat berupa isi konten HTML dari sebuah laman web, *redirect*, 404 error, ataupun hal lain yang dapat ditampilkan oleh web browser. 

**Template**

Template merupakan sebuah .html file yang umumnya ditulis menggunakan HTML, CSS, dan JavaScript. Template berperan untuk menyediakan *frontend* dan *layout* terhadap tampilan website. 

> Kaitan antara urls.py, views.py, model.py dan HTML pada bagan tersebut yaitu urls.py berperan sebagai module yang berfungsi untuk memetakan *redirect requests* dari project URLS ke app URLS dan mencari View yang sesuai. Pada module views.py terdapat fungsi yang dapat memetakan context berupa data hasil *query* ke HTML (template). Value dari context yang akan dipetakan diperoleh dengan menginisiasi objek dari model.py dimana objek tersebut akan berisi *query set* dari data-data hasil *query* View terhadap Model. Model menyediakan data tersebut melalui *information exchange* dengan *database*. 
 
### Alasan menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment

- *Virtual environments allow you to isolate your projects*

Setiap projects memiliki librarynya masing-masing. Ketika ingin melakukan perubahan di salah satu library, penggunaan *virtual environment* berfungsi sebagai 'isolasi' terhadap project yang ada didalamanya sehingga tidak akan mempengaruhi keseluruhan library pada project yang lain. 
- *Upgrade* pada project apabila dilakukan pada virtual environment tidak akan mengganggu project yang sudah memasuki fase *running*. 

Pembuatan web app berbasis Django bukan merupakan sebuah obligasi sehingga tetap memungkinkan untuk membuat web app berbasis Django tanpa menggunakan *virtual environment*. Namun, pembuatan web app berbasis Django menggunakan virtual environment dapat dikatakan sebagai langkah *best practice*. 

### Bagaimana cara kamu implementasi poin 1 sampai dengan poin 4

- Membuat fungsi show_katalog pada views.py 

show_katalog berfungsi untuk memetakan data dari Model pada models.py ke template katalog.html. Fungsi show_katalog memiliki parameter berupa *request* dan mengembalikan HTTP response (HTML) serta context. Data pada context akan ikut di-*render* sehingga hasil query pada context dapat muncul di halaman html. Isi dari {} menandakan *dictionary values* yang dapat ditambahkan ke konteks sesuai pada template. Values dari variabel tersebut diperoleh dari hasil *query* terhadap Model dan disimpan pada variabel yang memiliki *key name* yang sama dengan variabel context pada html. 

- *Routing* untuk memetakan fungsi show_katalog dan *routing* pada file urls.py yang terdapat pada folder katalog berfungsi untuk memetakan URL *path expressions* ke fungsi show_katalog. 

Pada module urls.py di folder aplikasi_django terdapat keyword include() di dalam path pada urlpatterns. Apabila Django bertemu keyword include() maka Django akan memangkas bagian dari URL yang sama sampai dengan bagian ‘katalog/’ dan akan menyatukan *string* yang tersisa dengan URLconf agar *request* user dapat diproses lebih lanjut. 

URL mapping pada folder project Django dan folder katalog berfungsi untuk *redirect requests* dari project URLS ke app URLS (katalog) dan berakhir di fungsi views yang sesuai (show_katalog).

- Menyediakan tempat untuk pemetaan data ke template pada katalog.html yang ditandai dengan {{}}

{{variable_name}} akan diisi dengan data hasil query melalui pemanggilan fungsi show_katalog pada views.py
- Deployment

Deployment dilakukan agar halaman HTML dapat diakses secara umum melalui URL yang tepat. Deployment dilakukan dengan memasukkan Heroku API Key dan Heroku App Name pada secrets variable repository GitHub.






    

