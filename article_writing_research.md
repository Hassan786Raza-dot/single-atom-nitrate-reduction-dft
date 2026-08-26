# Deep research: writing and reporting a rigorous computational chemistry article

## Sources consulted

1. ACS Author Guidelines, last updated 26 June 2025: https://researcher-resources.acs.org/publish/author_guidelines?coden
2. Nature Portfolio reporting standards and data/code/protocol availability: https://www.nature.com/nature-portfolio/editorial-policies/reporting-standards
3. Nature Chemistry AIP and formatting guidance: https://www.nature.com/nchem/submission-guidelines/aip-and-formatting
4. Siesta India, *Scientific Writing for Computational Material Science (DFT) Research*, YouTube, 12 December 2025: https://www.youtube.com/watch?v=w8jmOCwgJQ8
5. Washington University in St Louis, Chemistry Writing guide: https://libguides.wustl.edu/chemwriting/labreport
6. Chemistry Europe, Methods: Notice to Authors: https://chemistry-europe.onlinelibrary.wiley.com/hub/journal/26289725/notice-to-authors

## Cross-source principles

### 1. A research article must have a defensible contribution

Publisher guidance and representative papers converge on the requirement that the paper should make a specific contribution supported by the data. A long literature review, a large candidate list, or a workflow alone does not establish a catalyst-discovery contribution. The title, abstract, introduction, results, and conclusion must all describe the same contribution. For this project, the contribution must be narrowed to either a completed nitrate-reduction catalyst study or an explicitly methodological/reproducibility benchmark. It cannot imply a completed ranking when the production calculations are absent.

### 2. The introduction must create a testable gap

A strong introduction moves from context to a precise unresolved problem, explains why existing approaches are insufficient, states the hypothesis or research question, and ends with the study's strategy and contribution. It should not simply list nitrate pollution, ammonia demand, SACs, and DFT. The present project needs a sharper gap: whether matched support/metal comparisons remain interpretable when spin, cell-size, vacuum, charged nitrate, solvation, and potential dependence are controlled. The final paragraph should state the exact test, not claim impact in advance.

### 3. Methods must be reproducible, not merely plausible

ACS explicitly requires computational methods to be described in sufficient detail for reproduction; ACS fast-format guidance requires standard sections, embedded figures/tables/equations, complete references, and separate supporting information. For periodic DFT, reproducibility requires the code version, dataset/POTCAR identity, exchange–correlation functional, dispersion, cell, vacuum, k-points, cutoff, smearing, spin initialisation, charge treatment, solvation, convergence thresholds, optimiser, and raw outputs. A nominal “PBE-D3 calculation” is not enough.

### 4. Results must report evidence before interpretation

Tables and figures should display the actual observations first. Each figure needs a purpose, a source-data file, a clear caption, units, sample size where applicable, and a statement of uncertainty or numerical tolerance. A convergence figure should not be presented as a catalyst-performance figure. Total-energy changes across different cutoffs or k-point meshes are diagnostics and should not be interpreted as adsorption-energy errors unless the same chemical observable is compared.

### 5. Discussion must distinguish result, inference, and limitation

High-quality papers separate direct computational observations from mechanistic interpretation. The discussion should explain what the data show, what model assumptions permit, what alternative explanations remain, and which tests would distinguish them. For this project, a statement such as “isolated sites suppress N–N coupling” must be framed as a literature-supported mechanistic rationale or hypothesis unless the calculated pathway directly demonstrates it in the current model.

### 6. Data, code, and protocols are part of the research record

Nature Portfolio requires materials, data, code, and associated protocols to be promptly available without undue qualifications. The minimum dataset must allow readers to interpret, verify, and extend the claims. ACS likewise strongly encourages public availability of research data. The project should therefore include raw calculation outputs, machine-readable processed tables, exact environment information, checksums or dataset identifiers, and a data-availability statement that does not imply data exist when they do not.

### 7. References must support claims, not inflate appearance

Nature Chemistry guidance requires numerical citations in sequence, complete article titles for long-form manuscripts, and no unpublished or under-review items without an available preprint. The manuscript should cite a small number of highly relevant sources for each claim. A target of 25–30 references is acceptable only if each reference is genuinely used and bibliographically verified; it should not be used to disguise weak original evidence.

### 8. Figures must be journal-ready and editable where required

Nature Chemistry guidance specifies sequential figure citation, at least 300 dpi, appropriate panel descriptions, readable labelling, and explanation of error bars or sample sizes where relevant. The present convergence figure is data-driven and embedded, but it should remain labelled as a diagnostic benchmark. The project should not create decorative band structures, DOS plots, charge-density maps, or free-energy diagrams without real underlying calculations.

### 9. Video material is supplementary guidance, not scientific authority

The selected YouTube lecture is useful for practical communication advice: IMRaD organisation, clear introductions, methods transparency, figures/tables, references, publication ethics, and reproducibility. It is not a peer-reviewed source and should not be cited as evidence for nitrate chemistry or DFT methodology. Its value is pedagogical: use it to improve structure and communication, while relying on publisher policies and peer-reviewed literature for scientific claims.

## Implications for the present project

The existing manuscript's principal weakness is not word count. It is that the research question, evidentiary hierarchy, and contribution are not sufficiently differentiated. A revision should choose a defensible article type, remove claims of a completed catalyst screen, report the executed benchmark as the central result, place all pending work in a clearly named future-production section, simplify the tables, and add an explicit claim-to-evidence audit. The project should be judged against a reviewer checklist rather than against a superficial target length.
