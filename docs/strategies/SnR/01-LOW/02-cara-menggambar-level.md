# Modul 02 — Cara Menggambar Level SnR yang Benar

**Level:** 🟢 LOW  
**Estimasi waktu baca:** 20–25 menit  
**Prasyarat:** Modul 01 — Apa itu SnR

---

## Tujuan Modul

Setelah membaca modul ini, kamu akan:
- Memahami perbedaan body candle vs wick dalam menentukan level
- Tahu berapa banyak sentuhan yang cukup untuk memvalidasi sebuah level
- Bisa membedakan level kuat vs level lemah
- Menghindari kesalahan umum dalam menggambar level SnR

---

## 1. Alat yang Dibutuhkan

Untuk menggambar level SnR, kamu hanya butuh:
- **Horizontal line tool** di platform charting (TradingView, MT4, MT5)
- Chart dengan minimal 3–6 bulan data historis
- Mata yang terlatih untuk melihat "area di mana harga pernah bereaksi"

---

## 2. Body vs Wick: Mana yang Digunakan?

Ini adalah perdebatan klasik dalam komunitas SnR. Jawabannya: **keduanya penting, tapi untuk tujuan berbeda.**

### 2.1 Menggambar dengan Body Candle

Gunakan **harga close/open** (body candle) sebagai referensi level ketika:
- Kamu ingin menemukan level di mana **konsensus pasar** berada
- Mencari area di mana harga "menetap" (tidak sekadar menyentuh)
- Membuat supply/demand zone

```
LEVEL BERDASARKAN BODY CANDLE:

Harga
│
1.1200 ─────────────────────────────────────────────
│          ┌──┐        ┌──┐        ┌──┐
│          │  │        │  │        │  │
│          │  │        │  │  ╭─────┤  │
│          │  ╰────────┤  │──╯     │  │
│          │           └──┘        │  │
│          │             ↑         └──┘
│          └──┘     Level ditarik   ↑
│          ↑        dari BODY       Body close
│          Body close               di sekitar 1.1200
│          di sekitar 1.1200
│
── Level ditarik dari titik di mana BODY candle menutup/membuka
   bukan dari ujung wick
```

### 2.2 Menggambar dengan Wick (High/Low)

Gunakan **high/low** (ujung wick) ketika:
- Kamu ingin tahu **sejauh mana** harga mencoba nembus sebelum ditolak
- Membuat batas "no man's land" di area SnR
- Menentukan zona "bahaya" di sekitar level

```
LEVEL BERDASARKAN WICK:

Harga
│                     ↑ Wick tertinggi (pernah dicoba tapi ditolak)
1.1250 ─────────────────────────────────────────────  ← Batas atas wick
│          │           │           │
│         ─┤─         ─┤─         ─┤─
│          │           │           │
│         ┌┴┐         ┌┴┐         ┌┴┐
│         │ │         │ │         │ │
│         └─┘         └─┘         └─┘
│
1.1200 ─────────────────────────────────────────────  ← Body close
│
└─────────────────────────────────────────────────────→ Waktu
```

### 2.3 Rekomendasi Praktis

```
CARA TERBAIK: Buat ZONE, bukan line

                    ┌─────────────────────┐
1.1250 ─ ─ ─ ─ ─ ─ ┤  RESISTANCE ZONE    ├ ─ ─ ─ ─ ─  ← Batas atas (dari wick)
                    │  (shadow area)      │
1.1200 ════════════ ┤  ─────────────────  ├ ═══════════  ← Level utama (dari body)
                    │                     │
1.1180 ─ ─ ─ ─ ─ ─ ┤                     ├ ─ ─ ─ ─ ─  ← Batas bawah zone
                    └─────────────────────┘

Cara membuat zone:
- Batas atas: dari ujung wick tertinggi di area itu
- Level utama: dari body close/open mayoritas candle
- Batas bawah: dari body close/open candle yang paling rendah
```

---

## 3. Berapa Banyak Sentuhan yang Cukup?

### Minimum Valid: 2 Sentuhan

Level dengan **2 sentuhan** sudah bisa dianggap valid, tapi kekuatannya masih rendah.

### Standard: 3 Sentuhan

