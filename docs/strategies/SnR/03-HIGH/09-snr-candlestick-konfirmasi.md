# Modul 09 — SnR + Candlestick Konfirmasi

**Level:** 🔴 HIGH  
**Estimasi waktu baca:** 30–35 menit  
**Prasyarat:** Modul 01–08

---

## Tujuan Modul

Setelah membaca modul ini, kamu akan:
- Mengenal candle-candle yang mengkonfirmasi support bounce
- Mengenal candle yang mengkonfirmasi resistance rejection
- Bisa membedakan false breakout dari real breakout berdasarkan candle
- Mengkombinasikan sinyal candlestick dengan level SnR untuk entry berkualitas tinggi

---

## Prinsip Dasar: Level + Konfirmasi = Setup

Level SnR tanpa konfirmasi candle adalah **spekulasi**. Level SnR dengan konfirmasi candle adalah **setup trading yang tervalidasi**.

```
TANPA KONFIRMASI (berbahaya):

Harga
│
1.1000 ─── SUPPORT ─────────────────────────────────
│    │   ← Harga menyentuh support
│    │   ← Entry BUY langsung!
│    │   ← TANPA melihat apakah ada konfirmasi
│    ↓   ← Harga turun tembus support! LOSS!

DENGAN KONFIRMASI (lebih aman):

Harga
│
1.1000 ─── SUPPORT ─────────────────────────────────
│    │   ← Harga menyentuh support
│   ─┤─  ← Muncul Hammer: wick panjang, body kecil
│    │   ← Ini adalah sinyal bullish!
│    │   ← Entry BUY setelah close Hammer
│    │   ← Harga memantul ke atas → PROFIT!
│    ╰───────────────────────────────────
```

---

## 1. Candle Konfirmasi Support Bounce (Bullish)

### 1.1 Hammer

Candlestick dengan body kecil di atas dan wick panjang ke bawah. Menunjukkan bahwa seller mencoba mendorong harga lebih rendah tapi buyer mengambil alih.

```
HAMMER — Konfirmasi Support Bounce:

Struktur Hammer:          Contoh di Support:
                          
     ┌─┐ ← Body kecil   1.1000 ─── SUPPORT ──────────
     │ │                        │   ↓ Harga turun ke support
     │ │                        │
     └─┘                        │     ┌─┐ ← Hammer!
      │  ← Wick panjang         │     │ │   Body di atas
      │  (minimal 2x body)      │     │ │   
      │                         │     └─┘
                                │      │ ← Wick ke bawah
                                │      │   (buyer menolak harga rendah)

Syarat Hammer yang Valid:
✓ Body di upper half candle (close lebih tinggi dari open)
✓ Wick bawah minimal 2x panjang body
✓ Minimal atau tidak ada wick di atas
✓ Terjadi setelah downtrend atau di area support
✓ Body bisa bullish (putih/hijau) atau bearish (hitam/merah)
  → Bullish hammer lebih kuat

Setup:
Entry: Close candle setelah hammer (candle konfirmasi)
   atau close candle hammer itu sendiri
SL: Di bawah wick hammer (dengan 5-10 pip buffer)
TP: Resistance berikutnya
```

### 1.2 Bullish Engulfing

Dua candle: candle pertama bearish (merah), candle kedua bullish (hijau) yang bodynya "menelan" body candle pertama.

```
BULLISH ENGULFING di Support:

Struktur:               Di Support:

     ┌──┐               1.0800 ─── SUPPORT ──────────
     │  │ ← Candle 1          │
     │  │   (bearish)         │    ┌──┐ ← Candle bearish kecil
     └──┘                     │    │▓▓│
                               │    └──┘
  ┌────┐                       │  ┌────┐ ← Engulfing candle!
  │    │ ← Candle 2            │  │████│   Body besar bullish
  │    │   (bullish,           │  │████│   "menelan" candle sebelumnya
  │    │    body lebih         │  └────┘
  └────┘    besar)             │
                               │  ╰────────────────────────────
                                      ↑ Harga rally setelah engulfing

Syarat Bullish Engulfing yang Valid:
✓ Candle ke-2 (bullish) membuka di bawah atau sama dengan close candle ke-1
✓ Candle ke-2 menutup di atas atau sama dengan open candle ke-1
✓ Body candle ke-2 lebih besar dari body candle ke-1
✓ Terjadi di area support yang valid
✓ Volume candle ke-2 lebih tinggi (konfirmasi lebih kuat)
```

