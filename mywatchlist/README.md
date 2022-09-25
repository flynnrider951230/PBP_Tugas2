### Tugas 3 - Shafa Aleyda Tsabitah (2106634534)\_PBP F
#

##### [Link Aplikasi Heroku HTML](https://pbpshafa.herokuapp.com/mywatchlist/html/) | [Link Aplikasi Heroku XML](https://pbpshafa.herokuapp.com/mywatchlist/xml/) | [Link Aplikasi Heroku JSON](https://pbpshafa.herokuapp.com/mywatchlist/json/)

#### Jelaskan perbedaan antara HTML, JSON, dan XML

HTML merupakan sebuah bahasa yang umumnya digunakan untuk membuat struktur dan konten dari sebuah laman web serta menampilkan data. 
JSON merupakan sebuah bahasa yang digunakan untuk menyimpan data dalam bentuk *key-value* dan melakukan proses transfer dari data. 
XML merupakan bahasa untuk mempermudah proses pertukaran data dan penyimpanan data serta digunakan untuk mendeskripsikan isi dari semua laman web dengan representasi simbol-simbol khusus 

Berdasarkan pengertian diatas, HTML dengan JSON dan XML merupakan dua hal yang berbeda secara harfiah maupun tujuan. Oleh karena itu perbedaan yang dapat ditelusuri lebih lanjut merupakan perbedaan antara JSON dan XML. 

| JSON          | XML           |
| ------------- |:-------------:|
| Objek pada JSON memiliki tipe | Data pada XML tidak terikat pada suatu tipe tertentu  |
| JSON dapat terdiri atas string, number, array, maupun boolean | XML hanya dapat menerima data dalam bentuk string     |
| JSON hanya compatible dengan tipe data primitive | XML compatible dengan berbagai jenis tipe data yang kompleks seperti charts, gambar, dan tipe data non-primitive lainnya  |
| Proses parsing menggunakan JavaScript lebih cepat karena ukuran file cenderung lebih kecil sehingga proses transmisi data lebih cepat dilakukan  | Proses parsing memakan waktu yang lama dan besar sehingga transmisi data yang dilakukan cenderung lama |
| Tidak dapat menulis comment di file JSON | File XML memungkinkan untuk ditulis comment |

#### Jelaskan mengapa kita membutuhkan *data delivery* dalam pengimplementasian sebuah platform 

Data-data yang akan ditampilkan pada platform umumnya disimpan pada berbagai jenis tempat penyimpanan data. Apabila dalam pembuatan platform diperlukan adanya pengiriman data dengan format spesifik, *data delivery* akan berfungsi untuk mengirimkan data dengan format yang sesuai terhadap requests.

#### Jelaskan bagaimana kamu mengimplementasikan checklist di atas

Pertama-tama, dilakukan **pembuatan aplikasi** dengan command `python manage.py startapp mywatchlist` untuk membuat sebuah direktori dari aplikasi baru *mywatchlist*. Nama aplikasi kemudian didaftarkan pada INSTALLED_APPS yang terdapat pada *settings.py* di dalam folder project_django sehingga aplikasi *mywatchlist* dapat didaftarkan pada django-app. 

Pada *urls.py* yang terdapat di folder project_django juga didaftarkan urls aplikasi mywatchlist. Kemudian, pada *models.py* yang terdapat pada folder mywatchlist akan dibuat jenis data yang akan ditampilkan pada laman web. Model data yang ada kemudian dimigrasi ke database Django lokal dengan menjalankan command `python manage.py makemigrations` untuk menyiapkan proses migrasi dan `python manage.py migrate` untuk melakukan migrasi data.

Pada sebuah folder baru bernama fixtures, dibuat sebuah file json baru untuk menyimpan value dari model data. Data kemudian dimasukkan ke database Django lokal dengan melakukan command` python manage.py loaddata initial_mywatchlist_data.json`. Setelah data dimasukkan ke dalam database Django lokal, selanjutnya akan dibuat beberapa fungsi pada *views.py* yang akan memetakan request terhadap jenis data yang sesuai. Pada views tersebut, juga terdapat proses pemetaan model data dengan value data. Routing dari fungsi-fungsi tersebut kemudian akan dibuat pada file *urls.p*y yang terdapat di mywatchlist.

Pengembalian data berupa XML atau JSON dilakukan dengan bantuan package django berupa HttpResponse dan serializers. Proses tersebut terjadi pada function yang terdapat di *views.py* yang dimulai dengan menyimpan hasil query data pada sebuah variabel dan kemudian variabel tersebut diserialisasi menjadi bentuk XML atau JSON sebelum di-*return*. 

> Postman HTML
> ![image](https://user-images.githubusercontent.com/91953656/191579478-26a77e14-8729-45e8-8226-0ddb48fb8558.png)

> Postman XML
> ![image](https://user-images.githubusercontent.com/91953656/191579589-0aee8990-c0fe-463d-93c7-36320f7f164e.png)

> Postman JSON
> ![image](https://user-images.githubusercontent.com/91953656/191579720-2bc3587d-daaa-4628-b44f-54b87872b16f.png)


