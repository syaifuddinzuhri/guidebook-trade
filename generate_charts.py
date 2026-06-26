"""
Chart generator untuk Trading Guidebook.
Menghasilkan gambar candlestick PNG untuk setiap konsep trading.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import matplotlib.patheffects as pe
import os

OUTPUT_DIR = "docs/assets/charts"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Style global ──────────────────────────────────────────────
DARK_BG    = "#0d1117"
GRID_COLOR = "#21262d"
TEXT_COLOR = "#e6edf3"
GREEN      = "#26a641"
RED        = "#da3633"
BLUE       = "#388bfd"
ORANGE     = "#f0883e"
PURPLE     = "#a371f7"
YELLOW     = "#e3b341"
GRAY       = "#8b949e"

def setup_dark_chart(figsize=(14, 7), title=""):
    fig, ax = plt.subplots(figsize=figsize, facecolor=DARK_BG)
    ax.set_facecolor(DARK_BG)
    ax.grid(True, color=GRID_COLOR, linewidth=0.5, alpha=0.7)
    ax.tick_params(colors=TEXT_COLOR, labelsize=9)
    for spine in ax.spines.values():
        spine.set_edgecolor(GRID_COLOR)
    if title:
        ax.set_title(title, color=TEXT_COLOR, fontsize=13, fontweight='bold', pad=12)
    return fig, ax

def draw_candles(ax, data):
    """data: list of (open, high, low, close)"""
    for i, (o, h, l, c) in enumerate(data):
        color = GREEN if c >= o else RED
        # wick
        ax.plot([i, i], [l, h], color=color, linewidth=1.2, zorder=2)
        # body
        body_bot = min(o, c)
        body_h   = abs(c - o) or 0.5
        rect = plt.Rectangle((i - 0.35, body_bot), 0.7, body_h,
                              color=color, zorder=3)
        ax.add_patch(rect)

def label(ax, x, y, text, color=TEXT_COLOR, fontsize=9, ha='left', va='center',
          arrow=False, arrow_end=None, bg=None):
    kwargs = dict(color=color, fontsize=fontsize, ha=ha, va=va,
                  fontweight='bold', zorder=10)
    if bg:
        kwargs['bbox'] = dict(boxstyle='round,pad=0.3', facecolor=bg,
                               edgecolor='none', alpha=0.85)
    ax.text(x, y, text, **kwargs)
    if arrow and arrow_end:
        ax.annotate('', xy=arrow_end, xytext=(x, y),
                    arrowprops=dict(arrowstyle='->', color=color, lw=1.5))

def hline(ax, y, xmin, xmax, color=GRAY, lw=1, ls='--', label_text='', side='right'):
    ax.axhline(y=y, xmin=xmin, xmax=xmax, color=color, linewidth=lw,
               linestyle=ls, zorder=5)
    if label_text:
        xa = ax.get_xlim()[1] * 0.98 if side == 'right' else ax.get_xlim()[0] * 1.01
        ax.text(xa, y, label_text, color=color, fontsize=8,
                va='center', ha='right' if side == 'right' else 'left',
                fontweight='bold')

def zone_box(ax, x0, x1, y0, y1, color, alpha=0.18, label_text='', lw=1):
    ax.axhspan(y0, y1, xmin=x0, xmax=x1, color=color, alpha=alpha)
    ax.axhspan(y0, y1, xmin=x0, xmax=x1, color=color, alpha=0,
               linewidth=lw, edgecolor=color,
               linestyle='--')
    if label_text:
        mx = (x0 + x1) / 2 * (ax.get_xlim()[1] - ax.get_xlim()[0]) + ax.get_xlim()[0]
        my = (y0 + y1) / 2
        ax.text(mx, my, label_text, color=color, fontsize=8,
                ha='center', va='center', fontweight='bold', alpha=0.9)

def save(fig, name):
    path = f"{OUTPUT_DIR}/{name}.png"
    fig.savefig(path, dpi=150, bbox_inches='tight',
                facecolor=DARK_BG, edgecolor='none')
    plt.close(fig)
    print(f"  ✓ {path}")


# ══════════════════════════════════════════════════════════════
# SMC-ICT CHARTS
# ══════════════════════════════════════════════════════════════

def chart_bos_bullish():
    candles = [
        (2040,2048,2035,2038),(2038,2042,2030,2032),(2032,2036,2025,2027),
        (2027,2031,2022,2024),(2024,2028,2019,2021),(2021,2025,2018,2023),
        (2023,2030,2020,2028),(2028,2035,2026,2033),(2033,2040,2030,2038),
        (2038,2048,2036,2046),(2046,2052,2043,2050),
    ]
    fig, ax = setup_dark_chart(title="BOS Bullish — XAUUSD H4\nBreak of Structure Terkonfirmasi")
    draw_candles(ax, candles)
    n = len(candles)
    ax.set_xlim(-1, n + 2)
    prices = [p for c in candles for p in c]
    ax.set_ylim(min(prices)-8, max(prices)+12)

    # Swing High level
    sh_level = 2042
    ax.axhline(sh_level, color=BLUE, lw=1.5, ls='--', zorder=4)
    ax.text(n+0.3, sh_level, f'Swing High\n{sh_level}', color=BLUE,
            fontsize=8, va='center', fontweight='bold')

    # HL area
    zone_box(ax, 4/n, 6/n, 2018, 2025, GREEN, 0.15)
    ax.text(4.5, 2021, 'Higher Low\n(HL)', color=GREEN, fontsize=8,
            ha='center', va='center', fontweight='bold')

    # BOS arrow
    ax.annotate('BOS ✓\nClose 2046 > SH 2042', xy=(9.5, 2046),
                xytext=(7, 2055),
                arrowprops=dict(arrowstyle='->', color=BLUE, lw=2),
                color=BLUE, fontsize=9, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#0d2b5e', edgecolor=BLUE))

    # Annotations
    ax.text(0.5, 2044, 'LH', color=RED, fontsize=9, fontweight='bold')
    ax.text(3.2, 2023, 'LL', color=RED, fontsize=9, fontweight='bold')
    ax.text(5.2, 2020, 'HL', color=GREEN, fontsize=9, fontweight='bold')

    # Entry zone
    zone_box(ax, 8.5/n, 10/n, 2035, 2040, GREEN, 0.2)
    ax.text(9, 2037, 'Entry Zone\n(Pullback ke FVG)', color=GREEN,
            fontsize=7.5, ha='center', fontweight='bold')

    ax.set_ylabel('Price (USD)', color=TEXT_COLOR, fontsize=10)
    ax.set_xlabel('Candle Index →  Waktu', color=TEXT_COLOR, fontsize=10)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    save(fig, 'bos_bullish')


def chart_bos_bearish():
    candles = [
        (1950,1958,1946,1955),(1955,1962,1952,1960),(1960,1968,1957,1965),
        (1965,1970,1960,1962),(1962,1966,1955,1958),(1958,1960,1948,1950),
        (1950,1955,1944,1946),(1946,1950,1940,1942),(1942,1946,1936,1938),
        (1938,1942,1932,1934),
    ]
    fig, ax = setup_dark_chart(title="BOS Bearish — EURUSD H4\nKonfirmasi Trend Turun")
    draw_candles(ax, candles)
    n = len(candles)
    ax.set_xlim(-1, n + 2)
    prices = [p for c in candles for p in c]
    ax.set_ylim(min(prices)-6, max(prices)+10)

    sl_level = 1950
    ax.axhline(sl_level, color=RED, lw=1.5, ls='--', zorder=4)
    ax.text(n+0.3, sl_level, f'Swing Low\n{sl_level}', color=RED,
            fontsize=8, va='center', fontweight='bold')

    ax.annotate('BOS ✓\nClose 1942 < SL 1950', xy=(7.5, 1942),
                xytext=(5, 1930),
                arrowprops=dict(arrowstyle='->', color=RED, lw=2),
                color=RED, fontsize=9, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#3d0000', edgecolor=RED))

    ax.text(2.5, 1967, 'HH', color=GREEN, fontsize=9, fontweight='bold')
    ax.text(4.5, 1963, 'LH', color=RED, fontsize=9, fontweight='bold')
    ax.text(1.5, 1953, 'HL', color=GREEN, fontsize=9, fontweight='bold')
    ax.text(6.5, 1948, 'LL', color=RED, fontsize=9, fontweight='bold')

    zone_box(ax, 0.55, 0.75, 1944, 1950, RED, 0.2)
    ax.text(6.5, 1946, 'Pullback ke OB\n(Entry Sell)', color=RED,
            fontsize=7.5, ha='center', fontweight='bold')

    ax.set_ylabel('Price', color=TEXT_COLOR, fontsize=10)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    save(fig, 'bos_bearish')


def chart_choch():
    # Downtrend lalu CHOCH bullish
    candles = [
        (2060,2068,2056,2058),(2058,2062,2050,2052),(2052,2055,2044,2046),
        (2046,2050,2040,2042),(2042,2048,2036,2044),(2044,2050,2040,2048),
        (2048,2055,2044,2053),(2053,2060,2050,2058),(2058,2066,2055,2064),
        (2064,2072,2061,2070),
    ]
    fig, ax = setup_dark_chart(title="CHOCH — Change of Character XAUUSD H1\nPeralihan dari Bearish ke Bullish")
    draw_candles(ax, candles)
    n = len(candles)
    ax.set_xlim(-1, n + 3)
    prices = [p for c in candles for p in c]
    ax.set_ylim(min(prices)-8, max(prices)+15)

    lh_level = 2052
    ax.axhline(lh_level, color=ORANGE, lw=1.5, ls='-.', zorder=4)
    ax.text(n+0.3, lh_level, f'Last LH\n{lh_level}', color=ORANGE,
            fontsize=8, va='center', fontweight='bold')

    ax.annotate('CHOCH ✓\nClose 2053 > LH 2052\n(Struktur berubah!)', xy=(6.5, 2053),
                xytext=(4.5, 2072),
                arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2),
                color=ORANGE, fontsize=9, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#3d2000', edgecolor=ORANGE))

    # Labels
    for xi, txt, col in [(0,  'LH', RED),(2,  'LH', RED),
                          (3,  'LL', RED),(4,  'LL', RED),
                          (4,  'IDM?', GRAY)]:
        ax.text(xi+0.3, candles[xi][1]+1.5, txt, color=col, fontsize=8, fontweight='bold')

    ax.text(4.5, candles[4][2]-4, 'SSL Sweep\n(Wick panjang)', color=BLUE,
            fontsize=8, ha='center', fontweight='bold')
    ax.annotate('', xy=(4.5, candles[4][2]), xytext=(4.5, candles[4][2]-3),
                arrowprops=dict(arrowstyle='->', color=BLUE, lw=1.5))

    # IDM zone
    zone_box(ax, 4/n, 5/n, 2036, 2044, PURPLE, 0.15)

    ax.set_ylabel('Price (USD)', color=TEXT_COLOR, fontsize=10)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    save(fig, 'choch_bullish')


def chart_order_block_bullish():
    candles = [
        (2030,2038,2028,2035),(2035,2040,2033,2038),(2038,2042,2030,2032),
        # OB candle (bearish terakhir sebelum displacement)
        (2032,2036,2026,2028),
        # Displacement bullish
        (2028,2048,2026,2046),(2046,2052,2044,2050),(2050,2055,2047,2053),
        # Pullback ke OB
        (2053,2055,2040,2042),(2042,2045,2034,2036),
        # Rejection dari OB
        (2036,2050,2034,2048),(2048,2058,2046,2056),
    ]
    fig, ax = setup_dark_chart(title="Order Block Bullish — XAUUSD H1\nEntry di OB setelah Displacement")
    draw_candles(ax, candles)
    n = len(candles)
    ax.set_xlim(-1, n + 3)
    prices = [p for c in candles for p in c]
    ax.set_ylim(min(prices)-8, max(prices)+14)

    # OB zone (candle index 3: open=2032, close=2028, high=2036, low=2026)
    ob_high, ob_low = 2036, 2026
    zone_box(ax, 3/n, 9.5/n, ob_low, ob_high, GREEN, 0.25)
    ax.text(-0.5, (ob_high+ob_low)/2, f'BULLISH OB\n{ob_low}–{ob_high}',
            color=GREEN, fontsize=8, va='center', ha='right', fontweight='bold')

    # Displacement arrow
    ax.annotate('Displacement\nBullish Kuat', xy=(4.5, 2046),
                xytext=(5.5, 2055),
                arrowprops=dict(arrowstyle='->', color=BLUE, lw=1.5),
                color=BLUE, fontsize=8, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#0d2b5e', edgecolor=BLUE))

    # BOS line
    ax.axhline(2042, color=BLUE, lw=1, ls='--', alpha=0.6)
    ax.text(n+0.3, 2042, 'BOS Level', color=BLUE, fontsize=7.5, va='center')

    # Pullback to OB
    ax.annotate('Harga pullback\nke OB', xy=(8.5, 2036),
                xytext=(9.8, 2028),
                arrowprops=dict(arrowstyle='->', color=YELLOW, lw=1.5),
                color=YELLOW, fontsize=8, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#2d2000', edgecolor=YELLOW))

    # Entry/SL/TP
    ax.axhline(2036, color=GREEN, lw=1.5, ls='-', alpha=0.8)
    ax.axhline(2024, color=RED, lw=1.5, ls='-', alpha=0.8)
    ax.axhline(2058, color=YELLOW, lw=1.5, ls='-', alpha=0.8)
    ax.text(n+0.3, 2036, 'ENTRY 2036', color=GREEN, fontsize=8, va='center', fontweight='bold')
    ax.text(n+0.3, 2024, 'SL 2024', color=RED, fontsize=8, va='center', fontweight='bold')
    ax.text(n+0.3, 2058, 'TP 2058\n(RR 1:1.8)', color=YELLOW, fontsize=8, va='center', fontweight='bold')

    ax.set_ylabel('Price (USD)', color=TEXT_COLOR, fontsize=10)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    save(fig, 'order_block_bullish')


def chart_order_block_bearish():
    candles = [
        (1980,1985,1975,1982),(1982,1988,1980,1986),(1986,1992,1984,1990),
        # OB candle (bullish terakhir)
        (1990,1996,1988,1994),
        # Displacement bearish
        (1994,1995,1972,1974),(1974,1978,1968,1970),(1970,1974,1964,1966),
        # Pullback ke OB
        (1966,1980,1964,1978),(1978,1990,1976,1988),
        # Rejection dari OB
        (1988,1992,1974,1976),(1976,1978,1962,1964),
    ]
    fig, ax = setup_dark_chart(title="Order Block Bearish — EURUSD H1\nEntry Sell di OB setelah Displacement")
    draw_candles(ax, candles)
    n = len(candles)
    ax.set_xlim(-1, n + 3)
    prices = [p for c in candles for p in c]
    ax.set_ylim(min(prices)-8, max(prices)+10)

    ob_high, ob_low = 1996, 1988
    zone_box(ax, 3/n, 9.5/n, ob_low, ob_high, RED, 0.25)
    ax.text(-0.5, (ob_high+ob_low)/2, f'BEARISH OB\n{ob_low}–{ob_high}',
            color=RED, fontsize=8, va='center', ha='right', fontweight='bold')

    ax.annotate('Displacement\nBearish Kuat', xy=(4.5, 1974),
                xytext=(5.8, 1966),
                arrowprops=dict(arrowstyle='->', color=BLUE, lw=1.5),
                color=BLUE, fontsize=8, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#0d2b5e', edgecolor=BLUE))

    ax.annotate('Pullback ke OB\n→ Entry Sell', xy=(8.5, 1988),
                xytext=(9.8, 1996),
                arrowprops=dict(arrowstyle='->', color=YELLOW, lw=1.5),
                color=YELLOW, fontsize=8, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#2d2000', edgecolor=YELLOW))

    ax.axhline(1988, color=RED, lw=1.5, ls='-', alpha=0.8)
    ax.axhline(1998, color=RED, lw=1.5, ls='-', alpha=0.8)
    ax.axhline(1964, color=YELLOW, lw=1.5, ls='-', alpha=0.8)
    ax.text(n+0.3, 1988, 'ENTRY 1988', color=RED, fontsize=8, va='center', fontweight='bold')
    ax.text(n+0.3, 1998, 'SL 1998', color=RED, fontsize=8, va='center', fontweight='bold')
    ax.text(n+0.3, 1964, 'TP 1964\n(RR 1:2.4)', color=YELLOW, fontsize=8, va='center', fontweight='bold')

    ax.set_ylabel('Price', color=TEXT_COLOR, fontsize=10)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    save(fig, 'order_block_bearish')


def chart_fvg():
    candles = [
        (2020,2026,2018,2024),(2024,2028,2022,2026),
        # Candle 1 of FVG sequence
        (2026,2030,2023,2028),
        # Displacement (candle 2)
        (2028,2055,2027,2053),
        # Candle 3
        (2053,2058,2040,2056),
        (2056,2060,2053,2058),
        # Pullback ke FVG
        (2058,2060,2048,2050),(2050,2052,2038,2040),
        # Bounce dari FVG
        (2040,2055,2038,2053),(2053,2062,2050,2060),
    ]
    fig, ax = setup_dark_chart(title="Fair Value Gap (FVG) — XAUUSD M15\nFill & Bounce dari FVG Bullish")
    draw_candles(ax, candles)
    n = len(candles)
    ax.set_xlim(-1, n + 3)
    prices = [p for c in candles for p in c]
    ax.set_ylim(min(prices)-8, max(prices)+10)

    # FVG = High candle 1 (index 2) to Low candle 3 (index 4)
    fvg_top = candles[2][1]  # High candle 2: 2030
    fvg_bot = candles[4][2]  # Low candle 4: 2040
    # Actually for bullish FVG: High of candle[2] to Low of candle[4]
    fvg_top = 2040
    fvg_bot = 2030
    ce = (fvg_top + fvg_bot) / 2  # 2035

    zone_box(ax, 2/n, 10/n, fvg_bot, fvg_top, BLUE, 0.25)
    ax.axhline(ce, xmin=2/n, xmax=10/n, color=BLUE, lw=1, ls=':', alpha=0.8)
    ax.text(-0.5, fvg_top, f'FVG Top {fvg_top}', color=BLUE, fontsize=8,
            va='center', ha='right', fontweight='bold')
    ax.text(-0.5, fvg_bot, f'FVG Bot {fvg_bot}', color=BLUE, fontsize=8,
            va='center', ha='right', fontweight='bold')
    ax.text(-0.5, ce, f'CE (50%) {ce}', color=BLUE, fontsize=7.5,
            va='center', ha='right')

    ax.annotate('Displacement Candle\n(Menciptakan FVG)', xy=(3.5, 2053),
                xytext=(5, 2063),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5),
                color=GREEN, fontsize=8, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#0d3d00', edgecolor=GREEN))

    ax.annotate('Harga fill FVG\nlalu bounce', xy=(7.5, 2038),
                xytext=(9, 2025),
                arrowprops=dict(arrowstyle='->', color=YELLOW, lw=1.5),
                color=YELLOW, fontsize=8, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#2d2000', edgecolor=YELLOW))

    ax.axhline(2038, color=GREEN, lw=1.5, ls='-', alpha=0.8)
    ax.axhline(2028, color=RED, lw=1.5, ls='-', alpha=0.8)
    ax.axhline(2060, color=YELLOW, lw=1.5, ls='-', alpha=0.8)
    ax.text(n+0.3, 2038, 'ENTRY 2038', color=GREEN, fontsize=8, va='center', fontweight='bold')
    ax.text(n+0.3, 2028, 'SL 2028', color=RED, fontsize=8, va='center', fontweight='bold')
    ax.text(n+0.3, 2060, 'TP 2060 (RR 1:2.2)', color=YELLOW, fontsize=8, va='center', fontweight='bold')

    ax.set_ylabel('Price (USD)', color=TEXT_COLOR, fontsize=10)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    save(fig, 'fvg_bullish')


def chart_liquidity_sweep():
    candles = [
        (2030,2034,2028,2032),(2032,2036,2030,2034),(2034,2036,2032,2034),
        (2034,2036,2032,2033),(2033,2036,2031,2034),
        # SSL sweep
        (2034,2035,2022,2033),
        # Recovery + CISD
        (2033,2046,2031,2044),(2044,2050,2042,2048),(2048,2055,2045,2053),
    ]
    fig, ax = setup_dark_chart(title="Liquidity Sweep (SSL) — XAUUSD M15\nSweep → Reversal Bullish")
    draw_candles(ax, candles)
    n = len(candles)
    ax.set_xlim(-1, n + 3)
    prices = [p for c in candles for p in c]
    ax.set_ylim(min(prices)-6, max(prices)+12)

    # EQL (Equal Lows) = SSL
    ssl_level = 2030
    ax.axhline(ssl_level, color=RED, lw=2, ls='--', zorder=5)
    ax.text(-0.5, ssl_level, f'SSL / EQL\n{ssl_level}', color=RED,
            fontsize=8, va='center', ha='right', fontweight='bold')

    # BSL at top
    bsl_level = 2036
    ax.axhline(bsl_level, color=GREEN, lw=1.5, ls='--', zorder=5, alpha=0.7)
    ax.text(n+0.3, bsl_level, f'BSL {bsl_level}', color=GREEN,
            fontsize=8, va='center', fontweight='bold')

    # Sweep annotation
    ax.annotate('SWEEP!\nWick ke 2022\n(Trigger stop loss retail)', xy=(5.5, 2022),
                xytext=(7, 2020),
                arrowprops=dict(arrowstyle='->', color=RED, lw=2),
                color=RED, fontsize=9, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#3d0000', edgecolor=RED))

    ax.annotate('Reversal!\nClose kembali di atas SSL', xy=(6.5, 2033),
                xytext=(7.5, 2043),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2),
                color=GREEN, fontsize=9, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#0d3d00', edgecolor=GREEN))

    # Equal lows label
    for i in [0,1,2,3,4]:
        ax.text(i+0.1, 2028, '▼', color=RED, fontsize=7, ha='center')
    ax.text(2, 2025, '← Equal Lows (SSL terkumpul di sini)', color=RED,
            fontsize=7.5, ha='center')

    ax.axhline(2033, color=GREEN, lw=1.5, ls='-', alpha=0.8)
    ax.axhline(2020, color=RED, lw=1.5, ls='-', alpha=0.8)
    ax.axhline(2053, color=YELLOW, lw=1.5, ls='-', alpha=0.8)
    ax.text(n+0.3, 2033, 'ENTRY 2033', color=GREEN, fontsize=8, va='center', fontweight='bold')
    ax.text(n+0.3, 2020, 'SL 2020', color=RED, fontsize=8, va='center', fontweight='bold')
    ax.text(n+0.3, 2053, 'TP 2053 (RR 1:1.5)', color=YELLOW, fontsize=8, va='center', fontweight='bold')

    ax.set_ylabel('Price (USD)', color=TEXT_COLOR, fontsize=10)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    save(fig, 'liquidity_sweep')


def chart_cisd():
    candles = [
        (2040,2045,2038,2042),(2042,2044,2035,2037),(2037,2040,2033,2035),
        (2035,2038,2030,2032),(2032,2034,2027,2029),
        # Sweep SSL
        (2029,2031,2022,2030),
        # CISD candle (bullish, close di atas swing high lokal)
        (2030,2046,2028,2044),
        # Konfirmasi
        (2044,2050,2042,2048),(2048,2055,2045,2053),
    ]
    fig, ax = setup_dark_chart(title="CISD — Change in State of Delivery XAUUSD M15\nPerubahan Cara Harga Dikirim")
    draw_candles(ax, candles)
    n = len(candles)
    ax.set_xlim(-1, n + 3)
    prices = [p for c in candles for p in c]
    ax.set_ylim(min(prices)-8, max(prices)+14)

    # Bearish delivery phase
    ax.axvspan(-0.5, 5.5, alpha=0.08, color=RED, zorder=1)
    ax.text(2.5, 2047, 'BEARISH DELIVERY', color=RED, fontsize=9,
            ha='center', fontweight='bold', alpha=0.7)

    # Bullish delivery phase
    ax.axvspan(5.5, n+1, alpha=0.08, color=GREEN, zorder=1)
    ax.text(7.5, 2056, 'BULLISH DELIVERY', color=GREEN, fontsize=9,
            ha='center', fontweight='bold', alpha=0.7)

    # Swing high lokal yang ditembus CISD
    swing_local = 2034
    ax.axhline(swing_local, xmin=3/n, xmax=7/n, color=ORANGE, lw=1.5, ls='-.', zorder=4)
    ax.text(3.5, swing_local+0.8, f'Swing High Lokal {swing_local}', color=ORANGE,
            fontsize=7.5, fontweight='bold')

    # SSL
    ssl = 2029
    ax.axhline(ssl, color=RED, lw=1.5, ls='--', alpha=0.7, zorder=4)
    ax.text(-0.5, ssl, f'SSL {ssl}', color=RED, fontsize=8, va='center',
            ha='right', fontweight='bold')

    # CISD annotation
    ax.annotate('CISD CANDLE!\nClose 2044 > Swing High 2034\n→ Perubahan delivery!', xy=(6.5, 2044),
                xytext=(7.8, 2055),
                arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2),
                color=ORANGE, fontsize=9, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#3d2000', edgecolor=ORANGE))

    # Sweep annotation
    ax.annotate('SSL Sweep\n(Wick ke 2022)', xy=(5.5, 2022),
                xytext=(4, 2018),
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.5),
                color=RED, fontsize=8, fontweight='bold')

    # Entry/SL/TP
    ax.axhline(2044, color=GREEN, lw=1.5, ls='-', alpha=0.9)
    ax.axhline(2020, color=RED, lw=1.5, ls='-', alpha=0.9)
    ax.axhline(2058, color=YELLOW, lw=1.5, ls='-', alpha=0.9)
    ax.text(n+0.3, 2044, 'ENTRY 2044', color=GREEN, fontsize=8, va='center', fontweight='bold')
    ax.text(n+0.3, 2020, 'SL 2020', color=RED, fontsize=8, va='center', fontweight='bold')
    ax.text(n+0.3, 2058, 'TP 2058 (RR 1:0.6)', color=YELLOW, fontsize=8, va='center', fontweight='bold')

    ax.set_ylabel('Price (USD)', color=TEXT_COLOR, fontsize=10)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    save(fig, 'cisd')


def chart_multi_timeframe():
    fig, axes = plt.subplots(1, 3, figsize=(18, 6), facecolor=DARK_BG)
    fig.suptitle('Multi-Timeframe Analysis — XAUUSD\nD1 → H4 → H1: Top-Down Framework',
                 color=TEXT_COLOR, fontsize=13, fontweight='bold')

    configs = [
        ("D1 — HTF BIAS", [
            (1980,1995,1978,1992),(1992,2005,1990,2002),(2002,2015,1998,2010),
            (2010,2020,2005,2008),(2008,2012,2000,2003),(2003,2010,2001,2008),
            (2008,2018,2006,2015),(2015,2025,2013,2022),
        ], "BULLISH BIAS ↑"),
        ("H4 — ITF ZONE", [
            (2022,2028,2020,2025),(2025,2030,2022,2023),(2023,2025,2018,2019),
            (2019,2022,2016,2020),(2020,2026,2018,2024),(2024,2032,2022,2030),
        ], "CHOCH Bullish\nOB Zone: 2016-2020"),
        ("H1 — LTF ENTRY", [
            (2020,2022,2018,2019),(2019,2020,2016,2017),(2017,2020,2015,2019),
            (2019,2025,2017,2024),(2024,2028,2022,2026),(2026,2030,2024,2028),
        ], "CISD → Entry\n2017 | SL 2013 | TP 2030"),
    ]

    for ax, (title, candles, note) in zip(axes, configs):
        ax.set_facecolor(DARK_BG)
        ax.grid(True, color=GRID_COLOR, linewidth=0.5, alpha=0.5)
        ax.tick_params(colors=TEXT_COLOR, labelsize=8)
        for spine in ax.spines.values():
            spine.set_edgecolor(GRID_COLOR)
        ax.set_title(title, color=TEXT_COLOR, fontsize=11, fontweight='bold', pad=8)
        draw_candles(ax, candles)
        n = len(candles)
        ax.set_xlim(-1, n + 1)
        prices = [p for c in candles for p in c]
        ax.set_ylim(min(prices)-6, max(prices)+10)
        ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
        ax.text(0.5, 0.05, note, transform=ax.transAxes,
                color=YELLOW, fontsize=8.5, fontweight='bold',
                ha='center', va='bottom',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#1a1a00', edgecolor=YELLOW, alpha=0.9))

    axes[0].text(0.5, 0.92, '▲ BULLISH', transform=axes[0].transAxes,
                 color=GREEN, fontsize=11, fontweight='bold', ha='center',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#0d3d00', edgecolor=GREEN))
    axes[1].text(0.5, 0.92, '🎯 ZONA: 2016-2020', transform=axes[1].transAxes,
                 color=ORANGE, fontsize=10, fontweight='bold', ha='center',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#3d2000', edgecolor=ORANGE))
    axes[2].text(0.5, 0.92, '⚡ ENTRY!', transform=axes[2].transAxes,
                 color=BLUE, fontsize=11, fontweight='bold', ha='center',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#0d2b5e', edgecolor=BLUE))

    plt.tight_layout()
    save(fig, 'multi_timeframe')


# ══════════════════════════════════════════════════════════════
# SnR CHARTS
# ══════════════════════════════════════════════════════════════

def chart_snr_support_bounce():
    candles = [
        (1.1100,1.1120,1.1080,1.1095),(1.1095,1.1110,1.1082,1.1105),
        (1.1105,1.1115,1.1085,1.1088),(1.1088,1.1092,1.1079,1.1082),
        # Bounce 1
        (1.1082,1.1110,1.1078,1.1108),(1.1108,1.1130,1.1105,1.1125),
        (1.1125,1.1140,1.1120,1.1135),(1.1135,1.1145,1.1125,1.1140),
        # Pullback ke support
        (1.1140,1.1142,1.1082,1.1085),
        # Bounce 2
        (1.1085,1.1115,1.1080,1.1112),(1.1112,1.1130,1.1108,1.1128),
        (1.1128,1.1145,1.1125,1.1142),
        # Pullback ke support lagi
        (1.1142,1.1145,1.1081,1.1084),
        # Bounce 3 (entry)
        (1.1084,1.1115,1.1079,1.1112),(1.1112,1.1135,1.1108,1.1132),
        (1.1132,1.1150,1.1128,1.1148),
    ]
    fig, ax = setup_dark_chart(title="Support Bounce — EURUSD H4\n3x Sentuhan = Level Kuat (Zone)")
    draw_candles(ax, candles)
    n = len(candles)
    ax.set_xlim(-1, n + 2)
    prices = [p for c in candles for p in c]
    ax.set_ylim(min(prices)-0.002, max(prices)+0.004)

    # Support zone
    s_top, s_bot = 1.1090, 1.1078
    zone_box(ax, 0, 1, s_bot, s_top, GREEN, 0.2)
    ax.text(-0.5, (s_top+s_bot)/2, f'SUPPORT ZONE\n{s_bot}–{s_top}',
            color=GREEN, fontsize=8, va='center', ha='right', fontweight='bold')

    # Resistance
    r_level = 1.1145
    ax.axhline(r_level, color=RED, lw=1.5, ls='--', zorder=4)
    ax.text(n+0.2, r_level, f'RESISTANCE\n{r_level}', color=RED,
            fontsize=8, va='center', fontweight='bold')

    # Bounce labels
    for xi, label_txt in [(4, 'Bounce 1'), (9, 'Bounce 2'), (13, 'Bounce 3\n(Entry)')]:
        ax.annotate(label_txt, xy=(xi, s_top),
                    xytext=(xi, s_top+0.0015),
                    arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.2),
                    color=GREEN, fontsize=8, ha='center', fontweight='bold')

    # Entry
    ax.axhline(1.1090, color=GREEN, lw=1.5, ls='-', alpha=0.8)
    ax.axhline(1.1070, color=RED, lw=1.5, ls='-', alpha=0.8)
    ax.axhline(1.1148, color=YELLOW, lw=1.5, ls='-', alpha=0.8)
    ax.text(n+0.2, 1.1090, 'ENTRY\n1.1090', color=GREEN, fontsize=8, va='center', fontweight='bold')
    ax.text(n+0.2, 1.1070, 'SL 1.1070', color=RED, fontsize=8, va='center', fontweight='bold')
    ax.text(n+0.2, 1.1148, 'TP 1.1148\n(RR 1:2.9)', color=YELLOW, fontsize=8, va='center', fontweight='bold')

    ax.set_ylabel('Price (EURUSD)', color=TEXT_COLOR, fontsize=10)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    save(fig, 'snr_support_bounce')


def chart_snr_resistance_rejection():
    candles = [
        (1.0850,1.0875,1.0845,1.0870),(1.0870,1.0895,1.0868,1.0890),
        (1.0890,1.0910,1.0885,1.0908),(1.0908,1.0940,1.0905,1.0935),
        # Resistance hit 1
        (1.0935,1.0958,1.0930,1.0935),(1.0935,1.0940,1.0905,1.0910),
        (1.0910,1.0920,1.0885,1.0888),(1.0888,1.0895,1.0870,1.0875),
        # Rally ke resistance lagi
        (1.0875,1.0900,1.0872,1.0898),(1.0898,1.0930,1.0895,1.0928),
        # Resistance hit 2
        (1.0928,1.0960,1.0925,1.0930),(1.0930,1.0935,1.0900,1.0903),
        (1.0903,1.0908,1.0875,1.0878),
        # Rally ke resistance 3 (entry sell)
        (1.0878,1.0905,1.0875,1.0902),(1.0902,1.0932,1.0898,1.0930),
        # Sell entry
        (1.0930,1.0962,1.0928,1.0932),(1.0932,1.0938,1.0900,1.0902),
        (1.0902,1.0908,1.0870,1.0873),
    ]
    fig, ax = setup_dark_chart(title="Resistance Rejection — EURUSD H1\nSell Entry di Zona Resistance (3x Sentuhan)")
    draw_candles(ax, candles)
    n = len(candles)
    ax.set_xlim(-1, n + 2)
    prices = [p for c in candles for p in c]
    ax.set_ylim(min(prices)-0.003, max(prices)+0.005)

    r_top, r_bot = 1.0962, 1.0948
    zone_box(ax, 0, 1, r_bot, r_top, RED, 0.2)
    ax.text(-0.5, (r_top+r_bot)/2, f'RESISTANCE ZONE\n{r_bot}–{r_top}',
            color=RED, fontsize=8, va='center', ha='right', fontweight='bold')

    for xi, lbl in [(4, 'Rejection 1'), (10, 'Rejection 2'), (15, 'Rejection 3\n(Entry Sell)')]:
        ax.annotate(lbl, xy=(xi, r_bot),
                    xytext=(xi, r_bot+0.002),
                    arrowprops=dict(arrowstyle='->', color=RED, lw=1.2),
                    color=RED, fontsize=8, ha='center', fontweight='bold')

    ax.axhline(1.0948, color=RED, lw=1.5, ls='-', alpha=0.8)
    ax.axhline(1.0970, color=RED, lw=1.5, ls='-', alpha=0.8)
    ax.axhline(1.0870, color=YELLOW, lw=1.5, ls='-', alpha=0.8)
    ax.text(n+0.2, 1.0948, 'ENTRY\n1.0948', color=RED, fontsize=8, va='center', fontweight='bold')
    ax.text(n+0.2, 1.0970, 'SL 1.0970', color=RED, fontsize=8, va='center', fontweight='bold')
    ax.text(n+0.2, 1.0870, 'TP 1.0870\n(RR 1:3.5)', color=YELLOW, fontsize=8, va='center', fontweight='bold')

    ax.set_ylabel('Price (EURUSD)', color=TEXT_COLOR, fontsize=10)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    save(fig, 'snr_resistance_rejection')


def chart_snr_role_reversal():
    candles = [
        # Downtrend dengan resistance
        (1.0900,1.0920,1.0895,1.0915),(1.0915,1.0935,1.0912,1.0930),
        (1.0930,1.0952,1.0928,1.0948),(1.0948,1.0958,1.0942,1.0945),
        # Breakout di atas resistance
        (1.0945,1.0975,1.0943,1.0972),(1.0972,1.0985,1.0968,1.0982),
        (1.0982,1.0995,1.0978,1.0990),(1.0990,1.1005,1.0985,1.1000),
        # Pullback ke level (retest sebagai support baru)
        (1.1000,1.1002,1.0952,1.0955),(1.0955,1.0960,1.0948,1.0957),
        # Bounce dari ex-resistance (sekarang support)
        (1.0957,1.0990,1.0953,1.0988),(1.0988,1.1010,1.0985,1.1008),
        (1.1008,1.1025,1.1005,1.1022),
    ]
    fig, ax = setup_dark_chart(title="Role Reversal (SR Flip) — EURUSD H4\nResistance Menjadi Support setelah Breakout")
    draw_candles(ax, candles)
    n = len(candles)
    ax.set_xlim(-1, n + 3)
    prices = [p for c in candles for p in c]
    ax.set_ylim(min(prices)-0.003, max(prices)+0.006)

    flip_level = 1.0950
    ax.axhline(flip_level, color=PURPLE, lw=2, ls='--', zorder=5)

    ax.text(-0.5, flip_level+0.001, 'RESISTANCE', color=RED,
            fontsize=9, ha='right', fontweight='bold')
    ax.text(-0.5, flip_level-0.002, 'Sebelum Breakout', color=RED,
            fontsize=7.5, ha='right')

    ax.text(n+0.3, flip_level+0.001, 'SUPPORT', color=GREEN,
            fontsize=9, ha='left', fontweight='bold')
    ax.text(n+0.3, flip_level-0.002, 'Setelah Breakout', color=GREEN,
            fontsize=7.5, ha='left')

    ax.annotate('BREAKOUT!\nClose di atas Resistance', xy=(4.5, 1.0972),
                xytext=(5.5, 1.0998),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2),
                color=GREEN, fontsize=8.5, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#0d3d00', edgecolor=GREEN))

    ax.annotate('RETEST!\nEx-Resistance jadi Support\n→ Entry BUY', xy=(9.5, 1.0957),
                xytext=(11, 1.0938),
                arrowprops=dict(arrowstyle='->', color=PURPLE, lw=2),
                color=PURPLE, fontsize=8.5, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a0030', edgecolor=PURPLE))

    ax.axhline(1.0957, color=GREEN, lw=1.5, ls='-', alpha=0.8)
    ax.axhline(1.0938, color=RED, lw=1.5, ls='-', alpha=0.8)
    ax.axhline(1.1022, color=YELLOW, lw=1.5, ls='-', alpha=0.8)
    ax.text(n+0.3, 1.0957, 'ENTRY 1.0957', color=GREEN, fontsize=7.5, va='center', fontweight='bold')
    ax.text(n+0.3, 1.0938, 'SL 1.0938', color=RED, fontsize=7.5, va='center', fontweight='bold')
    ax.text(n+0.3, 1.1022, 'TP 1.1022 (RR 1:3.4)', color=YELLOW, fontsize=7.5, va='center', fontweight='bold')

    ax.set_ylabel('Price (EURUSD)', color=TEXT_COLOR, fontsize=10)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    save(fig, 'snr_role_reversal')


def chart_snr_breakout_retest():
    candles = [
        (2010,2018,2008,2015),(2015,2020,2012,2018),(2018,2022,2016,2020),
        (2020,2024,2018,2022),(2022,2026,2020,2024),
        # Breakout bullish
        (2024,2040,2023,2038),(2038,2045,2036,2043),(2043,2050,2040,2048),
        # Retest ke breakout level
        (2048,2050,2025,2028),(2028,2032,2023,2030),
        # Bounce (entry)
        (2030,2048,2028,2046),(2046,2055,2043,2052),(2052,2060,2050,2058),
    ]
    fig, ax = setup_dark_chart(title="Breakout & Retest — XAUUSD H1\nEntry di Retest setelah Breakout Valid")
    draw_candles(ax, candles)
    n = len(candles)
    ax.set_xlim(-1, n + 3)
    prices = [p for c in candles for p in c]
    ax.set_ylim(min(prices)-6, max(prices)+10)

    brk_level = 2024
    zone_box(ax, 0, 1, brk_level-2, brk_level+4, PURPLE, 0.2)
    ax.text(-0.5, brk_level, f'BREAKOUT ZONE\n{brk_level}', color=PURPLE,
            fontsize=8, va='center', ha='right', fontweight='bold')

    ax.annotate('BREAKOUT!\nCandle besar menembus\nresistance lama', xy=(5.5, 2038),
                xytext=(6.5, 2050),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2),
                color=GREEN, fontsize=8.5, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#0d3d00', edgecolor=GREEN))

    ax.annotate('RETEST!\nHarga kembali ke zona\n→ Entry BUY', xy=(9, 2028),
                xytext=(10.5, 2018),
                arrowprops=dict(arrowstyle='->', color=PURPLE, lw=2),
                color=PURPLE, fontsize=8.5, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a0030', edgecolor=PURPLE))

    ax.axhline(2028, color=GREEN, lw=1.5, ls='-', alpha=0.8)
    ax.axhline(2018, color=RED, lw=1.5, ls='-', alpha=0.8)
    ax.axhline(2058, color=YELLOW, lw=1.5, ls='-', alpha=0.8)
    ax.text(n+0.3, 2028, 'ENTRY 2028', color=GREEN, fontsize=8, va='center', fontweight='bold')
    ax.text(n+0.3, 2018, 'SL 2018', color=RED, fontsize=8, va='center', fontweight='bold')
    ax.text(n+0.3, 2058, 'TP 2058 (RR 1:3)', color=YELLOW, fontsize=8, va='center', fontweight='bold')

    ax.set_ylabel('Price (USD)', color=TEXT_COLOR, fontsize=10)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    save(fig, 'snr_breakout_retest')


# ══════════════════════════════════════════════════════════════
# FUNDAMENTAL CHARTS
# ══════════════════════════════════════════════════════════════

def chart_fundamental_nfp_reaction():
    """NFP miss → Gold rally"""
    # Simplified line chart for NFP reaction
    fig, ax = setup_dark_chart(figsize=(14, 7),
        title="Reaksi NFP Miss — XAUUSD M5\nNFP Actual 100K vs Forecast 180K (USD Melemah → Gold Naik)")

    # Pre-NFP ranging
    pre_nfp = [(i, 2020 + np.sin(i)*2) for i in np.linspace(0, 10, 40)]
    # Initial spike down (confusion)
    spike_down = [(i, 2020 - (i-10)*3) for i in np.linspace(10, 12, 10)]
    # Recovery and rally
    rally = [(i, 2008 + (i-12)*8) for i in np.linspace(12, 20, 40)]
    # Continuation
    cont = [(i, 2072 + np.sin(i)*1.5) for i in np.linspace(20, 28, 20)]

    all_points = pre_nfp + spike_down + rally + cont
    xs = [p[0] for p in all_points]
    ys = [p[1] for p in all_points]

    ax.plot(xs[:40], ys[:40], color=GRAY, lw=2, label='Pre-NFP (Ranging)')
    ax.plot(xs[40:50], ys[40:50], color=RED, lw=2.5, label='Initial Spike ↓ (Confusion)')
    ax.plot(xs[50:90], ys[50:90], color=GREEN, lw=2.5, label='Reversal & Rally ↑')
    ax.plot(xs[90:], ys[90:], color=BLUE, lw=2, label='Continuation')

    # NFP line
    ax.axvline(x=10, color=ORANGE, lw=2, ls='--')
    ax.text(10.2, 2010, '📢 NFP RILIS\n19:30 WIB\nActual: 100K\nForecast: 180K\n→ MISS!',
            color=ORANGE, fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#2d1500', edgecolor=ORANGE))

    ax.axhline(2020, color=GRAY, lw=1, ls=':', alpha=0.5)
    ax.text(0.5, 2021, 'Pre-NFP level: 2020', color=GRAY, fontsize=8)

    ax.annotate('Spike DOWN 8 menit\n(Pasar bingung)', xy=(11, 2008),
                xytext=(13, 2005),
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.5),
                color=RED, fontsize=8.5, fontweight='bold')

    ax.annotate('Entry BUY di sini!\nSetelah spike selesai\n+ candle reversal', xy=(13, 2020),
                xytext=(15, 2015),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2),
                color=GREEN, fontsize=9, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#0d3d00', edgecolor=GREEN))

    ax.text(25, 2072, '+$52 (52 pip)\ndalam 40 menit', color=YELLOW,
            fontsize=10, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#2d2000', edgecolor=YELLOW))

    ax.set_ylabel('XAUUSD Price (USD)', color=TEXT_COLOR, fontsize=10)
    ax.set_xlabel('Waktu (menit)', color=TEXT_COLOR, fontsize=10)
    ax.legend(loc='upper left', facecolor='#161b22', edgecolor=GRID_COLOR,
              labelcolor=TEXT_COLOR, fontsize=8)
    ax.set_ylim(2000, 2082)
    save(fig, 'fundamental_nfp_reaction')


def chart_fundamental_rate_hike():
    """Fed rate hike impact on DXY vs Gold"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 9), facecolor=DARK_BG)
    fig.suptitle('Dampak Fed Rate Hike — DXY vs XAUUSD\nRate Hike → USD Kuat → Gold Turun',
                 color=TEXT_COLOR, fontsize=12, fontweight='bold')

    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    # DXY naik saat hike cycle
    dxy = [96, 97, 98.5, 97, 99, 101, 103, 105, 107, 108, 106, 104]
    # Gold turun
    gold = [1850, 1880, 1960, 1920, 1870, 1840, 1800, 1760, 1720, 1700, 1740, 1780]

    for ax in [ax1, ax2]:
        ax.set_facecolor(DARK_BG)
        ax.grid(True, color=GRID_COLOR, linewidth=0.5, alpha=0.5)
        ax.tick_params(colors=TEXT_COLOR)
        for spine in ax.spines.values():
            spine.set_edgecolor(GRID_COLOR)

    ax1.plot(months, dxy, color=BLUE, lw=2.5, marker='o', markersize=5)
    ax1.fill_between(range(len(months)), dxy, min(dxy)-2, alpha=0.15, color=BLUE)
    ax1.set_title('DXY (Dollar Index)', color=BLUE, fontsize=11, fontweight='bold')
    ax1.set_ylabel('DXY Level', color=TEXT_COLOR)
    ax1.tick_params(axis='x', colors=TEXT_COLOR)

    ax2.plot(months, gold, color=YELLOW, lw=2.5, marker='o', markersize=5)
    ax2.fill_between(range(len(months)), gold, min(gold)-20, alpha=0.15, color=YELLOW)
    ax2.set_title('XAUUSD (Gold)', color=YELLOW, fontsize=11, fontweight='bold')
    ax2.set_ylabel('Price (USD)', color=TEXT_COLOR)
    ax2.tick_params(axis='x', colors=TEXT_COLOR)

    # Rate hike markers
    hike_months = [2, 5, 7, 9]  # Mar, Jun, Aug, Oct
    for hm in hike_months:
        ax1.axvline(x=hm, color=RED, lw=1.5, ls='--', alpha=0.7)
        ax2.axvline(x=hm, color=RED, lw=1.5, ls='--', alpha=0.7)

    ax1.text(2.1, 104, '🔺 Rate Hike\n+0.25%', color=RED, fontsize=7.5, fontweight='bold')
    ax2.text(5.1, 1760, '🔺 Rate Hike\n+0.75%', color=RED, fontsize=7.5, fontweight='bold')

    ax1.annotate('DXY Naik ↑', xy=(9, 108), xytext=(10, 108.5),
                 arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5),
                 color=GREEN, fontsize=9, fontweight='bold')
    ax2.annotate('Gold Turun ↓', xy=(9, 1720), xytext=(10, 1710),
                 arrowprops=dict(arrowstyle='->', color=RED, lw=1.5),
                 color=RED, fontsize=9, fontweight='bold')

    plt.tight_layout()
    save(fig, 'fundamental_rate_hike')


