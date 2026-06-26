# Modul 03 — Cara Baca Kalender Ekonomi

**Level:** LOW (Pemula)
**Estimasi Waktu:** 30 menit
**Prasyarat:** Modul 01 & 02

---

## Pendahuluan

Kalender ekonomi adalah "jadwal pertandingan" dunia trading. Sama seperti atlet yang tahu kapan pertandingan besar, trader profesional selalu tahu kapan data penting akan dirilis. Tidak pernah membuka posisi tanpa mengecek kalender ekonomi adalah aturan tak tertulis di dunia trading profesional.

---

## 1. Platform Kalender Ekonomi Terbaik

| Platform | URL | Kelebihan | Kekurangan |
|----------|-----|-----------|------------|
| ForexFactory | forexfactory.com | Gratis, filter lengkap, komunitas | Interface agak lama |
| Investing.com | investing.com | Real-time, mobile friendly | Iklan banyak |
| Myfxbook | myfxbook.com | Sederhana, cepat | Kurang detail |
| Bloomberg | bloomberg.com | Paling akurat | Berbayar ($2000+/bulan) |
| Trading Economics | tradingeconomics.com | Data historis lengkap | Beberapa fitur berbayar |

**Rekomendasi untuk pemula:** ForexFactory (gratis dan paling lengkap)

---

## 2. Anatomy Kalender Ekonomi

### Kolom-kolom di ForexFactory

```
LAYOUT KALENDER EKONOMI (ForexFactory)
═══════════════════════════════════════════════════════════════

┌──────────┬────┬────────────────────────────┬───┬─────┬────────┬────────┐
│  Tanggal │Jam │          Event             │ ! │Prev │Forcast │ Actual │
├──────────┼────┼────────────────────────────┼───┼─────┼────────┼────────┤
│Fri Aug 2 │    │                            │   │     │        │        │
│          │19:30│ Non-Farm Employment Change │███│ 179K│  175K  │  142K  │
│          │19:30│ Unemployment Rate          │███│  4.1%│  4.1% │   4.3% │
│          │19:30│ Average Hourly Earnings m/m│██ │ 0.3%│  0.3% │   0.2% │
│          │20:00│ ISM Services PMI           │██ │ 48.8│  51.0  │  51.4  │
├──────────┼────┼────────────────────────────┼───┼─────┼────────┼────────┤
│Mon Aug 5 │    │                            │   │     │        │        │
│          │09:00│ JP Monetary Policy Meeting │███│      │        │        │
│          │11:30│ AU Retail Sales m/m        │█  │  0.5%│  0.3% │        │
│          │16:30│ EU Sentix Investor Conf    │█  │  -7.3│  -5.0  │        │
└──────────┴────┴────────────────────────────┴───┴──────┴────────┴────────┘

Keterangan Kolom:
! = Impact level (1 bar = low, 2 bar = medium, 3 bar = high)
Prev = Data bulan/kuartal sebelumnya
Forecast = Ekspektasi konsensus analis
Actual = Data yang keluar (berwarna hijau jika lebih baik, merah jika lebih buruk)
```

### Kode Warna Impact

```
KODE WARNA DAMPAK
═══════════════════════════════════════════════════════════

[MERAH/ORANGE] █ █ █ = HIGH IMPACT
  → Wajib diperhatikan, bisa menggerakkan 50-200+ pip
  → Contoh: NFP, CPI, FOMC, GDP

[KUNING/ORANYE] █ █   = MEDIUM IMPACT
  → Perlu diperhatikan, bisa menggerakkan 20-60 pip
  → Contoh: PMI, Retail Sales, Trade Balance

[HIJAU/ABU]    █     = LOW IMPACT
  → Biasanya diabaikan, kecuali sangat jauh dari est
  → Contoh: Existing Home Sales, Richmond Fed Index
```

---

## 3. Cara Baca: Previous, Forecast, Actual

### Rumus Dasar Interpretasi

