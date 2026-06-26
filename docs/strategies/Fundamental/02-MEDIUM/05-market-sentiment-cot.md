# Modul 05 — Market Sentiment & COT Report

**Level:** MEDIUM (Menengah)
**Estimasi Waktu:** 45 menit
**Prasyarat:** Modul 04

---

## Pendahuluan

Market bergerak bukan hanya karena data ekonomi — tetapi karena bagaimana MANUSIA merespons data ekonomi. Sentimen adalah kekuatan psikologis kolektif yang bisa memperkuat atau membalikkan tren fundamental. Memahami sentimen adalah memahami "mood" pasar.

---

## 1. Apa Itu Market Sentiment?

```
MARKET SENTIMENT — DEFINISI
═══════════════════════════════════════════════════════════

Market Sentiment = Pandangan kolektif pelaku pasar tentang
                   arah market di masa depan.

Bukan tentang apa yang SEHARUSNYA terjadi secara logis,
tapi tentang apa yang DIPERCAYA akan terjadi oleh mayoritas.

Spektrum Sentimen:

EXTREME FEAR                                    EXTREME GREED
    │                                                │
    ▼                                                ▼
 Semua orang           Normal           Semua orang
  mau jual              Range             mau beli
    │                                                │
    │                                                │
  Safe haven         Mixed signals          Risk assets
  Gold, JPY, CHF     tidak jelas          naik, AUD/NZD
  naik                                    naik

PENTING: Ekstrem sentimen sering menjadi sinyal REVERSAL!
  Extreme fear = kontrarian → pertimbangkan beli
  Extreme greed = kontrarian → pertimbangkan jual
```

---

## 2. COT Report — Commitment of Traders

### Apa Itu COT Report?

COT (Commitment of Traders) adalah laporan mingguan dari CFTC (Commodity Futures Trading Commission) yang menunjukkan **posisi bersih** (net position) para pelaku besar di futures market.

**Jadwal rilis:** Setiap Jumat pukul 15:30 ET (02:30 WIB Sabtu), mencerminkan data posisi Selasa.

### Tiga Kelompok Utama dalam COT

```
TIGA KELOMPOK DALAM COT REPORT
═══════════════════════════════════════════════════════════

1. COMMERCIAL TRADERS (Hedgers)
   ─────────────────────────────
   Siapa: Perusahaan yang gunakan futures untuk hedge
          (produser emas, eksportir, importir)
   Karakteristik: Biasanya BERLAWANAN dengan tren harga
                  (mereka hedge risiko bisnis mereka)
   Kegunaan untuk trader: Kontrarian indicator

2. NON-COMMERCIAL (Large Speculators / Smart Money)
   ──────────────────────────────────────────────────
   Siapa: Hedge fund, bank besar, institusional
   Karakteristik: Mengikuti tren, posisi besar
                  Paling penting untuk trader retail
   Kegunaan: Ikuti arah mereka! "Follow the big money"

3. NON-REPORTABLE (Small Speculators / Retail)
   ──────────────────────────────────────────────
   Siapa: Trader retail kecil
   Karakteristik: Sering wrong direction di ekstrem
   Kegunaan: Kontrarian indicator di level ekstrem
```

### Cara Membaca COT Report

```
CONTOH COT DATA: XAUUSD (Gold Futures)
═══════════════════════════════════════════════════════════

Tanggal: Week ending [date]

                    LONG      SHORT    NET
Non-Commercial:    285,000   120,000  +165,000 ← BULLISH
Commercial:        120,000   280,000  -160,000 ← BEARISH (hedging)
Non-Reportable:     45,000    50,000   -5,000

Cara membaca:
Non-Commercial NET LONG 165,000 kontrak
= Hedge fund dan institusi besar NET BULLISH gold
= Signal: follow mereka → bias bullish gold

PERUBAHAN DARI MINGGU LALU:
Sebelum: Non-Commercial NET LONG 120,000
Sekarang: Non-Commercial NET LONG 165,000
Perubahan: +45,000 ← mereka menambah posisi long!
= Sentiment bullish gold SEMAKIN KUAT
```

### Cara Akses COT Report (Gratis)

