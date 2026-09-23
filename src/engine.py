from dataclasses import dataclass
import pandas as pd

@dataclass
class Config:
    threshold: float = -0.02     # event: close-to-close return <= this
    hold: int = 5                # entry = next open (day 1), exit = close of day `hold`
    decluster: bool = True       # skip events while a trade is still open
    cost_per_side: float = 0.0005

def load_clean(path="../data/clean_nifty.csv"):
    return pd.read_csv(path, parse_dates=["Date"]).set_index("Date")

def prepare(df, hold):
    d = df.copy()
    d["ret"] = d["Close"].pct_change()
    d["entry_price"] = d["Open"].shift(-1)
    d["exit_price"] = d["Close"].shift(-hold)
    d["exit_date"] = d.index.to_series().shift(-hold)
    d["fwd_ret"] = d["exit_price"] / d["entry_price"] - 1
    return d

def _window(d, start, end):
    m = d["fwd_ret"].notna()
    if start:
        m &= d.index >= pd.Timestamp(start)
    if end:  # the whole trade must finish inside the period
        m &= d["exit_date"] <= pd.Timestamp(end)
    return d[m]

def get_events(df, cfg, start=None, end=None):
    d = prepare(df, cfg.hold)
    ev = _window(d, start, end)
    ev = ev[ev["ret"] <= cfg.threshold]
    if cfg.decluster:
        pos = {dt: i for i, dt in enumerate(d.index)}
        keep, busy_until = [], -1
        for dt in ev.index:
            i = pos[dt]
            if i >= busy_until:
                keep.append(dt)
                busy_until = i + cfg.hold
        ev = ev.loc[keep]
    return ev

def get_baseline(df, cfg, start=None, end=None):
    d = prepare(df, cfg.hold)
    b = _window(d, start, end)
    return b[b["ret"] > cfg.threshold]