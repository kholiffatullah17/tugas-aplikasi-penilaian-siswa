import sqlite3

# Koneksi ke database (atau buat database jika belum ada)
conn = sqlite3.connect('penilaian_siswa.db')
cursor = conn.cursor()

# Membuat tabel Siswa
cursor.execute('''
CREATE TABLE IF NOT EXISTS Siswa (
    No INTEGER PRIMARY KEY AUTOINCREMENT,
    Nama_siswa VARCHAR(50) NOT NULL,
    Nis INTEGER(20) UNIQUE NOT NULL,
    Tanggal_lahir DATETIME NOT NULL,
    Alamat TEXT NOT NULL,
    Jenis_kelamin TEXT CHECK(Jenis_kelamin IN ('Laki-laki', 'Perempuan')) NOT NULL,
    Agama TEXT CHECK(Agama IN ('Islam', 'Kristen', 'Katolik', 'Hindu', 'Buddha', 'Konghucu')) NOT NULL
)
''')

# Membuat tabel Penilaian
cursor.execute('''
CREATE TABLE IF NOT EXISTS Penilaian (
    No INTEGER PRIMARY KEY AUTOINCREMENT,
    Nis INTEGER(20) NOT NULL,
    Mata_pelajaran VARCHAR(20) NOT NULL,
    Nilai INTEGER(3) CHECK(Nilai BETWEEN 0 AND 100) NOT NULL,
    FOREIGN KEY (Nis) REFERENCES Siswa(Nis) ON DELETE CASCADE ON UPDATE CASCADE
)
''')

# Commit perubahan dan tutup koneksi
conn.commit()
conn.close()
