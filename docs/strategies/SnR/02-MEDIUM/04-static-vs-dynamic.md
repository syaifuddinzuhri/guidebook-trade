# Modul 04 — Static vs Dynamic SnR

**Level:** 🟡 MEDIUM  
**Estimasi waktu baca:** 20–25 menit  
**Prasyarat:** Modul 01–03

---

## Tujuan Modul

Setelah membaca modul ini, kamu akan:
- Memahami perbedaan mendasar antara static dan dynamic SnR
- Tahu kapan menggunakan masing-masing pendekatan
- Bisa menggabungkan keduanya dalam analisis yang komprehensif
- Menghindari bias menggunakan hanya satu jenis

---

## 1. Konsep Dasar

### Static SnR

**Static SnR** adalah level yang **tidak berubah** seiring berjalannya waktu. Level ini tetap berada di harga yang sama minggu depan, bulan depan, atau bahkan tahun depan — sampai ada kondisi yang mengubahnya.

Contoh: Horizontal resistance di 1.1200 tetap di 1.1200 selama-lamanya (kecuali ada role reversal).

### Dynamic SnR

**Dynamic SnR** adalah level yang **bergerak** seiring berjalannya waktu, menyesuaikan diri dengan pergerakan harga. Level ini mengikuti arah trend.

Contoh: MA 50 yang hari ini di 1.0800 bisa berada di 1.0900 minggu depan jika harga terus naik.

---

## 2. Static SnR — Detail

```
STATIC SnR — Visualisasi:

Waktu →    Jan    Feb    Mar    Apr    May

Harga
│
1.1200 ════════════════════════════════════════════  ← Level TIDAK BERUBAH
│    ↓       ↓              ↓
│   ┌┴┐     ┌┴┐            ┌┴┐
│   │▓│     │▓│            │▓│
│   └┬┘     └┬┘     ╭──────└┬┘
│    │       ╰──────╯       │
│    ╰─────────────────────╯
│
│   Level 1.1200 tetap di 1.1200 dari Januari hingga Mei
│   → Ini adalah STATIC resistance

Keuntungan Static SnR:
+ Mudah diidentifikasi — sekali gambar, berlaku lama
+ Tidak ada ambiguitas — level jelas dan tepat
+ Banyak trader melihat level yang sama → konfluensi lebih kuat
+ Mudah untuk planning trade (TP/SL dari awal)

Kelemahan Static SnR:
- Tidak mempertimbangkan perubahan trend
- Bisa menjadi "terlalu jauh" dari harga saat market trending
- Perlu update manual jika ada role reversal
```

**Jenis-jenis Static SnR:**
- Horizontal Support/Resistance
- Round Number / Psychological Level
- Previous High/Low (PWH/PWL/PMH/PML)
- Fibonacci Retracement level

---

## 3. Dynamic SnR — Detail

```
DYNAMIC SnR — Visualisasi:

Waktu →    Jan    Feb    Mar    Apr    May

Harga
│                                        ╭── Harga
│                              ╭─────────╯
│                    ╭─────────╯
│          ╭─────────╯
│╭─────────╯
│╯
│
│═══════════════════════════════════════════  ← MA 50 (bergerak naik)
│          Level MA 50:
│          Jan: 1.0800
│          Feb: 1.0900
│          Mar: 1.1000
│          Apr: 1.1100
│          May: 1.1200
│
│   → Level bergerak mengikuti trend → DYNAMIC support

Keuntungan Dynamic SnR:
+ Mengikuti pergerakan harga — selalu relevan
+ Memberikan konteks trend saat ini
+ Berguna untuk trailing stop di trend trade
+ Otomatis terupdate

Kelemahan Dynamic SnR:
- Tidak ada level "pasti" — berubah setiap hari/jam
- Lebih sulit untuk pre-planning trade yang tepat
- Setiap MA memiliki lag (tertinggal dari harga)
- Pilihan MA yang berbeda memberikan level berbeda
```

**Jenis-jenis Dynamic SnR:**
- Moving Average (20, 50, 100, 200)
- Trendline (bergerak mengikuti High/Low baru)
- Bollinger Bands (batas atas/bawah)

---

## 4. Perbandingan Langsung

