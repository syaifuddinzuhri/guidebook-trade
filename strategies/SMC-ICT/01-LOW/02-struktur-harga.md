# Modul 02 — Struktur Harga (Market Structure)

> **Level**: 🟢 LOW | **Estimasi belajar**: 3-4 hari

---

## 2.1 Building Block: Swing High & Swing Low

Sebelum memahami trend, kamu harus bisa mengidentifikasi **Swing Point**.

### Swing High (SH)
Candle yang punya **higher high** dan **higher low** di kiri-kanannya.

```
        ▲ Swing High
       /|\
      / | \
     /  |  \
────/   |   \────
```

### Swing Low (SL)
Candle yang punya **lower low** dan **lower high** di kiri-kanannya.

```
────\   |   /────
     \  |  /
      \ | /
       \|/
        ▼ Swing Low
```

### Aturan Identifikasi
- Minimal **2 candle di kiri** dan **2 candle di kanan** yang lebih rendah (untuk SH)
- Jangan terlalu ketat, jangan terlalu longgar
- Gunakan **body candle**, bukan wick untuk struktur utama

---

## 2.2 Jenis Trend

### Uptrend (Bullish Structure)
```
        SH2
       /    \
     SH1     \
    /    \    SL2
  SL1    SL2     \
```

Ciri: **Higher High (HH)** dan **Higher Low (HL)**

```
HH2
    \
HH1  \
  \  HL2
  HL1
```

### Downtrend (Bearish Structure)
Ciri: **Lower High (LH)** dan **Lower Low (LL)**

```
LH1
   \
   LH2  \
        LL1
            \
            LL2
```

### Ranging / Sideways
Harga bergerak dalam range horizontal. Neither HH nor LL terbentuk secara konsisten.

---

## 2.3 Cara Membaca Struktur

### Step-by-Step

**1. Mulai dari timeframe besar (D1/H4)**
```
D1 → Tentukan trend besar
H4 → Konfirmasi arah
H1 → Cari setup
M15 → Entry
```

**2. Tandai Swing High dan Swing Low terbaru**

**3. Tentukan apakah sedang:**
- Membuat HH + HL → Bullish
- Membuat LH + LL → Bearish
- Ranging → Tunggu breakout

---

## 2.4 Key Levels

### Previous High & Previous Low
Level harga yang pernah menjadi swing high atau swing low di masa lalu. Sering menjadi area support/resistance.

### Equal Highs (EQH) & Equal Lows (EQL)
```
─────────── EQH ───────────
 ▲           ▲           ▲
             
─────────── EQL ───────────
 ▼           ▼           ▼
```

EQH dan EQL adalah **zona likuiditas** — institusi akan memburu area ini.

### Round Numbers (Big Figures)
Level harga bulat seperti 1.10000, 2000.00, dll. Sering jadi magnet harga.

---

## 2.5 Contoh Identifikasi Struktur

### Skenario Bullish
```
Kondisi awal (downtrend):
LH → LL → LH → LL

Tanda pembalikan:
LH → LL → [harga naik, gagal buat LL baru, malah buat HL]

Konfirmasi bullish:
HL terbentuk → kemudian buat HH → STRUKTUR BERUBAH
```

### Skenario Bearish
```
Kondisi awal (uptrend):
HH → HL → HH → HL

Tanda pembalikan:
HH → HL → [harga turun, gagal buat HH baru, malah buat LH]

Konfirmasi bearish:
LH terbentuk → kemudian buat LL → STRUKTUR BERUBAH
```

---

## 2.6 Kesalahan Umum Pemula

| Kesalahan | Yang Benar |
|-----------|-----------|
| Labeling setiap candle sebagai swing | Minimal 2 candle konfirmasi |
| Hanya lihat satu timeframe | Selalu cek HTF dulu |
| Mengubah label setelah harga bergerak | Tentukan sebelum candle close |
| Terlalu banyak garis di chart | Fokus pada swing terbaru |

---

## 2.7 Kesimpulan Modul 02

- Swing High + Swing Low adalah dasar dari segalanya
- Trend = rangkaian HH-HL (bullish) atau LH-LL (bearish)
- Selalu analisis dari timeframe besar ke kecil
- EQH/EQL = zona likuiditas penting

---

> **Latihan**: Buka EURUSD H4. Tandai 10 Swing High dan 10 Swing Low terbaru. Tentukan trend yang sedang terjadi. Tandai EQH/EQL jika ada.

---

**[← Modul 01](./01-fondasi-market.md)** | **[→ Modul 03: Candlestick](./03-candlestick.md)**
