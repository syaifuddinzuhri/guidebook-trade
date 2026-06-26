# Modul 07 — FVG & Imbalance

> **Level**: 🟡 MEDIUM | **Estimasi belajar**: 3-4 hari

---

## 7.1 Apa itu Fair Value Gap (FVG)?

**Fair Value Gap** adalah celah harga yang terbentuk ketika pasar bergerak terlalu cepat sehingga **tidak semua order terisi** di zona tersebut. FVG menunjukkan **ketidakseimbangan** antara supply dan demand.

### Konsep Dasar
Market selalu berusaha mencari "fair value" — harga yang menyeimbangkan buyer dan seller. Ketika ada gap besar, market cenderung **kembali mengisi** gap tersebut.

---

## 7.2 Cara Mengidentifikasi FVG

FVG terbentuk dari **3 candle berurutan**:

### Bullish FVG
```
Candle 1: ┌─┐  High = A
           └─┘  Low  = B

Candle 2: ┌──┐  (candle besar bullish = displacement)
           │██│
           └──┘

Candle 3: ┌─┐  High = C
           └─┘  Low  = D

FVG = celah antara HIGH Candle 1 (A) dan LOW Candle 3 (D)
Kondisi: A < D (ada gap, tidak overlap)

        D ─── Low candle 3
        ↑
   [FVG zona] ← Area yang tidak pernah diperdagangkan
        ↓
        A ─── High candle 1
```

### Bearish FVG
```
Candle 1: ┌─┐  Low = A (yang relevan adalah LOW)
           └─┘

Candle 2: ┌──┐  (candle besar bearish = displacement)
           │░░│
           └──┘

Candle 3: ┌─┐  High = B
           └─┘

FVG = celah antara LOW Candle 1 (A) dan HIGH Candle 3 (B)
Kondisi: A > B (ada gap)

        A ─── Low candle 1
        ↑
   [FVG zona] ← Area yang tidak pernah diperdagangkan
        ↓
        B ─── High candle 3
```

---

## 7.3 Cara Trading dengan FVG

### Bullish FVG (zona support)
```
FVG terbentuk saat harga naik impulsif
→ Harga koreksi turun ke zona FVG
→ FVG bertindak sebagai support
→ Harga bangkit kembali dari FVG
→ ENTRY BUY di dalam FVG
```

### Bearish FVG (zona resistance)
```
FVG terbentuk saat harga turun impulsif
→ Harga koreksi naik ke zona FVG
→ FVG bertindak sebagai resistance
→ Harga turun kembali dari FVG
→ ENTRY SELL di dalam FVG
```

---

## 7.4 Level Entry di dalam FVG

Ada 3 area entry di dalam FVG:

```
          ┌──────────────────┐
          │   50% (midpoint) │ ← Entry paling umum
          │                  │
          │   Lower 25%      │ ← Entry agresif (RR lebih baik)
          └──────────────────┘
```

| Area Entry | Karakteristik |
|-----------|---------------|
| **Upper FVG** | Konservatif, kemungkinan fill tinggi |
| **50% Midpoint** | Balanced, paling sering digunakan |
| **Lower FVG** | Agresif, RR terbaik tapi risiko stop lebih besar |

---

## 7.5 FVG yang Valid vs Tidak Valid

### FVG Valid:
- Terbentuk dari displacement yang signifikan (candle besar)
- Belum di-fill sepenuhnya
- Searah dengan trend HTF
- Terbentuk di area yang "penting" (di atas/bawah OB, dekat swing point)

### FVG Tidak Valid / Lemah:
- Terbentuk dari candle kecil (insignificant)
- Sudah di-fill sepenuhnya (harga melewati seluruh FVG)
- Berlawanan dengan trend HTF
- Terlalu banyak FVG di area yang sama

---

## 7.6 Inverse FVG (IFVG)

Ketika FVG sudah **di-fill sepenuhnya** dan harga malah terus melewatinya — FVG berubah fungsi menjadi **kebalikannya**.

```
Bullish FVG → Di-fill → Harga menembus ke bawah FVG
→ FVG berubah menjadi IFVG (Bearish) = resistance baru

Contoh:
    [Bullish FVG] ← Terbentuk
    Harga turun mengisi FVG
    Harga terus turun melewati batas bawah FVG
    [FVG ini sekarang = Bearish IFVG]
    Jika harga naik ke sini → expect sell
```

---

## 7.7 Volume Imbalance (VI)

**Volume Imbalance** lebih kecil dari FVG — terbentuk ketika ada gap antara Close candle sebelumnya dan Open candle berikutnya.

```
Candle 1: Close = X
Candle 2: Open  = Y (di atas X, ada gap)

Gap antara X dan Y = Volume Imbalance
```

VI biasanya lebih cepat diisi karena ukurannya kecil.

---

## 7.8 Consequent Encroachment (CE)

**CE** = titik tengah (50%) dari FVG. Ini adalah level yang paling sering menjadi area di mana harga bereaksi sebelum melanjutkan pergerakan.

```
FVG:
───── High FVG
  ↑
  CE (50%) ← Harga sering berhenti di sini
  ↓
───── Low FVG
```

---

## 7.9 FVG + OB Kombinasi (Premium Entry)

Ketika FVG dan OB berada di zona yang sama atau overlapping:

```
Bullish Setup:
─────────── High OB ─────────
   [OB Zone]                  ← OB bullish
─────────── Low OB / High FVG ← Area overlap = PREMIUM
   [FVG Zone]
─────────── Low FVG ──────────

Entry di zona overlap = Optimal Trade Entry (OTE)
Highest probability setup
```

---

## 7.10 Contoh Skenario

### Skenario: XAUUSD Bullish FVG Entry
```
1. D1/H4: Trend bullish, baru saja BOS ke atas
2. H1: Displacement bullish terjadi → FVG terbentuk
3. Harga koreksi ke bawah
4. Harga masuk ke dalam FVG
5. Di FVG: muncul candle bullish engulfing
6. Entry BUY di close engulfing
7. SL: Di bawah Low FVG
8. TP: Swing High terbaru / BSL yang terlihat
9. RR: Minimal 1:2
```

---

## 7.11 Gap pada Market Open

Khusus untuk **indeks (NAS100, S&P500)** dan **saham** — ada **weekend gap** atau **overnight gap** yang fungsinya mirip FVG. Market cenderung mengisi gap ini sebelum melanjutkan trend.

---

## 7.12 Kesimpulan Modul 07

- FVG = celah dari 3 candle yang tidak sempat diperdagangkan
- Market cenderung kembali mengisi FVG
- FVG + OB = zona entry premium (OTE)
- FVG yang sudah ditembus sepenuhnya → berubah jadi IFVG
- CE (50% FVG) adalah level reaksi yang umum

---

> **Latihan**: Di NAS100 H1, temukan 5 Bullish FVG dan 5 Bearish FVG. Tandai CE (50%) di setiap FVG. Amati: apakah harga bereaksi di CE? Berapa yang sudah di-fill sepenuhnya?

---

**[← Modul 06](./06-order-block.md)** | **[→ Modul 08: Liquidity](./08-liquidity.md)**
