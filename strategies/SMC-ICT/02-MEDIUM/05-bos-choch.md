# Modul 05 — BOS & CHOCH

> **Level**: 🟡 MEDIUM | **Estimasi belajar**: 4-5 hari

---

## 5.1 Mengapa BOS & CHOCH Penting?

BOS dan CHOCH adalah **inti dari struktur SMC**. Tanpa memahami ini, kamu tidak bisa:
- Menentukan bias (bullish/bearish)
- Tahu kapan trend berubah
- Menemukan zona entry yang tepat

---

## 5.2 BOS — Break of Structure

### Definisi
**BOS** terjadi ketika harga melanjutkan arah trend dengan **menembus Swing High atau Swing Low yang signifikan**.

### BOS Bullish
```
              BOS ↑
         ─────────── ← Swing High ditembus
        /
  ──── /
      /
SH1──     ← Swing High sebelumnya belum ditembus
    \
     HL1
```

Artinya: Trend bullish **terkonfirmasi berlanjut**.

### BOS Bearish
```
LH1──     ← Swing Low sebelumnya belum ditembus
    \
     LL1
      \
  ──── \
        \
         ─────────── ← Swing Low ditembus
              BOS ↓
```

Artinya: Trend bearish **terkonfirmasi berlanjut**.

---

## 5.3 CHOCH — Change of Character

### Definisi
**CHOCH** terjadi ketika harga **melanggar struktur yang berlawanan dengan trend saat ini** — pertanda pembalikan awal.

### CHOCH dari Bearish ke Bullish
```
Kondisi: Sedang downtrend (LH → LL → LH → LL)

LH1
   \
    LL1
       \
       LH2 ← Ini masih LH (lower high)
       /
      /
     /──────── ← CHOCH! Harga tembus LH sebelumnya
    /
  LL2
```

Artinya: Struktur berubah — potensi reversal ke bullish.

### CHOCH dari Bullish ke Bearish
```
Kondisi: Sedang uptrend (HH → HL → HH → HL)

          HH2
         /
       HH1
       /
     HL1
         \
          HL2
              \──────── ← CHOCH! Harga tembus HL sebelumnya
```

Artinya: Struktur berubah — potensi reversal ke bearish.

---

## 5.4 Perbedaan BOS vs CHOCH

| | BOS | CHOCH |
|--|-----|-------|
| **Artinya** | Lanjutan trend | Perubahan trend |
| **Konteks** | Dalam trend yang sudah ada | Setelah series LH/LL atau HH/HL |
| **Tindakan** | Cari entry searah trend | Bersiap reversal |
| **Risiko** | Lebih rendah | Lebih tinggi (perlu konfirmasi) |

---

## 5.5 Cara Membaca BOS & CHOCH Step by Step

### Langkah 1: Identifikasi Swing Points
Tandai semua Swing High dan Swing Low yang signifikan.

### Langkah 2: Tentukan Trend Awal
Apakah membuat HH/HL atau LH/LL?

### Langkah 3: Monitor Penembusan
- Jika ditembus searah trend → **BOS**
- Jika ditembus berlawanan trend → **CHOCH**

### Langkah 4: Konfirmasi dengan Candle Close
**Penting**: BOS/CHOCH hanya valid jika candle **CLOSE** di luar level, bukan hanya wick.

```
TIDAK VALID:          VALID:
   ─────               ─────
  ╱ wick menembus     ┌─┐  Close menembus
─╱                    └─┘
                         ─────
```

---

## 5.6 BOS & CHOCH pada Multi-Timeframe

### Prinsip
- **HTF (H4/D1)**: BOS/CHOCH menentukan bias besar
- **ITF (H1)**: BOS/CHOCH menentukan arah trading hari ini
- **LTF (M15/M5)**: BOS/CHOCH menentukan entry precision

### Contoh:
```
D1: Uptrend (HH/HL) → Bias Bullish
H4: Sedang koreksi ke bawah → Tunggu CHOCH bullish di H4
H1: CHOCH bullish terjadi di OB → Setup entry!
M15: BOS bullish kecil → Konfirmasi entry
```

---

## 5.7 Inducement (IDM)

Konsep penting sebelum CHOCH: **Inducement**.

```
Kondisi downtrend:
LH1
   \
    LL1
       \
       LH2 (ini adalah IDM — "umpan" untuk seller)
       /↑
      /   ← harga naik dulu, TAPI belum CHOCH
     /
   LL2 (masih buat LL baru → trend masih bearish)
       \
        LH3
        /
       /──── CHOCH! (baru sekarang reversal)
```

**IDM** adalah gerakan harga yang terlihat seperti reversal tapi sebenarnya hanya "umpan" sebelum harga melanjutkan trend aslinya.

Cara membedakan IDM vs CHOCH:
- IDM: Tidak menembus swing point tertinggi sebelumnya
- CHOCH: Menembus swing point tertinggi sebelumnya (dalam downtrend)

---

## 5.8 Contoh Real Skenario

### Skenario 1: Entry setelah BOS Bullish
```
Situasi: XAUUSD H4 uptrend
1. HH terbentuk di 2050
2. Harga koreksi ke HL di 2030
3. Harga naik lagi dan BOS di atas 2050 ✓
4. Setelah BOS: cari pullback ke OB atau FVG untuk entry BUY
5. Target: Swing High berikutnya / likuiditas di atas
```

### Skenario 2: Entry setelah CHOCH Bullish
```
Situasi: XAUUSD H1 downtrend
1. LH → LL → LH → LL → LH (sudah jelas downtrend)
2. Harga tembus LH terakhir → CHOCH!
3. Konfirmasi: cari OB bullish atau FVG yang terbentuk
4. Entry BUY di zona tersebut
5. SL: di bawah LL terakhir
6. TP: Area resistensi / swing high HTF
```

---

## 5.9 Kesalahan Umum

| Kesalahan | Solusi |
|-----------|--------|
| BOS dari wick, bukan close | Tunggu candle close |
| Label CHOCH tanpa konteks trend | Pastikan ada series HH/HL atau LH/LL dulu |
| Terlalu banyak BOS di chart | Fokus pada swing yang signifikan saja |
| Entry langsung saat CHOCH tanpa konfirmasi | Tunggu pullback ke OB/FVG |

---

## 5.10 Kesimpulan Modul 05

- BOS = konfirmasi trend berlanjut
- CHOCH = sinyal awal pembalikan
- Wajib candle CLOSE untuk validasi
- IDM bisa menipu — tunggu konfirmasi CHOCH sejati
- Kombinasikan dengan OB dan FVG untuk entry (modul berikutnya)

---

> **Latihan**: Buka EURUSD D1. Mulai dari 3 bulan yang lalu. Tandai semua BOS dan CHOCH. Hitung: berapa BOS yang valid dan berapa CHOCH yang valid? Apakah arah setelah CHOCH benar-benar berbalik?

---

**[← Modul 04](../01-LOW/04-session-waktu.md)** | **[→ Modul 06: Order Block](./06-order-block.md)**
