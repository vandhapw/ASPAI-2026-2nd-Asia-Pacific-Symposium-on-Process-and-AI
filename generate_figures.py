"""
Generate all result figures for the multi-dataset ASPAI 2026 paper.
Reads data from dataset_configs.py to produce cross-dataset comparison figures.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dataset_configs import DATASETS, DATASET_ORDER, DATASET_COLORS, METHODS, METHOD_SHORT_LABELS, METHOD_COLORS

output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figures')
os.makedirs(output_dir, exist_ok=True)

# ============================================================
# Figure 1: Architecture / Workflow Diagram (dataset-agnostic)
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(10, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

C_DEEPSEEK = '#1a73e8'
C_GLM = '#34a853'
C_KIMI = '#ea4335'
C_CONFORMANCE = '#fbbc04'
C_STATISTICAL = '#9334e6'
C_RANDOM = '#ff6d01'
C_ORIGINAL = '#5f6368'

rect1 = mpatches.FancyBboxPatch((0.5, 8.5), 2.5, 1.2, boxstyle="round,pad=0.1",
    facecolor='#e8f0fe', edgecolor=C_DEEPSEEK, linewidth=2)
ax.add_patch(rect1)
ax.text(1.75, 9.1, 'Original\nEvent Log $L$', ha='center', va='center', fontsize=10, fontweight='bold')

rect2 = mpatches.FancyBboxPatch((4, 8.5), 2.5, 1.2, boxstyle="round,pad=0.1",
    facecolor='#e8f0fe', edgecolor=C_DEEPSEEK, linewidth=2)
ax.add_patch(rect2)
ax.text(5.25, 9.1, 'Context\nExtraction', ha='center', va='center', fontsize=10, fontweight='bold')
ax.annotate('', xy=(4, 9.1), xytext=(3, 9.1), arrowprops=dict(arrowstyle='->', lw=1.5, color=C_DEEPSEEK))

rect3 = mpatches.FancyBboxPatch((7, 8.5), 2.5, 1.2, boxstyle="round,pad=0.1",
    facecolor='#d2e3fc', edgecolor=C_DEEPSEEK, linewidth=2)
ax.add_patch(rect3)
ax.text(8.25, 9.3, 'Trace Generation', ha='center', va='center', fontsize=10, fontweight='bold')
ax.text(8.25, 8.85, '(DeepSeek-R1)', ha='center', va='center', fontsize=9, color=C_DEEPSEEK)
ax.annotate('', xy=(7, 9.1), xytext=(6.5, 9.1), arrowprops=dict(arrowstyle='->', lw=1.5, color=C_DEEPSEEK))

ax.annotate('', xy=(8.25, 7.3), xytext=(8.25, 8.5), arrowprops=dict(arrowstyle='->', lw=1.5, color='#333'))

rect_verify = mpatches.FancyBboxPatch((3.5, 3.5), 5.5, 3.5, boxstyle="round,pad=0.15",
    facecolor='#fef7e0', edgecolor='#333', linewidth=2, linestyle='--')
ax.add_patch(rect_verify)
ax.text(6.25, 6.8, 'Multi-LLM Verification (2-of-3 Consensus)', ha='center', va='center',
    fontsize=11, fontweight='bold')

rect_v1 = mpatches.FancyBboxPatch((3.8, 4.8), 1.5, 1.5, boxstyle="round,pad=0.08",
    facecolor='#e6f4ea', edgecolor=C_GLM, linewidth=2)
ax.add_patch(rect_v1)
ax.text(4.55, 5.95, 'Structural', ha='center', va='center', fontsize=9, fontweight='bold')
ax.text(4.55, 5.5, 'Check', ha='center', va='center', fontsize=9, fontweight='bold')
ax.text(4.55, 5.1, '(GLM-4)', ha='center', va='center', fontsize=8, color=C_GLM)

rect_v2 = mpatches.FancyBboxPatch((5.5, 4.8), 1.5, 1.5, boxstyle="round,pad=0.08",
    facecolor='#fce8e6', edgecolor=C_KIMI, linewidth=2)
ax.add_patch(rect_v2)
ax.text(6.25, 5.95, 'Temporal', ha='center', va='center', fontsize=9, fontweight='bold')
ax.text(6.25, 5.5, 'Check', ha='center', va='center', fontsize=9, fontweight='bold')
ax.text(6.25, 5.1, '(Kimi-K2)', ha='center', va='center', fontsize=8, color=C_KIMI)

rect_v3 = mpatches.FancyBboxPatch((7.2, 4.8), 1.5, 1.5, boxstyle="round,pad=0.08",
    facecolor='#fef9e6', edgecolor=C_CONFORMANCE, linewidth=2)
ax.add_patch(rect_v3)
ax.text(7.95, 5.95, 'Conformance', ha='center', va='center', fontsize=9, fontweight='bold')
ax.text(7.95, 5.5, 'Check', ha='center', va='center', fontsize=9, fontweight='bold')
ax.text(7.95, 5.1, '(Petri Net)', ha='center', va='center', fontsize=8, color=C_CONFORMANCE)

ax.annotate('', xy=(6.25, 3.2), xytext=(6.25, 3.5), arrowprops=dict(arrowstyle='->', lw=1.5, color='#333'))

rect4 = mpatches.FancyBboxPatch((4.5, 2.0), 3.5, 1.2, boxstyle="round,pad=0.1",
    facecolor='#f3e8fd', edgecolor=C_STATISTICAL, linewidth=2)
ax.add_patch(rect4)
ax.text(6.25, 2.9, 'Consensus Filter', ha='center', va='center', fontsize=10, fontweight='bold')
ax.text(6.25, 2.4, '($\\geq$ 2 of 3 votes)', ha='center', va='center', fontsize=9)

ax.annotate('', xy=(6.25, 1.2), xytext=(6.25, 2.0), arrowprops=dict(arrowstyle='->', lw=1.5, color='#333'))

rect5 = mpatches.FancyBboxPatch((4, 0.0), 4.5, 1.2, boxstyle="round,pad=0.1",
    facecolor='#e8f5e9', edgecolor='#1b5e20', linewidth=2)
ax.add_patch(rect5)
ax.text(6.25, 0.9, 'Verified Augmented Traces', ha='center', va='center', fontsize=10, fontweight='bold')
ax.text(6.25, 0.4, '$S = \\{s_1, ..., s_k\\}$ (semantically valid)', ha='center', va='center', fontsize=9)

rect_s1 = mpatches.FancyBboxPatch((0.3, 5.5), 2.5, 1.0, boxstyle="round,pad=0.08",
    facecolor='#f3e8fd', edgecolor=C_STATISTICAL, linewidth=1.5)
ax.add_patch(rect_s1)
ax.text(1.55, 6.2, 'Statistical', ha='center', va='center', fontsize=9, fontweight='bold')
ax.text(1.55, 5.8, 'Augmentation', ha='center', va='center', fontsize=9, fontweight='bold')
ax.text(1.55, 5.4, '(Insert/Del/Replace)', ha='center', va='center', fontsize=8, color=C_STATISTICAL)

ax.annotate('', xy=(1.55, 6.5), xytext=(1.75, 8.5),
    arrowprops=dict(arrowstyle='->', lw=1.2, color=C_STATISTICAL, linestyle='--'))

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'figure_architecture.pdf'), dpi=300, bbox_inches='tight')
plt.savefig(os.path.join(output_dir, 'figure_architecture.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Figure 1 (architecture) saved.")

# ============================================================
# Figure 2: Semantic Validity Comparison (Cross-Dataset)
# ============================================================
key_methods = ["random", "stat_insert", "stat_delete", "stat_replace", "llm_single", "llm_consensus"]
method_labels_short = ["Random", "Stat.\nInsert", "Stat.\nDelete", "Stat.\nReplace", "LLM\nSingle", "LLM\nConsensus"]
method_bar_colors = [C_RANDOM, C_STATISTICAL, C_STATISTICAL, C_STATISTICAL, C_DEEPSEEK, '#1b5e20']

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

metrics = ["fitness", "trans_validity", "activity_coverage"]
metric_labels = ["Conformance Fitness", "Transition Validity Rate", "Activity Coverage"]

for ax_idx, (metric, label) in enumerate(zip(metrics, metric_labels)):
    x = np.arange(len(DATASET_ORDER))
    width = 0.12
    n_methods = len(key_methods)

    for m_idx, (method, m_label) in enumerate(zip(key_methods, method_labels_short)):
        values = [DATASETS[dk]["results"][metric][method] for dk in DATASET_ORDER]
        offset = (m_idx - n_methods / 2 + 0.5) * width
        bars = axes[ax_idx].bar(x + offset, values, width, label=m_label.replace('\n', ' '),
                                  color=method_bar_colors[m_idx], edgecolor='#333', linewidth=0.3)
        # Add value labels for LLM Consensus only (to avoid clutter)
        if method == "llm_consensus":
            for i, v in enumerate(values):
                axes[ax_idx].text(x[i] + offset, v + 0.01, f'{v:.2f}', ha='center', fontsize=6, fontweight='bold')

    # Add original baseline
    for dk_idx, dk in enumerate(DATASET_ORDER):
        axes[ax_idx].plot([dk_idx - 0.45, dk_idx + 0.45], [1.0, 1.0],
                          color=C_ORIGINAL, linewidth=1.2, linestyle='--', alpha=0.6)

    ds_labels = [DATASETS[dk]["short_name"] for dk in DATASET_ORDER]
    axes[ax_idx].set_xticks(x)
    axes[ax_idx].set_xticklabels(ds_labels, fontsize=8)
    axes[ax_idx].set_ylabel(label, fontsize=9)
    axes[ax_idx].set_ylim(0, 1.15)
    if ax_idx == 1:
        axes[ax_idx].legend(fontsize=6, loc='lower left', ncol=2)

plt.suptitle('Semantic Validity Metrics Across Six Event Logs (2.0x Augmentation)', fontsize=12, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'figure_semantic_validity.pdf'), dpi=300, bbox_inches='tight')
plt.savefig(os.path.join(output_dir, 'figure_semantic_validity.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Figure 2 (semantic validity) saved.")

# ============================================================
# Figure 3: Prediction Accuracy (Cross-Dataset)
# ============================================================
fig, ax = plt.subplots(figsize=(10, 5))

key_methods_acc = ["random", "stat_insert", "stat_delete", "stat_replace", "llm_single", "llm_consensus"]
method_labels_acc = ["Random", "Stat. Insert", "Stat. Delete", "Stat. Replace", "LLM Single", "LLM Consensus"]
method_colors_acc = [C_RANDOM, C_STATISTICAL, C_STATISTICAL, C_STATISTICAL, C_DEEPSEEK, '#1b5e20']

x = np.arange(len(DATASET_ORDER))
width = 0.12
n_methods = len(key_methods_acc)

for m_idx, (method, m_label, m_color) in enumerate(zip(key_methods_acc, method_labels_acc, method_colors_acc)):
    values = [DATASETS[dk]["results"]["accuracy"][method] for dk in DATASET_ORDER]
    offset = (m_idx - n_methods / 2 + 0.5) * width
    bars = ax.bar(x + offset, values, width, label=m_label, color=m_color, edgecolor='#333', linewidth=0.3)
    if method == "llm_consensus":
        for i, v in enumerate(values):
            ax.text(x[i] + offset, v + 0.005, f'{v:.3f}', ha='center', fontsize=6.5, fontweight='bold')

# Add original baseline
for dk_idx, dk in enumerate(DATASET_ORDER):
    orig = DATASETS[dk]["results"]["accuracy"]["original"]
    ax.plot([dk_idx - 0.5, dk_idx + 0.5], [orig, orig],
            color=C_ORIGINAL, linewidth=1.2, linestyle='--', alpha=0.6)

ds_labels = [DATASETS[dk]["short_name"] for dk in DATASET_ORDER]
ax.set_xticks(x)
ax.set_xticklabels(ds_labels, fontsize=9)
ax.set_ylabel('Next-Activity Prediction Accuracy', fontsize=11)
ax.set_ylim(0.4, 1.0)
ax.legend(fontsize=8, loc='upper right')
ax.axhline(y=0.543, color=C_ORIGINAL, linestyle=':', linewidth=0.8, alpha=0.4)

plt.title('Next-Activity Prediction Accuracy Across Six Event Logs (2.0x Augmentation)', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'figure_prediction_accuracy.pdf'), dpi=300, bbox_inches='tight')
plt.savefig(os.path.join(output_dir, 'figure_prediction_accuracy.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Figure 3 (prediction accuracy) saved.")

# ============================================================
# Figure 4: Ablation Study (Cross-Dataset)
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

ablation_configs = ["full", "without_glm", "without_kimi", "without_conformance", "single_model"]
ablation_labels = ["Full\nConsensus\n(2-of-3)", "Without\nGLM\n(structural)", "Without\nKimi\n(temporal)",
                   "Without\nConformance\n(programmatic)", "Single-Model\nOnly\n(DeepSeek)"]
ablation_colors = ['#1b5e20', '#ea4335', '#fbbc04', '#9334e6', '#1a73e8']

# Panel A: Fitness
x = np.arange(len(DATASET_ORDER))
width = 0.15
n_configs = len(ablation_configs)

for c_idx, (config, c_label, c_color) in enumerate(zip(ablation_configs, ablation_labels, ablation_colors)):
    values = [DATASETS[dk]["results"]["ablation"][config]["fitness"] for dk in DATASET_ORDER]
    offset = (c_idx - n_configs / 2 + 0.5) * width
    axes[0].bar(x + offset, values, width, label=c_label.replace('\n', ' '), color=c_color, edgecolor='#333', linewidth=0.3)

ds_labels = [DATASETS[dk]["short_name"] for dk in DATASET_ORDER]
axes[0].set_xticks(x)
axes[0].set_xticklabels(ds_labels, fontsize=8)
axes[0].set_ylabel('Conformance Fitness', fontsize=10)
axes[0].set_ylim(0.5, 1.05)
axes[0].legend(fontsize=6, loc='lower left', ncol=2)

# Panel B: Accuracy
for c_idx, (config, c_label, c_color) in enumerate(zip(ablation_configs, ablation_labels, ablation_colors)):
    values = [DATASETS[dk]["results"]["ablation"][config]["accuracy"] for dk in DATASET_ORDER]
    offset = (c_idx - n_configs / 2 + 0.5) * width
    axes[1].bar(x + offset, values, width, label=c_label.replace('\n', ' '), color=c_color, edgecolor='#333', linewidth=0.3)

axes[1].set_xticks(x)
axes[1].set_xticklabels(ds_labels, fontsize=8)
axes[1].set_ylabel('Prediction Accuracy', fontsize=10)
axes[1].set_ylim(0.5, 1.0)
axes[1].legend(fontsize=6, loc='lower left', ncol=2)

plt.suptitle('Ablation Study: Contribution of Each Verification Component Across Six Event Logs (2.0x)', fontsize=11, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'figure_ablation.pdf'), dpi=300, bbox_inches='tight')
plt.savefig(os.path.join(output_dir, 'figure_ablation.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Figure 4 (ablation) saved.")

# ============================================================
# Figure 5: Augmentation Diversity (Cross-Dataset)
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

div_methods = ["random", "stat_insert", "stat_delete", "stat_replace", "llm_consensus"]
div_labels = ["Random", "Stat. Insert", "Stat. Delete", "Stat. Replace", "LLM Consensus"]
div_colors = [C_RANDOM, C_STATISTICAL, C_STATISTICAL, C_STATISTICAL, '#1b5e20']

# Panel A: Trace Entropy
x = np.arange(len(DATASET_ORDER))
width = 0.14
n_div = len(div_methods)

for m_idx, (method, m_label, m_color) in enumerate(zip(div_methods, div_labels, div_colors)):
    values = [DATASETS[dk]["results"]["diversity"]["trace_entropy"][method] for dk in DATASET_ORDER]
    offset = (m_idx - n_div / 2 + 0.5) * width
    axes[0].bar(x + offset, values, width, label=m_label, color=m_color, edgecolor='#333', linewidth=0.3)

ds_labels = [DATASETS[dk]["short_name"] for dk in DATASET_ORDER]
axes[0].set_xticks(x)
axes[0].set_xticklabels(ds_labels, fontsize=9)
axes[0].set_ylabel('Trace Entropy', fontsize=10)
axes[0].legend(fontsize=7, loc='upper right')

# Panel B: Novel Variants
for m_idx, (method, m_label, m_color) in enumerate(zip(div_methods, div_labels, div_colors)):
    values = [DATASETS[dk]["results"]["diversity"]["novel_variants"][method] for dk in DATASET_ORDER]
    offset = (m_idx - n_div / 2 + 0.5) * width
    axes[1].bar(x + offset, values, width, label=m_label, color=m_color, edgecolor='#333', linewidth=0.3)

axes[1].set_xticks(x)
axes[1].set_xticklabels(ds_labels, fontsize=9)
axes[1].set_ylabel('Novel Variants', fontsize=10)
axes[1].legend(fontsize=7, loc='upper right')

plt.suptitle('Augmentation Diversity Metrics Across Six Event Logs (2.0x)', fontsize=11, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'figure_diversity.pdf'), dpi=300, bbox_inches='tight')
plt.savefig(os.path.join(output_dir, 'figure_diversity.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Figure 5 (diversity) saved.")

# ============================================================
# Figure 6: Cross-Dataset Improvement Summary
# ============================================================
fig, ax = plt.subplots(figsize=(10, 5))

improvement_metrics = {
    "Fitness Gain": lambda dk: DATASETS[dk]["results"]["fitness"]["llm_consensus"] - DATASETS[dk]["results"]["fitness"]["random"],
    "Accuracy Gain (pp)": lambda dk: (DATASETS[dk]["results"]["accuracy"]["llm_consensus"] - DATASETS[dk]["results"]["accuracy"]["original"]) * 100,
    "Novel Variants": lambda dk: DATASETS[dk]["results"]["diversity"]["novel_variants"]["llm_consensus"],
}

x = np.arange(len(DATASET_ORDER))
width = 0.25
colors_summary = ['#1a73e8', '#34a853', '#ea4335']

for m_idx, (metric_name, fn) in enumerate(improvement_metrics.items()):
    values = [fn(dk) for dk in DATASET_ORDER]
    # Normalize for visualization (scale to 0-1 range)
    if metric_name == "Novel Variants":
        max_val = max(values) if max(values) > 0 else 1
        normalized = [v / max_val for v in values]
        display_vals = values
    elif metric_name == "Accuracy Gain (pp)":
        normalized = [v / 5.0 for v in values]  # scale: 5pp = 1.0
        display_vals = values
    else:
        normalized = values  # already 0-1
        display_vals = [f'{v:.2f}' for v in values]

    bars = ax.bar(x + (m_idx - 1) * width, values, width, label=metric_name,
                   color=colors_summary[m_idx], edgecolor='#333', linewidth=0.5)
    for i, v in enumerate(values):
        fmt = f'{v:.1f}' if v >= 10 else f'{v:.2f}'
        ax.text(x[i] + (m_idx - 1) * width, v + 0.5, fmt, ha='center', fontsize=7, fontweight='bold')

ds_labels = [DATASETS[dk]["short_name"] for dk in DATASET_ORDER]
ax.set_xticks(x)
ax.set_xticklabels(ds_labels, fontsize=10)
ax.set_ylabel('Improvement Value', fontsize=11)
ax.legend(fontsize=9)
ax.set_title('Cross-Dataset Improvement from LLM Consensus Augmentation (2.0x)', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'figure_cross_dataset_summary.pdf'), dpi=300, bbox_inches='tight')
plt.savefig(os.path.join(output_dir, 'figure_cross_dataset_summary.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Figure 6 (cross-dataset summary) saved.")

print(f"\nAll figures saved to: {output_dir}")