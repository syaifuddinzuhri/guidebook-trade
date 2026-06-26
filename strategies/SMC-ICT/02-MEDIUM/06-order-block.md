# Modul 06 — Order Block (OB)

> **Level**: 🟡 MEDIUM | **Estimasi belajar**: 5-7 hari

---

## 6.1 Apa itu Order Block?

**Order Block** adalah zona harga terakhir di mana institusi menempatkan order besar **sebelum** pergerakan impulsif terjadi. OB menjadi area di mana harga cenderung **kembali** untuk mengisi order yang belum tereksekusi.

```
Analogi:
Bayangkan kamu punya order beli 10.000 lot di harga 1.1000.
Harga lalu naik ke 1.1200 (order tidak semua terisi).
Harga kemudian turun kembali ke 1.1000 → kamu tambah beli lagi.
Ini yang dilakukan institusi di Order Block.
```

---

## 6.2 Bullish Order Block

### Definisi
Candle **bearish (merah) terakhir** sebelum pergerakan bullish impulsif yang membuat BOS ke atas.

```
Contoh:
     ┌─┐
     │░│ ← Candle bearish = BULLISH ORDER BLOCK
     └─┘
      │
     ┌─┐
     │█│ ← Displacement bullish (impulsif, buat BOS)
     │█│
     │█│
     └─┘
      ...harga terus naik (BOS terkonfirmasi)
      
      Kemudian harga pullback ke zona OB:
      ┌─┐
      └─┘  ← Area OB bullish (zona beli)
```

### Cara Menggambar Bullish OB
1. Temukan BOS bullish yang valid
2. Lihat ke belakang — cari candle bearish **terakhir** sebelum displacement
3. Kotak dari **High ke Low** candle bearish tersebut = zona OB bullish

---

## 6.3 Bearish Order Block

### Definisi
Candle **bullish (hijau) terakhir** sebelum pergerakan bearish impulsif yang membuat BOS ke bawah.

```
Contoh:
     ┌─┐
     │█│ ← Candle bullish = BEARISH ORDER BLOCK
     └─┘
      │
     ┌─┐
     │░│ ← Displacement bearish (impulsif, buat BOS)
     │░│
     │░│
     └─┘
      ...harga terus turun (BOS terkonfirmasi)
      
      Kemudian harga pullback ke zona OB:
      ┌─┐
      └─┘  ← Area OB bearish (zona jual)
```

---

## 6.4 Syarat OB yang Valid

Bukan semua candle sebelum gerakan besar adalah OB yang valid. Syarat:

| Syarat | Penjelasan |
|--------|-----------|
| **Ada BOS setelahnya** | Displacement harus membuat break structure |
| **Displacement impulsif** | Candle displacement harus besar/kuat |
| **Belum di-mitigasi** | OB yang sudah "dikunjungi" dan ditembus ke bawah/atas tidak valid lagi |
| **Konteks HTF mendukung** | Arah OB harus sejalan dengan trend HTF |

---

## 6.5 Mitigasi OB

**Mitigasi** = OB sudah "digunakan" atau dikunjungi oleh harga.

```
Bullish OB Belum Dimitigasi (masih valid):
   [OB zone] ─────────────────────────────
                                          ← Harga belum kembali ke OB
              Harga naik terus

Bullish OB Sudah Dimitigasi (tidak valid):
   [OB zone] ────────────
              ↑
              Harga kembali ke OB → lanjut naik (mitigasi normal)

Bullish OB Gugur (invalid):
   [OB zone] ────────────
              ↑
              Harga kembali ke OB → TURUN MENEMBUS OB ke bawah
              → OB ini sudah tidak valid
```

---

## 6.6 Jenis OB Lanjutan

### 1. Breaker Block
OB yang sudah gagal (dimitigasi dan ditembus) — kini berubah fungsi jadi resistance/supply.

```
Bullish OB → Harga kembali, ditembus ke bawah → 
Sekarang zona ini menjadi Bearish Breaker Block
```

### 2. Rejection Block
Candle dengan wick panjang di area yang kemudian menjadi OB. Wick menunjukkan penolakan kuat dari zona tersebut.

### 3. Propulsion Block
OB yang terbentuk dalam serangkaian gerakan naik/turun — setiap pullback ke OB menjadi opportunity entry.

### 4. Vacuum Block
Zona harga di mana terjadi "kekosongan" order — harga biasanya bergerak cepat melewati area ini.

---

## 6.7 OB + FVG Kombinasi

Sangat sering OB dan FVG (Fair Value Gap) terbentuk berdekatan atau overlap — ini disebut **Optimal Trade Entry (OTE)**.

```
Bullish Displacement:
     ┌─┐ Candle 1 (bearish = OB)
     └─┘
          [FVG di sini — celah antara candle 1 dan 3]
     ┌─┐ Candle 3 (bullish besar = displacement)
     │█│
     └─┘

Zona terbaik untuk entry:
→ High OB sampai Low FVG = Zona Confluent Entry
```

---

## 6.8 Volume Imbalance pada OB

OB yang lebih kuat biasanya memiliki **volume imbalance** — terlihat dari:
- Badan candle sangat besar
- Hampir tidak ada wick
- Pergerakan terjadi cepat (satu atau dua candle)

---

## 6.9 Entry di Order Block

### Setup Entry Bullish OB:
```
1. HTF: Trend bullish (D1/H4 BOS ke atas)
2. ITF: CHOCH bullish atau BOS bullish di H1
3. OB bullish terbentuk di H1/M15
4. Harga pullback ke zona OB
5. Konfirmasi entry: CISD candle atau engulfing bullish di dalam OB
6. Entry: Open candle konfirmasi
7. SL: Di bawah Low OB (+ beberapa pip buffer)
8. TP: Swing High berikutnya / BSL yang terlihat
```

---

## 6.10 Contoh Real Scenario

### XAUUSD — Bullish OB Setup
```
Analisis:
D1: Uptrend, harga baru saja buat HH
H4: Pullback, CHOCH bullish terjadi
H1: Displacement bullish → OB terbentuk di H1

Eksekusi:
- Harga pullback ke OB H1
- Di dalam OB: muncul hammer + wick panjang ke bawah
- Entry BUY di close hammer
- SL: 5 pip di bawah Low OB
- TP: Swing High H4 (2x-3x risk)
- RR ratio: 1:3
```

---

## 6.11 Kesalahan Umum OB

| Kesalahan | Solusi |
|-----------|--------|
| Label setiap candle sebagai OB | Hanya candle sebelum displacement + BOS |
| Tidak cek apakah OB sudah dimitigasi | Selalu cek history — sudah dikunjungi belum? |
| Entry tanpa konfirmasi candle | Tunggu rejection / CISD di dalam OB |
| OB berlawanan dengan HTF | Pastikan OB sejalan dengan bias HTF |

---

## 6.12 Kesimpulan Modul 06

- OB = candle terakhir sebelum displacement impulsif
- Bullish OB = candle bearish sebelum naik
- Bearish OB = candle bullish sebelum turun
- OB yang sudah dimitigasi dan ditembus → tidak valid (jadi Breaker)
- Entry di OB butuh konfirmasi candle

---

> **Latihan**: Di EURUSD H1, cari 5 Bullish OB dan 5 Bearish OB. Tandai dengan kotak. Cek: berapa yang sudah dimitigasi? Berapa yang masih fresh? Apakah harga bereaksi saat kembali ke OB?

---

**[← Modul 05](./05-bos-choch.md)** | **[→ Modul 07: FVG & Imbalance](./07-fvg-imbalance.md)**