def chart_fundamental_hawkish_dovish():
    """Hawkish vs Dovish impact"""
    fig, ax = setup_dark_chart(figsize=(14, 7),
        title="Hawkish vs Dovish Central Bank\nDampak ke Market (EURUSD Example)")

    x = np.linspace(0, 20, 200)

    # Hawkish scenario (USD kuat, EURUSD turun)
    hawkish = 1.1000 - 0.001 * x + 0.003 * np.sin(x * 1.5)
    # Dovish scenario (USD lemah, EURUSD naik)
    dovish = 1.0800 + 0.002 * x + 0.003 * np.sin(x * 1.5)

    ax.plot(x, hawkish, color=RED, lw=2.5, label='Hawkish (Rate Hike / Taper) → EURUSD Turun')
    ax.plot(x, dovish, color=GREEN, lw=2.5, label='Dovish (Rate Cut / QE) → EURUSD Naik')

    ax.axvline(x=5, color=ORANGE, lw=2, ls='--')
    ax.text(5.2, 1.115, '📢 FOMC\nStatement', color=ORANGE, fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#2d1500', edgecolor=ORANGE))

    ax.text(15, hawkish[150]-0.002, '🦅 HAWKISH\n"We will raise rates\nas needed"',
            color=RED, fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#3d0000', edgecolor=RED))

    ax.text(15, dovish[150]+0.002, '🕊️ DOVISH\n"Cuts appropriate\nin coming months"',
            color=GREEN, fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#0d3d00', edgecolor=GREEN))

    ax.axhline(1.1000, color=GRAY, lw=1, ls=':', alpha=0.5)
    ax.text(0.5, 1.1005, 'Pre-FOMC level', color=GRAY, fontsize=8)

    ax.set_ylabel('EURUSD Price', color=TEXT_COLOR, fontsize=10)
    ax.set_xlabel('Waktu setelah FOMC (jam)', color=TEXT_COLOR, fontsize=10)
    ax.legend(loc='upper center', facecolor='#161b22', edgecolor=GRID_COLOR,
              labelcolor=TEXT_COLOR, fontsize=9)
    ax.set_ylim(1.070, 1.125)
    save(fig, 'fundamental_hawkish_dovish')


def chart_fundamental_intermarket():
    """Intermarket correlation: Gold vs DXY vs Yields"""
    fig, axes = plt.subplots(3, 1, figsize=(14, 10), facecolor=DARK_BG)
    fig.suptitle('Intermarket Analysis — Korelasi Gold, DXY, US10Y Yields\n(Korelasi Negatif: DXY/Yields Naik → Gold Turun)',
                 color=TEXT_COLOR, fontsize=12, fontweight='bold')

    x = np.linspace(0, 12, 100)
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    gold_vals = [1900+50*np.sin(i/2-1) for i in x]
    dxy_vals = [100-5*np.sin(i/2-1) for i in x]
    yield_vals = [4.0-0.5*np.sin(i/2-1) for i in x]

    datasets = [
        (axes[0], gold_vals, YELLOW, 'XAUUSD (Gold)', 'Price (USD)', (1840, 1960)),
        (axes[1], dxy_vals, BLUE, 'DXY (Dollar Index)', 'Level', (94, 106)),
        (axes[2], yield_vals, RED, 'US 10Y Yield', 'Yield (%)', (3.4, 4.7)),
    ]

    for ax, vals, col, title, ylabel, ylim in datasets:
        ax.set_facecolor(DARK_BG)
        ax.grid(True, color=GRID_COLOR, linewidth=0.5, alpha=0.5)
        ax.tick_params(colors=TEXT_COLOR, labelsize=8)
        for spine in ax.spines.values():
            spine.set_edgecolor(GRID_COLOR)
        ax.plot(range(len(months)), vals[::8][:12], color=col, lw=2.5, marker='o', markersize=4)
        ax.fill_between(range(len(months)), vals[::8][:12], min(ylim), alpha=0.12, color=col)
        ax.set_title(title, color=col, fontsize=10, fontweight='bold')
        ax.set_ylabel(ylabel, color=TEXT_COLOR, fontsize=9)
        ax.set_xticks(range(12))
        ax.set_xticklabels(months, color=TEXT_COLOR, fontsize=8)
        ax.set_ylim(*ylim)

    # Highlight correlation
    axes[0].text(0.5, 0.85, '↑ Gold Naik saat DXY & Yields Turun',
                 transform=axes[0].transAxes, color=YELLOW, fontsize=9, fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#2d2000', edgecolor=YELLOW))
    axes[1].text(0.5, 0.1, '↓ DXY Turun = USD Melemah = Gold Naik',
                 transform=axes[1].transAxes, color=BLUE, fontsize=9, fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#0d2b5e', edgecolor=BLUE))
    axes[2].text(0.5, 0.1, '↓ Yields Turun = Bonds Rally = Gold Naik',
                 transform=axes[2].transAxes, color=RED, fontsize=9, fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#3d0000', edgecolor=RED))

    plt.tight_layout()
    save(fig, 'fundamental_intermarket')


# ══════════════════════════════════════════════════════════════
# CANDLESTICK FOUNDATION CHARTS
# ══════════════════════════════════════════════════════════════

def chart_candlestick_anatomy():
    fig, ax = setup_dark_chart(figsize=(10, 7),
        title="Anatomi Candlestick\nBullish vs Bearish")

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Bullish candle
    ax.add_patch(plt.Rectangle((1.5, 3), 1, 4, color=GREEN, zorder=3))
    ax.plot([2, 2], [0.5, 3], color=GREEN, lw=2)   # lower wick
    ax.plot([2, 2], [7, 9.5], color=GREEN, lw=2)   # upper wick

    # Labels bullish
    ax.annotate('HIGH', xy=(2, 9.5), xytext=(3.5, 9.5),
                arrowprops=dict(arrowstyle='->', color=TEXT_COLOR, lw=1.2),
                color=TEXT_COLOR, fontsize=10, fontweight='bold')
    ax.annotate('CLOSE', xy=(2.5, 7), xytext=(3.5, 7.2),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.2),
                color=GREEN, fontsize=10, fontweight='bold')
    ax.text(3.5, 5, 'BODY\n(Close > Open\n= Bullish)',
            color=GREEN, fontsize=9, fontweight='bold', va='center')
    ax.annotate('OPEN', xy=(2.5, 3), xytext=(3.5, 2.8),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.2),
                color=GREEN, fontsize=10, fontweight='bold')
    ax.annotate('LOW', xy=(2, 0.5), xytext=(3.5, 0.5),
                arrowprops=dict(arrowstyle='->', color=TEXT_COLOR, lw=1.2),
                color=TEXT_COLOR, fontsize=10, fontweight='bold')
    ax.text(1.5, -0.3, 'BULLISH', color=GREEN, fontsize=11,
            fontweight='bold', ha='center')

    # Bearish candle
    ax.add_patch(plt.Rectangle((6.5, 3), 1, 4, color=RED, zorder=3))
    ax.plot([7, 7], [0.5, 3], color=RED, lw=2)
    ax.plot([7, 7], [7, 9.5], color=RED, lw=2)

    ax.annotate('HIGH', xy=(7, 9.5), xytext=(5, 9.5),
                arrowprops=dict(arrowstyle='->', color=TEXT_COLOR, lw=1.2),
                color=TEXT_COLOR, fontsize=10, fontweight='bold', ha='right')
    ax.annotate('OPEN', xy=(6.5, 7), xytext=(4.8, 7.2),
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.2),
                color=RED, fontsize=10, fontweight='bold', ha='right')
    ax.text(4.5, 5, 'BODY\n(Open > Close\n= Bearish)',
            color=RED, fontsize=9, fontweight='bold', va='center', ha='right')
    ax.annotate('CLOSE', xy=(6.5, 3), xytext=(4.8, 2.8),
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.2),
                color=RED, fontsize=10, fontweight='bold', ha='right')
    ax.annotate('LOW', xy=(7, 0.5), xytext=(5, 0.5),
                arrowprops=dict(arrowstyle='->', color=TEXT_COLOR, lw=1.2),
                color=TEXT_COLOR, fontsize=10, fontweight='bold', ha='right')
    ax.text(7, -0.3, 'BEARISH', color=RED, fontsize=11,
            fontweight='bold', ha='center')

    # Upper & lower wick labels
    ax.text(5, 8.5, '← Upper Wick / Shadow →', color=GRAY,
            fontsize=8.5, ha='center')
    ax.text(5, 1.2, '← Lower Wick / Shadow →', color=GRAY,
            fontsize=8.5, ha='center')

    save(fig, 'candlestick_anatomy')


def chart_candlestick_patterns():
    fig, ax = setup_dark_chart(figsize=(16, 7),
        title="Pola Candlestick Penting dalam Trading\n(dengan Interpretasi)")

    patterns = [
        # (x_center, candle data [(o_rel, h_rel, l_rel, c_rel)], name, color, desc)
        (1,   [(0.3, 0.9, 0.05, 0.85)], 'Hammer\n(Bullish)', GREEN, 'Rejection kuat\ndi bawah'),
        (2.5, [(0.7, 0.95, 0.1, 0.15)], 'Shooting Star\n(Bearish)', RED, 'Rejection kuat\ndi atas'),
        (4,   [(0.6, 0.65, 0.35, 0.4),(0.35, 0.9, 0.3, 0.85)], 'Bullish\nEngulfing', GREEN, 'Pembalikan\nbullish kuat'),
        (5.8, [(0.4, 0.65, 0.35, 0.6),(0.65, 0.7, 0.1, 0.15)], 'Bearish\nEngulfing', RED, 'Pembalikan\nbearish kuat'),
        (7.5, [(0.5, 0.55, 0.45, 0.5)], 'Doji\n(Ragu)', GRAY, 'Ketidak-\npastian'),
        (9,   [(0.1, 0.95, 0.05, 0.9)], 'Bullish\nMarubozu', GREEN, 'Momentum\nkuat naik'),
        (10.5,[(0.9, 0.95, 0.05, 0.1)], 'Bearish\nMarubozu', RED, 'Momentum\nkuat turun'),
        (12,  [(0.6, 0.65, 0.35, 0.4),(0.5, 0.55, 0.45, 0.5),(0.4, 0.9, 0.35, 0.85)], 'Morning Star\n(Bullish Rev.)', GREEN, '3-candle\nbullish rev.'),
    ]

    ax.set_xlim(0, 14)
    ax.set_ylim(-0.5, 1.6)
    ax.axis('off')

    for xc, cands, name, col, desc in patterns:
        width = 0.3
        for ci, (o, h, l, c) in enumerate(cands):
            x = xc + ci * (width + 0.05)
            cc = col if c >= o else RED if col == GREEN else GREEN
            if name.startswith('Bullish Eng') or name.startswith('Bearish Eng') or name.startswith('Morning'):
                cc = GREEN if c >= o else RED
            ax.add_patch(plt.Rectangle((x - width/2, min(o,c)), width, abs(c-o) or 0.02,
                                       color=cc, zorder=3))
            ax.plot([x, x], [l, min(o,c)], color=cc, lw=1.5)
            ax.plot([x, x], [max(o,c), h], color=cc, lw=1.5)

        mid_x = xc + (len(cands)-1) * (width+0.05) / 2
        ax.text(mid_x, -0.12, name, color=col, fontsize=7.5, ha='center',
                fontweight='bold', va='top')
        ax.text(mid_x, -0.32, desc, color=GRAY, fontsize=6.5, ha='center', va='top')

    ax.text(7, 1.55, 'Bullish Patterns', color=GREEN, fontsize=10,
            fontweight='bold', ha='center')
    ax.text(7, 1.45, '(Konfirmasi di Support / Order Block)', color=GRAY,
            fontsize=8, ha='center')

    save(fig, 'candlestick_patterns')


# ══════════════════════════════════════════════════════════════
# MARKET STRUCTURE CHARTS
# ══════════════════════════════════════════════════════════════

def chart_market_structure_trend():
    fig, axes = plt.subplots(1, 3, figsize=(18, 6), facecolor=DARK_BG)
    fig.suptitle('Jenis Trend — Uptrend, Downtrend, Sideways\nMembaca Struktur Market dengan Benar',
                 color=TEXT_COLOR, fontsize=12, fontweight='bold')

    # Uptrend
    up_candles = [
        (100,106,98,104),(104,110,102,108),(108,112,106,110),
        (110,115,108,106),(106,112,104,110),(110,118,108,116),
        (116,120,114,118),(118,122,116,120),
    ]
    # Downtrend
    down_candles = [
        (120,122,116,118),(118,120,112,114),(114,116,108,110),
        (110,114,108,112),(112,115,106,108),(108,110,102,104),
        (104,106,100,102),(102,104,96,98),
    ]
    # Sideways
    side_candles = [
        (108,114,106,112),(112,115,108,110),(110,114,106,108),
        (108,116,106,114),(114,116,108,110),(110,114,106,112),
        (112,116,108,110),(110,114,107,112),
    ]

    configs = [
        (up_candles, 'UPTREND ↑', GREEN, 'Higher High (HH)\nHigher Low (HL)',
         [(1,112,'HH1'),(3,106,'HL1'),(5,118,'HH2'),(7,116,'HL2')]),
        (down_candles, 'DOWNTREND ↓', RED, 'Lower High (LH)\nLower Low (LL)',
         [(1,118,'LH1'),(3,108,'LL1'),(5,110,'LH2'),(7,98,'LL2')]),
        (side_candles, 'SIDEWAYS ↔', GRAY, 'No clear HH/HL\nor LH/LL',
         []),
    ]

    for ax, (candles, title, col, desc, labels) in zip(axes, configs):
        ax.set_facecolor(DARK_BG)
        ax.grid(True, color=GRID_COLOR, linewidth=0.5, alpha=0.5)
        ax.tick_params(colors=TEXT_COLOR, labelsize=8)
        for spine in ax.spines.values():
            spine.set_edgecolor(GRID_COLOR)
        ax.set_title(title, color=col, fontsize=12, fontweight='bold', pad=8)
        draw_candles(ax, candles)
        n = len(candles)
        ax.set_xlim(-1, n + 1)
        prices = [p for c in candles for p in c]
        ax.set_ylim(min(prices)-5, max(prices)+10)
        ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)

        for xi, yi, lbl in labels:
            ax.text(xi+0.3, yi+1, lbl, color=col, fontsize=8, fontweight='bold')

        ax.text(0.5, 0.05, desc, transform=ax.transAxes,
                color=col, fontsize=9, fontweight='bold', ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=DARK_BG,
                           edgecolor=col, alpha=0.9))

        if title == 'SIDEWAYS ↔':
            prices_all = [p for c in candles for p in c]
            top = max(prices_all) - 1
            bot = min(prices_all) + 1
            ax.axhline(top, color=RED, lw=1.5, ls='--', alpha=0.7)
            ax.axhline(bot, color=GREEN, lw=1.5, ls='--', alpha=0.7)
            ax.text(n-1, top+0.5, 'Resistance', color=RED, fontsize=7.5)
            ax.text(n-1, bot-1.5, 'Support', color=GREEN, fontsize=7.5)

    plt.tight_layout()
    save(fig, 'market_structure_trend')


