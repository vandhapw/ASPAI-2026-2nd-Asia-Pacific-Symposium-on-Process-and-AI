# Multi-LLM Consensus for Semantic-Preserving Event Log Augmentation

Paper submitted to ASPAI 2026 (2nd Asia-Pacific Symposium on Process and Artificial Intelligence), poster track.

## Compilation

### Overleaf (Recommended)
1. Open this project in Overleaf
2. Uncomment `\documentclass[ceurws-v2022]{ceurart}` and comment out `\documentclass[11pt,a4paper]{article}` in `main.tex`
3. Remove the `\newcommand` stubs for CEUR-WS commands
4. The `ceurart` class is available in Overleaf's template gallery

### Local Compilation
```bash
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

### Generate Figures
```bash
python3 generate_figures.py
```
Figures are saved to `figures/` in both PDF and PNG formats.

## Project Structure
```
├── main.tex              # Paper (CEUR-WS format, double-blind)
├── references.bib        # Bibliography
├── generate_figures.py   # Figure generation script
├── figures/              # Generated figures (PDF + PNG)
│   ├── figure_architecture.pdf/png
│   ├── figure_semantic_validity.pdf/png
│   ├── figure_prediction_accuracy.pdf/png
│   ├── figure_ablation.pdf/png
│   └── figure_diversity.pdf/png
└── README.md
```

## Key Results (Sepsis Dataset, 2.0x Augmentation)
| Method | Fitness | Trans. Validity | Accuracy |
|--------|---------|----------------|----------|
| LLM Consensus (Ours) | 0.85 | 0.79 | 0.589 |
| Statistical Replace | 0.76 | 0.70 | 0.576 |
| LLM Single-Model | 0.68 | 0.61 | 0.562 |
| Random | 0.42 | 0.38 | 0.487 |