```
RUMUS INTERPRETASI DATA EKONOMI
═══════════════════════════════════════════════════════════

Untuk data POSITIF (lebih tinggi = lebih baik, misal NFP):
  Actual > Forecast = BULLISH untuk mata uang tersebut
  Actual < Forecast = BEARISH untuk mata uang tersebut
  Actual = Forecast = NETRAL

Untuk data NEGATIF (lebih rendah = lebih baik, misal Unemployment Rate):
  Actual < Forecast = BULLISH (pengangguran turun = bagus)
  Actual > Forecast = BEARISH (pengangguran naik = buruk)
  Actual = Forecast = NETRAL

CONTOH KONKRET:

NFP (lebih tinggi = lebih baik):
  Previous: 179K
  Forecast: 175K
  Actual: 142K  ← MISS (lebih rendah dari forecast)
  = BEARISH USD, BULLISH GOLD

CPI (inflasi, interpretasi tergantung konteks):
  Dalam siklus rate hike Fed:
    CPI actual > forecast = BULLISH USD (Fed lebih hawkish)
    CPI actual < forecast = BEARISH USD (Fed bisa lebih dovish)
```

### Pentingnya Revisi Data Bulan Lalu

```
MENGAPA REVISI PENTING?
═══════════════════════════════════════════════════════════

Contoh kasus:
  Bulan lalu NFP dirilis:  179,000
  Bulan ini keluar revisi: 114,000 (revisi ke bawah 65K!)
  Bulan ini NFP actual:    142,000 (vs forecast 175,000)

  Analisis:
  1. NFP actual miss dari forecast (142K vs 175K)
  2. PLUS revisi bulan lalu sangat besar ke bawah (179K → 114K)
  3. Kumulatif: Pasar tenaga kerja JAUH lebih lemah dari dugaan
  4. Dampak: USD jatuh LEBIH BESAR dari seandainya hanya miss saja

  Ini yang terjadi pada NFP Agustus 2024!

Aturan: Selalu baca baris revisi sebelum baca angka baru.
        Revisi besar ke bawah = data makin bearish
        Revisi besar ke atas = data makin bullish
```

---

## 4. Cara Plan Trading Sebelum News

### Framework 3 Skenario

Sebelum setiap news penting, siapkan 3 skenario:

```
FRAMEWORK 3 SKENARIO PRE-NEWS
═══════════════════════════════════════════════════════════

Contoh: Persiapan sebelum CPI besok
  Forecast: 3.1% YoY
  Previous: 3.4% YoY

SKENARIO 1: Actual BEAT (lebih tinggi dari forecast, misal 3.3%+)
  → CPI lebih tinggi dari dugaan
  → Fed kemungkinan hawkish lebih lama
  → USD menguat
  → Plan: Sell EURUSD di resistance / Sell XAUUSD di highs

SKENARIO 2: Actual IN-LINE (sekitar 3.0-3.2%)
  → Sesuai ekspektasi = netral
  → Market tidak bergerak banyak
  → Plan: Jangan buka posisi, tunggu clarity

SKENARIO 3: Actual MISS (lebih rendah dari forecast, misal 2.8%)
  → CPI jauh di bawah dugaan → disinflationary
  → Fed kemungkinan cut lebih cepat
  → USD melemah
  → Plan: Buy EURUSD di support / Buy XAUUSD di support zone
```

### Template Persiapan News Harian

```
TEMPLATE PERSIAPAN NEWS HARIAN
═══════════════════════════════════════════════════════════

Tanggal: _______________
Pair yang akan ditrading: _______________

NEWS HARI INI:
┌────────────────────────────────────────────────────────┐
│ Waktu  │ Event    │ Forecast │ Previous │ Impact        │
├────────────────────────────────────────────────────────┤
│ 19:30  │ CPI MoM  │  0.3%    │  0.4%    │ HIGH          │
│ 19:30  │ CPI YoY  │  3.1%    │  3.4%    │ HIGH          │
│ 22:00  │ ISM Mfg  │  49.5    │  48.5    │ MEDIUM        │
└────────────────────────────────────────────────────────┘

BIAS SAAT INI (sebelum news): BEARISH USD
Alasan: ______________________________

SKENARIO JIKA BEAT: Arah = ______  Plan = ______
SKENARIO JIKA MISS: Arah = ______  Plan = ______
SKENARIO JIKA IN-LINE: Arah = Netral  Plan = Tunggu

ZONE ENTRY YANG SUDAH DITANDAI DI CHART:
  BUY ZONE: _______________
  SELL ZONE: _______________

KEPUTUSAN: Trading hari ini? YA / TIDAK
Alasan: ______________________________
```

---

