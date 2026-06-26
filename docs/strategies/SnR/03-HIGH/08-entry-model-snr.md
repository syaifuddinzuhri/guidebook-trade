# Modul 08 — Entry Model SnR: Bounce, Breakout, dan Retest

**Level:** 🔴 HIGH  
**Estimasi waktu baca:** 35–40 menit  
**Prasyarat:** Modul 01–07

---

## Tujuan Modul

Setelah membaca modul ini, kamu akan:
- Menguasai 3 model entry utama dalam SnR trading
- Tahu kapan menggunakan model mana
- Bisa menentukan SL dan TP yang optimal untuk setiap model
- Memahami risk/reward yang realistis untuk setiap model

---

## Overview: 3 Model Entry SnR

| Model | Kapan Entry | Risiko | Reward Potensial | Kesulitan |
|-------|------------|--------|-----------------|-----------|
| Bounce | Saat harga menyentuh level | Sedang | Sedang | Mudah |
| Breakout | Saat harga menembus level | Tinggi | Tinggi | Menengah |
| Retest | Setelah breakout + pullback | Rendah | Tinggi | Menengah |

---

## Model 1: Bounce Entry

### Konsep

Entry **langsung saat harga menyentuh level SnR** dengan konfirmasi candle. Tidak menunggu breakout atau retest.

```
BOUNCE ENTRY — Support:

Harga
│
│         ╭──────────────────────── ← Target TP (resistance berikutnya)
│    ╭────╯
│    │   ↑ Bounce dari support
│    │
1.0800 ═══════════════════════════  ← SUPPORT
│    │
│    │   ↓ Harga turun ke support
│   ─┤─  ← Hammer candle terbentuk (konfirmasi)
│    │
│   ─┘
│
Entry: Close hammer candle
SL: Di bawah wick hammer (dengan buffer)
TP: Resistance berikutnya
```

### Kapan Menggunakan Bounce Entry

- Market sideways / ranging (tidak ada trend jelas)
- Level SnR sudah teruji 3+ kali sebelumnya
- Ada konfirmasi candle yang kuat di level
- Level memiliki konfluensi (round number, Fibonacci, dll)

### Detail Setup Bullish Bounce

```
SETUP LENGKAP: EURUSD H4 — Support Bounce

Harga
│
1.1100 ─── TP Area ─────────────────────────────  ← Resistance berikutnya
│
│    ╭──────────────────── (setelah bounce, harga rally)
│    │
│    │                     → Entry di sini saat hammer close
│
1.0850 ─────────────────────────────────────────  ← Batas atas support zone
│              │   ← Hammer candle
│              │   ← Body kecil, wick panjang ke bawah
│    ─ ─ ─ ─ ─┼─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
│              │   ← Wick turun ke 1.0820
1.0820 ─────────────────────────────────────────  ← Batas bawah support zone
│              │
│          ╭──╯
│     ╭────╯
│     │   ← Harga turun ke support
│     │

Setup Parameter:
├── Pair: EURUSD
├── Timeframe: H4
├── Setup: Bullish Bounce dari Support Zone 1.0820-1.0850
├── Entry: 1.0855 (close hammer candle, setelah harga kembali ke atas batas zone)
├── SL: 1.0810 (di bawah wick + buffer 10 pip)
├── TP1: 1.0980 (minor resistance H4)
├── TP2: 1.1100 (resistance utama)
├── Risk: 45 pip (1.0855 - 1.0810)
├── TP1 Reward: 125 pip → RR 1:2.8
└── TP2 Reward: 245 pip → RR 1:5.4
```

### Detail Setup Bearish Bounce

```
SETUP LENGKAP: XAUUSD H1 — Resistance Bounce (Rejection)

Harga
│
2080 ─────────────────────────────────────────  ← Batas atas resistance zone
│              │
│             ─┤─  ← Shooting Star candle
│              │     ← Wick panjang ke atas (mencoba tembus tapi gagal)
│              │     ← Body kecil di bawah batas zone
2060 ─────────────────────────────────────────  ← Batas bawah resistance zone
│   SL di atas 2085 (above zone top + buffer)
│
│    Entry: SELL saat close Shooting Star
│
│    ↓ Setelah rejection
│    ╰──────────────────────────────────────── → Harga turun
│
2020 ─────────────────────────────────────────  ← TP1 (support terdekat)
│
2000 ─────────────────────────────────────────  ← TP2 (round number / support kuat)

Setup Parameter:
├── Pair: XAUUSD
├── Timeframe: H1
├── Setup: Bearish Rejection dari Resistance Zone 2060-2080
├── Entry: 2058 (close shooting star)
├── SL: 2088 (di atas batas zone + buffer 8)
├── TP1: 2020 (minor support)
├── TP2: 2000 (round number support kuat)
├── Risk: 30 pip
├── TP1 Reward: 38 pip → RR 1:1.3 (minimal, ambil partial di TP1)
└── TP2 Reward: 58 pip → RR 1:1.9 (lebih baik)
```

