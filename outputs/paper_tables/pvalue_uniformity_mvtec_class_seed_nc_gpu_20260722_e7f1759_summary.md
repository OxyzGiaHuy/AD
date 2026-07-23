# Normal P-Value Uniformity (Discrete-Grid KS)

Under exchangeability P(p <= j/(k+1)) = j/(k+1); the discrete KS statistic
uses a cluster-aware Monte Carlo reference under an idealized exchangeable null.

| dataset | k | corruption | n | clusters | KS_D | MC p-value | worst grid | empirical | direction |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| mvtec | 4 | blur | 2335 | 75 | 0.1148 | 0.0005 | 0.400 | 0.5148 | anti-conservative |
| mvtec | 4 | brightness_contrast | 2335 | 75 | 0.1118 | 0.0005 | 0.400 | 0.5118 | anti-conservative |
| mvtec | 4 | clean | 2335 | 75 | 0.1071 | 0.0005 | 0.400 | 0.5071 | anti-conservative |
| mvtec | 4 | gaussian_noise | 2335 | 75 | 0.2732 | 0.0005 | 0.400 | 0.6732 | anti-conservative |
| mvtec | 4 | jpeg | 2335 | 75 | 0.2180 | 0.0005 | 0.400 | 0.6180 | anti-conservative |
| mvtec | 8 | blur | 2335 | 75 | 0.1193 | 0.0005 | 0.333 | 0.4527 | anti-conservative |
| mvtec | 8 | brightness_contrast | 2335 | 75 | 0.1258 | 0.0005 | 0.333 | 0.4591 | anti-conservative |
| mvtec | 8 | clean | 2335 | 75 | 0.1159 | 0.0005 | 0.333 | 0.4493 | anti-conservative |
| mvtec | 8 | gaussian_noise | 2335 | 75 | 0.2988 | 0.0005 | 0.333 | 0.6321 | anti-conservative |
| mvtec | 8 | jpeg | 2335 | 75 | 0.2320 | 0.0005 | 0.333 | 0.5653 | anti-conservative |
