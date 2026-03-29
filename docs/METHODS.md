# Reproducibility Methods

## Exact Computational Environment

| Component | Version / Source |
|-----------|----------------|
| AlphaFold Server | alphafoldserver.com (March 2026) |
| Boltz-2 | v2.2.0 via Tamarind Bio (March 2026) |
| Python | 3.12+ |
| Analysis pipeline | analyze.py (this repository) |
| Structure validation | validate_structure.py (this repository) |
| Language compliance | validate_language.py (21 rules) |
| Reference structure | PDB 6FCX (Froese et al., 2018, 2.5 A resolution) |
| Structural superposition | gemmi library |
| Statistical tests | scipy (Welch's t-test, Mann-Whitney U) |

## Protein Sequences

All sequences derive from canonical human MTHFR (UniProt P42898, 656 amino acids).

| Variant | Mutation | Position | Sequence File |
|---------|----------|----------|---------------|
| Wild-type | None | -- | sequences/MTHFR_wildtype.fasta |
| C677T | A222V | 222 (catalytic) | sequences/MTHFR_C677T.fasta |
| A1298C | E429A | 429 (regulatory) | sequences/MTHFR_A1298C.fasta |
| Compound | A222V + E429A | 222 + 429 | sequences/MTHFR_compound.fasta |

## AlphaFold Server Settings

| Setting | Value |
|---------|-------|
| Model seeds | Auto (random) |
| Ligand | FAD (CCD code: FAD) |
| Models per job | 5 (ranked 0-4) |
| Best model selection | rank 0 (highest ranking_score) |
| Protein copies (monomer) | 1 |
| Protein copies (homodimer) | 2 |
| Compound heterodimer | 1 compound + 1 wildtype chain |
| FAD copies (monomer) | 1 |
| FAD copies (dimer) | 2 |

## Boltz-2 Settings (Tamarind Bio)

| Setting | Value |
|---------|-------|
| Version | Boltz 2.2.0 |
| Number of samples | 5 |
| Number of recycles | 3 |
| Step scale | 1.638 |
| Seeds | 1 (auto) |
| Output format | PDB |
| MSA database | UniRef30 + ColabFold environmental |
| THF ligand | SMILES: C1=CC(=CC=C1C(=O)NC(CCC(=O)O)C(=O)O)NCC2CNC3=C(N2)C(=O)NC(=N3)N |
| SAM ligand | SMILES: C[S+](CCC(C(=O)[O-])N)CC1C(C(C(O1)N2C=NC3=C(N=CN=C32)N)O)O |

## Job Configuration (34 Total)

| Configuration | Seeds | Platform | Jobs |
|--------------|-------|----------|------|
| WT monomer + FAD | 5 | AlphaFold 3 | wt_mono_run1-5 |
| WT dimer + FAD | 5 | AlphaFold 3 | wt_dimer_run1-5 |
| C677T monomer + FAD | 5 | AlphaFold 3 | c677t_mono_run1-5 |
| C677T dimer + FAD | 5 | AlphaFold 3 | c677t_dimer_run1-5 |
| A1298C monomer + FAD | 5 | AlphaFold 3 | a1298c_mono_run1-5 |
| Compound heterodimer + FAD | 5 | AlphaFold 3 | compound_dimer_run1-5 |
| WT dimer + FAD + THF | 1 | Boltz-2 | wt_dimer_thf |
| C677T dimer + FAD + THF | 1 | Boltz-2 | c677t_dimer_thf |
| Compound dimer + FAD + THF | 1 | Boltz-2 | compound_dimer_thf |
| WT dimer + FAD + SAM | 1 | Boltz-2 | wt_dimer_sam |

## Statistical Methods

| Test | Purpose | Application |
|------|---------|-------------|
| Welch's t-test | Parametric comparison of means | WT vs compound dimer (n=5 each) |
| Mann-Whitney U | Non-parametric comparison | Confirmatory test for small n |
| Cohen's d | Effect size | Magnitude of group differences |
| Bonferroni correction | Multiple comparison adjustment | 8 simultaneous tests, threshold p < 0.00625 |

## Validation Against Experimental Data

| Prediction | Reference | RMSD | Classification |
|-----------|-----------|------|----------------|
| WT monomer | PDB 6FCX chain A | 1.42 A | High accuracy |
| C677T monomer | PDB 6FCX chain A | 1.44 A | High accuracy |
| Compound dimer chain A | PDB 6FCX chain A | 1.64 A | High accuracy |
| A1298C monomer | PDB 6FCX chain A | 1.97 A | High accuracy |

## How to Reproduce

```bash
git clone https://github.com/DSMPromo/mthfr-target-validation.git
cd mthfr-target-validation
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python analyze.py
python validate_structure.py
python generate_figures.py
python generate_pdf.py
open analysis/outputs/report.html
```
