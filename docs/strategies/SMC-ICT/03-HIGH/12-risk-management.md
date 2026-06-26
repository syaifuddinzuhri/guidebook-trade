# Modul 12 — Risk Management

> **Level**: 🔴 HIGH | **Estimasi belajar**: 3-5 hari

---

## 12.1 Mengapa Risk Management adalah Segalanya?

> "Trader yang bertahan adalah trader yang masih punya uang untuk trading besok."

Strategi terbaik pun akan bangkrut tanpa risk management. Sebaliknya, risk management yang baik bisa membuat kamu profitable meski win rate hanya 40%.

```
Simulasi: Win Rate 40%, RR 1:2

10 trade:
- 4 win x 2R = +8R
- 6 loss x 1R = -6R
- Net: +2R → PROFIT!

Tanpa risk management:
- 1 trade rugi 50% akun → perlu naik 100% untuk balik
- 2 trade rugi 50% masing-masing → hampir bangkrut
```

---

## 12.2 Konsep Risk per Trade (R)

**R = jumlah yang kamu siap rugi dalam satu trade**

```
Contoh akun $1000, risk 1% per trade:
R = $1000 x 1% = $10

Jika trade ini rugi → rugi $10
Jika TP1 (1:2 RR) hit → profit $20
Jika TP2 (1:3 RR) hit → profit $30
```

### Aturan Risk per Trade:

| Level Trader | Risk per Trade |
|-------------|----------------|
| Pemula | 0.5% - 1% |
| Intermediate | 1% - 2% |
| Advanced | 2% - 3% (max) |
| **JANGAN PERNAH** | > 5% per trade |

---

## 12.3 Cara Hitung Lot Size

### Formula:

```
Lot Size = (Risk Amount) / (SL dalam pip × Pip Value)
```

### Pip Value (Forex):
- Standard Lot (1.0): ~$10 per pip (EURUSD)
- Mini Lot (0.1): ~$1 per pip
- Micro Lot (0.01): ~$0.10 per pip

### Contoh Perhitungan EURUSD:
```
Akun: $1,000
Risk: 1% = $10
SL: 20 pip

Pip Value (per lot): $10

Lot Size = $10 / (20 × $10) = $10 / $200 = 0.05 lot
```

### Contoh Perhitungan XAUUSD:
```
Akun: $1,000
Risk: 1% = $10
SL: 10 pip (= $1 per pip untuk 0.01 lot)

Lot Size = $10 / (10 × $1) = 1.0 lot ??? 

HATI-HATI: XAUUSD pip value berbeda!
XAUUSD: 1 lot = $100 per pip (bukan $10)
Mini lot 0.1 = $10 per pip
Micro lot 0.01 = $1 per pip

Jadi: Lot = $10 / (10 pip × $1/pip) = 1.0 micro lot (0.01)
Atau: $10 / (10 × $10/pip) = 0.1 mini lot (0.1)... 

Cek selalu dengan kalkulator broker atau myfxbook.com
```

### Kalkulator Sederhana:

```
1. Tentukan risk amount: Akun × Risk%
2. Tentukan SL dalam pip
3. Cari pip value pair tersebut di broker kamu
4. Lot = Risk Amount / (SL pip × Pip Value per lot)
```

---

## 12.4 Aturan Maksimum Drawdown

**Drawdown** = penurunan akun dari peak tertinggi.

```
Akun mulai: $1,000
Setelah serangkaian loss: $800
Drawdown: 20%
```

### Aturan:

| Drawdown | Tindakan |
|----------|---------|
| < 5% | Normal, lanjut |
| 5-10% | Review setup, apakah ada yang salah? |
| 10-15% | Kurangi risk 50%, pause trading |
| > 15% | STOP. Evaluasi total sebelum lanjut |
| > 20% | Full stop. Demo dulu 1-2 minggu |

---

## 12.5 Maksimum Trade Bersamaan

Jangan buka terlalu banyak posisi sekaligus — terutama pair yang berkorelasi.

