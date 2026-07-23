# Normal P-Value Uniformity (Discrete-Grid KS)

Under exchangeability P(p <= j/(k+1)) = j/(k+1); the discrete KS statistic
uses a cluster-aware Monte Carlo reference under an idealized exchangeable null.

| dataset | k | corruption | n | clusters | KS_D | MC p-value | worst grid | empirical | direction |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| visa | 4 | blur | 3400 | 60 | 0.0247 | 0.6787 | 0.600 | 0.5753 | conservative |
| visa | 4 | brightness_contrast | 3400 | 60 | 0.0109 | 0.9790 | 0.200 | 0.1891 | conservative |
| visa | 4 | clean | 3400 | 60 | 0.0297 | 0.5537 | 0.600 | 0.5703 | conservative |
| visa | 4 | gaussian_noise | 3400 | 60 | 0.0306 | 0.5312 | 0.200 | 0.1694 | conservative |
| visa | 4 | jpeg | 3400 | 60 | 0.0097 | 0.9850 | 0.800 | 0.8097 | anti-conservative |
| visa | 8 | blur | 3400 | 60 | 0.0392 | 0.1824 | 0.667 | 0.7059 | anti-conservative |
| visa | 8 | brightness_contrast | 3400 | 60 | 0.0580 | 0.0235 | 0.667 | 0.7247 | anti-conservative |
| visa | 8 | clean | 3400 | 60 | 0.0369 | 0.2399 | 0.667 | 0.7035 | anti-conservative |
| visa | 8 | gaussian_noise | 3400 | 60 | 0.0675 | 0.0070 | 0.667 | 0.7341 | anti-conservative |
| visa | 8 | jpeg | 3400 | 60 | 0.0813 | 0.0010 | 0.667 | 0.7479 | anti-conservative |
