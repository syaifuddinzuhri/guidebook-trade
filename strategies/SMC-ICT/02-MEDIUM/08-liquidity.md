# Modul 08 — Liquidity (Likuiditas)

> **Level**: 🟡 MEDIUM | **Estimasi belajar**: 4-5 hari

---

## 8.1 Mengapa Likuiditas Sangat Penting?

Institusi besar tidak bisa langsung "klik beli" seperti retail. Mereka butuh **penjual** dalam jumlah besar untuk mengisi posisi beli mereka. 

Likuiditas = kumpulan order yang bisa dieksekusi institusi.

```
Institusi mau BUY 10.000 lot → butuh penjual 10.000 lot
→ Penjual terbesar = Stop Loss para retail buyer
→ Stop Loss retail buyer biasanya: DI BAWAH swing low, di bawah round number, di bawah EQL
→ Institusi gerakkan harga ke sana dulu, trigger stop → mereka dapat likuiditas
→ Setelah itu baru harga naik ke tujuan mereka yang sebenarnya
```

---

## 8.2 Buy Side Liquidity (BSL)

**BSL** = kumpulan order yang ada **di atas** harga saat ini.

Siapa yang membentuk BSL?
- Stop Loss para trader yang SELL (stop mereka ada di atas)
- Buy Stop order dari breakout trader
- Limit Sell order yang menunggu di swing high

```
─────────── Swing High / Equal High ← BSL ada di sini
                                       (stop loss para seller)
  Harga saat ini
─────────────────────────────────────
```

**Skenario**: Institusi ingin SELL. Mereka perlu beli dulu di harga lebih tinggi, jadi mereka push harga naik ke BSL, trigger stop loss seller → sekarang ada "penjual" → institusi masuk sell.

---

## 8.3 Sell Side Liquidity (SSL)

**SSL** = kumpulan order yang ada **di bawah** harga saat ini.

Siapa yang membentuk SSL?
- Stop Loss para trader yang BUY (stop mereka ada di bawah)
- Sell Stop order dari breakdown trader
- Limit Buy order yang menunggu di swing low

```
─────────────────────────────────────
  Harga saat ini

─────────── Swing Low / Equal Low ← SSL ada di sini
                                      (stop loss para buyer)
```

---

## 8.4 Jenis-Jenis Zona Likuiditas

### 1. Swing High/Low Liquidity
Area di atas swing high atau di bawah swing low — paling umum.

### 2. Equal Highs (EQH) / Equal Lows (EQL)
```
EQH: Dua atau lebih high yang berdekatan di level sama
─────── H1 ─── H2 ─── H3 ─── ← BSL (sangat kuat)

EQL: Dua atau lebih low yang berdekatan di level sama
─────── L1 ─── L2 ─── L3 ─── ← SSL (sangat kuat)
```

EQH/EQL lebih kuat karena lebih banyak stop loss yang terkumpul di satu level.

### 3. Round Number Liquidity
Level psikologis seperti 2000.00, 1.1000, 150.00 — banyak order ditempatkan di sini.

### 4. Previous High/Low (PWH/PWL)
- Previous Week High/Low
- Previous Day High/Low
- Previous Month High/Low

Level-level ini sangat diperhatikan institusi.

### 5. Trendline Liquidity
Stop loss trader yang mengikuti trendline ditempatkan di bawah/atas trendline.

---

## 8.5 Liquidity Sweep (Stop Hunt)

**Sweep** terjadi ketika harga menembus zona likuiditas — trigger semua stop — lalu **berbalik arah**.

```
Bullish Sweep (Sweep SSL untuk naik):
─────────────────────────────────────
 Harga turun ke SSL
 ─── SSL ─── ← Harga tembus ke bawah (trigger stop)
     ↓↓↓
     wick panjang ke bawah
     ↑↑↑
 Harga balik naik → THIS IS THE MOVE
─────────────────────────────────────
```

