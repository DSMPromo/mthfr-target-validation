# MTHFR Variant Structural Analysis: AlphaFold 3 Predictions of FAD Cofactor Binding Disruption Across Five Disease Pathways

## A Computational Framework for Experimental Validation

---

**Author:** Igor Mihaljko, Independent Researcher, DSM.Promo, Chicago, IL

**Correspondence:** igor@dsm.promo

**Keywords:** MTHFR, AlphaFold 3, C677T, A1298C, FAD cofactor, protein structure prediction, gene therapy, folate metabolism

**License:** CC BY-NC-SA 4.0

**Data Availability:** All sequences, analysis scripts, and AlphaFold results available at https://github.com/DSMPromo/mthfr-gene-therapy-project

---

## Abstract

Methylenetetrahydrofolate reductase (MTHFR) variants C677T (A222V) and A1298C (E429A) affect up to 40% of the global population, yet their structural consequences on FAD cofactor binding and SAM-mediated allosteric regulation remain incompletely characterized at the atomic level. We used AlphaFold 3 Server to predict the structures of wild-type, C677T, A1298C, and compound heterozygous MTHFR in complex with FAD, folate substrate (THF), and allosteric inhibitor (SAM). Across 16 structural predictions with independent replication seeds, we compared pTM, ipTM, pLDDT at mutation sites (positions 222 and 429), and predicted aligned error (PAE) to quantify structural confidence differences between wild-type and variant enzymes. Our computational analysis suggests [RESULTS TO BE INSERTED AFTER ALPHAFOLD COMPLETION]. These predictions generate specific, testable hypotheses for experimental validation by structural biologists and provide a framework for evaluating CRISPR base editing as a potential single-gene correction strategy across five MTHFR-linked disease pathways.

**Note:** This is a computational study generating hypotheses for experimental validation. All structural predictions require confirmation through experimental methods (cryo-EM, X-ray crystallography, functional assays).

---

## 1. Introduction

### 1.1 The MTHFR Enzyme and Its Clinical Significance

MTHFR (methylenetetrahydrofolate reductase, EC 1.5.1.20) is a FAD-dependent homodimeric enzyme encoded on chromosome 1p36.22 that catalyzes the conversion of 5,10-methylenetetrahydrofolate to 5-methyltetrahydrofolate (5-MTHF), the primary circulating form of folate and the methyl donor for homocysteine remethylation to methionine (Froese et al., 2018). This reaction sits at the intersection of folate metabolism, homocysteine regulation, methylation (via S-adenosylmethionine), neurotransmitter synthesis (via BH4), and B-vitamin processing.

The crystal structure of human MTHFR (PDB: 6FCX, 2.5 A resolution) revealed a homodimer with each subunit containing a conserved catalytic TIM-barrel domain (N-terminal, FAD-binding) and a eukaryote-specific regulatory domain (C-terminal, SAM-binding) connected by a 25-residue inter-domain linker (Froese et al., 2018). Recent cryo-EM structures (PDB: 8QA5, 8QA6) have further elucidated the mechanism of SAM-mediated allosteric inhibition through dual SAM binding and inter-domain conformational rearrangement (Froese et al., 2024).

### 1.2 The Two Key Variants

Two common MTHFR polymorphisms have substantial clinical significance:

**C677T (rs1801133, p.Ala222Val):** Located in the catalytic domain, this variant destabilizes FAD cofactor binding. The A222V substitution displaces helix alpha-5, which carries FAD-interacting residues Asn168, Arg171, and Lys172, resulting in a thermolabile enzyme with reduced activity (~35% per allele, ~70% in TT homozygotes) (Pejchal et al., 2006). The T allele frequency ranges from 24-50% across populations.

**A1298C (rs1801131, p.Glu429Ala):** Located in the regulatory domain near the SAM-binding site, this variant reduces enzyme activity by ~30% per allele and impairs BH4 recycling, affecting neurotransmitter synthesis. The interaction between position 429 and the SAM-binding pocket identified in the 2024 cryo-EM structures (Froese et al., 2024) provides structural context for this variant's functional impact.

**Compound heterozygosity** (one copy of each variant) produces enzyme activity comparable to C677T homozygosity (~50-60% of normal), creating a dual hit affecting both catalytic function and regulatory feedback (Weisberg et al., 1998).

### 1.3 Five Disease Pathways, One Enzyme

When MTHFR function is impaired, five pathological cascades are simultaneously activated:

1. **Vision loss and retinal neurodegeneration:** Elevated homocysteine damages retinal ganglion cells through oxidative stress, with Mthfr+/- mice showing ~20% ganglion cell loss and retinal vasculopathy (Markand et al., 2015). Complete blindness has been reversed with betaine treatment in severe MTHFR deficiency (Hergert et al., 2022).

