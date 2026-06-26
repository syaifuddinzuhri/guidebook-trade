# Modul 06 — Intermarket Analysis

**Level:** MEDIUM (Menengah)
**Estimasi Waktu:** 45 menit
**Prasyarat:** Modul 04 & 05

---

## Pendahuluan

Tidak ada market yang bergerak sendiri. Forex, komoditas, obligasi, dan saham semuanya terhubung dalam sebuah ekosistem yang kompleks. Trader yang hanya melihat satu market seperti dokter yang hanya memeriksa satu organ pasien — gambaran yang didapat tidak lengkap. Intermarket analysis mengajarkan Anda melihat "big picture" dengan memahami hubungan antar market.

---

## 1. Empat Market Utama dan Hubungannya

```
EMPAT MARKET DAN INTERKONEKSINYA
═══════════════════════════════════════════════════════════

         ┌─────────────┐
         │   BONDS     │
         │ (Obligasi)  │
         │ US Treasury │
         └──────┬──────┘
                │ Yield naik = risk meningkat
                │ Yield turun = safe haven demand
      ┌─────────┴──────────┐
      │                    │
┌─────▼─────┐        ┌─────▼──────┐
│  FOREX    │        │ COMMODITIES │
│ (Valas)   │◄──────►│ (Komoditas) │
│ USD, EUR  │        │ Gold, Oil   │
└─────┬─────┘        └─────┬───────┘
      │                    │
      └──────────┬──────────┘
                 │ Risk-on/off sentiment
           ┌─────▼──────┐
           │  EQUITIES  │
           │   (Saham)  │
           │  S&P 500   │
           └────────────┘

HUBUNGAN KUNCI:
  Bonds Yield ↑ → Equities tertekan, Gold turun, USD biasanya naik
  Bonds Yield ↓ → Equities naik, Gold naik, USD biasanya turun
  DXY ↑ → Gold turun, EURUSD turun, Commodities umumnya turun
  VIX ↑ → Equities turun, Gold naik, JPY naik
```

---

## 2. Gold vs USD — Korelasi Negatif Paling Konsisten

```
KORELASI GOLD vs DXY
═══════════════════════════════════════════════════════════

Gold (XAUUSD) dan DXY memiliki korelasi negatif ~-0.80 sampai -0.90

Mengapa?
1. Gold dihargai dalam USD
   → DXY naik → butuh lebih sedikit USD beli gold → harga gold turun
   → DXY turun → butuh lebih banyak USD beli gold → harga gold naik

2. Safe haven kompetitor
   → Saat stress: orang beli USD (liquidity) ATAU gold (store of value)
   → Dalam jangka panjang: keduanya bersaing sebagai safe haven

VISUALISASI 2022-2023:
═══════════════════════════════════════════════════════════

DXY:
 114 ────────────────────────────────── September 2022 (PUNCAK DXY)
      │
 110 ─│──────────────────────────────── Agustus 2022
      │
 106 ─│──────────────────────────────── Juli 2022
      │
 102 ─│──────────────────────────────── Awal 2022
      │                ↓ DXY mulai turun Oktober 2022
  98 ─│────────────────────────────────── Akhir 2022
      │
  96 ─│────────────────────────────────── Pertengahan 2023

XAUUSD (berlawanan arah):
1850 ─────────────────────────────────── Awal 2022
      │ ↓ saat DXY naik, Gold turun
1620 ─│────────────────────────────────── Sept/Okt 2022 (BOTTOM GOLD)
      │ ↑ saat DXY turun, Gold naik
1980 ─│────────────────────────────────── April-Mei 2023
      │
2050 ─│────────────────────────────────── Desember 2023

Keduanya MIRROR IMAGE satu sama lain!

CARA MENGGUNAKAN:
1. Buka chart DXY di tab terpisah
2. Tentukan arah DXY (uptrend/downtrend)
3. Ambil posisi BERLAWANAN di Gold
4. Konfirmasi dengan teknikal Gold

CAVEAT: Korelasi tidak selalu sempurna
  - Saat extreme risk-off: keduanya bisa naik bersamaan
    (orang beli USD dan Gold sebagai safe haven)
  - Jangka pendek (intraday): korelasi bisa melemah
  - Yang konsisten: korelasi jangka menengah (H4-Daily)
```

---

## 3. Gold vs US 10-Year Yield