```
PERBANDINGAN: Static vs Dynamic dalam Satu Chart

EURUSD H4 — Uptrend dengan kedua jenis SnR

Harga
│
1.1200 ════════════════════════════════════════════  ← STATIC resistance
│         ↓ Rejection dari static resistance
│   ┌───┐
│   │   └──╮
│   │      ╰────╮
│   │           ╰─────────────────────────────────  ← MA 50 (dynamic)
│   │                   ↑ MA 50 bergerak naik
│   │                   ↑ Harga pullback ke MA 50
│   │                   ↑ Support ditemukan di MA 50
│   │           ╭────────╯
│   │      ╭────╯
│   │ ╭────╯
│   ╰─╯
│
1.0900 ════════════════════════════════════════════  ← STATIC support
│

Analisis:
- Resistance STATIC di 1.1200 → harga rejected
- Support DYNAMIC (MA 50) bergerak naik → harga bounce
- Support STATIC di 1.0900 → backstop jika MA 50 ditembus
```

---

## 5. Kapan Menggunakan Static vs Dynamic?

### Gunakan Static SnR saat:

| Kondisi | Alasan |
|---------|--------|
| Market ranging/sideways | Dynamic SnR kurang relevan di non-trending market |
| Planning swing trade | Butuh target TP/SL yang pasti |
| Mencari area reversal mayor | Historical high/low lebih signifikan |
| Awal sesi (tidak ada trend intraday) | Belum ada context dari MA |

### Gunakan Dynamic SnR saat:

| Kondisi | Alasan |
|---------|--------|
| Market trending jelas | MA mengikuti arah trend |
| Pullback dalam trend | Mencari "buy the dip" atau "sell the rally" |
| Trailing stop management | MA bisa jadi acuan trailing stop |
| Intraday trend trading | MA 20/50 pada H1/H4 sangat efektif |

---

## 6. Strategi Kombinasi: Static + Dynamic

Cara paling efektif adalah **menggunakan keduanya bersama-sama**. Ketika static dan dynamic SnR bertemu di area yang sama, kekuatan level meningkat drastis.

```
STRATEGI KOMBINASI: XAUUSD H4

Scenario: Uptrend, harga sedang pullback

Harga
│                                   ╭─── HARGA saat ini
│
│
2050 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ← Dynamic: MA 50
│   \                                             MA 50 ada di 2050
│    \                                            dan bergerak naik
│     ───────────────────────────────────────
2040 ════════════════════════════════════════  ← Static: Horizontal Support
│        ↑ Sentuhan 1   ↑ Sentuhan 2            (2x sentuhan historis)
│       ─┤─            ─┤─
│                                     ↑
│                                   CONFLUENCE!
│                              MA 50 + Horizontal Support
│                              berada di area yang sama (2040-2050)
│                              → High Probability Setup!

Setup Trading:
├── Entry: Buy di zona 2040-2050 (saat MA 50 dan horizontal support bertemu)
├── Konfirmasi: Tunggu candle bullish (hammer, engulfing, dll)
├── SL: Di bawah 2030 (di bawah static support)
├── TP1: 2100 (resistance berikutnya)
├── TP2: 2150 (jika trend kuat berlanjut)
└── RR: Min 1:3
```

---

## 7. Studi Kasus: GBPUSD D1 — Static + Dynamic Kombination

```
Studi Kasus: GBPUSD D1 — Downtrend dengan Resistance Confluensi
════════════════════════════════════════════════════════════════

Konteks: GBPUSD dalam downtrend. Harga rally (pullback dalam downtrend).
Pertanyaan: Di mana rally akan berhenti dan harga turun lagi?

Harga (menyederhanakan untuk ilustrasi)
│
│
1.2800 ════════════════════════════════════════  ← STATIC resistance
│           (Previous Month High)
│    ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ← DYNAMIC: MA 200 di 1.2780
│                                               (resistance dalam downtrend)
│     ↑ ZONE KONFLUENSI: 1.2780 - 1.2800
│
│                 ╭── Harga rally ke zona
│                 │   (mencoba nembus)
│    ─────────────┤── Rejection terjadi!
│                 │
│            ╭───╯
│       ╭────╯
│  ╭────╯
│  │
│──╯
1.2400 ─────────────────────────────────── ← Target TP (support berikutnya)

Narasi Lengkap:
1. GBPUSD dalam downtrend (Lower High, Lower Low)
2. Harga rally (pullback normal dalam downtrend)
3. Rally mencapai zona 1.2780-1.2800:
   - STATIC: Previous Month High di 1.2800
   - DYNAMIC: MA 200 berada di sekitar 1.2780
4. Dua jenis SnR bertemu → zona konfluensi kuat
5. Harga ditolak dari zona → lanjut turun

Setup:
├── Entry: Sell di 1.2780-1.2800 (saat harga menyentuh zona)
├── Konfirmasi: Candle bearish (shooting star, bearish engulfing)
├── SL: Di atas 1.2840 (di atas static resistance + buffer)
├── TP: 1.2400 (support berikutnya)
└── RR: 1:6.7 (40 pip risk, 380 pip target) → Excellent!
```