### 1.3 Bullish Pinbar (Variasi Hammer)

Mirip hammer tapi lebih ekstrem: body sangat kecil, wick bawah sangat panjang.

```
BULLISH PINBAR:

     • ← Open dan close sangat berdekatan (body sangat kecil)
      │
      │
      │  ← Wick bawah sangat panjang (3x+ body)
      │
      │

Contoh di Support Zone:

1.0820 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ← Batas bawah zone
     •    ← Pinbar! Wick turun ke 1.0810
      │
      │   ← Wick sangat panjang
1.0840 ════════════════════════════════════════  ← Level utama zone
      │
1.0860 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ← Batas atas zone

Interpretasi:
- Harga sempat turun ke 1.0810 (memasuki deep zone)
- Tapi langsung ditolak naik → close kembali di sekitar 1.0835
- Wick panjang menunjukkan tekanan buyer sangat kuat di area itu

Setup:
Entry: 1.0845 (sedikit di atas high pinbar)
SL: 1.0805 (di bawah wick pinbar)
TP: Resistance terdekat
```

---

## 2. Candle Konfirmasi Resistance Rejection (Bearish)

### 2.1 Shooting Star

Kebalikan dari hammer. Body kecil di bawah, wick panjang ke atas. Menunjukkan bahwa buyer mencoba mendorong harga lebih tinggi tapi seller mengambil alih.

```
SHOOTING STAR — Konfirmasi Resistance Rejection:

Struktur Shooting Star:       Contoh di Resistance:

      │  ← Wick panjang ke    1.1200 ─── RESISTANCE ──────────
      │     atas                      │
     ┌─┐ ← Body kecil                 │      │ ← Shooting Star!
     │ │                              │      │   Wick panjang ke atas
     │ │                              │      │   
     └─┘                              │      │
                                      │     ┌─┐
                                      │     │ │ ← Body kecil di bawah
                                      │     └─┘
                                      │   ╮    ← Harga turun setelah
                                      │   │      shooting star
                                      │   ╰─────────────────────────

Syarat Shooting Star yang Valid:
✓ Body di lower half candle
✓ Wick atas minimal 2x panjang body
✓ Minimal atau tidak ada wick di bawah
✓ Terjadi setelah uptrend atau di area resistance
✓ Lebih kuat jika body bearish (merah/hitam) = Bearish Shooting Star
```

### 2.2 Bearish Engulfing

Kebalikan bullish engulfing. Candle bearish besar "menelan" candle bullish sebelumnya.

```
BEARISH ENGULFING di Resistance:

1.1200 ─── RESISTANCE ──────────
│
│    ┌──┐ ← Candle bullish kecil (uptrend sebelumnya)
│    │██│
│    └──┘
│  ┌────┐ ← Bearish Engulfing!
│  │▓▓▓▓│   Body besar bearish menelan candle sebelumnya
│  │▓▓▓▓│   → Pergeseran kontrol ke seller
│  └────┘
│    ↓
│  ╭─────────── Harga turun signifikan setelah engulfing
│  │
│  ╰─────────────────────────────────────────────────────
│
Setup:
Entry: Close candle bearish engulfing
SL: Di atas high candle engulfing + buffer
TP: Support berikutnya
```

### 2.3 Evening Star (3-Candle Pattern)

Pattern 3 candle yang menandakan reversal dari uptrend ke downtrend.