```
Bearish Sweep (Sweep BSL untuk turun):
─────────── BSL ─── ← Harga tembus ke atas (trigger stop)
                ↑↑↑
                wick panjang ke atas
                ↓↓↓
 Harga balik turun → THIS IS THE MOVE
─────────────────────────────────────
```

---

## 8.6 Cara Membaca Liquidity Sweep

### Ciri Sweep yang Valid:
1. Harga menembus level dengan **wick** (bukan close)
2. Setelah wick: candle berikutnya menutup **kembali** ke dalam range
3. Volume spike (jika tersedia)
4. Terjadi di zona SMC yang relevan (OB, FVG)

```
SWEEP VALID:
        │   ← Wick menembus ke bawah SSL
       ┌─┐
       │█│  ← Candle berikutnya close di atas SSL = sweep terkonfirmasi
       └─┘
────── SSL ─────

BUKAN SWEEP (Breakdown):
       ┌─┐
       │░│  ← Candle CLOSE di bawah SSL = ini bukan sweep, ini breakdown
       └─┘
────── SSL ─────
```

---

## 8.7 HTF vs LTF Liquidity

### HTF Liquidity (D1/W/MN)
- Swing high/low dari timeframe besar
- Bergerak jauh, perlu waktu berminggu-minggu
- Target TP jarak jauh

### ITF Liquidity (H4/H1)
- Swing high/low dari timeframe menengah
- Target TP jarak menengah

### LTF Liquidity (M15/M5)
- Swing micro / equal high/low kecil
- Digunakan untuk entry precision dan SL placement

---

## 8.8 Urutan Pergerakan Harga (Liquidity Logic)

Institusi selalu bergerak dari satu zona likuiditas ke zona likuiditas berikutnya:

```
1. Harga ada di area bawah
2. SSL di bawah → di-SWEEP dulu
3. Setelah sweep SSL → harga naik (likuiditas sudah dapat)
4. Harga naik menuju BSL di atas
5. BSL → di-SWEEP
6. Setelah sweep BSL → harga turun lagi
7. Menuju SSL berikutnya di bawah...
```

Ini seperti "hunt → move → hunt → move" yang berulang.

---

## 8.9 Drawing Liquidity Levels

### Cara Menandai di Chart:
1. Identifikasi semua Swing High dan Swing Low signifikan
2. Cari Equal High/Low (lebih dari 1 sentuhan di level yang sama)
3. Tandai Previous Day/Week High dan Low
4. Perhatikan round numbers

### Tips Visual:
- Gunakan garis horizontal putus-putus untuk liquidity
- Warna berbeda untuk BSL (biru/hijau) dan SSL (merah/orange)
- Jangan terlalu banyak level — fokus pada 3-5 yang paling jelas

---

## 8.10 Contoh Skenario Trading

### Skenario: SSL Sweep → Entry Bullish
```
Setup:
1. D1: Uptrend, HTF bias bullish
2. H4: Pullback, EQL terbentuk di bawah
3. H1: Harga mendekati EQL
4. M15: Candle wick panjang ke bawah EQL (sweep SSL)
5. M15: Candle berikutnya bullish engulfing, close di atas EQL
6. Entry: Buy di close engulfing
7. SL: Di bawah wick terendah
8. TP: BSL terdekat di atas
```

---

## 8.11 Kesimpulan Modul 08

- Likuiditas = target gerakan harga institusi
- BSL di atas (stop loss seller), SSL di bawah (stop loss buyer)
- EQH/EQL = likuiditas yang sangat kuat
- Sweep = harga tembus lalu balik (wick) = sinyal entry
- Market selalu bergerak dari satu zona likuiditas ke lainnya

---

> **Latihan**: Di XAUUSD H4, tandai 5 BSL dan 5 SSL yang paling jelas. Amati pergerakan harga 1 bulan ke belakang: berapa kali harga di-sweep sebelum berbalik? Apa yang terjadi setelah sweep?

---

**[← Modul 07](./07-fvg-imbalance.md)** | **[→ Modul 09: CISD](../03-HIGH/09-cisd.md)**
