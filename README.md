# Tugas Kecil 1 IF2211 Strategi Algoritma

> by Irfan Sidiq Permana

## Daftar Konten

- [Informasi Umum](#informasi-umum)
- [Deskripsi Singkat](#deskripsi-singkat)
- [Setup dan Penggunaan](#setup-dan-penggunaan)
- [Kreator](#kreator)

## Informasi Umum

Penyelesaian Cyberpunk 2077 Breach Protocol dengan Algoritma Brute Force.

## Deskripsi Singkat

Cyberpunk 2077 Breach Protocol adalah minigame meretas pada permainan video Cyberpunk 2077. Minigame ini terdiri dari beberapa komponen,
yaitu Token (dua karakter alfanumerik seperti 7A, BD, dsb.), Matriks (berisi kumpulan token), Sekuens (rangkaian token yang harus dicocokkan),
dan Buffer (jumlah maksimal token yang dapat dipilih pemain). Pada permainan ini, pemain harus memilih token dimulai dari baris paling atas
matriks lalu bergerak secara vertikal, horizontal, vertikal, horizontal (bergantian) untuk memilih token selanjutnya hingga buffer penuh atau semua token berhasil dicocokkan. Buffer yang berisi rangkaian token yang dipilih kemudian dicocokkan oleh daftar sekuens yang ada, bila sekuens terdapat dalam buffer maka skor pemain akan bertambah sesuai dengan bobot sekuens tersebut. Tujuan pemain adalah mendapatkan skor setinggi mungkin.

## Setup dan Penggunaan

1. Clone repository ini dengan perintah `git clone https://github.com/IrfanSidiq/Tucil1_13522007.git`
2. Pindah current folder ke folder `src`
3. Untuk menjalankan program, ketik command berikut pada terminal: `python main.py` atau `python3 main.py`
4. Bila ingin menginput melalui file, masukkan file txt kedalam folder `test\input\` lalu ketikkan nama file saat diprompt oleh program.
   Format dari file txt adalah sebagai berikut:

```
buffer_size
matrix_width matrix_height
matrix
number_of_sequences
sequences_1
sequences_1_reward
sequences_2
sequences_2_reward
…
sequences_n
sequences_n_reward
```

Contoh file dapat dilihat pada file txt pada folder `test\input`.<br>

## Struktur File

```
.
├── README.md
├── __pycache__
│   ├── protocol.cpython-310.pyc
│   ├── protocol.cpython-311.pyc
│   ├── protocol.cpython-312.pyc
│   ├── util.cpython-310.pyc
│   └── util.cpython-311.pyc
├── img
│   └── contoh_input_nama_file.png
├── input
│   ├── input.txt
│   ├── percobaan3.txt
│   └── percobaan5.txt
├── main.py
├── output
│   ├── 2024-02-07 01-19-30.txt
│   ├── 2024-02-07 01-20-59.txt
│   ├── 2024-02-12 13-07-21.txt
│   └── 2024-02-12 13-07-47.txt
├── protocol.py
└── util.py
```

## Kreator

| NIM      | Nama                |
| -------- | ------------------- |
| 13522007 | Irfan Sidiq Permana |
