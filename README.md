Untuk membuat aplikasi *rapor online* menggunakan Python, Anda perlu mendesain sistem database yang mencakup berbagai data yang relevan, seperti data siswa, mata pelajaran, nilai, dan data lainnya yang mendukung. Berikut adalah struktur tabel yang bisa Anda buat untuk mendukung aplikasi rapor online:

### 1. *Tabel Siswa*
Tabel ini menyimpan informasi dasar tentang siswa.

- *ID_Siswa* (Primary Key)
- *Nama_Siswa*
- *NISN* (Nomor Induk Siswa Nasional)
- *Tanggal_Lahir*
- *Jenis_Kelamin*
- *Alamat*
- *Email*
- *Telepon*
- *Kelas*
- *Angkatan*
- *Tanggal_Masuk*

### 2. *Tabel Mata Pelajaran*
Tabel ini menyimpan daftar mata pelajaran yang diajarkan di sekolah.

- *ID_Mata_Pelajaran* (Primary Key)
- *Nama_Pelajaran*
- *Kode_Pelajaran*
- *Deskripsi_Pelajaran*
- *SKS* (Satuan Kredit Semester)
- *Guru_Pengajar* (Foreign Key ke Tabel Guru)

### 3. *Tabel Guru*
Tabel ini menyimpan data guru yang mengajar mata pelajaran.

- *ID_Guru* (Primary Key)
- *Nama_Guru*
- *NIP* (Nomor Induk Pegawai)
- *Email*
- *Telepon*
- *Alamat*
- *Mata_Pelajaran* (Bisa banyak, untuk relasi ke Tabel Mata Pelajaran)

### 4. *Tabel Nilai*
Tabel ini menyimpan nilai yang diberikan untuk setiap siswa dalam mata pelajaran tertentu.

- *ID_Nilai* (Primary Key)
- *ID_Siswa* (Foreign Key ke Tabel Siswa)
- *ID_Mata_Pelajaran* (Foreign Key ke Tabel Mata Pelajaran)
- *Nilai_Akhir*
- *Grade* (Misalnya: A, B, C, D, E)
- *Bobot_Nilai* (Nilai dalam angka, seperti 4.0 untuk A)
- *Tanggal_Ujian*

### 5. *Tabel Kehadiran*
Tabel ini menyimpan data kehadiran siswa pada setiap pertemuan kelas.

- *ID_Kehadiran* (Primary Key)
- *ID_Siswa* (Foreign Key ke Tabel Siswa)
- *ID_Mata_Pelajaran* (Foreign Key ke Tabel Mata Pelajaran)
- *Tanggal*
- *Status_Hadir* (Hadir, Tidak Hadir, Sakit, Izin, dll.)

### 6. *Tabel Rapor*
Tabel ini menyimpan rapor per siswa untuk semester tertentu, yang berisi ringkasan nilai dan evaluasi.

- *ID_Rapor* (Primary Key)
- *ID_Siswa* (Foreign Key ke Tabel Siswa)
- *Semester*
- *Tahun_Ajaran*
- *Rata_Rata_Nilai*
- *Status* (Lulus/Tidak Lulus)
- *Tanggal_Terbit*

### 7. *Tabel Kelas*
Tabel ini berisi data kelas yang ada di sekolah, yang berhubungan dengan siswa.

- *ID_Kelas* (Primary Key)
- *Nama_Kelas* (Misalnya: 10A, 12B, dll.)
- *Wali_Kelas* (Foreign Key ke Tabel Guru)
- *Tahun_Ajaran*

### 8. *Tabel Jadwal*
Tabel ini berisi data jadwal pelajaran yang diajarkan di sekolah.

- *ID_Jadwal* (Primary Key)
- *ID_Mata_Pelajaran* (Foreign Key ke Tabel Mata Pelajaran)
- *ID_Guru* (Foreign Key ke Tabel Guru)
- *Hari*
- *Jam*
- *Ruang*

---

### Desain Relasi Antara Tabel
- *Siswa* memiliki *nilai* untuk beberapa *mata pelajaran*.
- Setiap *mata pelajaran* diampu oleh *guru*.
- *Siswa* hadir dalam *pertemuan kelas* yang terkait dengan *mata pelajaran* tertentu.
- *Rapor* berisi ringkasan dari nilai siswa untuk setiap *semester*.
- *Kelas* adalah grup siswa yang memiliki wali kelas dan jadwal pelajaran masing-masing.

### Struktur Tabel Contoh dengan SQLAlchemy (Python)

Berikut adalah contoh bagaimana membuat struktur tabel di atas menggunakan Python dan SQLAlchemy.

python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Tabel Siswa
class Siswa(Base):
    __tablename__ = 'siswa'
    id_siswa = Column(Integer, primary_key=True)
    nama_siswa = Column(String)
    nisn = Column(String, unique=True)
    tanggal_lahir = Column(Date)
    jenis_kelamin = Column(String)
    alamat = Column(String)
    email = Column(String)
    telepon = Column(String)
    kelas = Column(String)
    angkatan = Column(Integer)
    tanggal_masuk = Column(Date)