```
EVENING STAR:

Struktur:                    Di Resistance:

Candle 1: Bullish besar      1.1200 ── RESISTANCE ─────────
   ┌──┐                              │   ┌──┐ ← Candle 1 (bullish besar)
   │██│                              │   │██│
   └──┘                              │   └──┘
                                     │     • ← Candle 2: Doji/kecil
Candle 2: Doji/bintang kecil        │   (hesitation — seller masuk)
     •                               │   ┌──┐ ← Candle 3 (bearish besar)
                                     │   │▓▓│   Close menembus ke bawah
Candle 3: Bearish besar             │   │▓▓│   midpoint candle 1
   ┌──┐                             │   └──┘
   │▓▓│                             │     ↓ Harga lanjut turun
   └──┘

Syarat Evening Star:
✓ Candle 1: Bullish besar
✓ Candle 2: Body kecil (gap di atas candle 1 → lebih kuat)
✓ Candle 3: Bearish, close masuk ke dalam body candle 1
✓ Terjadi di resistance yang valid
```

---

## 3. Candle Konfirmasi Breakout Valid

### 3.1 Candle Breakout yang Valid

```
CANDLE BREAKOUT BULLISH YANG VALID:

1.1200 ─── RESISTANCE (LAMA) ─────────────────────
      │   ┌──────┐ ← Candle breakout:
      │   │██████│   - Body BESAR (>50% high-low range)
      │   │██████│   - Close JAUH di atas resistance
      │   │██████│   - Minimal wick di atas (buyer kuat)
      │   └──────┘   - Volume sangat tinggi
      │               (misalnya 2x rata-rata)
      │           ← Harga terus naik setelah breakout
      │
      │   BREAKOUT VALID!
      │   → Siap untuk entry breakout atau tunggu retest

CANDLE BREAKOUT YANG TIDAK VALID (fakeout):

1.1200 ─── RESISTANCE ────────────────────────────
      │      │
      │     ─┤─  ← Wick panjang di atas resistance
      │      │     tapi body kecil, close di dekat resistance
      │      │     → INI BUKAN BREAKOUT, ini pin bar rejection!
      │      │
      │   ╭──╯ ← Harga langsung berbalik
      │   │
      │   ╰──────────────────────────────────────── (turun)
```

### 3.2 Membedakan Real Breakout vs False Breakout (Fakeout)

```
PERBANDINGAN VISUAL:

REAL BREAKOUT:                    FALSE BREAKOUT (FAKEOUT):
─────────────────────────         ─────────────────────────────
      ┌──────────────             1.1200 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
      │  ← Body besar                      │ ← Wick panjang
      │     naik kuat                     ─┤─   menembus
1.1200│     Close tinggi                   │   
──────┤     Volume tinggi         1.1200 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
      │                                    │ ← Body kecil
      │                                   ─┘   close dekat level
      │                           ╭──────────────────────────
                                   ↑ Harga berbalik = FAKEOUT

Ciri Real Breakout vs Fakeout:

Aspek              Real Breakout        Fakeout
─────────────────  ─────────────────    ─────────────────────
Body candle        Besar                Kecil/wick
Volume             Spike tinggi         Normal atau rendah
Close candle       Jauh dari level      Dekat dengan level
Follow-through     Ya (2-3 candle       Tidak (langsung
                    berikutnya searah)   berbalik)
Konteks            Setelah konsolidasi  Tanpa momentum
                   panjang              
Timing             Sesi aktif           Sesi tipis (Asia)
```

---

## 4. Kombinasi: SnR Level + Candle Konfirmasi

### Skenario 1: Support + Hammer

```
Studi Kasus: EURUSD H1 — Support Bounce + Hammer
═══════════════════════════════════════════════════

Setup:
- Level: Support H4 di 1.0850 (3x sentuhan sebelumnya)
- Timeframe konfirmasi: H1
- Konfirmasi candle: Hammer

Chart H1:

1.0920 ─── TP1 ─────────────────────────────────────
│
│
│     ╭──────────────────────────── Rally setelah bounce
│     │
│     │
│     │ ← Close candle konfirmasi (entry H1)
│     │
1.0860─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ← Batas atas zone
│          │   ← Hammer muncul di sini
│          │     Body di 1.0855-1.0865
│     ───── ←   Wick turun ke 1.0835
│
1.0840 ════════════════════════════════════════════  ← Level utama support
│
1.0820 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ← Batas bawah zone
│
1.0790 ─── SL ──────────────────────────────────────

Parameter:
├── Level: Support zone 1.0820-1.0860
├── Candle: Hammer di 1.0855 (body), wick ke 1.0835
├── Entry: 1.0870 (close candle setelah hammer)
├── SL: 1.0815 (di bawah batas bawah zone + buffer)
├── TP1: 1.0920 (minor resistance H1)
├── TP2: 1.0980 (resistance mayor H4)
├── Risk: 55 pip
└── RR TP1: 1:0.9 (partial), TP2: 1:2 (total)
```