**3 sentuhan** adalah standar minimum untuk level yang dianggap signifikan oleh kebanyakan trader.

### Kuat: 4+ Sentuhan

**4 sentuhan atau lebih** mengindikasikan level yang sangat diperhatikan oleh market.

```
VISUALISASI KEKUATAN BERDASARKAN SENTUHAN:

1 SENTUHAN (invalid):
─────────────────────────────────────────────────── level
              │
              ↑ Harga menyentuh 1x → belum cukup bukti

2 SENTUHAN (lemah tapi valid):
─────────────────────────────────────────────────── level
              │                   │
              ↑                   ↑
         Sentuhan 1          Sentuhan 2

3 SENTUHAN (standar kuat):
─────────────────────────────────────────────────── level
              │                   │              │
              ↑                   ↑              ↑
         Sentuhan 1          Sentuhan 2    Sentuhan 3
              ★★★              ★★★★           ★★★★★
           Probabilitas bounce meningkat di setiap sentuhan

4+ SENTUHAN (sangat kuat):
─────────────────────────────────────────────────── level
              │         │         │         │
              ↑         ↑         ↑         ↑
              1         2         3         4
         ════════════════════════════════════════
         Level ini adalah "highway" utama market
```

---

## 4. Strong vs Weak Level

### 4.1 Ciri-ciri Level KUAT (Strong Level)

```
STRONG LEVEL — Ciri-ciri Visual:

Harga
│
1.1200 ════════════════════════════════════════════
│         │       │         │          │
│    ╭────╯  ╭────╯    ╭────╯     ╭────╯
│    │       │         │          │
│    ╰───    ╰───      ╰───       ╰───
│
Ciri-ciri STRONG level:
✓ 3+ sentuhan jelas
✓ Setiap bounce menghasilkan pergerakan signifikan (bukan sedikit)
✓ Ada candle kuat (hammer, engulfing) di setiap sentuhan
✓ Berada di timeframe tinggi (H4, D1, W1)
✓ Sejajar dengan round number (1.1200, 1.1000, 1.0800)
✓ Volume spike saat harga menyentuh level
✓ Sudah bertahan minimal beberapa minggu/bulan
```

### 4.2 Ciri-ciri Level LEMAH (Weak Level)

```
WEAK LEVEL — Ciri-ciri Visual:

Harga
│
1.1167 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
│              │
│         ╭───╯
│         ╰────────────────────────────────────────
│
Ciri-ciri WEAK level:
✗ Hanya 1-2 sentuhan
✗ Level di angka tidak bulat (1.1167 dll)
✗ Dari timeframe rendah (M5, M15)
✗ Candle di level itu kecil/doji — tidak ada tekanan jelas
✗ Bounce kecil, harga langsung turun lagi
✗ Level baru terbentuk — belum teruji waktu
```

---

## 5. Cara Menggambar yang Benar vs Salah

### Contoh: Resistance di Chart

```
CARA SALAH — Menggambar terlalu presisi:

Harga
│
1.1215 ════════════════════════════════════
│         │   ↑ body close        │
│    ╭────╯   1.1215 persis        ╰────╮
│    ╰───────────────────────────       │
│                                       ↑
│                          level ditarik dari 1 titik
│                          → tidak mencerminkan realita

Masalah:
- Harga jarang berhenti di angka persis yang sama
- Pendekatan ini terlalu kaku
- Kamu akan terus salah "level tertembus"
```

```
CARA BENAR — Menggambar sebagai zone:

Harga
│
1.1230 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ← Batas atas (wick max)
│              │               │                │
│         ─┬──┘           ─┬──┘            ─┬──┘
│          │               │                │
1.1200 ════╪═══════════════╪════════════════╪════  ← Level utama (body area)
│          │               │                │
│         ─┘              ─┘               ─┘
│
1.1185 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ← Batas bawah (body min)
│

Penjelasan:
- Batas atas dari wick tertinggi di area itu (1.1230)
- Level utama adalah "inti" zone (1.1200)
- Batas bawah dari body terendah (1.1185)
- Zone ini mencakup semua variasi sentuhan → lebih realistis
```

### Contoh: Support di Chart