```
CARA AKSES COT REPORT
═══════════════════════════════════════════════════════════

OPSI 1: CFTC Website (raw data)
  URL: cftc.gov/MarketReports/CommitmentsofTraders/index.htm
  Kelebihan: Paling akurat, data mentah
  Kekurangan: Tidak visual, butuh parsing

OPSI 2: Barchart.com (visual + gratis)
  URL: barchart.com/futures/commitment-of-traders
  Kelebihan: Ada grafik, mudah dibaca
  Kekurangan: Data 1 minggu tertinggal

OPSI 3: TradingView (terintegrasi dengan chart)
  Cari indicator: "COT Legacy"
  Kelebihan: Langsung muncul di chart pair Anda
  Kekurangan: Beberapa fitur berbayar

OPSI 4: Myfxbook.com
  URL: myfxbook.com/community/outlook
  Kelebihan: Menampilkan sentimen retail forex
  Berbeda dari COT (ini retail sentiment, bukan futures)

CARA BACA VISUAL COT:

   Long Positions:  ████████████████████████████  285,000
   Short Positions: ██████████████                120,000
                    ────────────────────────────────────
   Net Position:    ++++++++++++++                +165,000

   Tren net position 4 minggu:
   W-4: +120,000
   W-3: +130,000
   W-2: +145,000
   W-1: +165,000 ← terus naik = semakin bullish
```

### Menggunakan COT sebagai Contrarian Signal

```
COT EXTREME POSITIONING — CONTRARIAN SIGNAL
═══════════════════════════════════════════════════════════

Ketika Non-Commercial sudah SANGAT LONG (ekstrem):
  → Posisi long sudah jenuh
  → Tidak banyak pembeli baru tersisa
  → Sedikit berita negatif = massal keluar dari long
  → Harga bisa TURUN meski fundamental masih bagus

Ketika Non-Commercial sudah SANGAT SHORT (ekstrem):
  → Posisi short sudah jenuh
  → Short covering bisa memicu rally tajam
  → Fundamental catalyst kecil pun bisa jadi squeeze

CONTOH: Gold COT 2022
  Desember 2021: Net Long 180,000 (sangat ekstrem)
  Januari 2022: Gold mulai TURUN
  → Terlalu banyak yang long → koreksi terjadi

CONTOH: Gold COT Oktober 2022
  Oktober 2022: Net Short 20,000 (sangat ekstrem bearish!)
  → Ini adalah "capitulation" — semua orang sudah jual
  → November 2022: Gold rally +$200 dalam sebulan!

ATURAN:
  Net Long EKSTREM (>300K untuk gold) → pertimbangkan reduce long
  Net Short EKSTREM (<0 atau sangat kecil) → pertimbangkan buy the dip
  
  Tapi: COT bukan timing tool yang tepat
  Lebih baik: COT untuk BIAS, teknikal untuk TIMING
```

---

## 3. Fear & Greed Index

```
CNN FEAR & GREED INDEX
═══════════════════════════════════════════════════════════

URL: cnn.com/markets/fear-and-greed

Komponen:
  1. Stock Price Momentum (S&P 500 vs 125-day MA)
  2. Stock Price Strength (NYSE new highs vs new lows)
  3. Stock Price Breadth (Volume naik vs volume turun)
  4. Put/Call Ratio (opsi put vs call)
  5. Market Volatility (VIX)
  6. Safe Haven Demand (bonds vs stocks)
  7. Junk Bond Demand (spread high yield vs investment grade)

Skala: 0-100
  0-25: Extreme Fear → Potensi buy signal (kontrarian)
  25-45: Fear
  45-55: Neutral
  55-75: Greed
  75-100: Extreme Greed → Potensi sell signal (kontrarian)

Dampak ke Gold:
  Extreme Fear → Gold naik (safe haven demand)
  Extreme Greed → Gold bisa sideways/turun (risk assets diminati)

Penting: Index ini untuk S&P 500, tapi sangat berkorelasi
         dengan global risk sentiment
```

---

## 4. VIX — Volatility Index

```
VIX DAN DAMPAKNYA KE MARKET
═══════════════════════════════════════════════════════════

VIX = CBOE Volatility Index
     = Mengukur ekspektasi volatilitas S&P 500 30 hari ke depan
     = "Fear gauge" market

URL: tradingview.com → cari "VIX"

Level VIX dan interpretasi:
  < 15: Market sangat tenang → Risk-on → Buy equities, AUD, NZD
  15-20: Normal → Netral
  20-25: Sedikit khawatir → Mixed sentiment
  25-30: Khawatir → Risk-off mulai → Gold, JPY mulai naik
  30-40: Panik → Risk-off kuat → Gold, JPY, CHF menguat banyak
  > 40: Extreme Panic → Potential capitulation → Reversal dekat?

CHART KORELASI VIX vs GOLD (Maret 2020 — COVID Crash):
═══════════════════════════════════════════════════════════

VIX:
20 ──────────────────────────────── (Januari 2020)
    │
    │  COVID mulai menyebar
30 ─│────────────────────────────── (Februari)
    │
    │  Global panic selling
50 ─│────────────────────────────── (Awal Maret)
    │  ↑ Peak ketakutan
65 ─│─┐ VIX mencapai 65+!
    │ │
    │ └─────────────────────────────
50 ─│────────────────────────────── (April - mulai tenang)

GOLD (XAUUSD) chart yang bersesuaian:
1680 ─────────────────────────────── (Januari 2020)
      │   Awalnya gold naik karena ketidakpastian
1700 ─│─────────────────────────────
      │   Tapi kemudian jatuh saat margin call global!
1470 ─│──┐ → Ketika panic selling, bahkan gold dijual
      │  │   untuk cover margin call di equities
      │  └─────────────────────────────
1600 ─│────────────────────────────── recovery
      │
1750 ─│────────────────────────────── rebound kuat
         April-Agustus: Gold naik ke $2000+ (all-time high)

Pelajaran: VIX sangat tinggi (>50) bisa buat gold TURUN dulu
           (karena mass margin call), kemudian NAIK kuat setelahnya

Korelasi normal:
  VIX naik → Gold naik (keduanya safe haven)
  VIX turun → Gold bisa sideways (risk-on, orang jual gold beli equities)
```

