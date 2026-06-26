# Modul 11 — Entry Model Lengkap

> **Level**: 🔴 HIGH | **Estimasi belajar**: 7-10 hari

---

## 11.1 Komponen Entry yang Benar

Entry yang baik bukan hanya "kapan masuk" — tapi juga **bagaimana** masuk dengan risiko terkontrol.

```
Entry yang benar terdiri dari:
1. BIAS     — Arah yang dituju (bullish/bearish)
2. ZONA     — Di mana harga akan entry (OB, FVG, level)
3. TRIGGER  — Sinyal masuk yang spesifik (CISD, engulfing, dll)
4. SL       — Batas kerugian yang jelas
5. TP       — Target yang realistis dan terukur
6. RR       — Risk/Reward ratio minimum 1:2
```

---

## 11.2 Entry Type 1: Limit Order (Pending)

Pasang order di zona yang sudah diidentifikasi sebelum harga sampai ke sana.

### Keuntungan:
- Tidak perlu monitor chart terus
- Entry lebih awal = RR lebih baik
- Tidak terlambat karena emosi

### Kerugian:
- Bisa tidak terisi jika harga tidak sampai
- Tidak ada konfirmasi candle (lebih agresif)

### Cara Pasang:
```
1. Identifikasi OB atau FVG
2. Pasang Buy Limit di: High OB atau Low FVG (untuk bullish)
3. SL: Di bawah Low OB + buffer
4. TP: BSL/swing high berikutnya
5. Set alert jika harga mendekati zona
```

---

## 11.3 Entry Type 2: Market Order dengan Konfirmasi Candle

Masuk setelah ada sinyal konfirmasi candle di zona yang sudah diidentifikasi.

### Keuntungan:
- Konfirmasi lebih kuat (ada sinyal visual)
- Lebih aman dari false setup

### Kerugian:
- Entry lebih mahal (harga sudah bergerak sedikit)
- RR sedikit berkurang
- Perlu monitor chart lebih aktif

### Cara Masuk:
```
1. Identifikasi zona (OB/FVG)
2. Tunggu harga masuk ke zona
3. Tunggu candle konfirmasi (engulfing, hammer, CISD)
4. Masuk di CLOSE candle konfirmasi
5. SL: Beberapa pip di bawah Low candle konfirmasi
```

---

## 11.4 Model Entry A: Classic OB Entry

```
Kondisi:
- HTF: Bullish bias
- ITF: CHOCH bullish, OB bullish terbentuk

Eksekusi di LTF:
┌──────────────────────────────────────────────┐
│                                              │
│  High OB ─── Entry Zone ─────────────────── │
│  Low OB  ─── Stop Loss Area ─────────────── │
│                                              │
│  1. Harga masuk OB zone                      │
│  2. Tunggu rejection (wick / engulfing)       │
│  3. Entry saat candle konfirmasi close        │
│  4. SL: 5-10 pip di bawah Low OB             │
│  5. TP: Swing High / BSL berikutnya          │
└──────────────────────────────────────────────┘
```

---

## 11.5 Model Entry B: FVG Fill Entry

```
Kondisi:
- Displacement impulsif terjadi → FVG terbentuk
- HTF/ITF mendukung arah tersebut

Eksekusi:
┌──────────────────────────────────────────────┐
│  High FVG ─────────────────────────────────  │
│  CE (50%) ─── Entry Zone (ideal) ──────────  │
│  Low FVG  ─────────────────────────────────  │
│                                              │
│  1. Tandai FVG                               │
│  2. Pasang limit order di CE (50%) atau      │
│     tunggu harga masuk + konfirmasi          │
│  3. SL: Di bawah Low FVG                     │
│  4. TP: High yang terbentuk sebelum FVG      │
└──────────────────────────────────────────────┘
```

---

## 11.6 Model Entry C: Liquidity Sweep Entry

```
Setup terbaik — Sweep → Reversal Entry

Timeline:
1. Identifikasi SSL/BSL yang kuat (EQL/EQH atau previous low/high)
2. Tunggu harga mendekati level tersebut
3. Harga sweep level (wick menembus, lalu candle close kembali)
4. Saat candle close kembali di dalam range → ENTRY
5. SL: Di luar wick extreme (5 pip buffer)
6. TP: Likuiditas di sisi berlawanan

Visualisasi Bullish:
            Entry ↑
     ┌─┐───────────────────────
     │█│  ← Close kembali di atas SSL = ENTRY SIGNAL
     └─┘
      │  ← Wick panjang ke bawah
──── SSL ────────────────────── ← SSL tertembus (sweep)
```

---

## 11.7 Model Entry D: CISD Entry (Presisi Tertinggi)

```
Paling presisi — digunakan setelah sweep + di dalam OB/FVG

1. HTF bias confirmed ✓
2. ITF: CHOCH/BOS dan zona entry identified ✓
3. LTF: Harga dalam zona, bearish delivery sementara
4. Sweep SSL lokal dalam zona
5. CISD bullish candle → Close di atas swing high lokal
6. Entry: Close candle CISD atau open candle berikutnya
7. SL: Di bawah Low CISD candle

Keunggulan:
- SL sangat ketat → RR sangat bagus (1:4, 1:5, bahkan lebih)
- Konfirmasi kuat (perubahan delivery)
```

---

## 11.8 Stop Loss Placement

SL yang benar harus ditempatkan di level yang **membuktikan setup kamu SALAH** jika tertembus.

### Rules SL Placement:

