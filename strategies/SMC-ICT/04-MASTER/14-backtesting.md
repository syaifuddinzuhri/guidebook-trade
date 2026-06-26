# Modul 14 — Backtesting

> **Level**: 🏆 MASTER | **Estimasi belajar**: Ongoing (100+ setup)

---

## 14.1 Mengapa Backtesting Wajib?

Backtesting adalah **bukti bahwa strategi kamu bekerja** — bukan berdasarkan perasaan atau harapan, tapi data nyata.

```
Tanpa backtesting:
→ Kamu tidak tahu win rate sebenarnya
→ Kamu tidak tahu apakah RR target realistis
→ Kamu tidak punya kepercayaan diri saat trade (bisa panic)

Dengan backtesting 100+ setup:
→ Kamu tahu "secara statistik, 45% setup saya menang"
→ Kamu tahu "rata-rata RR saya 1:2.3"
→ Kamu percaya pada proses — 1 loss tidak mengguncang kamu
```

---

## 14.2 Jenis Backtesting

### Manual Backtesting
- Scroll chart ke belakang, identifikasi setup secara manual
- Catat entry, SL, TP, dan hasilnya
- **Pro**: Belajar membaca chart lebih baik
- **Kon**: Membutuhkan waktu banyak

### Semi-Automated (Replay Mode)
- Gunakan fitur Bar Replay di TradingView
- Chart bergerak candle per candle seperti real-time
- **Pro**: Lebih realistis, tidak bisa "cheat" lihat masa depan
- **Kon**: Butuh TradingView Premium (atau gratis terbatas)

### Automated
- Menggunakan software (Forex Tester, Strategy Tester MT4/MT5)
- **Pro**: Cepat, data banyak
- **Kon**: Tidak melatih mata untuk membaca chart manual

**Rekomendasi**: Mulai dengan manual/replay mode.

---

## 14.3 Cara Backtesting yang Benar

### Langkah 1: Persiapan
```
1. Pilih pair: XAUUSD atau EURUSD (likuiditas tinggi)
2. Pilih timeframe: Mulai dari H1 (ITF)
3. Tentukan periode: Minimal 3-6 bulan
4. Buka spreadsheet untuk catat hasil
5. Buka TradingView → Bar Replay (atau scroll ke belakang)
```

### Langkah 2: Identifikasi Setup
```
Untuk setiap titik di chart:
1. Tutup chart di masa depan (scroll atau replay)
2. Lakukan analisis top-down (D1 → H4 → H1 → M15)
3. Identifikasi apakah ada setup valid
4. Jika ya: catat entry, SL, TP sebelum "melihat hasilnya"
5. Baru buka/scroll ke depan untuk lihat hasil
```

**PENTING**: Jangan "curang" dengan melihat masa depan sebelum analisis selesai. Ini akan memberikan hasil yang terdistorsi.

### Langkah 3: Catat Hasil
```
Untuk setiap setup:
- Tanggal/waktu setup
- Pair & Timeframe
- Jenis setup (Playbook A/B/C/D)
- Entry, SL, TP (dalam pip)
- RR ratio
- Hasil: Win (berapa R?) / Loss (1R) / Breakeven
- Screenshot: sebelum entry, saat entry, saat close
- Notes: Apa yang bagus, apa yang bisa diperbaiki?
```

---

## 14.4 Template Backtesting Spreadsheet

```
Kolom yang diperlukan:
| # | Tanggal | Pair | TF | Setup | Entry | SL (pip) | TP (pip) | RR | Hasil | R | Notes |
|---|---------|------|----|-------|-------|----------|----------|-----|-------|---|-------|
| 1 | 2024-01 | XAUUSD | H1 | OB+CISD | 2020 | 15 | 45 | 1:3 | Win | +3R | Strong OB H4 |
| 2 | 2024-01 | EURUSD | H1 | FVG | 1.0820 | 12 | 24 | 1:2 | Loss | -1R | Bias salah |
```

### Summary Tab:
```
Total setup:
Total Win:
Total Loss:
Total Breakeven:
Win Rate: Win/Total
Average RR:
Total R:
Max Consecutive Loss:
Max Consecutive Win:
Best month:
Worst month:
```

---

## 14.5 Minimal Sample Size