---

## 8. Kesalahan Umum

### Kesalahan 1: Hanya menggunakan Static tanpa Dynamic context

```
KURANG OPTIMAL:
- Trader melihat support horizontal di 1.0800
- Langsung buy saat harga menyentuh 1.0800
- Tidak cek bahwa MA 200 berada di 1.0850 (resistance dynamic)
- Harga bounce tipis dari 1.0800 tapi langsung ditolak MA 200
- Trade tidak profitable karena tidak ada ruang gerak

LEBIH BAIK:
- Cek posisi MA 200 dulu
- Jika MA 200 berada di atas support → ruang gerak terbatas → skip trade
- Atau perkecil TP target
```

### Kesalahan 2: Hanya menggunakan Dynamic tanpa Static context

```
KURANG OPTIMAL:
- Trader buy saat harga menyentuh MA 50 (dynamic support)
- Tidak cek bahwa ada resistance horizontal kuat di 20 pip ke atas
- Harga bounce dari MA 50 tapi langsung ditolak horizontal resistance
- Trade profit sedikit atau bahkan loss karena TP terlalu jauh

LEBIH BAIK:
- Selalu cek static SnR sebelum entry
- Pastikan ada "ruang bersih" antara entry dan TP berikutnya
```

---

## 9. Framework Analisis Lengkap

Gunakan urutan ini setiap kali melakukan analisis:

```
URUTAN ANALISIS SnR:

Langkah 1: Tentukan Trend (bias)
          ↓
Langkah 2: Gambar Static SnR (horizontal, round number, PWH/PWL)
          ↓
Langkah 3: Tambahkan Dynamic SnR (MA 50, MA 200, trendline)
          ↓
Langkah 4: Cari zona konfluensi (static + dynamic bertemu)
          ↓
Langkah 5: Tentukan setup entry, SL, TP
          ↓
Langkah 6: Hitung RR ratio → ambil jika ≥ 1:2
```

---

## Checklist Modul 04

- [ ] Bisa membedakan static dan dynamic SnR dengan jelas
- [ ] Paham kapan menggunakan masing-masing
- [ ] Bisa menggabungkan keduanya dalam satu analisis
- [ ] Bisa mengidentifikasi zona konfluensi
- [ ] Menghindari trade yang tidak memiliki konfluensi

---

## Latihan Praktis

### Latihan 1: Identifikasi Static dan Dynamic
Buka USDJPY H4:
1. Tambahkan MA 50 dan MA 200
2. Gambar trendline (jika trending)
3. Gambar 3 horizontal level utama
4. Tandai dengan warna berbeda: Merah = static, Biru = dynamic

### Latihan 2: Cari Konfluensi
Di chart yang sama, identifikasi semua area di mana static dan dynamic SnR berdekatan (dalam 10-20 pip). Catat minimal 2 zona konfluensi.

### Latihan 3: Backtest 10 Setup
Dengan chart XAUUSD D1 (6 bulan lalu), cari 10 momen di mana terjadi konfluensi static + dynamic. Catat:
- Apakah harga bereaksi di zona konfluensi?
- Seberapa kuat reaksinya?
- Apakah trade ini profitable?

---

## Ringkasan

| Aspek | Static SnR | Dynamic SnR |
|-------|-----------|-------------|
| Perubahan | Tidak berubah | Bergerak setiap waktu |
| Contoh | Horizontal, Round Number | MA, Trendline |
| Terbaik untuk | Ranging market, swing trade | Trending market, trend trade |
| Identifikasi | Mudah dan jelas | Perlu pilih MA yang tepat |
| Kombinasi | Gabungkan keduanya untuk konfluensi terkuat |

---

**Modul Sebelumnya:** [03 — Jenis-jenis SnR](../01-LOW/03-jenis-jenis-snr.md)  
**Modul Berikutnya:** [05 — Zone vs Line](./05-zone-vs-line.md)
