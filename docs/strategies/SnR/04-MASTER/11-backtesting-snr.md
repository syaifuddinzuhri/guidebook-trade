# Modul 11 — Backtesting & Journal SnR

**Level:** 🏆 MASTER  
**Estimasi waktu baca:** 30–35 menit  
**Prasyarat:** Modul 01–10 (semua modul sebelumnya)

---

## Tujuan Modul

Setelah membaca modul ini, kamu akan:
- Memahami mengapa backtesting penting sebelum live trading
- Bisa melakukan backtesting SnR secara sistematis
- Tahu metrik apa yang harus dianalisis dari data backtest
- Mengerti benchmark win rate dan expectancy untuk SnR
- Memiliki template jurnal yang siap digunakan

---

## 1. Mengapa Backtesting Itu Penting?

Banyak trader langsung live trading setelah belajar strategi. Ini seperti dokter yang langsung operasi tanpa pernah belajar di simulasi. Backtesting memberikan:

```
MANFAAT BACKTESTING:

Tanpa Backtesting:               Dengan Backtesting:
─────────────────────            ─────────────────────────────
"Kelihatannya bagus"             "Saya tahu win rate 58%"
"Kayaknya RR 1:3"                "Average RR aktual 1:2.4"
"Strategi ini pasti works"       "Expectancy: +0.8R per trade"
"Kenapa selalu loss?"            "Drawdown max: 12% — masih aman"
→ Buta dengan uang nyata         → Siap dengan ekspektasi realistis
```

**Prinsip:** Validasi strategi di masa lalu sebelum menggunakannya di masa depan.

---

## 2. Persiapan Backtesting

### 2.1 Alat yang Dibutuhkan

| Alat | Fungsi | Gratis? |
|------|--------|---------|
| TradingView | Chart dan replay | Ya (terbatas) / Berbayar |
| MT4/MT5 Strategy Tester | Backtest lebih otomatis | Ya |
| Spreadsheet (Google Sheets/Excel) | Catat hasil | Ya |
| Kalkulator RR | Hitung risk/reward | Ya |

### 2.2 Data yang Dibutuhkan

```
MINIMUM DATA UNTUK BACKTEST VALID:

- Periode: Minimal 6 bulan (lebih baik 1-2 tahun)
- Sampel trade: Minimal 30 trade (lebih baik 50+)
- Kondisi market yang beragam:
  ├── Trending bullish
  ├── Trending bearish
  └── Sideways/ranging

Kenapa harus beragam?
- Strategi yang hanya bagus di trending market
  akan hancur saat market sideways
- 30+ sampel diperlukan agar data statistik valid
```

---

## 3. Cara Melakukan Backtesting SnR

### Metode: Manual Replay (TradingView)

```
LANGKAH BACKTESTING MANUAL:

LANGKAH 1: Pilih pair dan timeframe
├── Mulai dengan EURUSD atau XAUUSD
├── Gunakan H4 sebagai TF utama analisis
└── D1 untuk bias

LANGKAH 2: Mundurkan chart ke "waktu yang jauh"
├── TradingView: Bar Replay feature
├── Atau gunakan chart 1-2 tahun lalu
└── Jangan lihat "masa depan" (apa yang terjadi setelah bar saat ini)

LANGKAH 3: Gambar level SnR (seperti biasa)
├── Identifikasi level dari yang sudah ada
├── Jangan lihat level yang "belum terbentuk" saat itu
└── Gambar hanya dari data yang tersedia pada titik waktu itu

LANGKAH 4: Tunggu setup
├── Maju chart satu candle demi satu candle
├── Apakah ada candle konfirmasi di level?
└── Apakah semua checklist terpenuhi?

LANGKAH 5: Catat trade (jika ada setup)
├── Entry, SL, TP
├── Maju chart sampai SL atau TP hit
└── Catat hasilnya di spreadsheet

LANGKAH 6: Ulangi sampai 30-50 trade
└── Jangan skip trade yang loss — catat semua

LANGKAH 7: Analisis data
└── Hitung metrik (lihat section 4)
```