```
Fase 1: 50 setup → Data awal, mulai lihat pola
Fase 2: 100 setup → Cukup untuk analisis statistik
Fase 3: 200+ setup → Confidence tinggi pada strategi
```

Jangan berhenti di 20-30 setup dan mengambil kesimpulan — terlalu sedikit untuk statistik yang bermakna.

---

## 14.6 Analisis Hasil Backtesting

Setelah 100 setup, analisis ini:

### Win Rate per Setup Type:
```
Playbook A (Reversal Bullish): 38% win rate
Playbook B (Continuation Bullish): 52% win rate
Playbook C (Reversal Bearish): 35% win rate
Playbook D (Continuation Bearish): 48% win rate

Kesimpulan: Continuation setup lebih reliable dari reversal
→ Fokuskan energi pada Playbook B dan D
```

### Win Rate per Sesi:
```
Asia Session: 25% win rate → HINDARI
London Kill Zone: 55% win rate → FOKUS
NY Kill Zone: 48% win rate → BAGUS
```

### Win Rate per Pair:
```
XAUUSD: 50% win rate
EURUSD: 43% win rate
GBPUSD: 38% win rate

→ Fokus pada XAUUSD dulu
```

---

## 14.7 Red Flags dalam Backtesting

### Tanda-tanda masalah:
```
Win rate > 70%: Kemungkinan kamu "menipu" (hindsight bias)
Win rate < 30%: Setup tidak valid atau perlu revisi besar
RR rata-rata < 1:1.5: Risk management perlu diperbaiki
Max consecutive loss > 7: Perlu portfolio lebih diversified
```

### Hindsight Bias (Bias Belakang)
Ini adalah musuh terbesar backtesting. Terjadi ketika:
- Kamu melihat chart sudah tahu hasilnya sebelum analisis
- Kamu "memilih" setup yang jelas-jelas sudah terlihat benar

**Solusi**: Gunakan Bar Replay mode, atau tutup chart setelah zona yang relevan dan buka satu per satu.

---

## 14.8 Forward Testing (Paper Trading)

Setelah backtesting 100 setup:

```
Langkah berikutnya: Forward Testing di demo account
Durasi: 1-3 bulan
Tujuan: Verifikasi bahwa hasil backtesting bisa direplikasi
         dalam kondisi market real-time

Target:
- Win rate dalam 15% dari backtesting (misal: BT 50% → FT 35-65%)
- Total R positif setelah 30+ trade
- Bisa execute plan tanpa banyak deviasi
```

---

## 14.9 Kapan Siap Live Trading?

Checklist sebelum live trading:

```
[ ] 100+ setup backtesting selesai
[ ] Win rate stabil dan profitable secara agregat
[ ] 1-3 bulan forward testing selesai
[ ] Forward test sejalan dengan backtest
[ ] Risk management sudah terbiasa (tidak pernah melanggar rules)
[ ] Bisa execute plan tanpa emosi berlebihan
[ ] Punya modal yang siap "dikorbankan" untuk belajar (uang yang tidak bikin stress jika hilang)
[ ] Mulai dengan ukuran akun yang kecil (tidak perlu besar dulu)
```

---

## 14.10 Tools Backtesting

### Gratis:
- **TradingView Bar Replay**: Replay chart candle per candle
- **MT4/MT5 Strategy Tester**: Untuk manual testing
- **Google Sheets**: Untuk mencatat dan analisis

### Berbayar:
- **Forex Tester 5**: Software dedicated backtesting
- **Soft4FX**: Plugin MT4 untuk simulasi
- **TradingView Premium**: Akses replay lebih banyak

---

## 14.11 Kesimpulan Modul 14

- Backtesting wajib minimal 100 setup sebelum live
- Gunakan Bar Replay untuk hindari hindsight bias
- Catat semuanya di spreadsheet
- Analisis pola: setup mana, sesi mana, pair mana yang terbaik
- Setelah backtest → forward test 1-3 bulan di demo
- Baru live trading dengan akun kecil

---

> **Target Latihan**: Selesaikan 100 setup backtesting XAUUSD H1 dengan Bar Replay dalam 30 hari ke depan. Catat semua di spreadsheet. Di akhir 30 hari, analisis hasilnya dan identifikasi 3 perbaikan utama untuk strategi kamu.

---

**[← Modul 13](./13-full-strategy.md)** | **[→ Modul 15: Trading Journal](./15-trading-journal.md)**
