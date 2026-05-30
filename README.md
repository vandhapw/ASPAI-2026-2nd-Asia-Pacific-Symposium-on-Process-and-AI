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
python3 generate_dataset_figure.py
```
Figures are saved to `figures/` in both PDF and PNG formats.

## Project Structure
```
├── main.tex                      # Paper (CEUR-WS format, double-blind)
├── references.bib                # Bibliography (16 entries)
├── dataset_configs.py            # Central dataset configuration for all 6 event logs
├── generate_figures.py           # Result figures (cross-dataset comparison)
├── generate_dataset_figure.py   # Dataset illustration & Sepsis DFG figures
├── model_selection_experiment.py # Model selection justification experiments
├── model_selection_results.json   # Experiment results (per-dataset)
├── figures/                      # Generated figures (PDF + PNG)
│   ├── figure_architecture.*
│   ├── figure_dataset_illustration.*
│   ├── figure_sepsis_process_flow.*
│   ├── figure_semantic_validity.*
│   ├── figure_prediction_accuracy.*
│   ├── figure_ablation.*
│   ├── figure_diversity.*
│   ├── figure_cross_dataset_summary.*
│   └── (model selection figures from experiment)
└── README.md
```

## Datasets Evaluated
| Dataset | Domain | Cases | Activities | Variants | Variability |
|---------|--------|-------|-----------|----------|-------------|
| Sepsis | Healthcare | 1,050 | 16 | 830 | High |
| BPIC 2011 | Healthcare | 1,187 | 7 | 423 | Moderate |
| BPIC 2017 | Loan Application | 59,148 | 21 | 21,500 | Very High |
| BPIC 2020 | Municipality | 7,014 | 27 | 2,932 | Medium |
| Hospital Billing | Hospital | 100,000 | 18 | 1,000 | Medium |
| Road Traffic Fines | Government | 150,370 | 11 | 4 | Very Low |

## Key Results (2.0x Augmentation)
| Method | Sepsis | BPIC'11 | BPIC'17 | BPIC'20 | Hosp.Bill. | RTF |
|--------|--------|---------|---------|---------|-----------|-----|
| LLM Consensus (Ours) | **0.85** | **0.88** | **0.82** | **0.83** | **0.84** | **0.91** |
| Statistical Replace | 0.76 | 0.80 | 0.69 | 0.72 | 0.74 | 0.83 |
| LLM Single-Model | 0.68 | 0.73 | 0.63 | 0.66 | 0.65 | 0.78 |
| Random | 0.42 | 0.48 | 0.35 | 0.39 | 0.40 | 0.52 |