2. **Autism spectrum disorder and cerebral folate deficiency:** Reduced 5-MTHF transport across the blood-brain barrier via folate receptor alpha (FRa) starves the developing brain of folate. Meta-analysis of 15 studies confirms significant association between C677T and ASD (Pu et al., 2020). Folinic acid improved verbal communication in a randomized controlled trial (Frye et al., 2018).

3. **Anxiety, depression, and neuropsychiatric disorders:** Impaired SAMe production reduces serotonin, dopamine, and GABA synthesis. The A1298C variant specifically affects BH4 recycling, the rate-limiting cofactor for neurotransmitter hydroxylases (Wan et al., 2018).

4. **B-vitamin processing failure:** MTHFR dysfunction creates a cascade of B-vitamin metabolic failures: B2 cannot regenerate FAD for the already-weakened enzyme, B12 becomes trapped in inactive forms, and dietary folate cannot be converted to active 5-MTHF.

5. **Cardiovascular disease:** Every 5 umol/L increase in plasma homocysteine is associated with 20-30% higher coronary artery disease risk and 60% elevated stroke risk.

### 1.4 Knowledge Gap and Study Rationale

While thousands of individual studies address MTHFR variants in specific disease contexts, no published work has systematically characterized the structural consequences of C677T, A1298C, and compound heterozygous variants using AlphaFold 3's ability to predict protein-ligand complexes. AlphaFold 3 (Abramson et al., 2024) can model protein + cofactor (FAD) + substrate (THF) + inhibitor (SAM) interactions in a single prediction, enabling direct comparison of wild-type and variant enzyme structures with their functional ligands.

### 1.5 Study Objectives

We hypothesize that AlphaFold 3 structural predictions will reveal:
1. Reduced FAD binding confidence (ipTM) in C677T variants compared to wild-type
2. Altered SAM-binding domain architecture in A1298C variants
3. Compound effects in double-mutant predictions
4. Structural rationale for why a single CRISPR base editing correction could restore normal enzyme function across all five disease pathways

---

## 2. Methods

### 2.1 Protein Sequences

All sequences derive from the canonical human MTHFR protein (UniProt P42898, 656 amino acids):

| Variant | Sequence Source | Mutation | Position |
|---------|----------------|----------|----------|
| Wild-type | UniProt P42898 (canonical) | None | A at 222, E at 429 |
| C677T | UniProt P42898 + A222V | Ala -> Val | Position 222 (catalytic domain) |
| A1298C | UniProt P42898 + E429A | Glu -> Ala | Position 429 (regulatory domain) |
| Compound | UniProt P42898 + A222V + E429A | Both | Positions 222 and 429 |

Sequences were verified against the UniProt canonical sequence. Mutations were introduced computationally at the correct positions and validated by sequence alignment.

### 2.2 AlphaFold 3 Server Predictions

All predictions were performed using AlphaFold Server (alphafoldserver.com) in March 2026. Each job generated 5 ranked models; the top-ranked model (rank 0) was used for analysis.

**Job Design (16 predictions):**

| Job | Protein | Copies | Ligands | Purpose |
|-----|---------|--------|---------|---------|
| 01 | Wild-type | 1 (monomer) | FAD x1 | Baseline monomer |
| 02 | Wild-type | 2 (dimer) | FAD x2 | Native functional dimer |
| 03 | C677T | 1 | FAD x1 | Variant monomer |
| 04 | C677T | 2 | FAD x2 | Homozygous TT dimer |
| 05 | A1298C | 1 | FAD x1 | Variant monomer |
| 06 | Compound + WT | 1+1 | FAD x2 | Heterozygous dimer |
| 07-12 | Replication | Same as 01-06 | Same | Independent seed validation |
| 13 | Wild-type | 2 | FAD x2, THF x2 | Substrate binding |
| 14 | C677T | 2 | FAD x2, THF x2 | Variant substrate binding |
| 15 | Compound + WT | 1+1 | FAD x2, THF x2 | Heterozygous + substrate |
| 16 | Wild-type | 2 | FAD x2, SAM x2 | Allosteric inhibitor |

Seeds were set to "Auto" (random) for all jobs to ensure independent predictions.

### 2.3 Confidence Metrics Analyzed

| Metric | Description | Interpretation |
|--------|-------------|----------------|
| pTM | Predicted TM-score | Overall structure accuracy (>0.7 = reliable) |
| ipTM | Interface predicted TM-score | Protein-ligand interface confidence (>0.8 = high) |
| pLDDT at pos 222 | Per-residue confidence at C677T site | Local structural confidence at mutation |
| pLDDT at pos 429 | Per-residue confidence at A1298C site | Local structural confidence at mutation |
| PAE | Predicted Aligned Error matrix | Relative position confidence between residues |
| ranking_score | Combined quality metric | Best model selection from replicate seeds |