### Kelemahan Bounce Entry

- Tingkat false signal lebih tinggi (belum ada konfirmasi "harga diterima" atau "harga ditolak")
- Bisa entry terlalu dini sebelum harga benar-benar bouncing
- Risiko: harga menyentuh level → bounce tipis → lanjut tembus

---

## Model 2: Breakout Entry

### Konsep

Entry **segera setelah harga menembus level SnR** yang signifikan. Bertaruh bahwa harga akan terus bergerak ke arah breakout.

```
BREAKOUT ENTRY — Bullish Breakout:

Harga
│
│                              ╭── (lanjut naik = harapan)
│                         ╭────╯
│                    ╭────╯
│                    │ ← ENTRY di sini (candle close di atas resistance)
│
1.1200 ─────────────╪──────────────────────────  ← RESISTANCE (ditembus)
│         ↓         │ ← Breakout candle besar
│        ─┼─        │   (body besar, close jauh di atas level)
│         │         │
│    ╭────╯         │
│    │               │
│    ╰───────────────╯

Entry: Close candle breakout (atau sedikit di atas)
SL: Di bawah level yang baru ditembus (1.1180 misalnya)
TP: Level resistance berikutnya atau measured move
```

### Kapan Menggunakan Breakout Entry

- Volume spike jelas saat breakout
- Candle breakout memiliki body besar (bukan doji atau candle kecil)
- Ada katalis fundamental (news, event penting)
- Level yang ditembus sudah lama bertahan (semakin lama = lebih signifikan)

### Detail Setup Bullish Breakout

```
SETUP LENGKAP: GBPUSD D1 — Resistance Breakout

Kondisi sebelum breakout:
│
│    3 bulan lalu: Resistance di 1.2800 terbentuk
│    2 bulan lalu: 2x rejection di 1.2800
│    1 bulan lalu: 1x lebih rejection → level makin kuat
│
│    Kemudian:
│

Harga
│                         ┌─────────────────────
│                    ┌────┘ ← Close D1 candle besar
│                    │      ← Body 150 pip ke atas
│                    │      ← Volume 3x dari rata-rata
1.2800 ══════════════╪══════════════════════════════
│         ↓    ↓    ↓│
│        ─┴─  ─┴─  ─┴┘  ← 3 rejection sebelumnya
│
│ BREAKOUT TERJADI!
│
│ Setup:
│ ├── Entry: 1.2850 (sedikit di atas level, menghindari false breakout)
│ ├── SL: 1.2760 (di bawah 1.2800 + buffer 40 pip)
│ ├── TP1: 1.3000 (round number resistance)
│ ├── TP2: 1.3200 (resistance mayor berikutnya)
│ ├── Risk: 90 pip
│ ├── TP1 Reward: 150 pip → RR 1:1.7
│ └── TP2 Reward: 350 pip → RR 1:3.9
│
│   Catatan: Breakout entry memiliki risiko FOMO (entry terlambat)
│   dan risiko false breakout (retest gagal → harga kembali)
```

### Risiko Breakout Entry

```
BAHAYA BREAKOUT ENTRY — False Breakout (Fakeout):

Harga
│
│              ← Entry breakout di sini!
1.2800 ─ ─ ─ ─╪─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
│              │ ← Harga naik sedikit
│              ╰──────────────────────────────── ← FAKEOUT!
│                   Harga langsung berbalik!
│
│   Trader breakout:
│   - Entry di 1.2850
│   - SL di 1.2760
│   - Harga berbalik ke 1.2750 → SL HIT → LOSS

Cara mengurangi risiko false breakout:
1. Tunggu candle full close (bukan intracandle)
2. Cek volume: harus spike signifikan
3. Masang entry sedikit di atas level (bukan persis di level)
4. Jangan entry saat news volatility tinggi (dapat fake spike)
```

---

## Model 3: Retest Entry (Yang Paling Disukai)

### Konsep

Entry **setelah breakout terjadi + harga pullback kembali ke level yang baru ditembus** (SR Flip). Ini adalah kombinasi dari Modul 06 (Role Reversal) dan entry timing.