---

## 5. DXY — Dollar Index sebagai Sentiment Gauge

```
DXY DAN CARA MENGGUNAKANNYA
═══════════════════════════════════════════════════════════

DXY = Indeks kekuatan USD terhadap basket 6 mata uang:
  EUR (57.6% bobot) ← paling dominan!
  JPY (13.6%)
  GBP (11.9%)
  CAD (9.1%)
  SEK (4.2%)
  CHF (3.6%)

Mengapa penting:
  - DXY naik = USD menguat secara umum
  - DXY turun = USD melemah secara umum
  - XAUUSD berkorelasi NEGATIF dengan DXY (paling konsisten)
  - EURUSD berkorelasi NEGATIF dengan DXY (karena EUR = 57.6%)

CARA GUNAKAN DXY SEBAGAI KONFIRMASI:

Skenario 1: Ingin SELL EURUSD
  Konfirmasi yang diperlukan:
  → DXY trending NAIK? ✓ konfirmasi sell EURUSD
  → DXY trending turun? ✗ hati-hati, mungkin bias salah

Skenario 2: Ingin BUY XAUUSD
  Konfirmasi yang diperlukan:
  → DXY trending TURUN? ✓ konfirmasi buy gold
  → DXY trending naik? ✗ hati-hati

CHART DXY (2022):
106 ──────────────────────────────── (September 2022, puncak)
     ↑ DXY naik karena Fed hawkish

101 ─────────────────────────────── (Awal 2022)

XAUUSD (berlawanan, 2022):
2000 ─────────────────────────────── (Maret 2022, high)
      ↓ Gold turun karena Fed hawkish → DXY naik

1620 ─────────────────────────────── (September 2022, low)
      Tepat bersamaan dengan DXY mencapai puncak!

→ Korelasi negatif DXY-Gold hampir sempurna di 2022
```

---

## 6. Risk-On vs Risk-Off Market

```
RISK-ON vs RISK-OFF — PANDUAN LENGKAP
═══════════════════════════════════════════════════════════

RISK-ON (Market optimis, mau ambil risiko):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kondisi: Ekonomi tumbuh, inflasi terkontrol, geopolitik aman

Yang NAIK:
  ✓ Equities (S&P 500, Nasdaq, DAX)
  ✓ AUD, NZD (commodity currencies, risk-correlated)
  ✓ Emerging market currencies (BRL, ZAR, MXN)
  ✓ Oil (economic activity demand)
  ✓ High yield bonds

Yang TURUN:
  ✗ Gold (orang prefer equities yang berbunga/tumbuh)
  ✗ JPY (carry trade dilepas: jual JPY untuk beli asset berisiko)
  ✗ CHF (safe haven tidak diminati)
  ✗ USD (kadang — tergantung konteks)
  ✗ Treasury bonds (yield naik karena jual bonds)

RISK-OFF (Market takut, hindari risiko):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kondisi: Resesi risk, geopolitik tinggi, krisis keuangan

Yang NAIK:
  ✓ Gold (safe haven utama)
  ✓ JPY (carry trade unwind: beli kembali JPY)
  ✓ CHF (safe haven Eropa)
  ✓ USD (dalam krisis parah: orang butuh liquidity USD)
  ✓ US Treasury Bonds (flight to quality)

Yang TURUN:
  ✗ Equities
  ✗ AUD, NZD
  ✗ Emerging market currencies
  ✗ Oil (demand fear)
  ✗ High yield bonds

VISUALISASI:

RISK-ON ENVIRONMENT:          RISK-OFF ENVIRONMENT:
S&P 500: ↑                    S&P 500: ↓
AUD/USD: ↑                    AUD/USD: ↓
NZD/USD: ↑                    NZD/USD: ↓
USD/JPY: ↑ (JPY melemah)      USD/JPY: ↓ (JPY menguat)
Gold:    ↓ atau sideways       Gold:    ↑
VIX:     ↓ (rendah)           VIX:     ↑ (tinggi)
```

---

## 7. Sentiment Retail (Kontrarian)

