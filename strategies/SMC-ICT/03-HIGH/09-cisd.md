# Modul 09 — CISD (Change in State of Delivery)

> **Level**: 🔴 HIGH | **Estimasi belajar**: 5-7 hari

---

## 9.1 Apa itu CISD?

**CISD (Change in State of Delivery)** adalah konsep ICT yang mengidentifikasi **perubahan cara harga dikirimkan** — dari bearish delivery ke bullish delivery, atau sebaliknya.

"Delivery" dalam konteks ini mengacu pada **cara institusi mengeksekusi order** — apakah mereka sedang mendistribusikan (menjual) atau mengakumulasi (membeli).

```
State of Delivery = bagaimana harga bergerak dalam konteks yang lebih kecil

Bearish Delivery: Setiap rally diikuti lower high → trend turun
Bullish Delivery: Setiap pullback diikuti higher low → trend naik

CISD = momen ketika state ini BERUBAH
```

---

## 9.2 Ciri-Ciri CISD

### CISD Bullish (dari bearish ke bullish delivery)

**Kondisi sebelum**: Harga dalam bearish delivery (making LH/LL)

**CISD terjadi ketika**:
```
1. Harga membuat LL baru (SSL di-sweep)
2. Candle bullish yang kuat muncul
3. Candle ini MENUTUP DI ATAS swing high lokal sebelumnya
4. Ini menandai perubahan state dari bearish ke bullish

Visualisasi:
    LH
   /  \
  /    LL1
 /         \
/            LL2 (sweep SSL)
              ↑
              │ ← Candle CISD bullish
              │    Close di atas LH lokal
              │─────────────────────────
```

### CISD Bearish (dari bullish ke bearish delivery)

**Kondisi sebelum**: Harga dalam bullish delivery (making HH/HL)

**CISD terjadi ketika**:
```
1. Harga membuat HH baru (BSL di-sweep)
2. Candle bearish yang kuat muncul
3. Candle ini MENUTUP DI BAWAH swing low lokal sebelumnya
4. Ini menandai perubahan state dari bullish ke bearish

Visualisasi:
                HH2 (sweep BSL)
               /
            HL2
           /
        HH1
       /
     HL1
              ↓
              │ ← Candle CISD bearish
              │    Close di bawah HL lokal
              │─────────────────────────
```

---

## 9.3 CISD vs CHOCH

Banyak yang membingungkan CISD dan CHOCH. Ini perbedaannya:

| | CHOCH | CISD |
|--|-------|------|
| **Scope** | Perubahan struktur besar | Perubahan cara delivery lokal |
| **Timeframe** | Terlihat di ITF/HTF | Sering di LTF (M5/M15) |
| **Penggunaan** | Tentukan bias | Konfirmasi entry |
| **Validasi** | Close di luar swing point | Close yang mengubah momentum delivery |
| **Konteks** | Standalone signal | Digunakan setelah OB/FVG/sweep |

**Hubungan**: CISD sering terjadi SETELAH CHOCH sebagai konfirmasi entry — CHOCH di H1, lalu CISD di M15 untuk precision entry.

---

## 9.4 Cara Identifikasi CISD

### Step-by-Step

**Step 1**: Identifikasi state of delivery saat ini
```
Bearish delivery: Candle-candle membuat LH/LL berulang
Bullish delivery: Candle-candle membuat HH/HL berulang
```

**Step 2**: Cari area di mana perubahan mungkin terjadi
- Dekat OB atau FVG
- Setelah sweep likuiditas
- Di zona HTF yang signifikan

**Step 3**: Tunggu candle CISD
```
Untuk bullish CISD:
- Candle harus menutup di ATAS swing high lokal terakhir
- Body candle harus relatif besar (komitmen kuat)
- Idealnya ada wick bawah yang panjang (rejection)
```

**Step 4**: Konfirmasi
```
Setelah candle CISD: apakah candle berikutnya melanjutkan?
- Bullish CISD valid: candle berikutnya tidak turun ke bawah low CISD
- Jika turun ke bawah low CISD: CISD invalid / false signal
```

---

## 9.5 CISD Entry Model

### Model 1: CISD + OB
```
Setup Bullish:
1. HTF: Bias bullish
2. LTF: Harga dalam bearish delivery (pullback)
3. Harga masuk zona OB bullish
4. Dalam OB: Sweep SSL lokal
5. CISD bullish candle muncul (close di atas swing lokal)
6. ENTRY: Open candle setelah CISD atau close candle CISD
7. SL: Di bawah low CISD candle / di bawah low sweep
8. TP: BSL berikutnya / swing high HTF
```