def chart_swing_points():
    candles = [
        (100,108,98,105),(105,112,103,110),(110,118,108,115),
        (115,120,110,112),(112,116,105,107),(107,111,104,109),
        (109,118,107,116),(116,124,114,121),(121,126,118,120),
        (120,122,112,114),(114,118,110,112),(112,116,108,114),
        (114,122,112,120),(120,128,118,125),(125,130,122,128),
    ]
    fig, ax = setup_dark_chart(title="Swing High & Swing Low — Cara Identifikasi\n(Minimal 2 Candle Kiri + 2 Candle Kanan)")
    draw_candles(ax, candles)
    n = len(candles)
    ax.set_xlim(-1, n + 2)
    prices = [p for c in candles for p in c]
    ax.set_ylim(min(prices)-5, max(prices)+12)

    # Mark swing points
    swing_highs = [(2, candles[2][1], 'SH1'), (7, candles[7][1], 'SH2'), (13, candles[13][1], 'SH3')]
    swing_lows  = [(0, candles[0][2], 'SL1'), (5, candles[5][2], 'SL2'), (10, candles[10][2], 'SL3')]

    for xi, yi, lbl in swing_highs:
        ax.annotate(f'▲ {lbl}', xy=(xi, yi), xytext=(xi, yi+3),
                    arrowprops=dict(arrowstyle='-', color=BLUE, lw=1),
                    color=BLUE, fontsize=9, fontweight='bold', ha='center')

    for xi, yi, lbl in swing_lows:
        ax.annotate(f'▼ {lbl}', xy=(xi, yi), xytext=(xi, yi-4),
                    arrowprops=dict(arrowstyle='-', color=ORANGE, lw=1),
                    color=ORANGE, fontsize=9, fontweight='bold', ha='center')

    # HH/HL annotations
    ax.text(7.5, candles[7][1]+4, 'HH', color=GREEN, fontsize=10, fontweight='bold')
    ax.text(5.5, candles[5][2]-5, 'HL', color=GREEN, fontsize=10, fontweight='bold')
    ax.text(13.5, candles[13][1]+4, 'HH', color=GREEN, fontsize=10, fontweight='bold')
    ax.text(10.5, candles[10][2]-5, 'HL', color=GREEN, fontsize=10, fontweight='bold')

    ax.text(1, 132, '← Uptrend: HH + HL berulang', color=GREEN,
            fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#0d3d00', edgecolor=GREEN))

    ax.set_ylabel('Price', color=TEXT_COLOR, fontsize=10)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    save(fig, 'swing_points')


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print("Generating trading charts...")
    print()

    print("── SMC-ICT Charts ──")
    chart_bos_bullish()
    chart_bos_bearish()
    chart_choch()
    chart_order_block_bullish()
    chart_order_block_bearish()
    chart_fvg()
    chart_liquidity_sweep()
    chart_cisd()
    chart_multi_timeframe()

    print()
    print("── SnR Charts ──")
    chart_snr_support_bounce()
    chart_snr_resistance_rejection()
    chart_snr_role_reversal()
    chart_snr_breakout_retest()

    print()
    print("── Fundamental Charts ──")
    chart_fundamental_nfp_reaction()
    chart_fundamental_rate_hike()
    chart_fundamental_hawkish_dovish()
    chart_fundamental_intermarket()

    print()
    print("── Foundation Charts ──")
    chart_candlestick_anatomy()
    chart_candlestick_patterns()
    chart_market_structure_trend()
    chart_swing_points()

    print()
    print(f"✅ Semua chart tersimpan di: {OUTPUT_DIR}/")
    print(f"   Total: 22 chart")


# ══════════════════════════════════════════════════════════════
# FOUNDATION — ADDITIONAL CHARTS (XAUUSD)
# ══════════════════════════════════════════════════════════════

def chart_candle_types():
    """Jenis-jenis candle dengan label"""
    fig, ax = setup_dark_chart(figsize=(16, 7), title="Jenis-Jenis Candlestick — XAUUSD\nDari Marubozu sampai Doji")
    ax.set_xlim(0, 17)
    ax.set_ylim(0, 11)
    ax.axis('off')

    types = [
        # (x, o_rel, h_rel, l_rel, c_rel, name, color, desc)
        (1,   0.1, 0.9, 0.1, 0.9, 'Bullish\nMarubozu', GREEN,  'Momentum\nbullish penuh'),
        (2.5, 0.9, 0.9, 0.1, 0.1, 'Bearish\nMarubozu', RED,    'Momentum\nbearish penuh'),
        (4,   0.3, 0.92,0.05,0.88,'Hammer',             GREEN,  'Rejection\nbawah kuat'),
        (5.5, 0.7, 0.95,0.12,0.15,'Shooting\nStar',     RED,    'Rejection\natas kuat'),
        (7,   0.2, 0.88,0.08,0.82,'Inverted\nHammer',   GREEN,  'Potensi\nbullish rev.'),
        (8.5, 0.8, 0.92,0.18,0.22,'Hanging\nMan',       RED,    'Potensi\nbearish rev.'),
        (10,  0.5, 0.55,0.45,0.50,'Doji',               GRAY,   'Ketidak-\npastian'),
        (11.5,0.5, 0.92,0.08,0.50,'Long-Legged\nDoji',  GRAY,   'Konflik\nextreme'),
        (13,  0.5, 0.52,0.08,0.50,'Dragonfly\nDoji',    GREEN,  'Reversal\nbullish'),
        (14.5,0.5, 0.92,0.48,0.50,'Gravestone\nDoji',   RED,    'Reversal\nbearish'),
        (16,  0.4, 0.75,0.25,0.6, 'Spinning\nTop',      GRAY,   'Ragu, arah\ntidak jelas'),
    ]

    for xc, o, h, l, c, name, col, desc in types:
        w = 0.35
        body_bot = min(o, c); body_h = abs(c - o) or 0.04
        ax.add_patch(plt.Rectangle((xc - w/2, body_bot*9+0.5), w, body_h*9,
                                   color=col, zorder=3))
        ax.plot([xc, xc], [l*9+0.5, body_bot*9+0.5], color=col, lw=1.5)
        ax.plot([xc, xc], [(body_bot+body_h)*9+0.5, h*9+0.5], color=col, lw=1.5)
        ax.text(xc, -0.15, name, color=col, fontsize=7, ha='center',
                fontweight='bold', va='top')
        ax.text(xc, -0.75, desc, color=GRAY, fontsize=6, ha='center', va='top')

    save(fig, 'candle_types')


def chart_two_candle_patterns():
    """Pola dua candle"""
    fig, ax = setup_dark_chart(figsize=(16, 7), title="Pola Dua Candle Penting — XAUUSD\nKonfirmasi di Support/Resistance/OB")
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 11)
    ax.axis('off')

    patterns = [
        ('Bullish\nEngulfing', GREEN, [(0.7,0.75,0.6,0.65),(0.55,0.95,0.5,0.92)],
         'Candle bullish\nmencakup seluruh\ncandle bearish'),
        ('Bearish\nEngulfing', RED,   [(0.3,0.4,0.25,0.35),(0.4,0.45,0.08,0.12)],
         'Candle bearish\nmencakup seluruh\ncandle bullish'),
        ('Bullish\nHarami',   GREEN, [(0.8,0.85,0.2,0.25),(0.35,0.65,0.3,0.6)],
         'Candle kecil\nbullish dalam\nbody bearish besar'),
        ('Bearish\nHarami',   RED,   [(0.2,0.8,0.15,0.75),(0.35,0.65,0.4,0.45)],
         'Candle kecil\nbearish dalam\nbody bullish besar'),
        ('Tweezer\nBottom',   GREEN, [(0.65,0.7,0.1,0.62),(0.1,0.7,0.1,0.65)],
         'Low sama persis\n→ support kuat\n= potensi naik'),
        ('Tweezer\nTop',      RED,   [(0.3,0.92,0.28,0.88),(0.88,0.92,0.3,0.32)],
         'High sama persis\n→ resistance kuat\n= potensi turun'),
    ]

    xstart = 1
    for name, col, cands, desc in patterns:
        for ci, (o, h, l, c) in enumerate(cands):
            x = xstart + ci * 0.9
            cc = GREEN if c >= o else RED
            body_bot = min(o,c); body_h = abs(c-o) or 0.04
            ax.add_patch(plt.Rectangle((x-0.35, body_bot*8+1), 0.7, body_h*8,
                                       color=cc, zorder=3))
            ax.plot([x,x],[l*8+1, body_bot*8+1], color=cc, lw=1.5)
            ax.plot([x,x],[(body_bot+body_h)*8+1, h*8+1], color=cc, lw=1.5)
        mid = xstart + 0.45
        ax.text(mid, 0.3, name, color=col, fontsize=7.5,
                ha='center', fontweight='bold', va='top')
        ax.text(mid, -0.35, desc, color=GRAY, fontsize=6,
                ha='center', va='top')
        # Divider
        ax.axvline(xstart-0.4, color=GRID_COLOR, lw=0.5, alpha=0.5)
        xstart += 2.4

    save(fig, 'two_candle_patterns')


