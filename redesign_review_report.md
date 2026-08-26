# Final redesign and deep-review report

## Why the earlier article was inadequate

The earlier manuscript was not weak primarily because it lacked words or references. Its central problem was that its presentation resembled a catalyst-discovery paper while its evidence consisted mainly of structure generation, geometry checks, numerical diagnostics, and a small number of incomplete optimisations. This created an evidence-to-claim mismatch. The manuscript has now been reframed as a reproducibility and numerical-validation benchmark.

## Research basis for the redesign

The revision was informed by ACS author guidance, Nature Portfolio reporting standards, Nature Chemistry formatting guidance, Chemistry Europe article expectations, chemistry-writing guidance from Washington University in St Louis, and a specialised DFT scientific-writing video from Siesta India. The sources consistently emphasise a precise contribution, standard article sections, methods that support reproduction, figures and tables embedded at the point of relevance, complete references, separate Supporting Information, accessible data/code/protocols, and conclusions that are directly supported by the results.

The specialised video was used only for communication and IMRaD guidance. It was not treated as a scientific source for nitrate chemistry or DFT methodology. Peer-reviewed literature and publisher guidance remain the sources for scientific and publication claims.

## Substantive changes

The title now identifies a reproducible periodic-DFT benchmark rather than implying an accomplished catalyst ranking. The abstract reports the actual audited structure counts and convergence ranges, then states the evidence boundary. The introduction ends with a testable methodological question and hypothesis. The Results section reports only direct or transparently derived observations. A new evidence hierarchy separates direct measurements, derived diagnostics, literature-supported context, and unsupported claims.

The main-text tables were redesigned to summarise the scientific message rather than reproduce unwieldy raw records. Full source data remain in machine-readable files and Supporting Information. The convergence figure is explicitly labelled as a total-energy diagnostic and not an adsorption or activity figure. A duplicate caption artefact was removed, long tables were compacted, and the LaTeX header was adjusted to reduce table overflow.

The project now also includes an article-writing research synthesis, whole-project quality gap analysis, article redesign specification, claim-to-evidence matrix, figure/table source inventory, production-readiness checklist, revised Supporting Information, and final PDF audit notes.

## Validation outcome

The final audit reports 4,132 words in the revised Markdown manuscript, 25 DOI links, 25 reference entries, 11 convergence rows, and zero geometry-audit failures for the 36 bare/support structures and 60 adsorbate inputs. Direct code tests pass for the chemistry utilities and VASP input generator. The revised source compiles twice with XeLaTeX to a 14-page PDF with zero fatal errors and three minor overfull-box warnings. The figure is present and its caption appears once.

## Final scientific boundary

The revised article is substantially stronger as a benchmark and reproducibility paper. It still cannot honestly be described as a completed nitrate-SAC catalyst-discovery paper. The full production evidence—converged 30-SAC optimisation, charged and solvated nitrate energetics, pathway intermediates, transition states, stability, HER competition, uncertainty, and selectivity analysis—does not exist in the repository. The manuscript now treats this absence as a defined evidence boundary rather than concealing it behind prose, references, or decorative figures.