```
GOLD vs US 10-YEAR TREASURY YIELD
═══════════════════════════════════════════════════════════

Ini adalah korelasi PALING PENTING untuk Gold!

Hubungan: Gold vs Real Yield (bukan nominal yield)
  Real Yield = Nominal Yield - Inflation Expectation (Breakeven)

Logika:
  Gold = aset yang tidak berbunga (no yield)
  Bond US = aset yang berbunga (ada yield)

  Jika Real Yield NAIK:
    → Biaya oportunitas hold Gold semakin tinggi
    → Lebih menguntungkan hold Bond berbunga
    → Gold tidak menarik → GOLD TURUN

  Jika Real Yield TURUN:
    → Biaya oportunitas hold Gold berkurang
    → Bond tidak menarik (yield rendah atau negatif)
    → Gold lebih menarik sebagai store of value
    → GOLD NAIK

VISUALISASI 2020-2021 (Real Yield Negatif → Gold ATH):

Real Yield (US 10Y TIPS):
 0.5% ─────────────────────────────────── Awal 2020
       │ ↓ Fed cut ke 0, QE besar
-0.5% ─│──────────────────────────────── April 2020
-1.0% ─│──────────────────────────────── Juli 2020 (paling rendah)
       │

XAUUSD (korelasi negatif dengan yield):
1650 ─────────────────────────────────── Awal 2020
      │ ↑ real yield turun → Gold naik
1800 ─│────────────────────────────────── April 2020
2070 ─│────────────────────────────────── Agustus 2020 (ALL TIME HIGH!)

Korelasi sempurna: Real yield paling rendah = Gold paling tinggi!

VISUALISASI 2022 (Real Yield Naik → Gold Turun):

Real Yield:
-1.0% ─────────────────────────────────── Januari 2022
       │ ↑ Fed hike agresif → real yield naik
 0.0% ─│──────────────────────────────── April 2022
 1.0% ─│──────────────────────────────── Juli 2022
 1.5% ─│──────────────────────────────── September 2022

XAUUSD:
2000 ─────────────────────────────────── Awal 2022
      │ ↓ real yield naik → Gold turun
1810 ─│──────────────────────────────── April 2022
1680 ─│──────────────────────────────── Juli 2022
1620 ─│──────────────────────────────── September 2022

Gold turun $380 sejalan dengan kenaikan real yield!

CARA MONITOR:
  US 10Y Real Yield (TIPS): tradingeconomics.com → search "US 10Y TIPS"
  Atau TradingView: cari "US10Y" untuk nominal, "TIPS10Y" untuk real
```

---

## 4. Oil vs CAD, NOK

```
MINYAK (OIL) DAN HUBUNGANNYA DENGAN MATA UANG
═══════════════════════════════════════════════════════════

Mengapa Oil mempengaruhi mata uang?
  - Kanada adalah pengekspor minyak terbesar ke AS
  - Norwegia adalah pengekspor minyak besar di Eropa
  - Rusia (rubl) dan petrodollar negara Timur Tengah

USD/CAD vs Oil (Korelasi NEGATIF):
  Oil naik → CAD menguat → USD/CAD TURUN
  Oil turun → CAD melemah → USD/CAD NAIK

MENGAPA?
  Oil naik → Kanada dapat lebih banyak USD dari ekspor
           → Demand CAD naik (eksportir konversi USD ke CAD)
           → CAD menguat
           → USD/CAD turun

VISUALISASI 2022 (Oil Rally karena Russia-Ukraine):

WTI Oil:
 $80 ─────────────────────────────────── Januari 2022
      │ ↑ Russia invade Ukraine → supply shock
$100 ─│──────────────────────────────── Maret 2022
$120 ─│──────────────────────────────── Juni 2022

USD/CAD:
1.2700 ─────────────────────────────── Januari 2022
        │ ↓ Oil naik → CAD kuat → USDCAD turun
1.2400 ─│─────────────────────────────── April 2022
1.2300 ─│─────────────────────────────── Juni 2022

CARA MENGGUNAKAN:
  Sebelum trade USD/CAD atau USD/NOK:
  1. Cek harga Oil (WTI): naik atau turun?
  2. Oil naik → bias SELL USD/CAD
  3. Oil turun → bias BUY USD/CAD
  4. Konfirmasi dengan teknikal

PAIR OIL-SENSITIVE:
  USD/CAD: Korelasi kuat dengan WTI (oil AS)
  USD/NOK: Korelasi kuat dengan Brent (oil Eropa)
  AUD/USD: Sedikit korelasi (Australia commodity exporter)
  RUB: Sangat sensitif tapi jarang diperdagangkan
```

---

## 5. Equities vs Safe Haven (JPY, CHF, Gold)

