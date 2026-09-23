# Does NIFTY recover after a big one-day fall?



**Result: no evidence for the hypothesis.** This holds in the development period, out-of-sample, and across a robustness grid.



## Hypothesis

After NIFTY 50 falls 2% or more close-to-close in one day, the average 5-day forward return is higher than the average 5-day forward return on normal days.


## Data

- Source: Yahoo Finance via `yfinance`, ticker `^NSEI` (NIFTY 50 price index, daily). Downloaded 2026-09-23.

- Raw range: 2007-09-17 to 2026-09-23 (4665 rows). Fields: Date, Open, High, Low, Close.

- Cleaning (see `notebooks/02_validation.ipynb`): no duplicates, missing values or invalid OHLC found. Kept all extreme moves (2008, 2009-05-18, 2020) because they are real events. Dropped the last row (2026-09-23, Volume 0, possibly incomplete). 2026-09-22 is missing and I did not verify why. Dropped Adj Close (identical to Close) and Volume.

- Clean file: `data/clean_nifty.csv` (4664 rows, ends 2026-09-21).

- Price index only: dividends are ignored.



## Method

- **Event:** close-to-close return <= -2%. Alternatives tested: -1.5%, -3%.

- **Entry:** next trading day's open. The return is only known at the close, so buying at that close would be look-ahead.

- **Exit:** close of day `hold`, where the entry day counts as day 1. Main hold = 5. Alternatives: 1, 3, 10.

- **Overlap:** an event is skipped while a previous trade is still open (declustering).

- **Baseline:** all non-event days, with the same entry and exit rule and the same period.

- **Costs:** 0.05% per side, 0.10% round trip.

- **Split:** development = 2007-09 to 2017-12, out-of-sample = 2018-01 onward. Trades that would end after the period boundary are dropped.

- **Statistics:** mean, median, win rate, std, skew, bootstrap CI for the mean, and a difference-in-means test. The event side is resampled i.i.d. and the baseline is block-bootstrapped (block = 20 days) because baseline returns overlap. The Welch t-test p-value is optimistic for the same reason, so the bootstrap CI is the main evidence.



## Results

| Test (-2%, hold 5) | n events | Event mean | Baseline mean | Difference | 95% CI for difference |

|---|---|---|---|---|---|

| Development | 92 | 0.070% | 0.118% | -0.049% | about [-1.0, +0.9] |

| Out-of-sample | 39 | -0.107% | 0.116% | -0.224% | [-1.81, +1.11] |



- **Robustness grid** (3 thresholds x 4 holds, development only): all 12 confidence intervals include 0. The smallest p-value is 0.246, against a Bonferroni cutoff of 0.0042. The signs are mixed. Hold = 1 is negative at every threshold.

- **Out-of-sample:** the pre-set rule (difference > 0, CI excludes 0, net mean > 0 after costs) failed on all three conditions. 14 of 39 events fall in 2020.

- **Falsification (diagnostic, run after seeing OOS):** full-sample difference is -0.10%, CI [-0.88, 0.71], win rate 49.6% vs 54.0%, sign-test p = 0.86. Excluding 2008 and 2020, the difference becomes +0.57% with CI [-0.16, 1.31]. This was found post-hoc and is exploratory only.

- **Backtest (demonstration only, `08_backtest.ipynb`):** 131 trades, net return -22.7% (gross -11.9%), max trade-level drawdown -52.7%, time in market 14%. Buy and hold returned +336.8%.



## What would make me reject the hypothesis

Confidence intervals for the difference that include 0 in both periods, and a negative net mean after costs. Both were observed.



## Limitations

- Small samples (n = 92 and n = 39). The confidence intervals are about +-1 to 2% wide, so a small real effect could not be detected.

- Events cluster in 2008 and 2020, and results depend on those regimes.

- Yahoo is a single unaudited source. One date (2026-09-22) is unexplained.

- Bootstrap CIs vary slightly between runs and settings (seed and n_boot).

- Costs are a flat assumption. Real slippage in crashes would be higher, and the NIFTY index itself is not directly tradable (a future or ETF would be used).

- The backtest covers the full sample including OOS, uses trade-level drawdown, and is not a strategy proposal.

## Why these statistics
- **Mean and median:** the mean is the expected return but a few crash days can pull it. The median shows the typical event. Out-of-sample they differ (mean -0.107%, median -0.007%), and the skew of -1.98 shows the crash tail.
- **Win rate:** shows how often a trade makes money. Out-of-sample it was 48.7% for events against 53.4% for normal days.
- **Std, skew, worst case:** measure risk. In development, event trades had a std of 4.7% against 3.1% for normal days.
- **Bootstrap CI for the difference:** it needs no normality assumption, and block resampling respects the overlap in baseline returns. It shows which differences are compatible with the data. Here the interval includes 0, so the data cannot tell "no effect" from a small effect. The intervals are about +-1% wide, so an effect of up to about 1% could exist undetected. This is "no evidence", not "proof of no effect".
- **Welch t-test:** secondary only, because overlapping returns make its p-value optimistic.
- **Statistical vs economic significance:** even the best-looking grid cell (+0.58%) was not significant, and it is small compared with a 4.7% std and 0.10% costs.
- **Data snooping and overfitting:** the primary test was fixed in advance, and no parameter was tuned. The 12-cell grid is judged against a Bonferroni cutoff (0.0042), and the best cell was not picked. The "excluding 2008 and 2020" result is post-hoc and exploratory. The OOS period was run once with a pre-set rule.


## Reproduce

```

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

jupyter notebook

```

Run the notebooks in order: `01_data` (download, or use the saved `data/raw_nifty.csv`), `02_validation`, `03_events`, `04_stats`, `05_robustness`, `06_oos` (run once), `07_falsification`, `08_backtest`.

The engine is `src/engine.py` (configure with `Config(threshold, hold, decluster, cost_per_side)`) and the statistics are in `src/research_stats.py`.



## Repository layout

`data/` raw and clean data. `src/` engine and statistics. `notebooks/` analysis in order. `docs/` research note, AI usage note and AI log.

