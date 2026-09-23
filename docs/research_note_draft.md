\# Research Note Draft



\## Hypothesis

After NIFTY 50 falls 2% or more close-to-close in one day, the average 5-day forward return is higher than the average 5-day forward return on all normal days.



\## Definitions

\- Event: close-to-close return <= -2%. Robustness alternatives: -1.5%, -3%.

\- Entry: next trading day's open (the day's return is only known at the close).

\- Exit: close of the 5th trading day after entry. Alternative holding periods: 1, 3, 10.

\- Recovery: forward return > 0, and also forward return > baseline mean.

\- Data: NIFTY 50 (^NSEI) daily OHLC from Yahoo Finance.

\- Development period: Sept 2007 to Dec 2017.

\- Out-of-sample period: Jan 2018 onward (not touched until Phase 6).

\- Transaction costs: 0.05% per side, 0.10% round trip.



\## My reasoning (own words)

1\. Why -2%: it is a large enough fall to count as a real shock, but it still happens often enough to give a usable number of events

2\. Why next-day open: the close-to-close return is only known once the day ends, so buying at that close would use information you didn't have. The next open is the first price you could actually trade at

3\. Why split at 2018:about 10 years of data for development and the rest kept unseen. 2018 onward also includes different regimes (the 2020 COVID crash, for example) that will test whether the result holds