```
RETAIL SENTIMENT SEBAGAI KONTRARIAN INDICATOR
═══════════════════════════════════════════════════════════

Sumber data retail sentiment:
  - Myfxbook Community Outlook
  - IG Client Sentiment (IG.com)
  - OANDA Sentiment
  - DailyFX Sentiment

ATURAN KONTRARIAN:
  Retail traders sering salah di titik ekstrem!

  Jika 80%+ retail LONG pada pair:
  → Kemungkinan besar pair akan TURUN
  → Mengapa? Orang yang mau beli sudah beli, tidak ada pembeli baru
  → Smart money sering fade posisi retail ekstrem

  Jika 80%+ retail SHORT pada pair:
  → Kemungkinan besar pair akan NAIK
  → Short covering bisa memicu rally

CONTOH NYATA:
  GBP/USD saat Brexit referendum 2016:
  - 70% retail SHORT sebelum referendum
  - Retail expect GBP turun karena Brexit fear
  - Awalnya memang turun, tapi kemudian rally kuat
  - Retail yang terlalu early short terkena squeeze

CARA MENGGUNAKAN:
  Retail 80%+ long → bias BEARISH (kontrarian)
  Retail 80%+ short → bias BULLISH (kontrarian)
  Tapi konfirmasi dengan fundamental dan teknikal!
  Retail sentiment = TAMBAHAN, bukan standalone signal
```

---

## 8. Cara Buat Sentiment Dashboard

```
TEMPLATE SENTIMENT DASHBOARD MINGGUAN
═══════════════════════════════════════════════════════════

Tanggal: _______________
Pair: XAUUSD

┌─────────────────────────────────────────────────────────┐
│                SENTIMENT DASHBOARD                      │
├────────────────────┬────────────────────────────────────┤
│ Indicator          │ Reading          │ Sinyal           │
├────────────────────┼──────────────────┼──────────────────┤
│ VIX                │ 18 (Normal)      │ Netral           │
│ Fear & Greed Index │ 42 (Fear)        │ Slight Bullish   │
│ DXY Trend          │ Downtrend (H4)   │ Bullish Gold     │
│ COT Net (Gold)     │ +145K (moderate) │ Netral-Bullish   │
│ Retail Sentiment   │ 60% Short Gold   │ Bullish (kontra) │
│ US10Y Yield        │ Turun 0.1%/minggu│ Bullish Gold     │
│ S&P 500            │ Turun 2% minggu  │ Risk-off, Bullish│
└────────────────────┴──────────────────┴──────────────────┘

KESIMPULAN:
  5 dari 6 indikator bullish gold → Bias: BULLISH XAUUSD
  Konfirmasi: Tunggu entry teknikal di zona support

BIAS MINGGU INI: ___________
Pair yang akan ditrading: ___________
```

---

## Checklist Sentiment Analysis

- [ ] Cek VIX: di atas atau di bawah 20?
- [ ] Cek Fear & Greed: ekstrem fear atau greed?
- [ ] Cek DXY: trending naik atau turun?
- [ ] Cek COT (Jumat): net long atau net short? Ekstrem?
- [ ] Cek retail sentiment: 70%+ long atau short?
- [ ] Identifikasi: Risk-on atau Risk-off minggu ini?
- [ ] Simpulkan bias keseluruhan

---

## Latihan Modul 05

### Latihan 1 — Baca COT
Buka Barchart.com atau TradingView, cari COT untuk:
1. Gold Futures — berapa net position non-commercial saat ini?
2. Euro Futures (EUR) — net position?
3. Apakah ada yang ekstrem?

### Latihan 2 — Risk-On vs Risk-Off
Untuk masing-masing skenario berikut, tentukan Risk-on atau Risk-off? Dan apa dampaknya ke AUD/USD dan USD/JPY?
1. S&P 500 naik 3% dalam sehari
2. VIX melonjak dari 15 ke 28
3. Fed mengumumkan QE baru
4. GDP AS keluar sangat kuat

### Latihan 3 — Buat Dashboard
Buat sentiment dashboard untuk pair pilihan Anda hari ini menggunakan template di atas. Apa kesimpulan Anda?

---

## Rangkuman

| Tool | Cara Gunakan | Kontrarian? |
|------|-------------|-------------|
| COT Non-Commercial | Ikuti arah mereka | Ya, saat ekstrem |
| VIX | <15 risk-on, >25 risk-off | Tidak langsung |
| Fear & Greed | <25 extreme fear = buy? | Ya, sebagai filter |
| DXY | Berlawanan dengan Gold & EUR | Tidak, konfirmasi |
| Retail Sentiment | 80%+ satu arah = sinyal berlawanan | Ya |

---

**Modul Berikutnya:** [06 — Intermarket Analysis](./06-intermarket-analysis.md)