### Model 2: CISD + FVG Fill
```
Setup Bullish:
1. Displacement bullish terjadi → FVG terbentuk
2. Harga pullback ke FVG
3. Dalam FVG: bearish delivery sementara
4. CISD bullish terjadi di dalam/di bawah FVG
5. ENTRY: Close CISD candle
6. SL: Di bawah low CISD
7. TP: High yang terbentuk sebelum pullback / likuiditas berikutnya
```

### Model 3: CISD setelah Liquidity Sweep
```
Setup Bullish:
1. EQL terbentuk (SSL kuat)
2. Harga sweep ke bawah EQL
3. Wick panjang ke bawah
4. Candle berikutnya: CISD bullish (close di atas level sweep)
5. ENTRY: Segera setelah close CISD
6. SL: Di bawah wick sweep
7. TP: EQH di atas / BSL terdekat
```

---

## 9.6 CISD pada Berbagai Timeframe

### HTF CISD (H4/D1)
- Jarang terjadi tapi sangat powerful
- Menandai perubahan bias besar
- Biasanya setelah weekly/monthly sweep

### ITF CISD (H1)
- Paling umum untuk setup trading
- Konfirmasi setelah CHOCH H4
- Entry area yang baik

### LTF CISD (M15/M5)
- Precision entry
- Digunakan setelah CISD H1 untuk timing lebih baik
- Risk/reward lebih baik karena SL lebih ketat

---

## 9.7 Candle Pattern yang Menandai CISD

### Bullish CISD Candle Types:
```
1. Strong Bullish Engulfing
   ┌─┐
   │█│ ← Close di atas swing lokal
   │█│    Body besar
   └─┘

2. Hammer dengan Body Bullish
     │
   ┌─┐
   │█│ ← Close di atas swing lokal
   └─┘

3. Marubozu Bullish
   ┌─┐
   │█│ ← Close di atas, tidak ada wick
   │█│
   └─┘
```

### Bearish CISD Candle Types (kebalikannya):
- Bearish Engulfing yang menutup di bawah swing lokal
- Shooting Star + Body Bearish
- Marubozu Bearish

---

## 9.8 Invalidasi CISD

CISD dianggap **invalid** jika:
```
1. Setelah CISD bullish: harga turun melewati LOW candle CISD
2. Setelah CISD bearish: harga naik melewati HIGH candle CISD
3. Tidak ada konfirmasi — candle CISD langsung diikuti candle berlawanan
```

Jika CISD invalid → jangan entry, atau jika sudah entry → keluar dari posisi.

---

## 9.9 Contoh Real Scenario

### XAUUSD M15 — CISD Bullish Entry
```
Konteks:
- D1: Uptrend, baru buat HH
- H4: Pullback ke OB H4
- H1: CHOCH bullish sudah terjadi
- M15: Harga masuk OB H1

Yang terjadi di M15:
Jam 14:30 WIB (London Open Kill Zone):
- Harga turun dulu ke bawah swing low M15 lokal (sweep SSL kecil)
- Candle 14:45: Bullish besar, close di atas swing high M15 sebelumnya → CISD!
- Konfirmasi: Candle 15:00 bullish, tidak kembali ke bawah

Entry:
- BUY di close candle 14:45 (atau open candle 15:00)
- SL: 5 pip di bawah low candle 14:45
- TP1: Swing high H1 (1:2 RR)
- TP2: BSL H4 (1:4 RR)
```

---

## 9.10 Kesimpulan Modul 09

- CISD = perubahan cara harga dikirimkan oleh market maker
- Bullish CISD: candle close di atas swing high lokal dalam konteks bearish delivery
- Bearish CISD: candle close di bawah swing low lokal dalam konteks bullish delivery
- Paling powerful ketika terjadi di zona OB/FVG setelah sweep likuiditas
- Invalid jika harga menembus low/high candle CISD

---

> **Latihan**: Di XAUUSD M15, fokus pada London Kill Zone (14:00-16:00 WIB). Selama 2 minggu, amati dan catat setiap CISD yang terjadi. Hitung win rate: berapa yang dilanjutkan ke TP vs yang gagal?

---

**[← Modul 08](../02-MEDIUM/08-liquidity.md)** | **[→ Modul 10: Multi-Timeframe](./10-multi-timeframe.md)**