### Contoh Visualisasi Proses Backtesting

```
PROSES BACKTESTING — Timeline View:

T=0: Mulai dari 6 bulan lalu

Harga
│
│    (chart pada T=0: hanya lihat ini)
│
1.1200 ═══════════════════════════════  ← Level yang sudah ada
│    ↑ 3 bounce historis sudah terlihat
│
1.0900 ═══════════════════════════════  ← Level yang sudah ada
│

T=1: Maju 1 candle
→ Apakah ada setup? Tidak → maju lagi

T=2: Maju 1 candle
→ Apakah ada setup? Tidak → maju lagi

...

T=47: Maju 1 candle
→ Harga menyentuh 1.0900! Muncul Hammer!
→ SETUP VALID! → Catat trade

Harga
│
1.1200 ═══════════════════════════════  ← TP
│
│
│         ╭──────────────────────── (rally setelah bounce)
│    ╭────╯
│    │
1.0900 ═══════════════════════════════  ← Entry point
│    │   ← Hammer candle
│   ─┤─
│
1.0860 ─────────────────────────────  ← SL

→ Catat di spreadsheet: Trade #1, BUY, Entry 1.0910, SL 1.0860,
                        TP 1.1200, Risk 50 pip, Target 290 pip
→ Maju chart lagi...
→ T=110: TP hit! Profit 290 pip
→ Update di spreadsheet: Profit, RR aktual 1:5.8
```

---

## 4. Metrik yang Harus Dianalisis

### 4.1 Metrik Utama

```
METRIK BACKTESTING SnR:

1. WIN RATE
   Rumus: (Jumlah trade profit / Total trade) × 100%
   Contoh: 18 profit dari 30 trade = 60%

2. AVERAGE RR (Risk/Reward Ratio)
   Rumus: (Total pip profit dari trade profit / Rata-rata risk) ÷
          (Total pip loss dari trade loss / Rata-rata risk)
   Contoh: Average profit 120 pip, average risk 50 pip, average loss 50 pip
           Average RR = 120/50 = 2.4

3. EXPECTANCY (Ekspektasi per trade)
   Rumus: (Win Rate × Average Reward) - (Loss Rate × Average Risk)
   Semua dalam satuan R (1R = 1x risk)
   Contoh: (0.60 × 2.4R) - (0.40 × 1R) = 1.44R - 0.40R = 1.04R
   → Setiap trade memberikan ekspektasi +1.04R (positif = strategi bagus!)

4. MAXIMUM DRAWDOWN
   Jumlah kerugian beruntun terbesar (dalam R atau persen)
   Contoh: 4 loss berturut-turut × 1R = 4R drawdown

5. PROFIT FACTOR
   Rumus: Total pip profit / Total pip loss (keduanya absolut)
   Contoh: 1200 pip profit total / 400 pip loss total = 3.0
   > 1.5 = Bagus, > 2.0 = Sangat Bagus
```

### 4.2 Benchmark SnR — Angka yang Realistis

```
BENCHMARK SnR TRADING (berdasarkan pengalaman komunitas):

                 Rata-rata Trader  Trader Baik   Trader Expert
                 ─────────────────────────────────────────────
Win Rate:        40-50%            50-60%        60-70%
Average RR:      1:1.5-2.0        1:2-2.5       1:2.5-3.5
Expectancy:      +0.2-0.5R        +0.5-1.0R     +1.0-1.5R
Max Drawdown:    15-25%           8-15%         5-10%
Profit Factor:   1.2-1.5          1.5-2.0       2.0-3.0

PENTING:
- Win rate 40% MASIH BISA PROFITABLE jika RR cukup tinggi!
- Contoh: Win rate 40%, RR 1:3 = Expectancy +0.6R (positif!)

Kalkulasi:
(0.40 × 3R) - (0.60 × 1R) = 1.2R - 0.6R = +0.6R per trade ✓
```

---

## 5. Template Spreadsheet Backtesting