def chart_three_candle_patterns():
    """Morning Star, Evening Star, Three Soldiers/Crows"""
    fig, ax = setup_dark_chart(figsize=(16, 7), title="Pola Tiga Candle — XAUUSD\nSignal Pembalikan Kuat")
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 11)
    ax.axis('off')

    patterns = [
        ('Morning Star\n(Bullish Reversal)', GREEN,
         [(0.8,0.85,0.2,0.25),(0.28,0.36,0.22,0.32),(0.2,0.85,0.18,0.8)],
         'Candle bearish\nbesar → Doji/kecil\n→ Bullish besar'),
        ('Evening Star\n(Bearish Reversal)', RED,
         [(0.2,0.82,0.18,0.78),(0.74,0.82,0.68,0.76),(0.8,0.82,0.18,0.22)],
         'Candle bullish\nbesar → Doji/kecil\n→ Bearish besar'),
        ('Three White\nSoldiers', GREEN,
         [(0.3,0.65,0.28,0.62),(0.55,0.75,0.53,0.72),(0.7,0.92,0.68,0.90)],
         '3 candle bullish\nberturut, close\nmakin tinggi'),
        ('Three Black\nCrows', RED,
         [(0.72,0.74,0.38,0.40),(0.42,0.44,0.22,0.24),(0.26,0.28,0.08,0.10)],
         '3 candle bearish\nberturut, close\nmakin rendah'),
    ]

    xstart = 0.8
    for name, col, cands, desc in patterns:
        for ci, (o, h, l, c) in enumerate(cands):
            x = xstart + ci * 1.05
            cc = GREEN if c >= o else RED
            body_bot = min(o,c); body_h = abs(c-o) or 0.03
            ax.add_patch(plt.Rectangle((x-0.4, body_bot*8.5+0.5), 0.8, body_h*8.5,
                                       color=cc, zorder=3))
            ax.plot([x,x],[l*8.5+0.5, body_bot*8.5+0.5], color=cc, lw=1.5)
            ax.plot([x,x],[(body_bot+body_h)*8.5+0.5, h*8.5+0.5], color=cc, lw=1.5)
        mid = xstart + 1.05
        ax.text(mid, 0.2, name, color=col, fontsize=7.5,
                ha='center', fontweight='bold', va='top')
        ax.text(mid, -0.45, desc, color=GRAY, fontsize=6,
                ha='center', va='top')
        ax.axvline(xstart-0.6, color=GRID_COLOR, lw=0.5, alpha=0.5)
        xstart += 3.7

    save(fig, 'three_candle_patterns')


