# Struktur Database Sekolah

## Deskripsi

Struktur database ini digunakan untuk sistem informasi sekolah, yang mencakup data siswa, penilaian, dan informasi kelas. Relasi antar tabel dijelaskan melalui *foreign key* untuk menjaga integritas data.

---

## Tabel `siswa`

| Kolom          | Tipe Data          | Keterangan                       |
|-----------------|--------------------|-----------------------------------|
| `no`           | INT (Auto Increment) | Primary Key                      |
| `nama_siswa`   | VARCHAR(50)        | Nama siswa, maksimal 50 karakter |
| `nis`          | INT(20)            | Nomor Induk Siswa (Primary Key)  |
| `tanggal_lahir`| DATETIME           | Tanggal dan waktu lahir siswa    |
| `alamat`       | TEXT               | Alamat lengkap                   |
| `jenis_kelamin`| ENUM('L', 'P')     | Pilihan: Laki-laki (L), Perempuan (P) |
| `agama`        | ENUM('Islam', 'Kristen', 'Hindu', 'Budha', 'Lainnya') | Agama siswa |

---

## Tabel `penilaian`

| Kolom           | Tipe Data          | Keterangan                      |
|------------------|--------------------|----------------------------------|
| `no`            | INT (Auto Increment) | Primary Key                     |
| `nis`           | INT(20)            | Foreign Key dari tabel `siswa`  |
| `mata_pelajaran`| VARCHAR(20)        | Nama mata pelajaran             |
| `nilai`         | INT(3)             | Nilai siswa                     |

---

## Tabel `kelas`

| Kolom           | Tipe Data          | Keterangan                       |
|------------------|--------------------|----------------------------------|
| `no`            | INT (Auto Increment) | Primary Key                     |
| `id_kelas`      | INT                | Primary Key                      |
| `kelas`         | VARCHAR(20)        | Nama kelas                       |
| `jurusan`       | VARCHAR(20)        | Jurusan kelas                    |

---