```
RETEST ENTRY — Bullish (Resistance jadi Support):

Harga
│
│   ╭──────────────────────── ← Lanjut naik (harapan setelah retest)
│   │
│   │
│   │  ← ENTRY BUY di sini (konfirmasi hammer/engulfing)
│   ↑  ← Retest ke level lama (kini jadi support)
│   │
1.2800 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ← SR FLIP (dulu resistance)
│
│   ← Breakout terjadi sebelumnya
│   ← Harga rally dari 1.2800 ke 1.3050
│   ← Kemudian pullback ke 1.2800 (retest)
│

SL di bawah 1.2760 (di bawah zona SR flip)
TP di resistance berikutnya
```

### Mengapa Retest Entry adalah Model Terbaik?

```
PERBANDINGAN 3 MODEL dari sisi Risk/Reward:

Situasi: Breakout bullish dari resistance 1.2800

                BOUNCE          BREAKOUT        RETEST
                ─────────────   ─────────────   ─────────────
Entry           1.2780          1.2850          1.2810
(saat bounce)   (di support)    (setelah        (setelah
                                 breakout)        pullback)

SL              1.2740          1.2760          1.2760
                (40 pip SL)     (90 pip SL)     (50 pip SL)

TP (1.3000)     220 pip         150 pip         190 pip

RR              1:5.5           1:1.7           1:3.8

Probabilitas    Sedang          Sedang-Rendah   Tinggi
(karena belum   (karena belum   (karena false   (karena breakout
ada breakout    ada konfirmasi  breakout        sudah dikonfirmasi
konfirmasi)     breakout)       mungkin)        dan retest kuat)

KESIMPULAN:
- Bounce: RR tertinggi tapi probabilitas paling rendah
- Breakout: RR terendah, probabilitas sedang-rendah
- Retest: RR bagus, probabilitas tertinggi → PEMENANG!
```

### Detail Setup Retest Bearish

```
SETUP LENGKAP: XAUUSD H4 — SSL Sweep ke Bearish SR Flip

Konteks:
- Support kuat di 2050 (3 sentuhan, 2 bulan bertahan)
- Harga akhirnya ditembus ke bawah dengan candle besar
- Harga turun ke 1980, lalu bounce kembali ke atas

Harga
│
│   (harga rally dari 1980)
│                  ╭──── (mencapai zona retest)
│             ╭────╯
│        ╭────╯
│        │
2050 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ← SR FLIP ZONE
│        │   ← Harga masuk zona
│        │   ← Shooting Star muncul
│        │   ← Entry SELL di sini
│        │
│       ─┘  ← SL di atas 2070 (di atas zona + buffer 20)
│
│        ↓  ← Harga lanjut turun setelah retest
│
│
2010 ─────────────────────────────────────────  ← TP1 (minor support H4)
│
1980 ─────────────────────────────────────────  ← TP2 (previous low)

Setup Parameter:
├── Pair: XAUUSD
├── Timeframe: H4
├── Setup: Bearish Retest (SR Flip) setelah Support Breakdown
├── Breakout: Candle besar break di bawah 2050 (2 minggu lalu)
├── Retest: Harga kembali ke 2040-2060 zona SR flip
├── Konfirmasi: Shooting Star di 2048
├── Entry: SELL 2044 (close shooting star)
├── SL: 2070 (di atas zona + buffer)
├── TP1: 2010 (34 pip reward) → RR 1:1.3 (partial close)
├── TP2: 1980 (64 pip reward) → RR 1:2.5
└── Risk: 26 pip
```

---

## Studi Kasus Lengkap: Semua 3 Model dalam 1 Sesi