### Kolom Spreadsheet

```
TEMPLATE SPREADSHEET BACKTESTING SnR:

| # | Tanggal | Pair | TF | Arah | Level    | Model   | Entry   | SL      | TP1     | TP2     |
|---|---------|------|----|------|----------|---------|---------|---------|---------|---------|
| 1 | Jan 05  | EURUSD| H4 | BUY  | 1.0900 S | Bounce  | 1.0910  | 1.0860  | 1.0980  | 1.1050  |
| 2 | Jan 12  | XAUUSD| H4 | SELL | 2080 R   | Retest  | 2074    | 2095    | 2050    | 2020    |
...

| Risk_pip | TP1_pip | TP2_pip | RR_TP1 | Konfirmasi_Candle | Konfluensi | Hasil     | Net_pip |
|---------|---------|---------|--------|-------------------|------------|-----------|---------|
| 50      | 70      | 140     | 1.4    | Hammer           | Fib+Round  | TP2 HIT   | +140    |
| 21      | 24      | 54      | 1.14   | Shooting Star    | PMH+MA200  | TP1 HIT   | +24     |
...

| Notes                                          |
|------------------------------------------------|
| D1 bullish bias, konfluensi kuat, clean setup  |
| Masuk agak terlambat, sizing kecil             |
```

### Ringkasan Statistik (Sheet Terpisah)

```
RINGKASAN STATISTIK:

Total Trade:          30
Trade Profit:         17
Trade Loss:           11
Trade Breakeven:       2

Win Rate:             17/28 = 60.7% (exclude BE)
Loss Rate:            11/28 = 39.3%

Average Profit:       115 pip
Average Loss:         48 pip
Average RR:           115/48 = 2.4

Expectancy:           (0.607 × 2.4) - (0.393 × 1) = 1.457 - 0.393 = 1.064R

Max Consecutive Win:  5
Max Consecutive Loss: 3
Max Drawdown:         3 × 48 = 144 pip (atau 3R)

Total Profit:         17 × 115 = 1955 pip
Total Loss:           11 × 48  = 528 pip
Net:                  1955 - 528 = 1427 pip

Profit Factor:        1955 / 528 = 3.7 ← EXCELLENT!
```

---

## 6. Apa yang Harus Dicari dari Data Backtest?

### 6.1 Setup Terbaik

```
ANALISIS SETUP TERBAIK:

Filter data berdasarkan:

1. Model Entry:
   Bounce: Win rate 55%, Average RR 1:2.1
   Breakout: Win rate 48%, Average RR 1:1.8
   Retest: Win rate 65%, Average RR 1:2.6
   
   Kesimpulan: Retest terbaik! Focus lebih banyak di sini.

2. Jumlah Konfluensi:
   1 faktor: Win rate 42%
   2 faktor: Win rate 58%
   3+ faktor: Win rate 71%
   
   Kesimpulan: Hanya ambil trade dengan 2+ konfluensi!

3. Candle Konfirmasi:
   Hammer: Win rate 61%
   Bullish Engulfing: Win rate 67%
   Doji: Win rate 44%
   
   Kesimpulan: Lebih selektif - prefer engulfing daripada doji!

4. Timeframe Entry:
   D1: Win rate 68% (tapi jarang, hanya 5 trade)
   H4: Win rate 62% (17 trade)
   H1: Win rate 54% (8 trade)
   
   Kesimpulan: H4 adalah sweet spot untuk frekuensi + kualitas.
```

### 6.2 Kondisi Market Terbaik

```
ANALISIS KONDISI MARKET:

Trending Market:
- Win rate: 67%
- Average RR: 1:2.8
- Trade count: 18

Ranging Market (Sideways):
- Win rate: 50%
- Average RR: 1:1.9
- Trade count: 12

Kesimpulan:
Fokus di trending market. Di ranging market, kurangi ukuran posisi
atau hanya ambil trade dengan konfluensi 3+ faktor.
```

### 6.3 Red Flag dari Backtest

