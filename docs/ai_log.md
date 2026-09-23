\# AI Usage Log



\## Tools used

Claude (chat assistant). I used it for the project plan, PowerShell and git commands, the event engine and statistics code, and for help interpreting the outputs. I ran all the code myself and checked the outputs at each step.



\## How I used it

\- Broke the assignment into small steps: data, validation, engine, stats, robustness grid, out-of-sample test, falsification, backtest.

\- Generated the code for `src/engine.py` and `src/research\_stats.py`, which I then ran and tested in notebooks.

\- Asked for help reading the tables (confidence intervals, p-values, the robustness grid).



\## AI suggestions I used

\- Entering at the next day's open, to avoid look-ahead bias.

\- Declustering events so trades never overlap.

\- A block bootstrap for the baseline, because 5-day returns overlap.

\- A Bonferroni cutoff (0.05 / 12 = 0.0042) for the 12-cell robustness grid.

\- Writing the pass/fail rule for the out-of-sample test before running it.



\## Incorrect or problematic AI output I found and fixed

\- `mkdir data notebooks src docs` failed in PowerShell. It needs commas between the folder names.

\- `pip freeze > requirements.txt` saves UTF-16 in PowerShell, so I re-saved the file as UTF-8.

\- I ran the git remote command with the placeholder YOUR\_USERNAME, and fixed it with `git remote set-url`.

\- The first exit definition was ambiguous. I rewrote it so the entry day counts as day 1.

\- Some notebooks were saved without the .ipynb extension, so I renamed them.

\- The AI flagged the last data row (2026-09-23, Volume = 0) as a possibly incomplete bar, and I dropped it. The missing 2026-09-22 is still unverified.



\## My own decisions

\- I kept the 2008 and 2020 crash data. They are real market events, and removing them would delete exactly the falls I am studying.

\- I fixed the primary test (-2%, hold 5) before seeing results, and refused to pick the best-looking cell of the grid. With 12 tests, one lucky result is expected by chance.

\- I froze the out-of-sample period (2018 onward) and ran it once. I did not change any setting afterwards.

\- The falsification checks were run after seeing the OOS result, so I treat them as diagnostics only. The "excluding 2008 and 2020" result is post-hoc and exploratory, and I do not claim it as a finding.



\## What I learned

\- A negative result is a valid result. Here the hypothesis is not supported, in development or out-of-sample.

\- Statistical significance and trading significance are different things. Even the best grid cells had confidence intervals too wide to trust.

\- Overlapping events and clustered crashes (2008, 2020) can make a small sample look more informative than it is.

\- AI-generated code and commands need checking, because several suggestions failed or were ambiguous.