## 5. Strategi Sebelum, Saat, dan Sesudah News

### Strategi A: Trading Sebelum News (Pre-News Positioning)

```
STRATEGI PRE-NEWS POSITIONING
═══════════════════════════════════════════════════════════

Cocok untuk: Trader yang punya bias kuat dan yakin dengan arah news

Kondisi yang diperlukan:
  1. Fundamental bias sudah jelas
  2. Chart sudah di level teknikal yang bagus
  3. Risk management ketat (SL lebih lebar dari biasanya)

Contoh:
  - Hari Selasa: Data makro sebelumnya sudah menunjukkan tren melemah
  - NFP Jumat diperkirakan miss
  - XAUUSD sudah di strong support OB
  - Beli Rabu dengan SL lebar, target setelah NFP

CHART ILUSTRASI:
2400 ─────────────────────────────────────── Entry Pre-NFP
      │   ← Beli disini Rabu
      │
2380 ─│─────────────────────────────────────
      │                        NFP Rilis
      │                        ↓
2400 ─│────────────────────────┐────────────  +$20 dari entry
      │                        │
      │  SL: 2370 (di bawah    │
      │  support kuat)         │
      │                        │
      Wed     Thu             Fri

Risiko: News bisa keluar berlawanan dari ekspektasi
        Solusi: SL lebih lebar, size lebih kecil
```

### Strategi B: Trading Saat News (Tidak Disarankan untuk Pemula)

```
STRATEGI SAAT NEWS — FADE THE SPIKE
═══════════════════════════════════════════════════════════

Untuk trader berpengalaman saja!

Konsep: Market sering spike ke satu arah lalu reversal
        (terutama saat "buy the rumor, sell the fact")

Timing:
  T+0 : News rilis → spike awal (chaos, jangan masuk)
  T+5 menit: Spike mulai melambat
  T+8-10 menit: Potensi reversal candle muncul
  T+10-15 menit: BARU pertimbangkan entry jika ada konfirmasi

CHART SPIKE NFP:
2460 ─────────────────────────────────────── highs
      │   ← Spike NAIK 15 menit saat NFP "beat"
2445 ─│─────────────────────────────────────
      │          │ Kemudian....
2430 ─│──────────│──────────────────────────
      │  ranging │ reversal turun! (sell the fact)
2420 ─│──────────┘───────────────────────── target
      │
      │  "Buy the rumor, sell the fact"
      │  Market sudah price in NFP bagus sebelumnya
      │  Saat keluar: profit taking dari yang sudah buy duluan

RISIKO SANGAT TINGGI:
  - Spread melebar saat news (bisa 5-10x normal)
  - Slippage sering terjadi
  - Stop loss bisa tidak tereksekusi di harga yang diminta
```

### Strategi C: Trading Sesudah News (PALING DIREKOMENDASIKAN)

```
STRATEGI POST-NEWS — TRADE THE CONTINUATION
═══════════════════════════════════════════════════════════

Pendekatan terbaik untuk semua level trader

Langkah:
  1. Tunggu news rilis
  2. Tunggu 15-30 menit sampai volatilitas mereda
  3. Identifikasi arah sebenarnya
  4. Tunggu pullback ke support/resistance/OB
  5. Entry dengan konfirmasi teknikal

CHART ILUSTRASI (NFP Miss → Gold Naik):

2470 ─────────────────────────────────────── TP
      │                        ┌────────────
      │              ┌────────┘  ← continuation
2460 ─│─────────────┤
      │   Entry     │ pullback → OB → entry
2450 ─│─────────────┘
      │         ↑
      │      Zone OB (Order Block)
2445 ─│─────────────────────────────────────
      │      ↑
      │   Spike low (noise) diabaikan
      │
      19:30     19:45     20:00     21:00
       NFP      Konfirmasi  Entry    TP Hit
       Rilis    arah

Kelebihan strategi ini:
  + Spread sudah normal kembali
  + Arah sudah jelas
  + Entry lebih presisi
  + Risiko lebih terukur
```

---

## 6. Jadwal News Mingguan (Contoh Realistis)

### Contoh: Jadwal News Minggu Kedua Juli 2025

