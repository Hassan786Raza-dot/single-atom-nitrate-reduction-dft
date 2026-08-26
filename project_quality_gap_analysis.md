# Whole-project quality gap analysis

## Overall verdict

The existing project is organised and unusually transparent about its computational limitations, but it is not yet a strong original research article. Its central weakness is **evidence-to-contribution mismatch**. The current package contains a workflow, starting geometries, a compact convergence benchmark, and diagnostic GPAW runs. It does not contain the converged catalyst screen, chemically consistent adsorption thermochemistry, complete reaction network, transition-state evidence, or experimental validation needed to support a catalyst-discovery claim.

The manuscript is therefore neither a conventional full research paper nor a fully developed methods paper. It currently sits between a project report, a reproducibility note, and a planned computational study. Improving prose alone will not solve this. The scientific object of the paper must be redefined, or the missing production calculations must be executed on suitable hardware.

## Benchmark criteria derived from external guidance

| Criterion | Standard derived from guidance and strong papers | Current status | Severity |
|---|---|---|---|
| Novel contribution | One precise, testable contribution supported by original evidence | Workflow and benchmark contribution is present; catalyst-discovery contribution is not | Critical |
| Research question | Specific gap, hypothesis, and decision criterion | Broad support/metal screen is described, but no final hypothesis or preregistered ranking criterion | High |
| Methods | Sufficient detail to reproduce every reported result | Input and audit workflow is strong; production DFT settings and charged/solvated calculations are absent | Critical |
| Results | Original, validated observations before interpretation | Results are mostly file audits and numerical diagnostics | Critical for catalyst paper |
| Discussion | Separates observations, inference, alternative explanations, and limitations | Improved, but still longer than the evidence base warrants | Medium |
| Data/code | Minimum dataset, raw outputs, software versions, and protocols accessible | Strong for current diagnostics; incomplete for the intended production study | High |
| Figures | Each figure answers a scientific question and is traceable to source data | One diagnostic figure is valid; the paper lacks scientific result figures | High |
| Tables | Tables are complete, readable, and tied to claims | Input and convergence tables exist; no activity, stability, pathway, or uncertainty tables | Critical for catalyst paper |
| References | Complete, relevant, sequential, and used to support claims | 25 DOI-resolving references exist; some author metadata and source-to-claim matching need manual refinement | Medium |
| Journal fit | Article type and length match contribution and journal scope | Formatting resembles a paper, but the evidence level does not match a Q1 catalyst article | Critical |

## Article-level weaknesses

### Title and abstract

The title is too long and promises “screening” even though no scientifically accepted screening result is reported. It should either be changed to a methodological title such as “A reproducible periodic-DFT benchmark for modelling nitrate electroreduction on two-dimensional single-atom sites” or be retained only after the 30-model screen is actually completed. The abstract contains many methodological nouns but does not present one central quantitative result with an uncertainty or decision threshold. For a workflow paper, the abstract should state the number of structures audited, the exact convergence finding, the software route, and the practical reproducibility contribution. For a catalyst paper, it must instead report validated adsorption/pathway metrics and the principal catalyst insight.

### Introduction

The introduction currently contains sound background but is still a catalogue of nitrate pollution, ammonia, SACs, 2D supports, CHE, and solvation. A stronger introduction should end with a narrow unresolved problem. The best current gap is not “which of 30 metals is best?” because the project has not yet generated evidence for that question. It is: **how can a matched 2D-SAC nitrate-reduction screen be made interpretable when support reconstruction, spin, numerical settings, charged nitrate, and potential dependence are coupled?** The introduction should state this as a methodological hypothesis and explain why a compact audit benchmark is informative.

### Methods

The methods describe a recommended production protocol more extensively than they report what was actually executed. A reviewer needs a clear split between “executed calculations” and “planned production protocol”. The current document should use explicit labels such as `EXECUTED`, `DIAGNOSTIC`, `INPUT_ONLY`, and `NOT_RUN` in both prose and tables. The code version, dataset identity, numerical mode, cutoff, k-points, smearing, spin, optimisation thresholds, and run identifiers should appear beside every reported energy.

The current protocol also risks overpromising solvation. GPAW execution is verified, but the completed diagnostics are not a validated implicit-solvent nitrate campaign. Any sentence that sounds as though solvent-corrected nitrate energetics exist must be removed or rewritten as a planned check. Similarly, the 15 Å vacuum rule is a starting criterion, not evidence that the slab electrostatics are converged.

### Results

The Results section is dominated by quality control. That is valid for a reproducibility note but not for a catalyst article. The current convergence plot uses absolute total energies across settings. This is useful for exposing implementation sensitivity, but it is not an activity result and should be presented as a diagnostic figure. A stronger benchmark would also report observable-level convergence: adsorption-energy differences, relaxed bond lengths, residual forces, magnetic moments, and the change in a CHE free-energy step across numerical settings.

The structural inventory is not a chemical result. Passing a minimum-distance and vacuum audit confirms that files are usable starting inputs. It does not confirm that the metal remains isolated, that the defect is stable, that the support is realistic, or that the nitrate geometry is a valid aqueous adsorption state. The manuscript mostly says this, but the article architecture should make the distinction impossible to miss.

### Discussion and conclusion