```
CARA BENAR menggambar Support Zone:

Harga
│
│
│    ┌──┐        ┌──┐             ┌──┐
│    │  │        │  │             │  │
│    │  │        │  │             │  │
│    │  │   ┌──┐ │  │  ┌──┐ ┌──┐ │  │
│    │  │   │  │ │  │  │  │ │  │ │  │
│    │  │   │  │ │  │  │  │ │  │ │  │
│    │  ╰───┤  ╰─┤  │  │  │ │  ╰─┤  │
│    │      │    │  ╰──┤  ╰─┤    │  │
1.0820 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ← Batas bawah (wick min)
│    │  ╭───┤  ╭─┤      ╰────┤  ╭─┤
│    │  │   │  │ │           │  │ │
1.0840 ════════════════════════════════════  ← Level utama (body area)
│
1.0860 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ← Batas atas (body max)
│
│    Zone support: 1.0820 - 1.0860
│    Entry optimal: Di dalam zone (bukan persis di garis)
```

---

## 6. Berapa Banyak Level yang Ideal?

```
TERLALU SEDIKIT (blind):               TERLALU BANYAK (chaos):

Harga                                   Harga
│                                       │  ─────── 1.1280
│                                       │  ─────── 1.1250
│                                       │  ─────── 1.1230
│                                       │  ─────── 1.1210
│  ═════════ 1.1200                     │  ═════════ 1.1200
│                                       │  ─────── 1.1180
│                                       │  ─────── 1.1165
│                                       │  ─────── 1.1150
│                                       │  ─────── 1.1135
│  ═════════ 1.0900                     │  ─────── 1.1100
│                                       │  ═════════ 1.1050
│                                       │  ─────── 1.1020
│                                       │  ─────── 1.1000
│                                       │  ─────── 1.0980
│  ═════════ 1.0600                     │  ─────── 1.0950
│                                       │  ═════════ 1.0900
                                        (tidak tahu mana yang penting)

IDEAL: 3-5 Key Level + beberapa minor level yang jelas

Harga
│  ─ ─ ─ ─  1.1230 (minor resistance)
│  ═════════ 1.1200 (KEY resistance)    ← Focus di sini
│
│  ─ ─ ─ ─  1.1050 (minor support)
│  ═════════ 1.0900 (KEY support)       ← Focus di sini
│
│  ─ ─ ─ ─  1.0750 (minor support)
│  ═════════ 1.0600 (KEY support)       ← Focus di sini
```

---

## 7. Studi Kasus: Menggambar Level GBPUSD H4

```
Studi Kasus: GBPUSD H4 — Proses Menggambar Level
══════════════════════════════════════════════════

LANGKAH 1: Lihat chart mentah (tanpa level)

Harga
│         ┌┐    ┌──┐             ┌┐
│       ┌─┘└─┐  │  └─┐        ┌─┘└─┐
│  ┌──┐ │    └──┘    └──┐  ┌──┘    └──────
│  │  └─┘               └──┘
│  │
│──┘
│
└────────────────────────────────────────────────→

LANGKAH 2: Identifikasi HIGH dan LOW yang signifikan

Harga
│             H2
│         ┌┐  ↕    ┌──┐             H3
│       ┌─┘└─┐     │  └─┐    ┌┐    ↕
│  ┌──┐ │    └──┘       └──┐ └─┐
│  │H1└─┘↕               L2└──┘L3  ← LOW yang mirip (potential support)
│  │  L1
│──┘
│
Identifikasi:
H1 = 1.2850 (high pertama)
H2 = 1.3100 (high lebih tinggi)
H3 = 1.3080 (high hampir sama dengan H2 → potential resistance)
L1 = 1.2600 (low pertama)
L2 = 1.2750 (low lebih tinggi)
L3 = 1.2740 (low hampir sama dengan L2 → potential support)

LANGKAH 3: Tarik level di area yang bereaksi 2x+

1.3100 ═══════════════════════════════  ← Resistance (H2 dan H3 berdekatan)

1.2750 ═══════════════════════════════  ← Support (L2 dan L3 berdekatan)

LANGKAH 4: Buat zone (bukan line)

1.3120 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ← Batas atas (wick tertinggi)
1.3100 ═══════════════════════════════  ← Level utama
1.3080 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ← Batas bawah (body terendah area itu)

1.2770 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ← Batas atas zone support
1.2750 ═══════════════════════════════  ← Level utama
1.2730 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ← Batas bawah (wick terendah)

HASILNYA: 2 zone yang jelas untuk planning trade
```