```
Aturan umum:
- Maksimum 2-3 posisi sekaligus
- Pastikan pair tidak highly correlated (bisa double risk)
- Total risk semua posisi: maksimal 5-6% dari akun

Contoh salah:
BUY EURUSD + BUY GBPUSD + BUY AUDUSD
→ Semua ini bergerak vs USD
→ Jika USD menguat, semua loss sekaligus!

Contoh benar:
BUY EURUSD + SELL USDJPY (keduanya = USD lemah)
OR
BUY EURUSD saja, tunggu hasil dulu
```

---

## 12.6 Aturan Emosi dalam Risk Management

### No Revenge Trading
```
Rugi trade → JANGAN langsung buka trade baru karena emosi
Tunggu minimal 30 menit, tenangkan pikiran
Evaluasi: Apakah trade yang rugi tadi memang valid setup?
```

### Tidak Menggeser SL ke Rugi
```
SL sudah ditetapkan → TIDAK PERNAH digeser lebih jauh
Jika digeser → Kamu mengubah risiko tanpa alasan logis
Ini adalah salah satu kebiasaan paling merusak akun
```

### Tidak Averaging Down Sembarangan
```
Harga turun setelah BUY → JANGAN buka BUY lagi hanya karena "murah"
Jika tidak ada plan averaging di awal → jangan lakukan
```

---

## 12.7 Tabel Risk/Reward dan Win Rate

Berapa win rate minimum yang kamu butuhkan untuk tetap profitable?

| RR Ratio | Win Rate Minimum (BEP) |
|----------|----------------------|
| 1:1 | 50% |
| 1:2 | 33% |
| 1:3 | 25% |
| 1:4 | 20% |
| 1:5 | 17% |

```
Artinya:
Jika kamu konsisten entry dengan RR 1:3,
kamu hanya perlu benar 25% dari waktu untuk impas.
Jika win rate 40% dengan RR 1:3 → sangat profitable!
```

---

## 12.8 Compound Growth

Dengan risk management yang baik, akun bisa tumbuh eksponensial:

```
Akun: $1,000
Risk: 1% per trade
Target: 5 trade per minggu, RR 1:2, Win Rate 50%

Per minggu:
- 2.5 win × 2R = +5R = +5% akun
- 2.5 loss × 1R = -2.5R = -2.5%
- Net: +2.5% per minggu

Setelah 12 bulan (52 minggu):
$1,000 × (1.025)^52 ≈ $3,600

Dengan konsistensi: hampir 4x dalam setahun
```

---

## 12.9 Journal dan Evaluasi

Catat setiap trade:

```
Tanggal:
Pair:
Bias HTF:
Setup type (OB/FVG/Sweep/CISD):
Entry:
SL:
TP:
Risk (pip):
Reward (pip):
RR ratio:
Hasil: Win/Loss/BE
Profit/Loss ($):
Screenshot: [link atau nama file]
Catatan: [kenapa entry ini, ada yang salah?]
```

### Review Mingguan:
```
Total trade:
Win:
Loss:
Win Rate:
Total R:
Apakah ada pola kekalahan? (miss OB? terlalu early entry?)
Perbaikan untuk minggu depan:
```

---

## 12.10 Kesimpulan Modul 12

- Risk per trade: 1-2% untuk pemula-intermediate
- Lot size dihitung dari risiko, bukan feeling
- Max drawdown 10-15% → kurangi size atau pause
- Jangan pernah geser SL ke rugi lebih besar
- Journal adalah alat paling penting trader profesional

---

> **Latihan**: Buka spreadsheet baru. Buat template journal dengan kolom-kolom di 12.9. Masukkan 10 trade terakhir kamu (atau 10 setup backtesting). Hitung win rate dan total R. Pola apa yang kamu temukan?

---

**[← Modul 11](./11-entry-model.md)** | **[→ Modul 13: Full Strategy](../04-MASTER/13-full-strategy.md)**