```
HUBUNGAN EQUITIES DAN SAFE HAVEN
═══════════════════════════════════════════════════════════

CARRY TRADE MEKANISME:
  Investor pinjam JPY (bunga rendah) → beli aset berisiko (equities, AUD)
  = Jual JPY, beli asset berisiko

  Saat pasar NAIK (risk-on):
    Carry trade MENINGKAT → lebih banyak JPY dijual → USD/JPY NAIK

  Saat pasar TURUN (risk-off):
    Carry trade DILEPAS → JPY dibeli kembali → USD/JPY TURUN

S&P 500 vs USD/JPY (Korelasi POSITIF):
  S&P 500 naik → USD/JPY naik (risk-on)
  S&P 500 turun → USD/JPY turun (risk-off, JPY menguat)

S&P 500 vs Gold (Korelasi NEGATIF secara umum):
  S&P 500 crash → Gold naik (safe haven)
  S&P 500 bull run → Gold bisa sideways atau turun

VISUALISASI COVID CRASH Maret 2020:

S&P 500:
3300 ─────────────────────────────────── Awal 2020
      │
      │ COVID panic selling
2200 ─│──────────────────────────────── 23 Maret 2020 (-33%)
      │
3500 ─│──────────────────────────────── Agustus 2020 (new ATH!)

USD/JPY (turun saat S&P crash):
112 ─────────────────────────────────── Awal 2020
     │ ↓ JPY dibeli kembali (unwind carry trade)
101 ─│──────────────────────────────── Maret 2020

Gold:
1580 ─────────────────────────────────── Awal 2020
      │ Awalnya turun (margin call)
1460 ─│──────────────────────────────── Maret 2020 (dip)
      │ Kemudian naik kuat
2070 ─│──────────────────────────────── Agustus 2020 (ATH)
```

---

## 6. Tabel Korelasi Lengkap

```
TABEL KORELASI INTERMARKET
═══════════════════════════════════════════════════════════

Aset A          Aset B          Korelasi    Kekuatan
───────────────────────────────────────────────────────
XAUUSD          DXY             Negatif     Kuat (-0.85)
XAUUSD          US 10Y Real     Negatif     Kuat (-0.80)
XAUUSD          S&P 500         Negatif     Sedang (-0.50)
XAUUSD          VIX             Positif     Sedang (+0.55)
EURUSD          DXY             Negatif     Sangat Kuat (-0.95)
USD/JPY         S&P 500         Positif     Kuat (+0.70)
USD/JPY         VIX             Negatif     Kuat (-0.65)
USD/CAD         WTI Oil         Negatif     Kuat (-0.75)
AUD/USD         Iron Ore/Copper Positif     Kuat (+0.70)
AUD/USD         S&P 500         Positif     Sedang (+0.60)
GBP/USD         EUR/USD         Positif     Kuat (+0.80)
USD/CHF         EUR/USD         Negatif     Kuat (-0.85)

Catatan: Korelasi bersifat dinamis dan bisa berubah
         Terutama di periode stress market yang ekstrem
         Selalu verifikasi korelasi saat ini, bukan asumsi historis
```

---

## 7. Framework Konfirmasi Intermarket untuk Gold

```
FRAMEWORK KONFIRMASI INTERMARKET — XAUUSD
═══════════════════════════════════════════════════════════

Sebelum BELI Gold, cek:
  ✓ DXY trending TURUN? (konfirmasi bullish gold)
  ✓ US 10Y Yield turun atau real yield negatif/turun?
  ✓ VIX meningkat atau risk-off mode?
  ✓ COT: Non-commercial net long dan meningkat?
  ✓ S&P 500 melemah? (risk-off support gold)

Jika 4-5 dari 5 ✓ → Bias bullish gold KUAT
Jika 3 dari 5 ✓ → Bias bullish gold SEDANG
Jika < 3 ✓ → Hati-hati, bias tidak jelas

Sebelum JUAL Gold, cek:
  ✓ DXY trending NAIK?
  ✓ US 10Y Yield naik dan real yield positif/naik?
  ✓ VIX turun, risk-on environment?
  ✓ COT: Non-commercial net long mulai berkurang?
  ✓ S&P 500 menguat? (risk-on menekan gold)

Studi Kasus Konfirmasi Intermarket — Oktober 2022:
════════════════════════════════════════════════════

Saat itu:
  DXY: 114 (sangat tinggi, dekat puncak)
  US 10Y Yield: 4.2% (sangat tinggi)
  Real Yield: 1.7% (sangat tinggi → bearish gold)
  VIX: 32 (tinggi, risk-off)
  S&P 500: Di dekat lows
  Gold: $1620 (sangat rendah, 2-year low)

Apa yang terjadi kemudian:
  Oktober-November 2022:
  - DXY mulai turun dari 114 ke 105 (-8%)
  - US 10Y Yield mulai turun dari 4.2% ke 3.5%
  - Gold NAIK dari $1620 ke $1900 (+17% dalam 3 bulan)

Pelajaran: Ketika intermarket semua di titik ekstrem BEARISH gold
           dan kemudian mulai reversal → itu adalah sinyal BUY
           yang paling kuat!
```

