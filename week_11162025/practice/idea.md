1. Visual inspection (scatter plot):
Since target is binary (0 or 1), you'll see two vertical groups
If the distributions of the input column differ between target=0 and target=1 → NOT independent
If the distributions look similar → likely independent
2. Correlation coefficient:
Correlation close to 0 → suggests independence
Correlation significantly different from 0 → suggests dependence
Note: correlation measures linear relationships; non-linear relationships can still indicate dependence
3. Statistical tests (optional):
Compare means/medians of the input column for target=0 vs target=1
If they differ significantly → NOT independent