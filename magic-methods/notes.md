# Magic Methods
Atau dikenal juga dengan __dunder methods__ (dunder berarti double underscore) dimana disetiap method ini diawali dan diakhiri dengan double-underscore.
Berikut adalah contoh populer dari magic methods:

Special Methods | Description 
:---------------|:------------
.\_\_init_\_() | Initializer untuk python classes
.\_\_str_\_() dan .\_\_repr_\_() | String representation untuk object
.\_\_call_\_() | Membuat instance dari class menjadi callable
.\_\_len_\_() | support fungsi len()

Python dokumentasi mendefinisikan **special methods**:
> A method that is called implicitly by Python to execute a certain operation
> on a type, such as addition. Such methods have names starting and ending
> with double underscores.

Detail penting yang perlu dihinglight dari definisi ini. *Python implicitly calls special
methods to execute certain operations in your code.*
Contohnya dalam mengeksekusi `5 + 2` di REPL session, python menjalankan kode ini:
```python
>>> (5).__add__(2)
7
```

.\_\_add_\_() merupakan spesial method untuk integers yang mensupports 'operasi pertambahan'
yang typically kita run 5 + 2.
Walaupun dunder ini dapat kita *call* secara langsung pada code tapi dunder ini
sebenarnya tidak diperuntukan untuk itu. Jangan memanggilnya secara langsung pada code, kita harus biarkan *rely on python* untuk memanggil mereka secara otomatis dalam merespon 
pada sebuah operator yang diberikan.

Magic methods ada untuk banyak tujuan. Semua magic method mendukung fitur *built-in* dan 
memainkan peran penting dalam bahasa pemograman python. Dalam class yang di-*custom* 
contohnya, kita bisa menggunakan magic methods untuk membuat objek *callable*, *define how objects are compared*,
*tweak how you create objects*, dll.

Note:
> Karena magic methods mempunya arti penting bagi pythom, kita harus menghindari penamaan sebuah variable, fungsi,
> objek, dll menggunakan *double underscores*. Ini hanya akan membuat bingung programmer lain.


## Controlling the Object Creating Proccess
Saat membuat class dalam python, method paling umum dan sering digunakan mungkin adalah ._\_init__(). Method ini bekerja
sebagai **initializer** karena memperbolehkan kita untuk menyediakan *initial values* terhadap *instance attributes* 
yang kita define didalam class.

### Initializing Object With ._\_init__()
Python akan memanggil ._\_init__() method kapanpun kita memanggil constructor yang diberikan class.
Tujuan ._\_init__() ini adalah untuk menginisialisasikan *instance attributes* apapun yang kita berikan ke dalam class.

```python
>>> class Point:
...    def __init__(self, x, y):
...        self.x = x
...        self.y = y

>>> point = Point(10, 20)
>>> point.x
10
>>> point.y
20
```

Ketika kita membuat *instance* _**point**_ dengan memanggil *class contructor*, `Point()`, python secara otomatis akan
memanggil ._\_init__() menggunakan argument yang sama yang diberikan terhadap *class constructor*. Kita tidak perlu
memanggil fungsi ._\_init__(), python akan memanggilnya secara eksplisit. Sekarang .x dan .y attributes akan menyimpan
nilai yang kita *pass* kedalam *class constructor*


### Creating Object With ._\_new__()
Ketika kita memanggil sebuah *class constructor* untuk membuat *instance* yang baru dari sebuah class, Python secara implisit akan memanggil ._\_new__() method sebagai tahap pertama dalam proses *instantion*.
Method ini bertanggung jawab dalam membuat dan me-*return* sebuah objek kosong dari *underlying class*. Lalu python akan melemparkan objek yang baru dibuat tersebut ke ._\_init__() untuk initialisasi.
Default implementasi dari ._\_new__() sudah cukup untuk banyak kasus. Jadi, mungkin kita tidak akan terlalu membutuhkan method ini dalam menulis code di kebanyakan kasus.
Namun, kita akan menemukan method ini sangat berguna di beberapa kasus yang lebih *advance*. Sebagai contohnya, kita bisa menggunakan ._\_new__() untuk membuat subclass-subclass dari tipe **immutable** seperti *integer*, *float*, *tuple* dan *str*.
Contoh:
```python
class Storage(float):
    def __new__(cls, value, unit):
        instance = super().__new__(cls, value)
        instance.unit = unit
        return instance
```
pada contoh ini, kita akan melihat bahwa ._\_new__() adalah sebuah __*class methods*__ karena method ini mendapatkan *current class* (cls)
daripada *current instance* (self) sebagai sebuah argumen.
Kemudian kita akan menjalankan tiga step. Pertama, membuat sebuah *instace* baru dari class (cls) dengan memanggil ._\_new__() pada class **float** melalui fungsi built-in `super()`.
Pemanggilan ini membuat sebuah instance baru dari **float** dan menggunakan *value* sebagai sebuah argument.
Kemudian, kita mengkostumisasi *instance* baru dengan meng-*attach* sebuah .unit attribut secara dinamis.
Lalu akhirnya kita me-*return* instance baru tersebut yang *meet the default behavior of ._\_new__()*
```python
>>> disk = Storage(1024, "GB")

>>> disk
1024.0
>>> disk.unit
'GB'

>>> isinstance(disk, float)
True
```
.unit atribut ini bersifat mutable, jadi kita bisa menggantinya kapanpun kita mau. Tapi kita tidak bisa mengganti *numeric* tipe dari disk yaitu sebuah *float*.

### Representing Objects as Strings