---

## 8. Cara Setup Intermarket Dashboard

```
INTERMARKET DASHBOARD SETUP (TradingView)
═══════════════════════════════════════════════════════════

Buka TradingView, buat layout dengan 6 chart:

┌────────────────┬────────────────┬────────────────┐
│    XAUUSD      │     DXY        │   US10Y Yield  │
│  (target pair) │  (corr negatif)│ (corr negatif) │
├────────────────┼────────────────┼────────────────┤
│    S&P 500     │     VIX        │   EUR/USD      │
│  (risk gauge)  │  (fear gauge)  │  (DXY proxy)   │
└────────────────┴────────────────┴────────────────┘

Timeframe: Daily atau H4 untuk intermarket analysis

Cara baca dashboard:
  Setiap hari, lihat 6 chart sekaligus
  Apakah sebagian besar menunjukkan arah yang sama?
  → Jika ya: bias kuat
  → Jika tidak: mixed signal, hati-hati

Symbol TradingView:
  Gold: XAUUSD
  DXY: DXY atau TVC:DXY
  US 10Y: US10Y atau TVC:US10Y
  S&P 500: SPX atau SP:SPX
  VIX: VIX atau CBOE:VIX
```

---

## Checklist Intermarket Analysis

Sebelum buka posisi Gold, lakukan cek cepat (5 menit):

**Jika ingin BUY XAUUSD:**
- [ ] DXY: sedang downtrend atau di resistance?
- [ ] US 10Y Yield: turun atau stagnan?
- [ ] VIX: di atas 20 atau sedang naik?
- [ ] S&P 500: melemah?
- [ ] COT: net long dan tren meningkat?

**Jika ingin SELL XAUUSD:**
- [ ] DXY: sedang uptrend atau di support?
- [ ] US 10Y Yield: naik?
- [ ] VIX: turun (risk-on)?
- [ ] S&P 500: menguat kuat?
- [ ] COT: net long menurun atau mulai net short?

---

## Latihan Modul 06

### Latihan 1 — Identifikasi Korelasi
Tanpa melihat tabel, jawab: apa korelasi antara:
1. DXY naik → XAUUSD?
2. VIX melonjak dari 15 ke 30 → USD/JPY?
3. Oil naik 15% dalam sebulan → USD/CAD?
4. S&P 500 jatuh 10% → AUD/USD?

### Latihan 2 — Intermarket Konfirmasi
Skenario: Anda ingin buy XAUUSD
Buka TradingView dan cek:
1. Tren DXY (Daily): naik/turun?
2. US10Y Yield: naik/turun minggu ini?
3. VIX: di atas atau di bawah 20?
4. S&P 500: strong atau weak?
5. Berdasarkan data ini, apakah bias buy Anda terkonfirmasi?

### Latihan 3 — Historical Intermarket
Lihat chart DXY dan XAUUSD di TradingView, timeframe Daily.
Identifikasi 3 momen di mana keduanya bergerak berlawanan dengan jelas.
Catat: tanggal, arah DXY, arah XAUUSD, alasan fundamental yang mungkin.

---

## Rangkuman

| Pasangan | Korelasi | Penjelasan |
|---------|---------|------------|
| Gold vs DXY | Negatif Kuat | USD kuat = Gold turun |
| Gold vs Real Yield | Negatif Kuat | Yield naik = Gold turun |
| Gold vs VIX | Positif Sedang | Fear naik = Gold naik |
| USD/JPY vs S&P 500 | Positif Kuat | Risk-on = kedua naik |
| USD/CAD vs Oil | Negatif Kuat | Oil naik = USDCAD turun |
| AUD/USD vs Commodities | Positif Kuat | Commodity naik = AUD naik |

---

**Modul Berikutnya:** [07 — Konfluensi Fundamental + Teknikal](../03-HIGH/07-fundamental-teknikal-konfluensi.md)
