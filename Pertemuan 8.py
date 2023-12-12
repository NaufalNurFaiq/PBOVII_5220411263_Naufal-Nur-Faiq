class Katalog:
    def cari(self, kata_kunci):
        print(f"Mencari katalog dengan kata kunci: {kata_kunci}")

class PerpusItem:
    def __init__(self, judul, subjek, lokasi_penyimpanan, info):
        self.judul = judul
        self.subjek = subjek
        self.lokasi_penyimpanan = lokasi_penyimpanan
        self.info = info

class Pengarang:
    def __init__(self, nama):
        self.nama = nama

    def info_cari(self):
        print(f"Menampilkan informasi pencarian untuk pengarang: {self.nama}")

class Buku(PerpusItem):
    def __init__(self, ISBN, pengarang, jumlah_halaman, ukuran):
        super().__init__("Buku", "Umum", "Rak A", pengarang)
        self.ISBN = ISBN
        self.jumlah_halaman = jumlah_halaman
        self.ukuran = ukuran

class Majalah(PerpusItem):
    def __init__(self, volume, issue, judul, subjek, lokasi_penyimpanan, pengarang):
        super().__init__(judul, subjek, lokasi_penyimpanan, pengarang)
        self.volume = volume
        self.issue = issue

class DVD(PerpusItem):
    def __init__(self, aktor, genre, judul, subjek, lokasi_penyimpanan, pengarang):
        super().__init__(judul, subjek, lokasi_penyimpanan, pengarang)
        self.aktor = aktor
        self.genre = genre

katalog = Katalog()
katalog.cari("Python")

pengarang_buku = Pengarang("Demit")
pengarang_buku.info_cari()

buku1 = Buku("123456789", pengarang_buku, 200, "A5")
print(f"Informasi Buku: {buku1.judul}, {buku1.subjek}, {buku1.lokasi_penyimpanan}, {buku1.info.nama}, {buku1.ISBN}, {buku1.jumlah_halaman}, {buku1.ukuran}")