**Untuk Bullish Entry:**
```
SL di BAWAH:
- Low OB (jika entry di OB)
- Low FVG (jika entry di FVG)
- Wick terendah (jika entry setelah sweep)
- Low CISD candle (jika entry CISD)
+ Buffer: 5-15 pip (tergantung pair dan timeframe)
```

**Untuk Bearish Entry:**
```
SL di ATAS:
- High OB (jika entry di OB)
- High FVG (jika entry di FVG)
- Wick tertinggi (jika entry setelah sweep)
- High CISD candle (jika entry CISD)
+ Buffer: 5-15 pip
```

### SL terlalu ketat vs terlalu longgar:
```
Terlalu ketat:
→ Sering kena SL padahal arah akhirnya benar
→ Frustrasi dan overtrading

Terlalu longgar:
→ Rugi besar per trade
→ RR jelek

Optimal: Tepat di bawah/atas zona yang membuat setup invalid
```

---

## 11.9 Take Profit Placement

### TP Berdasarkan Likuiditas:
```
TP1: Swing high/low terdekat (BSL/SSL pertama)
TP2: Swing high/low berikutnya (BSL/SSL kedua)
TP3: HTF target (major swing / weekly level)
```

### TP Berdasarkan RR Ratio:
```
Minimal: RR 1:2 (risiko 1, target 2)
Ideal: RR 1:3 atau lebih
Premium setup: RR 1:5+

Cara hitung:
Risk = Entry - SL (untuk buy) = 20 pip
TP dengan RR 1:2 = Entry + (20 x 2) = Entry + 40 pip
TP dengan RR 1:3 = Entry + (20 x 3) = Entry + 60 pip
```

### Partial Take Profit:
```
Setup dengan multiple TP:
50% posisi → Close di TP1
Move SL ke Breakeven setelah TP1 hit
Sisa 50% → Biarkan jalan ke TP2 atau lebih
```

---

## 11.10 SL to Breakeven

Kapan pindah SL ke breakeven (entry price)?

```
Move to BE ketika:
1. TP1 sudah hit (jika ada partial TP)
2. Harga sudah bergerak 1:1 dari entry (risiko sama dengan potensi yang sudah berjalan)
3. Terbentuk structure baru yang mendukung (BOS di arah profit)

Jangan terlalu cepat move to BE:
→ Market butuh "nafas" — bisa kena SL lalu lanjut ke arah yang benar
```

---

## 11.11 Contoh Lengkap Entry Model

### EURUSD — Full Setup Documentation

```
Tanggal: [Tanggal analisis]
Pair: EURUSD
Sesi: London Kill Zone

=== ANALISIS TOP-DOWN ===

D1 (HTF Bias):
- Trend: Bullish (HH terbaru di 1.0950, HL di 1.0800)
- BOS: Bullish terkonfirmasi (close di atas 1.0900)
- Harga saat ini: Pullback ke area 1.0820
- Bias: BULLISH

H4 (Zona):
- CHOCH: Bullish sudah terjadi di H4
- OB Bullish H4: 1.0810 - 1.0830 (belum dimitigasi)
- FVG H4: 1.0815 - 1.0825 (overlap dengan OB)
- Target: Area 1.0810-1.0830

H1 (Refinement):
- Struktur H1: Bearish delivery (pullback ke OB H4)
- OB H1 bullish: 1.0815 - 1.0820
- Kill Zone: London (14:00-16:00 WIB)
- Wait for: SSL sweep di area 1.0808-1.0810

M15 (Entry):
- Harga masuk zona: 1.0812
- Sweep terjadi: Wick ke 1.0806 (trigger SSL)
- CISD candle: Close di 1.0822 (di atas swing high M15 lokal)
- Konfirmasi: Candle berikutnya bullish, hold di atas 1.0818

=== EKSEKUSI ===
Entry: 1.0823 (close CISD + 1 pip)
SL: 1.0804 (di bawah wick - 2 pip buffer) = 19 pip risk
TP1: 1.0862 (swing high H1) = 39 pip → RR 1:2.05
TP2: 1.0900 (BOS level H4) = 77 pip → RR 1:4.05
TP3: 1.0950 (HH D1 / BSL) = 127 pip → RR 1:6.68

Lot size: [lihat Modul 12]
Partial plan: Close 50% di TP1, move SL to BE, hold 50% ke TP2
```

---

## 11.12 Kesalahan Entry yang Umum

| Kesalahan | Dampak | Solusi |
|-----------|--------|--------|
| Entry terlalu dini (belum ada konfirmasi) | Sering kena SL | Tunggu candle konfirmasi |
| SL terlalu ketat | SL sering hit, frustrasi | SL di luar zona yang valid |
| Tidak ada TP yang jelas | Menutup terlalu cepat / terlalu lambat | Tetapkan TP sebelum entry |
| Entry counter HTF bias | Win rate rendah | Selalu cek HTF dulu |
| Pindah SL ke rugi lebih besar | Rugi besar | TIDAK PERNAH geser SL lebih jauh dari rencana |

---

## 11.13 Kesimpulan Modul 11

- Ada 4 model entry: OB, FVG, Sweep, CISD
- CISD entry = presisi tertinggi, RR terbaik
- SL harus di level yang "membuktikan setup salah"
- TP minimum 1:2, idealnya di zona likuiditas
- Partial TP + move to BE = cara profesional kelola trade

---

> **Latihan**: Cari 3 setup dari chart kemarin. Untuk setiap setup, tulis analisis lengkap: Bias HTF, Zona ITF, Entry LTF, SL, TP, RR ratio. Apakah semuanya memenuhi minimum 1:2 RR?

---

**[← Modul 10](./10-multi-timeframe.md)** | **[→ Modul 12: Risk Management](./12-risk-management.md)**
