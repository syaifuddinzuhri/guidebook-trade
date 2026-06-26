# Modul 03 — Candlestick

> **Level**: 🟢 LOW | **Estimasi belajar**: 2-3 hari

---

## 3.1 Anatomi Candlestick

```
        │  ← Upper Wick/Shadow
       ┌─┐
       │ │ ← Body (Open ke Close)
       └─┘
        │  ← Lower Wick/Shadow
```

| Bagian | Arti |
|--------|------|
| **Open** | Harga saat candle mulai |
| **Close** | Harga saat candle selesai |
| **High** | Harga tertinggi dalam periode |
| **Low** | Harga terendah dalam periode |
| **Body** | Selisih antara Open dan Close |
| **Wick/Shadow** | Harga yang "ditolak" market |

### Bullish vs Bearish Candle

```
Bullish (Naik)         Bearish (Turun)
      │                      │
     ┌─┐                    ┌─┐  ← Open
     │█│ ← Close            │░│
     │█│                    │░│
     └─┘ ← Open             └─┘  ← Close
      │                      │
```

- **Bullish**: Close > Open (biasanya warna hijau/putih)
- **Bearish**: Close < Open (biasanya warna merah/hitam)

---

## 3.2 Jenis Candle Berdasarkan Ukuran

### Marubozu (Candle Kuat)
```
    ┌─┐
    │█│  ← Tidak ada wick / wick sangat kecil
    │█│     Menunjukkan momentum kuat satu arah
    └─┘
```

### Doji (Keseimbangan)
```
      │
    ──┼──   ← Open ≈ Close
      │     Menunjukkan ketidakpastian
```

### Candle Berwick Panjang (Pin Bar / Hammer)
```
      │   ← Wick panjang ke atas = penolakan harga tinggi
    ┌─┐
    └─┘
      (kecil atau tidak ada)
```

---

## 3.3 Pola Candle Penting dalam SMC

### Hammer (Bullish)
```
      │
    ┌─┐   Wick bawah panjang (minimal 2x body)
    └─┘   Body kecil di atas
```
- **Sinyal**: Penolakan harga rendah, potensi naik
- **Konteks**: Lebih valid di zona support / OB bullish

### Shooting Star (Bearish)
```
    ┌─┐
    └─┘   Body kecil di bawah
      │   Wick atas panjang
```
- **Sinyal**: Penolakan harga tinggi, potensi turun
- **Konteks**: Lebih valid di zona resistance / OB bearish

### Engulfing (Pembalikan Kuat)
```
Bullish Engulfing:
Candle 1: ┌─┐ (kecil, bearish)
           └─┘
Candle 2:  ┌──┐ (besar, bullish, body mencakup candle 1)
           └──┘

Bearish Engulfing: Kebalikannya
```
- **Sinyal**: Perubahan arah yang kuat
- **Di SMC**: Sering terjadi di OB atau setelah sweep likuiditas

---

## 3.4 Candle Khusus ICT

### Displacement Candle
Candle dengan body besar yang bergerak jauh dalam satu arah — menciptakan FVG.

```
Bullish Displacement:
    │
   ┌─┐
   │█│  ← Body besar naik drastis
   │█│     Sering membuat FVG di bawahnya
   └─┘
```

### Mitigation Candle
Candle yang kembali ke zona OB setelah displacement — menunjukkan harga "mengisi" zona tersebut.

### CISD Candle (Change in State of Delivery)
Candle yang menutup kuat melewati level tertentu, menandakan perubahan momentum delivery.

```
Sebelum: ─┐   ┌─ harga ranging / delivery bearish
           └─┘

CISD: ─┐     ┌──────  candle bullish kuat melewati high sebelumnya
        └────┘
```

---

## 3.5 Cara Membaca Candle dalam Konteks SMC

Candle **tidak berdiri sendiri** — selalu baca dalam konteks:

```
BUKAN ini:
"Oh ada hammer, langsung buy!"

TAPI ini:
"Ada hammer DI DALAM Order Block bullish, 
setelah sweep SSL, 
pada uptrend H4 → ini valid setup"
```

### Checklist Konteks Candle:
- [ ] Trend HTF mendukung arah candle?
- [ ] Candle muncul di zona penting (OB, FVG, level key)?
- [ ] Ada liquidity yang sudah di-sweep sebelumnya?
- [ ] Volume / momentum mendukung?

---

## 3.6 Wick Analysis

Wick menunjukkan **penolakan harga** — sangat penting dalam SMC.

```
Upper wick panjang = Institusi MENJUAL di harga tinggi
Lower wick panjang = Institusi MEMBELI di harga rendah
```

### Wick ke dalam OB / FVG
Jika harga "wick" ke dalam Order Block lalu kembali — ini adalah **konfirmasi** bahwa zona tersebut valid.

---

## 3.7 Timeframe dan Candle

| Timeframe | Setiap Candle = | Digunakan untuk |
|-----------|-----------------|-----------------|
| MN | 1 Bulan | Bias jangka panjang |
| W | 1 Minggu | Bias besar |
| D1 | 1 Hari | Struktur utama |
| H4 | 4 Jam | Konfirmasi HTF |
| H1 | 1 Jam | Zona entry |
| M15 | 15 Menit | Refinement entry |
| M5 | 5 Menit | Precision entry |

---

## 3.8 Kesimpulan Modul 03

- Body candle = komitmen, wick = penolakan
- Candle harus dibaca dalam konteks zona dan trend
- Displacement candle menciptakan FVG
- CISD candle menandakan perubahan momentum

---

> **Latihan**: Di TradingView, identifikasi 5 Hammer dan 5 Shooting Star di XAUUSD H1. Catat: apakah masing-masing muncul di zona penting? Apakah hasilnya sesuai ekspektasi?

---

**[← Modul 02](./02-struktur-harga.md)** | **[→ Modul 04: Session & Waktu](./04-session-waktu.md)**
