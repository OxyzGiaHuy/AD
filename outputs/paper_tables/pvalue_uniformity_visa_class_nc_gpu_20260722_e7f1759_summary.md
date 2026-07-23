# Normal P-Value Uniformity (Discrete-Grid KS)

Under exchangeability P(p <= j/(k+1)) = j/(k+1); the discrete KS statistic
uses a cluster-aware Monte Carlo reference under an idealized exchangeable null.

| dataset | k | corruption | n | clusters | KS_D | MC p-value | worst grid | empirical | direction |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| visa | 4 | blur | 3400 | 12 | 0.0247 | 0.9790 | 0.600 | 0.5753 | conservative |
| visa | 4 | brightness_contrast | 3400 | 12 | 0.0109 | 0.9965 | 0.200 | 0.1891 | conservative |
| visa | 4 | clean | 3400 | 12 | 0.0297 | 0.9430 | 0.600 | 0.5703 | conservative |
| visa | 4 | gaussian_noise | 3400 | 12 | 0.0306 | 0.9350 | 0.200 | 0.1694 | conservative |
| visa | 4 | jpeg | 3400 | 12 | 0.0097 | 1.0000 | 0.800 | 0.8097 | anti-conservative |
| visa | 8 | blur | 3400 | 12 | 0.0392 | 0.8251 | 0.667 | 0.7059 | anti-conservative |
| visa | 8 | brightness_contrast | 3400 | 12 | 0.0580 | 0.5247 | 0.667 | 0.7247 | anti-conservative |
| visa | 8 | clean | 3400 | 12 | 0.0369 | 0.8671 | 0.667 | 0.7035 | anti-conservative |
| visa | 8 | gaussian_noise | 3400 | 12 | 0.0675 | 0.3563 | 0.667 | 0.7341 | anti-conservative |
| visa | 8 | jpeg | 3400 | 12 | 0.0813 | 0.2184 | 0.667 | 0.7479 | anti-conservative |