def chart_candle_in_context():
    """Candle yang sama, konteks berbeda — artinya beda"""
    candles = [
        (2040,2048,2025,2043),(2043,2050,2038,2046),(2046,2052,2032,2034),
        # Hammer di support (bullish)
        (2034,2036,2018,2035),
        (2035,2048,2033,2046),(2046,2055,2043,2052),
        # Shooting star di resistance (bearish)
        (2052,2072,2050,2053),
        (2053,2056,2038,2040),(2040,2042,2028,2030),
    ]
    fig, ax = setup_dark_chart(title="Konteks Menentukan Makna Candle — XAUUSD H1\nCandle yang Sama Bisa Berbeda Arti")
    draw_candles(ax, candles)
    n = len(candles)
    ax.set_xlim(-1, n+3)
    prices = [p for c in candles for p in c]
    ax.set_ylim(min(prices)-8, max(prices)+14)

    # Support zone
    zone_box(ax, 0.2, 0.55, 2018, 2028, GREEN, 0.15)
    ax.text(1.5, 2013, 'SUPPORT ZONE', color=GREEN, fontsize=8,
            ha='center', fontweight='bold')
    ax.annotate('Hammer di Support\n→ BULLISH SIGNAL ✓\n(Harga ditolak dari bawah)', xy=(3.5, 2018),
                xytext=(5, 2012),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.8),
                color=GREEN, fontsize=8.5, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#0d3d00', edgecolor=GREEN))

    # Resistance zone
    zone_box(ax, 0.6, 0.95, 2060, 2074, RED, 0.15)
    ax.text(7.5, 2077, 'RESISTANCE ZONE', color=RED, fontsize=8,
            ha='center', fontweight='bold')
    ax.annotate('Shooting Star di Resistance\n→ BEARISH SIGNAL ✓\n(Harga ditolak dari atas)', xy=(6.5, 2072),
                xytext=(8, 2078),
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.8),
                color=RED, fontsize=8.5, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#3d0000', edgecolor=RED))

    ax.text(n/2, max(prices)+10, '⚠ Candle tanpa konteks zona = sinyal palsu!',
            color=YELLOW, fontsize=9, fontweight='bold', ha='center',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#2d2000', edgecolor=YELLOW))

    ax.set_ylabel('Price (USD)', color=TEXT_COLOR, fontsize=10)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    save(fig, 'candle_in_context')


def chart_wick_analysis():
    """Analisis wick — apa yang diceritakan"""
    candles = [
        (2030,2060,2028,2032), # Long upper wick = rejection atas
        (2040,2042,2012,2038), # Long lower wick = rejection bawah
        (2038,2055,2010,2052), # Kedua wick panjang = konflik
        (2030,2032,2028,2031), # Doji = keseimbangan
        (2025,2060,2023,2058), # Bullish strong, sedikit upper wick
        (2058,2060,2025,2027), # Bearish strong, sedikit lower wick
    ]
    fig, ax = setup_dark_chart(title="Analisis Wick — XAUUSD\nApa yang Diceritakan Setiap Wick")
    draw_candles(ax, candles)
    n = len(candles)
    ax.set_xlim(-1, n+4)
    prices = [p for c in candles for p in c]
    ax.set_ylim(min(prices)-8, max(prices)+20)

    annotations = [
        (0, candles[0][1]+2, 'Upper wick panjang\n→ Seller menolak harga tinggi\n→ Bearish pressure', RED, 1, 0),
        (1, candles[1][2]-3, 'Lower wick panjang\n→ Buyer menolak harga rendah\n→ Bullish pressure', GREEN, -1, 1),
        (2, candles[2][1]+2, 'Kedua wick panjang\n→ Konflik keras\n→ Tidak ada pemenang', ORANGE, 1, 2),
        (3, (candles[3][0]+candles[3][3])/2, 'Doji (body mini)\n→ Open ≈ Close\n→ Keseimbangan penuh', GRAY, 1, 3),
        (4, candles[4][1]+2, 'Upper wick kecil\n→ Bullish kuat\n(sedikit profit taking)', GREEN, 1, 4),
        (5, candles[5][2]-3, 'Lower wick kecil\n→ Bearish kuat\n(sedikit buying)', RED, -1, 5),
    ]
    offsets = [(n+0.5,2068),(n+0.5,2008),(n+1,2075),(n+0.5,2030),(n+0.5,2068),(n+0.5,2010)]
    for i, (xi, yi, txt, col, direction, idx) in enumerate(annotations):
        tx, ty = offsets[i]
        ax.annotate(txt, xy=(xi, yi), xytext=(tx, ty),
                    arrowprops=dict(arrowstyle='->', color=col, lw=1.3),
                    color=col, fontsize=7.5, fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.25', facecolor=DARK_BG, edgecolor=col, alpha=0.9))

    ax.set_ylabel('Price (USD)', color=TEXT_COLOR, fontsize=10)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    save(fig, 'wick_analysis')


def chart_impulse_corrective():
    """Impulse vs Corrective wave dalam uptrend — XAUUSD"""
    candles = [
        # Impulse 1
        (1980,1990,1978,1988),(1988,2000,1986,1998),(1998,2012,1996,2010),
        (2010,2018,2008,2016),(2016,2025,2014,2022),
        # Corrective 1
        (2022,2024,2010,2012),(2012,2015,2008,2010),(2010,2013,2006,2011),
        # Impulse 2
        (2011,2022,2009,2020),(2020,2032,2018,2030),(2030,2042,2028,2040),
        (2040,2052,2038,2050),(2050,2058,2048,2056),
        # Corrective 2
        (2056,2058,2038,2040),(2040,2044,2036,2038),(2038,2040,2034,2039),
        # Impulse 3
        (2039,2052,2037,2050),(2050,2062,2048,2060),(2060,2072,2058,2070),
    ]
    fig, ax = setup_dark_chart(title="Impulse vs Corrective Wave — XAUUSD H4\nStruktur Gelombang dalam Uptrend")
    draw_candles(ax, candles)
    n = len(candles)
    ax.set_xlim(-1, n+3)
    prices = [p for c in candles for p in c]
    ax.set_ylim(min(prices)-8, max(prices)+14)

    # Impulse zones
    for x0, x1, label in [(0,4,'Impulse 1'),(8,12,'Impulse 2'),(16,18,'Impulse 3')]:
        zone_box(ax, x0/n, x1/n, min(prices)-5, max(prices)+10, GREEN, 0.07)
        ax.text((x0+x1)/2, max(prices)+8, label, color=GREEN,
                fontsize=8, ha='center', fontweight='bold')

    # Corrective zones
    for x0, x1, label in [(5,7,'Correction 1'),(13,15,'Correction 2')]:
        zone_box(ax, x0/n, x1/n, min(prices)-5, max(prices)+10, RED, 0.1)
        ax.text((x0+x1)/2, max(prices)+8, label, color=RED,
                fontsize=8, ha='center', fontweight='bold')

    # HL labels
    ax.text(5.5, candles[7][2]-3, 'HL', color=GREEN, fontsize=10, fontweight='bold', ha='center')
    ax.text(13.5, candles[15][2]-3, 'HL', color=GREEN, fontsize=10, fontweight='bold', ha='center')

    ax.annotate('Koreksi normal:\n38-61% dari impulse\n→ Cari entry di sini!', xy=(6, 2010),
                xytext=(9, 1998),
                arrowprops=dict(arrowstyle='->', color=YELLOW, lw=1.8),
                color=YELLOW, fontsize=8.5, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#2d2000', edgecolor=YELLOW))

    ax.set_ylabel('XAUUSD Price (USD)', color=TEXT_COLOR, fontsize=10)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    save(fig, 'impulse_corrective')


def chart_premium_discount():
    """Premium vs Discount zone — XAUUSD"""
    candles = [
        # Swing Low
        (1990,1998,1986,1994),
        # Rally ke Swing High
        (1994,2005,1992,2003),(2003,2015,2001,2012),(2012,2022,2010,2020),
        (2020,2030,2018,2028),(2028,2038,2026,2035),(2035,2042,2033,2040),
        # Swing High, lalu pullback
        (2040,2045,2038,2043),
        (2043,2046,2028,2030),(2030,2033,2025,2031),(2031,2034,2022,2032),
    ]
    fig, ax = setup_dark_chart(title="Premium vs Discount Zone — XAUUSD H4\nOTE (Optimal Trade Entry) di Discount Zone")
    draw_candles(ax, candles)
    n = len(candles)
    ax.set_xlim(-1, n+3)
    prices = [p for c in candles for p in c]
    ax.set_ylim(min(prices)-6, max(prices)+10)

    swing_low = 1986
    swing_high = 2045
    mid = (swing_low + swing_high) / 2  # 50% = 2015.5
    ote_top = swing_low + (swing_high - swing_low) * 0.62  # ~2033
    ote_bot = swing_low + (swing_high - swing_low) * 0.38  # ~2021

    # Premium zone (atas 50%)
    ax.axhspan(mid, swing_high, alpha=0.08, color=RED)
    ax.text(n+0.5, (mid+swing_high)/2, 'PREMIUM\nZone\n(Sell area)', color=RED,
            fontsize=8, va='center', fontweight='bold')

    # Discount zone (bawah 50%)
    ax.axhspan(swing_low, mid, alpha=0.08, color=GREEN)
    ax.text(n+0.5, (swing_low+mid)/2, 'DISCOUNT\nZone\n(Buy area)', color=GREEN,
            fontsize=8, va='center', fontweight='bold')

    # 50% line
    ax.axhline(mid, color=YELLOW, lw=1.5, ls='-.', alpha=0.8)
    ax.text(-0.5, mid, f'50% Equilibrium\n{mid:.0f}', color=YELLOW,
            fontsize=8, va='center', ha='right', fontweight='bold')

    # OTE zone
    zone_box(ax, 0.7, 1, ote_bot, ote_top, PURPLE, 0.3)
    ax.text(n+0.5, (ote_bot+ote_top)/2, f'OTE Zone\n62–79%\n{ote_bot:.0f}–{ote_top:.0f}',
            color=PURPLE, fontsize=8, va='center', fontweight='bold')

    # Swing points
    ax.axhline(swing_high, color=RED, lw=1, ls=':', alpha=0.6)
    ax.axhline(swing_low, color=GREEN, lw=1, ls=':', alpha=0.6)
    ax.text(-0.5, swing_high, f'Swing High {swing_high}', color=RED, fontsize=7.5, va='center', ha='right')
    ax.text(-0.5, swing_low, f'Swing Low {swing_low}', color=GREEN, fontsize=7.5, va='center', ha='right')

    ax.annotate('Harga pullback ke\nOTE (Discount Zone)\n→ Entry BUY!', xy=(9.5, 2025),
                xytext=(10.5, 2012),
                arrowprops=dict(arrowstyle='->', color=PURPLE, lw=1.8),
                color=PURPLE, fontsize=8.5, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a0030', edgecolor=PURPLE))

    ax.set_ylabel('XAUUSD Price (USD)', color=TEXT_COLOR, fontsize=10)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    save(fig, 'premium_discount')


def chart_key_levels_xauusd():
    """Key levels di XAUUSD"""
    candles = [
        (1990,2002,1988,1998),(1998,2010,1996,2008),(2008,2018,2006,2015),
        (2015,2020,2005,2007),(2007,2012,2004,2010),(2010,2022,2008,2020),
        (2020,2032,2018,2030),(2030,2038,2025,2027),(2027,2032,2022,2030),
        (2030,2048,2028,2045),(2045,2052,2040,2043),(2043,2048,2038,2046),
        (2046,2055,2043,2048),
    ]
    fig, ax = setup_dark_chart(title="Key Levels — XAUUSD H4\nLevel yang Wajib Ditandai setiap Minggu")
    draw_candles(ax, candles)
    n = len(candles)
    ax.set_xlim(-1, n+3)
    prices = [p for c in candles for p in c]
    ax.set_ylim(min(prices)-10, max(prices)+14)

    levels = [
        (2000, PURPLE, 'Round Number 2000 (Psikologis)', '--'),
        (2050, PURPLE, 'Round Number 2050 (Psikologis)', '--'),
        (2020, BLUE,   'Previous Week Low (PWL)', '-.'),
        (2048, ORANGE, 'Previous Week High (PWH)', '-.'),
        (2007, RED,    'Equal Low (EQL) — SSL', ':'),
        (2045, GREEN,  'Swing High terbaru', ':'),
    ]

    for price, col, label, ls in levels:
        ax.axhline(price, color=col, lw=1.5, ls=ls, alpha=0.8, zorder=4)
        ax.text(n+0.3, price, label, color=col, fontsize=7.5, va='center', fontweight='bold')

    ax.text(1, max(prices)+10,
            'Tandai level ini setiap awal minggu sebelum trading!',
            color=YELLOW, fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#2d2000', edgecolor=YELLOW))

    ax.set_ylabel('XAUUSD Price (USD)', color=TEXT_COLOR, fontsize=10)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    save(fig, 'key_levels_xauusd')


def chart_mtf_structure():
    """HTF structure menampung LTF pullback — XAUUSD"""
    fig, axes = plt.subplots(1, 2, figsize=(16, 7), facecolor=DARK_BG)
    fig.suptitle('HTF Structure Menampung LTF Pullback — XAUUSD\nD1 Uptrend → H4 Koreksi → H4 Entry Zone',
                 color=TEXT_COLOR, fontsize=12, fontweight='bold')

    # D1 view - uptrend besar
    d1_candles = [
        (1950,1968,1948,1962),(1962,1978,1960,1975),(1975,1990,1973,1988),
        (1988,1998,1980,1985),(1985,1992,1978,1990),(1990,2005,1988,2002),
        (2002,2018,2000,2015),(2015,2028,2012,2025),(2025,2040,2022,2038),
    ]
    # H4 view - pullback dalam D1 uptrend
    h4_candles = [
        (2038,2045,2036,2042),(2042,2048,2038,2040),(2040,2042,2030,2032),
        (2032,2035,2025,2027),(2027,2030,2022,2028),(2028,2038,2026,2036),
        (2036,2048,2034,2046),(2046,2055,2043,2052),
    ]

    for ax, candles, title, note in [
        (axes[0], d1_candles, 'D1 — Uptrend Besar (Bias: BULLISH)',
         'HH + HL terus terbentuk\n→ Bias D1: BUY ONLY'),
        (axes[1], h4_candles, 'H4 — Pullback dalam Uptrend D1\n(Cari Entry BUY di sini)',
         'H4 koreksi ke OB/FVG\n→ Entry BUY sesuai bias D1'),
    ]:
        ax.set_facecolor(DARK_BG)
        ax.grid(True, color=GRID_COLOR, linewidth=0.5, alpha=0.5)
        ax.tick_params(colors=TEXT_COLOR)
        for spine in ax.spines.values():
            spine.set_edgecolor(GRID_COLOR)
        ax.set_title(title, color=TEXT_COLOR, fontsize=10, fontweight='bold', pad=8)
        draw_candles(ax, candles)
        n = len(candles)
        ax.set_xlim(-1, n+2)
        prices = [p for c in candles for p in c]
        ax.set_ylim(min(prices)-8, max(prices)+14)
        ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
        ax.text(0.5, 0.06, note, transform=ax.transAxes,
                color=YELLOW, fontsize=8.5, fontweight='bold', ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#2d2000', edgecolor=YELLOW))
        ax.set_ylabel('XAUUSD (USD)', color=TEXT_COLOR, fontsize=9)

    # H4: annotate OB zone
    ob_top, ob_bot = 2030, 2022
    zone_box(axes[1], 2.5/8, 6/8, ob_bot, ob_top, GREEN, 0.25)
    axes[1].text(3.5, (ob_top+ob_bot)/2, 'OB Bullish H4\n(Entry Zone)', color=GREEN,
                 fontsize=8, ha='center', va='center', fontweight='bold')

    plt.tight_layout()
    save(fig, 'mtf_structure')


if __name__ == '__main__':
    print("Generating FOUNDATION charts...")
    chart_candle_types()
    chart_two_candle_patterns()
    chart_three_candle_patterns()
    chart_candle_in_context()
    chart_wick_analysis()
    chart_impulse_corrective()
    chart_premium_discount()
    chart_key_levels_xauusd()
    chart_mtf_structure()
    print(f"✅ 9 foundation charts saved to {OUTPUT_DIR}/")