```
STUDI KASUS: EURUSD D1 — 3 Setup dalam 1 Chart
════════════════════════════════════════════════

Level Kunci: 1.1000 (support), 1.1200 (resistance)
Periode: 3 bulan (ilustrasi)

BULAN 1: BOUNCE SETUP
══════════════════════

Harga
│
1.1200 ─── Resistance ───────────────────────────
│
│         ╭───────────────────────── ← Target TP
│    ╭────╯
│    │ ↑ Hammer bounce dari support
│    │
1.1000 ═══════════════════════════════════════  ← Support (2 sentuhan sebelumnya)
│         ← BOUNCE ENTRY SETUP
│    Entry: 1.1015 (close hammer)
│    SL: 1.0975 (di bawah wick)
│    TP: 1.1200
│    RR: 1:4.6 ← PROFIT

BULAN 2: BREAKOUT SETUP
═══════════════════════

Harga
│
│                              ╭──────────────────── (rally berlanjut)
│                         ╭────╯
│                    ╭────╯ ← BREAKOUT terjadi dengan candle besar
│
1.1200 ═══════════════════════════════════════  ← Resistance (ditembus)
│
│         (harga mengumpul energy di bawah 1.1200 selama 2 minggu)
│
│         ← BREAKOUT ENTRY SETUP
│    Entry: 1.1230 (sedikit di atas level)
│    SL: 1.1160 (di bawah 1.1200 + buffer)
│    TP: 1.1500 (resistance berikutnya)
│    RR: 1:3.7 ← (jika tidak false breakout)

BULAN 3: RETEST SETUP
═════════════════════

Harga
│
│                                       (rally berlanjut dari retest)
│                                   ╭───────────────────────────────
│                              ╭────╯
│                         ╭────╯ ← Retest ke 1.1200
│                         │
│                    ╭────╯ ← Pullback dari 1.1380 ke 1.1200
│               ╭────╯
│          ╭────╯ ← Rally setelah breakout
│     ╭────╯
│     │
1.1200 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ← SR FLIP ZONE
│                         │   ← Retest ke zona
│                         │   ← Hammer muncul
│                         │   ← ENTRY BUY
│                        ─┘  ← SL di bawah 1.1170
│
│         ← RETEST ENTRY SETUP
│    Entry: 1.1210 (close hammer)
│    SL: 1.1170 (di bawah zona)
│    TP1: 1.1380 (swing high sebelumnya)
│    TP2: 1.1500 (resistance mayor)
│    RR TP1: 1:4.25 ← PROFIT BESAR
│    RR TP2: 1:7.25 ← EXCELLENT

SUMMARY 3 TRADE:
Trade 1 (Bounce): Profit 1:4.6
Trade 2 (Breakout): Profit 1:3.7
Trade 3 (Retest): Profit 1:4.25 - 1:7.25

Semua 3 model berhasil karena level yang dipilih valid dan ada konfirmasi candle
```

---

## Checklist Entry — 3 Model

### Checklist Bounce Entry

- [ ] Level memiliki minimal 3 sentuhan sebelumnya
- [ ] Ada konfluensi (Fibonacci, round number, atau multi-TF)
- [ ] Ada konfirmasi candle yang kuat (hammer, engulfing)
- [ ] Volume saat bounce tidak abnormal rendah
- [ ] Tidak ada level SnR lain yang menghalangi dalam 50 pip pertama
- [ ] RR minimal 1:2

### Checklist Breakout Entry

- [ ] Candle breakout memiliki body besar (>50% range candle = body)
- [ ] Volume spike jelas (minimal 1.5x rata-rata)
- [ ] Level yang ditembus sudah bertahan minimal 2-3 sentuhan
- [ ] Tidak ada news besar dalam 1 jam ke depan (menghindari reversal)
- [ ] SL ditempatkan di sisi yang benar dari level yang ditembus
- [ ] RR minimal 1:1.5

### Checklist Retest Entry

- [ ] Breakout sebelumnya jelas dan valid (candle besar + volume)
- [ ] Harga sudah bergerak signifikan setelah breakout (minimal 50% dari range)
- [ ] Retest kembali ke zona SR flip (bukan terlalu jauh melampaui)
- [ ] Volume saat retest lebih rendah dari saat breakout (pullback lemah)
- [ ] Ada konfirmasi candle di zona SR flip
- [ ] SL ditempatkan di sisi salah dari zona SR flip
- [ ] RR minimal 1:2

---

## Latihan Praktis

### Latihan 1: Identifikasi 3 Model
Buka XAUUSD H4 chart (3 bulan ke belakang). Temukan:
- 2 contoh Bounce Entry yang valid
- 2 contoh Breakout Entry yang valid
- 2 contoh Retest Entry yang valid

### Latihan 2: Hitung RR Semua Setup
Untuk setiap setup yang kamu temukan, hitung RR aktual (bukan target). Apakah sesuai ekspektasi?

### Latihan 3: Paper Trade 2 Minggu
Selama 2 minggu, simulasikan trading menggunakan salah satu model (rekomendasi: Retest Entry). Catat setiap trade, hasil, dan pelajaran.

---

## Ringkasan

| Model | Entry Timing | SL | TP | Kelebihan | Kekurangan |
|-------|-------------|----|----|-----------|------------|
| Bounce | Di level SnR | Di bawah/atas level | Level berikutnya | RR tinggi | Probabilitas lebih rendah |
| Breakout | Saat close candle menembus | Di balik level | Measured move | Catch big move | False breakout |
| Retest | Setelah pullback ke SR flip | Di balik zona flip | Level berikutnya | Probabilitas tertinggi | Sering miss entry |

---

**Modul Sebelumnya:** [07 — SnR Multi-Timeframe](./07-snr-multi-timeframe.md)  
**Modul Berikutnya:** [09 — SnR + Candlestick Konfirmasi](./09-snr-candlestick-konfirmasi.md)