```
JADWAL NEWS MINGGUAN
═══════════════════════════════════════════════════════════

SENIN, 7 Juli 2025
  ─────────────────────────────────────────────────────
  15:30  EUR  Sentix Investor Confidence    [MEDIUM]
  16:00  EUR  Retail Sales MoM              [MEDIUM]
  21:00  USD  Consumer Credit               [LOW]

SELASA, 8 Juli 2025
  ─────────────────────────────────────────────────────
  16:30  GBP  Claimant Count Change         [MEDIUM]
  17:00  EUR  ZEW Economic Sentiment        [MEDIUM]
  22:00  USD  JOLTS Job Openings            [MEDIUM-HIGH]

RABU, 9 Juli 2025
  ─────────────────────────────────────────────────────
  01:30  AUD  Westpac Consumer Sentiment    [LOW]
  16:30  GBP  GDP MoM                       [HIGH]
  20:30  USD  CPI MoM & YoY               [HIGH] ← BIG ONE
  20:30  USD  Core CPI MoM & YoY           [HIGH] ← BIG ONE
  22:30  USD  Crude Oil Inventories         [MEDIUM]

KAMIS, 10 Juli 2025
  ─────────────────────────────────────────────────────
  02:00  USD  FOMC Meeting Minutes          [HIGH]
  07:30  JPY  PPI YoY                       [LOW]
  16:30  GBP  Manufacturing Production      [MEDIUM]
  20:30  USD  PPI MoM & YoY               [MEDIUM-HIGH]
  20:30  USD  Initial Jobless Claims        [MEDIUM]

JUMAT, 11 Juli 2025
  ─────────────────────────────────────────────────────
  *** TIDAK ADA NEWS BESAR ***
  17:00  EUR  Industrial Production MoM    [LOW]
  21:00  USD  University of Michigan        [MEDIUM]
              Consumer Sentiment

ANALISIS MINGGU INI:
  ─────────────────────────────────────────────────────
  Big Days: Rabu (CPI) & Kamis (FOMC Minutes + PPI)
  Pair yang paling terpengaruh: USD pairs semua
  Hari aman trading (sedikit news besar): Senin, Jumat
  Strategi: Tentukan bias setelah CPI Rabu, trade Kamis-Jumat
```

---

## 7. Cara Setup Kalender di ForexFactory

### Langkah-langkah:

```
SETUP FOREXFACTORY UNTUK TRADER PROFESSIONAL
═══════════════════════════════════════════════════════════

1. Buka forexfactory.com → Calendar

2. Filter "Impact": Centang hanya MEDIUM dan HIGH
   (matikan LOW untuk mengurangi noise)

3. Filter "Currency": Pilih sesuai pair yang Anda trade
   Jika trade XAUUSD: centang USD
   Jika trade EURUSD: centang USD + EUR
   Jika trade GBPUSD: centang USD + GBP

4. Filter "Time": Sesuaikan timezone ke WIB (UTC+7)
   Klik "Time" di bagian atas → pilih timezone

5. Bookmark halaman dengan filter yang sudah diatur

6. Set notifikasi di HP/browser untuk news besar:
   → Investing.com app: ada fitur alert news
   → Bisa set alarm 30 menit sebelum news besar

7. Rutin cek setiap Minggu malam untuk minggu depan
   Identifikasi "big days" dan rencanakan trading
```

---

## 8. Price Action Khas Sebelum dan Sesudah News

```
POLA PRICE ACTION KHAS INTORNO NEWS
═══════════════════════════════════════════════════════════

SEBELUM NEWS (30-60 menit sebelum rilis):
  ─── Biasanya range menyempit (market menunggu)
  ─── Volume menurun
  ─── Spread mulai melebar (terutama 5-10 menit sebelum)

  Harga terlihat seperti ini:
  ┌────────────────────────────┐
  │ ranging sempit             │ ← "compression"
  └────────────────────────────┘
  ←         30-60 menit       →
                               ↑
                           News rilis

SAAT NEWS (0-10 menit setelah rilis):
  ─── Spike tiba-tiba ke satu arah (sering tidak sustainable)
  ─── Spread sangat lebar
  ─── Volume sangat tinggi

  Pola 1: Direct Spike (langsung ke arah fundamental)
  ┌────────────────────────────┐
  │ range                      │───────────────────────
  └──────────────────────────────────── trend berlanjut

  Pola 2: Spike & Reverse (yang sering membingungkan)
  ┌────────────────────────────┐
  │ range                      ├────────
  └────────────────────────────┤        │ reversal
                               │spike   └────────────── (true direction)
                               │ke satu arah

SESUDAH NEWS (30-120 menit setelah rilis):
  ─── Volatilitas mereda
  ─── Arah fundamental mulai terbentuk
  ─── Volume mulai normal
  ─── INILAH WAKTU TERBAIK UNTUK ENTRY
```

