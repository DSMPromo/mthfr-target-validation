# v1.2 - Extended Seed Replicates for Statistical Power

## What v1.2 adds

v1.0 included 2 seed replicates (runs) per configuration. v1.2 adds 3 additional seeds (seeds 3-5) for each of the 6 configurations, bringing the total to 5 seeds per condition. This provides sufficient replicates for meaningful statistical comparisons of structural predictions across genotypes.

## Configurations (6 total)

| # | Genotype | Oligomer | Protein count | FAD count |
|---|----------|----------|---------------|-----------|
| 1 | Wild-type (WT) | Monomer | 1 | 1 |
| 2 | Wild-type (WT) | Homodimer | 2 | 2 |
| 3 | C677T (A222V) | Monomer | 1 | 1 |
| 4 | C677T (A222V) | Homodimer | 2 | 2 |
| 5 | A1298C (E429A) | Monomer | 1 | 1 |
| 6 | Compound heterodimer (C677T + WT) | Heterodimer | 1 + 1 | 2 |

## New jobs (Jobs 17-34)

18 new AlphaFold Server jobs (3 seeds x 6 configurations). Individual JSON files and a combined `ALL_18_SEED_JOBS.json` are in `jobs/json/`.

## Directory structure

```
v1.2/
  README.md
  jobs/
    json/           # 18 individual job files + 1 combined file
  results/          # AlphaFold Server output (to be populated)
```
