class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan:", self.jurusan.nama_jurusan)
# kelas mahasiswa memiliki tiga atribut: nama,nim,jurusan dan method tampilkan info digunakan untuk menampilkan informasi mahasiswa seperti nama,nim,dan jurusan

class Jurusan:
    def __init__(self, nama_jurusan):
        self.nama_jurusan = nama_jurusan
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa", self.nama_jurusan + ":")
        for mahasiswa in self.daftar_mahasiswa:
            mahasiswa.tampilkan_info()
# kelas jurusan memiliki dua atribut: nama_jurusan dan daftar_mahasiswa. ada juga method tambah_mahasiswa digunakan untuk menambahkan objek mahasiswa ke daftar mahasiswa jurusan. tampilkan_daftar_mahasiswa, digunakan untuk menampilkan daftar mahasiswa yang terdftar dalam jurusan

class Universitas:
    def __init__(self, nama_universitas):
        self.nama_universitas = nama_universitas
        self.daftar_jurusan = []

    def tambah_jurusan(self, jurusan):
        self.daftar_jurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di", self.nama_universitas + ":")
        for jurusan in self.daftar_jurusan:
            print(jurusan.nama_jurusan)
# kelas universitas memiliki dua atribut: nama_universitas dan daftar_jurusan. memiliki method tambah_jurusan digunakan untuk menambahkan objek jurusan ke daftar jurusan universitas. dan method tampilkan_daftar_jurusan digunakan untuk menampilkan daftar jurusan yang ada di universitas.

# 1. Implementasi kelas Mahasiswa, Jurusan, dan Universitas

# 2. Membuat objek Universitas "XYZ University"
universitas_xyz = Universitas("XYZ University")
#Pada bagian ini, objek universitas_xyz dibuat dengan menggunakan kelas Universitas. Nama universitasnya adalah "XYZ University".

# 3. Membuat objek Jurusan "Teknik Informatika" dan menambahkannya ke dalam Universitas XYZ
jurusan_ti = Jurusan("Teknik Informatika")
universitas_xyz.tambah_jurusan(jurusan_ti)
#Objek jurusan_ti dibuat dengan menggunakan kelas Jurusan, dan memiliki nama jurusan "Teknik Informatika". Selanjutnya, objek jurusan ini ditambahkan ke dalam daftar jurusan di universitas_xyz menggunakan method tambah_jurusan.

# 4. Membuat objek Mahasiswa "Mezi" dengan NIM "G1A022077" dan menambahkannya ke dalam Jurusan Teknik Informatika di Universitas XYZ
mahasiswa1 = Mahasiswa("Mezi", "G1A022077", jurusan_ti)
jurusan_ti.tambah_mahasiswa(mahasiswa1)
#Objek mahasiswa1 dibuat dengan menggunakan kelas Mahasiswa dan memiliki nama "Mezi", NIM "G1A022077", serta jurusan yang ditetapkan sebagai objek `jurusan_ti

# 5. Menampilkan daftar jurusan yang ada di Universitas XYZ
universitas_xyz.tampilkan_daftar_jurusan()

# 6. Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ
jurusan_ti.tampilkan_daftar_mahasiswa()