---

## Tips Pro: Seasonal Patterns di Kalender Ekonomi

```
POLA MUSIMAN YANG PERLU DIKETAHUI
═══════════════════════════════════════════════════════════

SENIN:
  - Biasanya tenang (no big US news)
  - Cocok untuk analisis dan persiapan
  - Hati-hati gap dari weekend

SELASA-RABU:
  - Banyak data medium (PMI, JOLTS, dll)
  - Setup teknikal sering lebih bersih
  - Hari paling "tradeable" bagi banyak trader

KAMIS:
  - Weekly Initial Jobless Claims selalu rilis
  - Sering ada ECB atau BoE decision
  - Volatilitas medium-high

JUMAT:
  - NFP (Jumat pertama tiap bulan) = PALING PENTING
  - Hati-hati: Market sering tipis mendekati weekend
  - "Window dressing" oleh institusi akhir bulan
  - Setelah NFP, market bisa bergerak 1-2 jam lagi

AKHIR BULAN:
  - "Window dressing": Fund manager sesuaikan portofolio
  - Bisa ada gerakan tidak biasa di akhir sesi
  - GDP (kuartalan), Core PCE biasanya rilis akhir bulan
```

---

## Checklist Kalender Ekonomi Harian

**Setiap Minggu Malam (Minggu):**
- [ ] Buka kalender ekonomi untuk minggu depan
- [ ] Identifikasi hari dengan news HIGH impact
- [ ] Tandai pair yang paling terpengaruh
- [ ] Rencanakan hari mana akan trading aktif

**Setiap Pagi Sebelum Trading:**
- [ ] Cek kalender hari ini: ada news HIGH/MEDIUM?
- [ ] Jika ada news dalam 2 jam: JANGAN buka posisi baru
- [ ] Siapkan 3 skenario untuk news yang akan datang
- [ ] Tandai zona entry di chart sesuai skenario

**30 Menit Sebelum News:**
- [ ] Tutup posisi yang tidak mau kena volatilitas news
- [ ] Atau pastikan SL sudah diperlebar
- [ ] Siap dengan notepad untuk mencatat actual vs forecast

---

## Latihan Modul 03

### Latihan 1 — Baca Kalender
Buka ForexFactory hari ini:
1. Filter hanya HIGH impact, semua mata uang
2. Catat 3 event terpenting minggu ini
3. Untuk setiap event, tulis: pair yang terpengaruh, arah bias jika beat, arah bias jika miss

### Latihan 2 — Simulasi Pre-News Planning
Pilih satu event HIGH impact minggu ini:
1. Catat forecast dan previous
2. Buat 3 skenario (beat/miss/in-line)
3. Tandai zona entry di chart untuk tiap skenario
4. Setelah news rilis, evaluasi: skenario mana yang terjadi?

### Latihan 3 — Review Trade History
Lihat 10 trade terakhir Anda:
1. Apakah ada news yang rilis saat posisi sedang terbuka?
2. Apakah news tersebut mempengaruhi harga secara signifikan?
3. Apakah Anda mengetahui berita tersebut sebelumnya?

---

## Rangkuman

| Konsep | Takeaway Utama |
|--------|---------------|
| Kolom kalender | Previous → Forecast → Actual → Bandingkan |
| Color code | Merah = HIGH (wajib perhatikan), Kuning = MEDIUM |
| Revisi data | Selalu baca revisi bulan lalu — sering mengejutkan |
| 3 strategi | Pre-news (risiko tinggi), Saat news (expert only), Post-news (terbaik) |
| Pola price action | Range → Spike → Reversal/Continuation → Entry terbaik di post-spike |
| Rutinitas | Cek kalender setiap Minggu malam + setiap pagi |

---

**Modul Berikutnya:** [04 — Central Bank & Kebijakan Moneter](../02-MEDIUM/04-central-bank-kebijakan-moneter.md)