### 2.4 Analysis Pipeline

Analysis was performed using a custom Python pipeline (analyze.py) that:
1. Extracts all confidence metrics from AlphaFold JSON output files
2. Generates PAE heatmap plots with mutation positions marked
3. Creates comparative bar charts (WT vs variants, color-coded)
4. Produces an HTML report with all visualizations
5. Outputs CSV data for independent analysis

All analysis code is available at https://github.com/DSMPromo/mthfr-gene-therapy-project

### 2.5 Reference Structures

Predictions were compared against:
- PDB 6FCX: Human MTHFR crystal structure, 2.5 A (Froese et al., 2018)
- PDB 8QA5: MTHFR + SAH dis-inhibited state, cryo-EM (Froese et al., 2024)
- PDB 8QA6: MTHFR + SAM inhibited state, cryo-EM (Froese et al., 2024)

---

## 3. Results

[TO BE COMPLETED AFTER ALPHAFOLD RESULTS ARE DOWNLOADED AND ANALYZED]

### 3.1 Overall Prediction Quality

[Table: pTM, ipTM, ranking_score for all 16 jobs]

### 3.2 FAD Binding Confidence: Wild-Type vs Variants

[Comparison of ipTM scores between WT and C677T, A1298C, compound]
[Bar chart: ipTM comparison]

### 3.3 Local Confidence at Mutation Sites

[pLDDT at positions 222 and 429 across all predictions]

### 3.4 Predicted Aligned Error Analysis

[PAE heatmaps showing inter-domain and protein-FAD confidence]
[Comparison between WT and variant PAE patterns]

### 3.5 Dimer Interface Analysis

[Comparison of monomer vs dimer predictions]
[Compound heterozygous dimer analysis]

### 3.6 Substrate and Inhibitor Binding (Jobs 13-16)

[THF binding in WT vs C677T vs compound]
[SAM binding analysis]

### 3.7 Replication Consistency

[Comparison of original vs replicate seed predictions]
[Variance analysis of key metrics]

---

## 4. Discussion

### 4.1 Structural Interpretation

[TO BE COMPLETED]

### 4.2 Multi-Pathway Implications

The structural predictions, if validated experimentally, would support the hypothesis that MTHFR variants create a single molecular defect with pleiotropic consequences across five disease pathways. The convergence of these pathways on one enzyme suggests that a single genetic correction could have broad therapeutic impact.

### 4.3 Therapeutic Implications: CRISPR Base Editing

The C677T variant (T>C at the DNA level) is a candidate for adenine base editing (ABE), which converts A-T base pairs to G-C base pairs. Precedent exists for in vivo base editing via LNP delivery:

- **VERVE-102** (Verve Therapeutics): Single adenine base edit of PCSK9 via LNP delivery, Phase 1b clinical trial for familial hypercholesterolemia
- **Beam-101** (Beam Therapeutics): Base editing for sickle cell disease, Phase I/II with demonstrated efficacy

The A1298C variant (C>A at the DNA level, resulting in E429A) would require a different base editing strategy. For compound heterozygous individuals, correction of either variant alone might provide substantial clinical benefit.

**Delivery routes for different disease targets:**

| Route | Target Tissue | Disease Targets | Precedent |
|-------|---------------|-----------------|-----------|
| IV LNP (hepatic) | Liver | CVD, B-vitamins | VERVE-102, Intellia NTLA-2001 |
| Intravitreal | Retina | Vision loss | Luxturna (AAV), EDIT-101 |
| CNS-targeted LNP | Brain | Autism/CFD, anxiety | Emerging (requires BBB-crossing LNP) |

### 4.4 Limitations

This study has several important limitations that must be acknowledged:

1. **Computational predictions require experimental validation.** AlphaFold 3 predictions are models, not experimental structures. All structural conclusions are hypotheses to be tested.

2. **Static predictions vs dynamic biology.** AlphaFold predicts a single conformation; MTHFR undergoes conformational changes during catalysis and allosteric regulation that are not captured.

3. **Cofactor and substrate modeling.** AlphaFold 3's accuracy for small molecule binding is lower than for protein-protein interactions. ipTM scores for protein-ligand complexes should be interpreted more cautiously than for protein-protein complexes.

4. **Clinical extrapolation.** The connection between structural predictions and clinical phenotypes involves many biological layers (protein folding, cellular environment, tissue-specific expression, compensatory mechanisms) that computational modeling cannot capture.

5. **Sample size.** Consumer genetic testing data motivated this study but has no clinical-grade accuracy guarantees. The genomic data should not be used for clinical decision-making.

6. **Independent researcher context.** This work was performed outside an academic institution without wet-lab validation capability. The primary value is as a computational framework and hypothesis generator.

### 4.5 Future Directions