```
TANDA BAHWA STRATEGI PERLU DIREVISI:

- Win rate di bawah 35% → Level yang dipilih tidak cukup kuat
- Average RR di bawah 1:1.5 → Pilih TP yang lebih jauh / SL terlalu besar
- Expectancy negatif → Strategi tidak profitable, STOP live trading
- Max drawdown di atas 25% → Risk per trade terlalu besar
- Win rate sangat berfluktuasi tiap bulan → Setup terlalu subjektif
                                             perlu rule yang lebih jelas

SOLUSI untuk tiap masalah:
Win rate rendah → Naikkan filter konfluensi (min 3 faktor)
RR rendah → Hanya ambil trade di HTF level (H4 ke atas)
Drawdown tinggi → Kurangi risk per trade (dari 2% ke 1%)
Inkonsisten → Tambahkan rule lebih spesifik ke checklist
```

---

## 7. Forward Testing: Langkah Berikutnya Setelah Backtest

Setelah backtest selesai dan hasilnya positif, lanjut ke **forward testing** (paper trading live):

```
TAHAPAN MENUJU LIVE TRADING:

BACKTEST (3-6 bulan data historis)
        ↓
    Evaluasi metrik:
    Win rate ≥ 45%? Expectancy positif?
        ↓
    YA                    TIDAK
    ↓                     ↓
FORWARD TEST        Revisi strategi →
(Paper trade live,   Backtest lagi
1-2 bulan)
    ↓
    Win rate konsisten?
    Expoectancy masih positif?
        ↓
    YA                    TIDAK
    ↓                     ↓
LIVE TRADING        Kembali ke Forward
(Ukuran kecil,       Test dengan revisi
0.01-0.1 lot)
    ↓
    Profit selama 3 bulan live?
        ↓
    YA
    ↓
Scale up ukuran posisi secara bertahap
```

---

## 8. Journal Harian yang Efektif

```
JOURNAL ENTRY TEMPLATE:

═════════════════════════════════════════════════════
TRADE JOURNAL — [Tanggal: ___________]
═════════════════════════════════════════════════════

SEBELUM TRADE:
Pair: _______  TF: _______  Waktu Entry: _______
Bias D1: Bullish / Bearish / Sideways
Level SnR: _______  Jenis: Support / Resistance / SR Flip
Jumlah Sentuhan Historis: ___
Model: Bounce / Breakout / Retest
Konfirmasi Candle: _______
Konfluensi: _______
Checklist Score: ___/15

Entry: _______  SL: _______  TP1: _______  TP2: _______
Risk (pip): ___  Risk (%): ___%
RR TP1: 1:___  RR TP2: 1:___

Kondisi Market:  Trending / Ranging
Sesi:  Asia / London / NY / Overlap

SETELAH TRADE:
Hasil: Profit / Loss / Breakeven
Pip: ___  % Akun: ___%
TP1 Hit: Ya / Tidak  TP2 Hit: Ya / Tidak

REFLEKSI:
Apa yang berjalan baik?
_______________________________________________
Apa yang bisa diperbaiki?
_______________________________________________
Pelajaran untuk trade selanjutnya:
_______________________________________________
Skor disiplin (1-10): ___  (apakah kamu mengikuti semua rule?)
═════════════════════════════════════════════════════
```

---

## 9. Backtesting vs Curve Fitting

Ada jebakan berbahaya yang disebut **curve fitting** atau **overfitting**: kamu menyesuaikan strategi terlalu khusus dengan data historis sehingga tidak berlaku di data baru.