---

## 8. Checklist Menggambar Level SnR

Gunakan checklist ini setiap kali kamu menggambar level:

**Validasi Level:**
- [ ] Apakah level ini bereaksi minimal 2 kali? (3x = lebih baik)
- [ ] Apakah reaksi di level ini menghasilkan pergerakan yang signifikan?
- [ ] Apakah level ini ada di timeframe H4 atau lebih tinggi?
- [ ] Apakah level ini berdekatan dengan round number? (bonus poin)
- [ ] Apakah ada candle kuat (hammer, engulfing) di setiap sentuhan?

**Cara Menggambar:**
- [ ] Sudahkah membuat zone (bukan hanya garis tunggal)?
- [ ] Apakah batas atas zone menggunakan wick high/low?
- [ ] Apakah level utama menggunakan body close/open?
- [ ] Apakah total level di chart tidak lebih dari 5-7?
- [ ] Apakah level yang paling penting sudah diberi highlight berbeda?

---

## 9. Kesalahan yang Harus Dihindari

| Kesalahan | Dampak | Solusi |
|-----------|--------|--------|
| Terlalu banyak level | Chart penuh, bingung mana yang penting | Batasi 3-5 KEY level |
| Level dari 1 sentuhan | Tidak valid, terlalu berisiko | Tunggu minimal 2 sentuhan |
| Tidak membuat zone | Entry terlalu kaku, sering salah timing | Selalu buat zone 3 garis |
| Hanya pakai wick atau hanya body | Kehilangan informasi | Kombinasikan keduanya |
| Menggambar di timeframe rendah | Level tidak signifikan | Mulai dari D1 turun ke H4 |

---

## 10. Latihan Praktis

### Latihan 1: Gambar dan Bandingkan
1. Buka chart XAUUSD (Gold) di timeframe H4
2. Gambar level HANYA menggunakan body candle
3. Gambar ulang HANYA menggunakan wick
4. Buat zone yang menggabungkan keduanya
5. Perhatikan: mana yang paling "masuk akal" dengan pergerakan harga?

### Latihan 2: Hitung Kualitas Level
Untuk 5 level yang kamu gambar di chart, isi scorecard:

| Level | Sentuhan | TF | Round No. | Candle Kuat | Score (0-10) |
|-------|----------|----|-----------|-------------|--------------|
|       |          |    |           |             |              |
|       |          |    |           |             |              |
|       |          |    |           |             |              |
|       |          |    |           |             |              |
|       |          |    |           |             |              |

Scoring:
- 3+ sentuhan = +3
- H4 atau lebih = +2, H1 = +1, LTF = 0
- Round number = +2
- Candle kuat di setiap sentuhan = +2
- Volume tinggi = +1

### Latihan 3: Peer Review (Opsional)
Kirim screenshot chart-mu ke grup trading dan minta trader lain menilai apakah level yang kamu gambar masuk akal. Ini adalah cara belajar yang sangat efektif.

---

## Ringkasan

| Konsep | Poin Utama |
|--------|------------|
| Body vs Wick | Gunakan body untuk level utama, wick untuk batas zone |
| Jumlah sentuhan | Min 2 (valid), 3 (standar), 4+ (sangat kuat) |
| Strong level | 3+ sentuhan, HTF, round number, volume tinggi |
| Weak level | 1-2 sentuhan, LTF, angka tidak bulat, bounce kecil |
| Zone vs Line | Selalu buat zone (3 garis: atas, tengah, bawah) |
| Jumlah level | Maksimal 5-7 level, fokus 3-5 KEY level |

---

**Modul Sebelumnya:** [01 — Apa itu SnR](./01-apa-itu-snr.md)  
**Modul Berikutnya:** [03 — Jenis-jenis SnR](./03-jenis-jenis-snr.md)