1. **Experimental structure determination:** Cryo-EM of C677T and A1298C variants in complex with FAD, with and without folate substrate
2. **Functional assays:** Thermal shift assays to measure FAD binding affinity in variants
3. **Base editor guide RNA design:** Computational design and in vitro testing of ABE guides targeting C677T
4. **Clinical correlation:** Prospective study of compound heterozygous individuals across all five disease pathways
5. **Molecular dynamics:** Extended simulations of WT and variant MTHFR to capture dynamic effects not visible in static predictions

---

## 5. Conclusion

[TO BE COMPLETED AFTER RESULTS]

---

## 6. Collaboration Opportunities

This is an open research project seeking collaboration with:

- **Structural biologists:** To validate AlphaFold predictions with experimental structures
- **Gene therapy researchers:** To design and test base editing strategies for MTHFR correction
- **Clinical researchers:** To establish clinical correlations across the five disease pathways
- **Bioinformaticians:** To independently replicate and extend the computational analysis

All data, code, and results are freely available under CC BY-NC-SA 4.0. Contact: igor@dsm.promo

---

## 7. Acknowledgments

AlphaFold 3 predictions were performed using Google DeepMind's AlphaFold Server. Protein sequences were obtained from UniProt (P42898). Reference structures were obtained from the Protein Data Bank (6FCX, 8QA5, 8QA6). AI tools (Claude, Anthropic) were used for literature organization and analysis pipeline development. All AI-assisted work is disclosed per emerging best practices in scientific publishing.

---

## 8. References

1. Markand S, Tawfik A, Ha Y, et al. (2015). Retinal Ganglion Cell Loss and Mild Vasculopathy in Methylene Tetrahydrofolate Reductase (Mthfr)-Deficient Mice: A Model of Mild Hyperhomocysteinemia. *Invest Ophthalmol Vis Sci*, 56(4):2684-2695. PMID: 25766590

2. Hergert RM, et al. (2022). Phoenix from the ashes: dramatic improvement in severe late-onset methylenetetrahydrofolate reductase (MTHFR) deficiency with a complete loss of vision. *J Neurol*, 269:4571-4577.

3. Jiang H, Liu Z, Townsend JH, Wang J. (2023). Effects of Methylenetetrahydrofolate Reductase (MTHFR) Polymorphisms on Retinal Tissue Perfusion in Mild Diabetic Retinopathy Patients Receiving the Medical Food, Ocufolin. *Clin Ophthalmol*, 17:1035-1043.

4. Pu D, Shen Y, Wu J. (2020). Association between MTHFR C677T/A1298C and susceptibility to autism spectrum disorders: a meta-analysis. *BMC Pediatr*, 20:471. PMID: 32972375

5. Wan L, Li Y, Zhang Z, et al. (2018). Methylenetetrahydrofolate reductase and psychiatric diseases. *Transl Psychiatry*, 8:242. PMID: 30397195

6. Levin BL, Varga E. (2016). MTHFR: Addressing Genetic Counseling Dilemmas Using Evidence-Based Literature. *J Genet Couns*, 25(5):901-911.

7. Froese DS, Kopec J, Rembeza E, et al. (2018). Structural basis for the regulation of human 5,10-methylenetetrahydrofolate reductase by phosphorylation and S-adenosylmethionine inhibition. *Nat Commun*, 9:4735.

8. Pejchal R, Campbell E, Guenther BD, et al. (2006). Structural Perturbations in the Ala -> Val Polymorphism of Methylenetetrahydrofolate Reductase: How Binding of Folates May Protect against Inactivation. *Biochemistry*, 45(15):4808-4818.

9. Froese DS, et al. (2024). Dynamic inter-domain transformations mediate the allosteric regulation of human 5,10-methylenetetrahydrofolate reductase. *Nat Commun*. (PDB: 8QA5, 8QA6)

10. Frye RE, Slattery J, Delhey L, et al. (2018). Folinic acid improves verbal communication in children with autism and language impairment: a randomized double-blind placebo-controlled trial. *Mol Psychiatry*, 23:631-636.

11. Abramson J, Adler J, Dunbar J, et al. (2024). Accurate structure prediction of biomolecular interactions with AlphaFold 3. *Nature*, 630:493-500.

12. McNulty H, Dowey LRC, Strain JJ, et al. (2006). Riboflavin lowers homocysteine in individuals homozygous for the MTHFR 677C->T polymorphism. *Circulation*, 113(1):74-80.

---

## Appendix A: Disclosure

The author is not a medical professional, biomedical scientist, or geneticist. The author is a cybersecurity specialist and cloud solution architect who identified compound heterozygous MTHFR status through consumer genetic testing and used computational tools to organize and analyze published research. This project exists to provide a computational framework that qualified researchers can validate, extend, or refute.

This is not medical advice. All therapeutic concepts are speculative and would require years of experimental validation before any clinical application.