The discussion is scientifically cautious, which is a strength, but it currently spends many paragraphs explaining why results are missing. A publishable paper should instead make the benchmark itself the contribution and move the unexecuted catalyst study to a short “scope and next stage” section. The conclusion should not sound like a completed discovery paper. It should state the validated benchmark finding, its reproducibility value, and the exact boundary of inference.

## Project-level weaknesses

### No final research dataset

The project has starting structures and diagnostic logs but no accepted production dataset for formation energies, adsorption energies, reaction free energies, transition states, descriptors, or selectivity. The empty templates are valuable controls, but they also prove that the intended scientific output is not present.

### Insufficient computational design for charged nitrate

Nitrate is an anion. A neutral visual starting geometry cannot be interpreted as a nitrate adsorption energy without a stated charge/compensation convention and a thermodynamic reference. The project must either implement and validate a consistent charged/solvated approach or remove nitrate energetics from the paper. CHE corrections alone do not solve all potential-dependent adsorption effects.

### No support-stability hierarchy

The starting supports and defects are generated procedurally, but the project does not yet compare defect formation, metal binding, alternative coordination, migration, aggregation, dissolution, or reconstruction. A 30-model ranking would be chemically misleading without a stability gate.

### No real mechanism or kinetics

The project discusses nitrate-to-ammonia pathways but does not yet calculate a complete pathway, transition states, coverage effects, or microkinetics. A nitrate adsorption descriptor cannot establish ammonia selectivity. The literature shows that nitrate-to-nitrite and nitrite-to-ammonia chemistry can be coupled and that the rate/selectivity outcome depends on multiple intermediates and competing hydrogen chemistry.

### Weak original-figure portfolio

A Q1 computational electrocatalysis paper would normally require a coherent figure sequence: model/site structures, convergence evidence, stability map, adsorption/descriptor map, free-energy pathway, spin/charge analysis, and ideally a microkinetic or uncertainty analysis. Creating these figures without the underlying calculations would be worse than having one honest diagnostic figure. The next priority is therefore data generation, not graphic decoration.

### Journal mismatch

ACS and Nature Portfolio guidance emphasise standard sections, complete reproducible methods, embedded figures/tables, supporting information, and data availability. These formatting requirements are now largely satisfied. The missing element is not presentation; it is the original evidence required for the claim. The current paper is better framed for a computational workflow/reproducibility venue than for a high-impact catalyst-discovery journal.

## Recommended redesign

The project should choose one of two legitimate routes.

| Route | Central paper claim | Required evidence | Feasibility in current sandbox |
|---|---|---|---|
| Benchmark/workflow paper | A reproducible audit framework exposes how numerical and model choices affect 2D-SAC nitrate-screening readiness | More observable-level convergence, code/data package, clear benchmark metrics, and comparison with accepted reporting practice | Plausible after focused reanalysis |
| Catalyst-discovery paper | A specific SAC/support combination improves nitrate-to-ammonia energetics/selectivity | Full converged matrix, charge/solvation, pathway, transition states, stability, uncertainty, and preferably experiment | Not feasible with current resources |

The first route is the only route that can be completed honestly in the present environment. It should be written as a compact, sharply argued benchmark article rather than as a failed catalyst screen. The title, abstract, figure sequence, results, and conclusion must all use the benchmark contribution consistently.

## Non-negotiable revision rules

1. Do not call the 30 models “screened” unless a declared screening observable has been calculated and audited for each model.
2. Do not call a structure “stable” based only on a negative atom-binding energy.
3. Do not call a nitrate starting geometry an adsorption result.
4. Do not call a total-energy convergence plot an adsorption-energy convergence test.
5. Do not infer ammonia selectivity from nitrate adsorption alone.
6. Do not describe GPAW diagnostics as VASP calculations.
7. Do not use a YouTube video as evidence for chemistry or DFT methodology; use it only as writing guidance.
8. Do not increase the reference count to compensate for missing original evidence.
9. Do not create free-energy, DOS, charge-density, or catalyst-ranking figures without real source data.
10. State the exact accepted contribution in the title, abstract, first paragraph of Results, and conclusion.

## Proposed new article architecture

1. **Title:** A reproducible periodic-DFT benchmark for nitrate-electroreduction modelling on two-dimensional single-atom sites.
2. **Abstract:** Problem, methodological gap, executed benchmark, quantitative findings, reproducibility output, and boundary of inference.
3. **Introduction:** Nitrate electroreduction challenge; why SAC/2D models are attractive; why numerical/electrochemical controls matter; precise hypothesis.
4. **Results 1:** Model construction and structural audit.
5. **Results 2:** Observable-level numerical convergence and sensitivity.
6. **Results 3:** Cross-code/input reproducibility and calculation-status taxonomy.
7. **Results 4:** What the benchmark permits and does not permit in a nitrate SAC screen.
8. **Discussion:** Relation to published nitrate and SAC studies; implications for reporting and model selection.
9. **Methods:** Fully reproducible environment, structure generation, GPAW calculations, VASP-compatible files, parsing, audit tests.
10. **Data availability and limitations:** Exact files, raw outputs, and missing production evidence.
11. **Conclusion:** One or two validated benchmark conclusions, not a catalyst ranking.

This architecture will make the paper smaller in claim, stronger in logic, and easier for reviewers to evaluate.