```
CURVE FITTING — Bahaya yang Harus Dihindari:

OVER-OPTIMIZED (Berbahaya):
"Saya menemukan bahwa setup terbaik adalah:
- EURUSD saja
- Senin dan Rabu saja
- Antara jam 10:00-14:00 saja
- Hanya Hammer dengan wick minimal 15 pip
- Hanya saat RSI di bawah 30
- Hanya saat MACD cross positif"

→ Rule yang terlalu spesifik = over-fitting
→ Di data historis mungkin win rate 80%
→ Tapi di live trading win rate mungkin hanya 40%
   karena terlalu spesifik untuk data masa lalu

HEALTHY APPROACH:
"Setup saya:
- Pair: 3-5 pair major atau gold
- Level: 3+ sentuhan di H4 atau lebih
- Model: Bounce, Breakout, atau Retest
- Konfirmasi: Hammer/Engulfing/Shooting Star
- Konfluensi: 2+ faktor
- Checklist: 13+/15 terpenuhi"

→ Fleksibel namun terstruktur
→ Berlaku di berbagai kondisi market
→ Win rate 55-65% yang konsisten
```

---

## 10. Checklist Backtesting

- [ ] Minimal 6 bulan data historis
- [ ] Minimal 30 trade tersampel (lebih baik 50+)
- [ ] Data mencakup trending dan ranging market
- [ ] TIDAK melihat "masa depan" saat menggambar level
- [ ] Semua trade dicatat, termasuk yang loss
- [ ] Metrik dihitung: Win rate, Average RR, Expectancy, Max Drawdown
- [ ] Setup dianalisis berdasarkan model, konfluensi, dan candle
- [ ] Benchmark dibandingkan dengan target yang realistis
- [ ] Tidak ada over-fitting atau rule yang terlalu spesifik
- [ ] Ada rencana forward test sebelum live trading

---

## 11. Latihan Praktis

### Latihan 1: Backtest 30 Trade
Pilih EURUSD H4 atau XAUUSD H4. Mundurkan chart ke 6 bulan lalu. Lakukan backtest manual 30 trade menggunakan framework SnR ini.

### Latihan 2: Analisis Hasil
Setelah 30 trade, hitung:
- Win rate
- Average profit dan loss (pip)
- Expectancy
- Max drawdown
- Profit factor

Bandingkan dengan benchmark. Di mana perlu perbaikan?

### Latihan 3: Identifikasi Pattern
Dari 30 trade, cari pola:
- Setup jenis apa yang paling sering profit?
- Di kondisi market apa win rate paling tinggi?
- Candle konfirmasi apa yang paling andal?

Gunakan insight ini untuk memperketat filter di forward test.

---

## Ringkasan

| Aspek | Detail |
|-------|--------|
| Minimal data | 6 bulan historis, 30+ trade sampel |
| Metrik utama | Win rate, Average RR, Expectancy, Max Drawdown |
| Benchmark SnR | Win rate 50-60%, Expectancy +0.5-1.0R |
| Cara analisis | Filter berdasarkan model, konfluensi, candle |
| Setelah backtest | Forward test (paper trade) 1-2 bulan sebelum live |
| Hindari | Curve fitting / over-optimization |

---

## Penutup: Perjalanan SnR Trader

Kamu telah menyelesaikan semua 11 modul SnR trading. Ini adalah ringkasan perjalanan:

```
PERJALANAN SnR TRADER:

Level 1 (LOW):
[01] Paham apa itu SnR
[02] Bisa menggambar level dengan benar
[03] Kenal semua jenis SnR
           ↓
Level 2 (MEDIUM):
[04] Bisa bedakan static vs dynamic
[05] Gunakan zone, bukan line
[06] Manfaatkan SR Flip untuk entry berkualitas tinggi
           ↓
Level 3 (HIGH):
[07] Analisis multi-timeframe (top-down)
[08] Kuasai 3 model entry
[09] Kombinasikan SnR dengan candlestick
           ↓
Level 4 (MASTER):
[10] Jalankan framework lengkap
[11] Backtest dan validasi strategi

SEKARANG:
→ Kamu siap untuk forward test
→ Kemudian live trading dengan confidence
→ Dan terus belajar, karena market selalu berubah

"The market is never wrong. Your analysis might be." 
— Prinsip SnR Trader
```

---

**Modul Sebelumnya:** [10 — Full Strategy SnR](./10-full-strategy-snr.md)  
**Kembali ke Overview:** [README — Strategi SnR](../README.md)
