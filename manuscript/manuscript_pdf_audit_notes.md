# Manuscript PDF audit notes

## Visual inspection status

The rebuilt manuscript PDF renders successfully as an 18-page document. Pages 1–5 show that the title, abstract, section headings, body text, and embedded tables are present and legible. The chemical formulas and subscripts now render visibly in the PDF rather than causing compilation failure.

## Issues observed

The table beginning in Section 2 is split across pages 4–5 and is readable, but some columns are tightly packed and require a targeted layout audit in the LaTeX source. The manuscript therefore compiles successfully, yet some table widths are close to the page limit and may need column simplification or landscape handling for cleaner journal submission.

## Immediate conclusions

1. The manuscript now exceeds the user's minimum length requirement and compiles.
2. At least one figure is embedded in the manuscript PDF.
3. The PDF is suitable for further line-by-line scientific and bibliographic audit, but not yet the final polished submission layout.

## Remaining audit tasks

- Inspect later manuscript pages for figure placement, reference list completeness, and any table clipping.
- Cross-check all references against the DOI-validated bibliography.
- Reconcile any manuscript claims that exceed executed evidence.
- Improve table layout where needed while preserving scientific accuracy.

## Additional visual findings from pages 6–10

Pages 6–8 render the methods and equation sections correctly. The adsorption-energy and CHE equations are now typeset as display mathematics and no longer fail compilation. Page 9 shows the structural-inventory table; it is present and readable, although the rightmost interpretation column is compressed. Page 10 shows the convergence table and its caption text, but the actual raster figure has not yet appeared within the inspected page set, indicating that figure placement may have been deferred to a later page by LaTeX.

The tables are scientifically intact but visually dense. The main layout issue is not missing data; it is table width and tight line wrapping. This will need a targeted manuscript-layout correction if a cleaner journal-style PDF is required.

## Additional visual findings from pages 11–15

Page 11 confirms that the convergence figure is embedded successfully in the manuscript PDF. The three-panel benchmark plot is visible and legible, with a caption beneath it. Page 12 contains the coarse-optimisation summary table; the content is present, but the columns remain cramped and would benefit from layout simplification. Pages 13–15 render the interpretation, reproducibility, limitations, and conclusions sections correctly, with no missing equations or obvious text corruption.

At this stage, the manuscript is scientifically readable and structurally complete through the conclusions. The principal remaining PDF-inspection task is the reference pages and any end-matter formatting on pages 16–18.

## Final visual findings from pages 16–18

The 25-reference list renders across pages 16–18 and all entries have visible DOI links. No duplicate reference number is visible after replacing the former duplicate. Reference entries [1]–[25] are present. Some long titles and DOI strings approach the right margin, but they remain readable. The manuscript therefore has a complete 25-reference bibliography in the compiled PDF.

The bibliography still contains abbreviated author lists using `et al.` for several records; this is acceptable only if consistent with the selected journal style. Before submission, the target journal's preferred author truncation convention should be applied uniformly. The DOI-validated bibliography file remains the provenance source.
