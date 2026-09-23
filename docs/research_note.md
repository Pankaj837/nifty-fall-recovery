\# Research Note: Recovery after large one-day NIFTY falls



\*\*Hypothesis.\*\* After NIFTY 50 falls 2% or more close-to-close in one day, the average 5-day forward return is higher than the average 5-day forward return on normal days.



\*\*Event.\*\* Close-to-close return <= -2%. I chose this because it is a real shock but still frequent enough to give a usable sample (145 raw events in 2007-2017). Robustness: -1.5% and -3%.



\*\*Recovery.\*\* Forward return above the baseline mean. I also report the share of trades with a positive return.



\*\*Entry and exit.\*\* Entry is the next trading day's open, because the day's return is only known at the close. Exit is the close of day 5, counting the entry day as day 1. Robustness holds: 1, 3, 10 days.



\*\*Overlap.\*\* New events are skipped while a trade is open, so observations do not overlap (145 raw events become 92 in development).



\*\*Baseline.\*\* All non-event days over the same period, using the same entry and exit rule.



\*\*Test period.\*\* Development is 2007-09 to 2017-12. Out-of-sample is 2018-01 onward, unseen until the primary test and the robustness grid were finished, and run once. Trades that cross the boundary are dropped.



\*\*Costs.\*\* 0.05% per side (brokerage plus slippage), 0.10% round trip.



\*\*Key assumptions.\*\*

\- Data is Yahoo Finance ^NSEI, a price index, so dividends are ignored.

\- Trades execute at the quoted open and close. Real fills in a crash would be worse.

\- Returns are compared as differences in means. The event side is resampled i.i.d. and the baseline is block-bootstrapped (20 days) because its returns overlap.

\- One primary test was fixed in advance. The 12-cell grid is only a stability check, judged against a Bonferroni cutoff of 0.0042.

\- One position at a time, and the full sample includes the 2008 and 2020 crashes.



\*\*Result in one line.\*\* Development difference -0.05% (CI about \[-1.0, +0.9]). Out-of-sample difference -0.22% (CI \[-1.81, +1.11]). No grid cell was significant. Net of costs, the average trade lost money. The hypothesis is not supported.



\*\*What would change my mind.\*\* A difference with the same sign across neighbouring thresholds and holds, a confidence interval that excludes 0 in both periods, and a positive net mean after costs. None of these were observed.

