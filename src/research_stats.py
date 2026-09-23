import numpy as np
from scipy import stats

def summarize(x, cost_round_trip=0.0):
    x = np.asarray(x, dtype=float)
    return {
        "n": len(x),
        "mean_%": x.mean() * 100,
        "median_%": np.median(x) * 100,
        "win_rate_%": (x > 0).mean() * 100,
        "std_%": x.std(ddof=1) * 100,
        "skew": stats.skew(x),
        "worst_%": x.min() * 100,
        "best_%": x.max() * 100,
        "net_mean_%": (x - cost_round_trip).mean() * 100,
    }

def bootstrap_ci(x, n_boot=10000, alpha=0.05, seed=42):
    rng = np.random.default_rng(seed)
    x = np.asarray(x, dtype=float)
    means = rng.choice(x, size=(n_boot, len(x)), replace=True).mean(axis=1)
    return np.percentile(means, [100 * alpha / 2, 100 * (1 - alpha / 2)])

def block_bootstrap_means(x, block=20, n_boot=5000, seed=43):
    # baseline returns overlap, so resample in blocks to keep their dependence
    rng = np.random.default_rng(seed)
    x = np.asarray(x, dtype=float)
    n = len(x)
    k = int(np.ceil(n / block))
    out = np.empty(n_boot)
    for b in range(n_boot):
        starts = rng.integers(0, n - block + 1, size=k)
        out[b] = np.concatenate([x[s:s + block] for s in starts])[:n].mean()
    return out

def diff_test(ev, base, block=20, n_boot=5000, seed=42):
    ev = np.asarray(ev, dtype=float)
    base = np.asarray(base, dtype=float)
    rng = np.random.default_rng(seed)
    ev_means = rng.choice(ev, size=(n_boot, len(ev)), replace=True).mean(axis=1)
    base_means = block_bootstrap_means(base, block, n_boot, seed + 1)
    diff = ev_means - base_means
    lo, hi = np.percentile(diff, [2.5, 97.5])
    t, p = stats.ttest_ind(ev, base, equal_var=False, alternative="greater")
    return {
        "diff_%": (ev.mean() - base.mean()) * 100,
        "ci_lo_%": lo * 100,
        "ci_hi_%": hi * 100,
        "welch_t": t,
        "p_one_sided": p,
        "boot_share_diff<=0": (diff <= 0).mean(),
    }