### Skenario 2: Resistance + Shooting Star

```
Studi Kasus: XAUUSD H4 — Resistance Rejection + Shooting Star
════════════════════════════════════════════════════════════════

Setup:
- Level: Resistance H4 di 2080 (4x sentuhan sebelumnya)
- Konfirmasi: Shooting Star

Chart H4:

Harga
│
2100 ─── SL ────────────────────────────────────────
│             ↑
│            ─┤─ ← Shooting Star!
│             │   Wick panjang ke atas 2098
│             │   Body kecil di 2077-2080
│            ─┘
│
2080 ─── RESISTANCE ────────────────────────────────
│    ↓ Rejection ke-4
│
│    ╭────── Harga jatuh setelah shooting star
│    │
│    │
2050 ─── TP1 ───────────────────────────────────────
│    │
│    │
2020 ─── TP2 ───────────────────────────────────────
│

Parameter:
├── Level: Resistance 2080 (konfluensi: 4 sentuhan + round-ish number)
├── Candle: Shooting Star (wick ke 2098, body 2076-2080)
├── Entry: SELL 2075 (close shooting star)
├── SL: 2105 (di atas wick + buffer 7)
├── TP1: 2050 (minor support) → Reward: 25 pip
├── TP2: 2020 (support mayor) → Reward: 55 pip
├── Risk: 30 pip
└── RR TP2: 1:1.8 (partial close di TP1, trail ke TP2)
```

### Skenario 3: SR Flip + Bearish Engulfing

```
Studi Kasus: GBPUSD D1 — SR Flip Retest + Bearish Engulfing
══════════════════════════════════════════════════════════════

Konteks:
- Support kuat di 1.2600 (3 bulan bertahan)
- Breakout bearish terjadi 2 minggu lalu
- Harga rally kembali ke 1.2600 (retest SR Flip)

Chart D1:

Harga
│
│    ╭──────────────────── (rally retest)
│    │
│    │
│    │
1.2600 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ← SR FLIP ZONE
│    │   ← Harga memasuki zona retest
│    │   ← Muncul Bearish Engulfing:
│   ┌┴┐    - Candle H1 ke-1: Bullish kecil (naik ke 1.2605)
│   │▓│    - Candle H1 ke-2: Bearish besar (menelan candle 1)
│   │▓│    → Konfirmasi rejection dari SR Flip zone!
│   └┬┘
│    ↓   ← Entry SELL!
│
│    ╰──────────────────────────────────── (lanjut turun)
│
1.2400 ─── TP ──────────────────────────────────

Parameter:
├── Level: SR Flip zone 1.2580-1.2620
├── Candle: Bearish Engulfing di 1.2605
├── Entry: SELL 1.2595 (close bearish engulfing)
├── SL: 1.2640 (di atas SR flip zone)
├── TP: 1.2400 (support berikutnya)
├── Risk: 45 pip
└── RR: 1:4.3 — Excellent!
```

---

## 5. False Breakout — Candle Memberikan Clue

False breakout (fakeout) sering kali bisa diidentifikasi lebih awal dengan membaca candle dengan benar.

```
FAKEOUT DI RESISTANCE — Contoh Lengkap:

Harga
│
│         │ ← CANDLE ini terlihat seperti "breakout"
│        ─┤─ ← Tapi perhatikan:
│         │   - Wick panjang DI ATAS level
│         │   - Body candle KECIL
│         │   - Close dekat atau DI BAWAH resistance
│   ┌──┐  │   → Ini adalah SHOOTING STAR, bukan breakout!
│   │  │  │
│   │  └──┘ ← Body close di bawah resistance
1.1200 ══════════════════════════════════════════  ← RESISTANCE
│   │   ← Harga tidak pernah benar-benar naik di atas level
│   │
│   ╰────────────────────────────────────────────
│        ↑ Harga langsung turun = FAKEOUT (false breakout)

Lesson:
- Wick yang mencuat di atas resistance BUKAN breakout
- Breakout yang valid: body candle close DI ATAS resistance
- Bukan wick yang tembus, tapi BODY yang tembus
```

---

## 6. Quick Reference: Candle Konfirmasi

| Candle | Muncul di | Signal | Kekuatan |
|--------|-----------|--------|----------|
| Hammer | Support | Bullish bounce | ★★★★ |
| Bullish Pinbar | Support | Bullish bounce (kuat) | ★★★★★ |
| Bullish Engulfing | Support | Bullish reversal | ★★★★ |
| Morning Star | Support | Bullish reversal | ★★★★★ |
| Shooting Star | Resistance | Bearish rejection | ★★★★ |
| Bearish Pinbar | Resistance | Bearish rejection (kuat) | ★★★★★ |
| Bearish Engulfing | Resistance | Bearish reversal | ★★★★ |
| Evening Star | Resistance | Bearish reversal | ★★★★★ |
| Marubozu Bullish | Breakout up | Valid breakout bullish | ★★★★ |
| Marubozu Bearish | Breakout down | Valid breakout bearish | ★★★★ |

---

## 7. Checklist Konfirmasi Candle

**Untuk Bounce Entry:**
- [ ] Apakah ada candle reversal yang jelas di level? (Hammer/Engulfing/Pinbar)
- [ ] Apakah wick candle tersebut menunjukkan penolakan yang kuat?
- [ ] Apakah body candle di sisi yang "benar" (untuk hammer: body di atas)?
- [ ] Apakah candle berikutnya mengkonfirmasi (follow-through)?
- [ ] Apakah volume lebih tinggi saat candle konfirmasi?

**Untuk Breakout Entry:**
- [ ] Apakah body candle breakout besar (bukan wick)?
- [ ] Apakah close candle jauh dari level yang ditembus?
- [ ] Apakah ada volume spike?
- [ ] Apakah 2-3 candle berikutnya melanjutkan arah breakout?

---

## 8. Latihan Praktis

### Latihan 1: Identifikasi 10 Candle
Buka chart XAUUSD H4 (2 bulan ke belakang). Identifikasi:
- 5 candle yang mengkonfirmasi bounce dari support/resistance
- 5 candle yang mengkonfirmasi breakout valid

### Latihan 2: Bandingkan Real vs False Breakout
Temukan 3 contoh real breakout dan 3 contoh false breakout. Untuk masing-masing, jelaskan ciri candle yang membedakannya.

### Latihan 3: Complete Setup Journal
Untuk minggu ini, setiap kali kamu melihat candle konfirmasi di level SnR yang valid, catat:
- Level SnR yang diidentifikasi
- Candle konfirmasi yang muncul
- Entry, SL, TP yang kamu rencanakan
- Hasil aktual

---

## Ringkasan

| Situasi | Candle yang Dicari | Tindakan |
|---------|-------------------|----------|
| Support bounce | Hammer, Bullish Pinbar, Bullish Engulfing | BUY setelah konfirmasi |
| Resistance rejection | Shooting Star, Bearish Pinbar, Bearish Engulfing | SELL setelah konfirmasi |
| Breakout bullish | Marubozu / body besar + volume | BUY atau tunggu retest |
| Breakout bearish | Marubozu / body besar + volume | SELL atau tunggu retest |
| False breakout | Wick tembus tapi body tidak | Ignore, bahkan ambil posisi berlawanan |

---

**Modul Sebelumnya:** [08 — Entry Model SnR](./08-entry-model-snr.md)  
**Modul Berikutnya:** [10 — Full Strategy SnR](../04-MASTER/10-full-strategy-snr.md)
