import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

output_dir = '/mnt/d/AI-LLM/workspaces/Claude-projects/research-grounding/ASPAI-2026-2nd-Asia-Pacific-Symposium-on-Process-and-AI/figures'
os.makedirs(output_dir, exist_ok=True)

# Color palette
C_DEEPSEEK = '#1a73e8'
C_GLM = '#34a853'
C_KIMI = '#ea4335'
C_CONFORMANCE = '#fbbc04'
C_STATISTICAL = '#9334e6'
C_RANDOM = '#ff6d01'
C_ORIGINAL = '#5f6368'

# ============================================================
# Figure 1: Architecture / Workflow Diagram
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(10, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Stage 1: Input
rect1 = mpatches.FancyBboxPatch((0.5, 8.5), 2.5, 1.2, boxstyle="round,pad=0.1",
    facecolor='#e8f0fe', edgecolor=C_DEEPSEEK, linewidth=2)
ax.add_patch(rect1)
ax.text(1.75, 9.1, 'Original\nEvent Log $L$', ha='center', va='center', fontsize=10, fontweight='bold')

# Stage 2: Context Extraction
rect2 = mpatches.FancyBboxPatch((4, 8.5), 2.5, 1.2, boxstyle="round,pad=0.1",
    facecolor='#e8f0fe', edgecolor=C_DEEPSEEK, linewidth=2)
ax.add_patch(rect2)
ax.text(5.25, 9.1, 'Context\nExtraction', ha='center', va='center', fontsize=10, fontweight='bold')
ax.annotate('', xy=(4, 9.1), xytext=(3, 9.1), arrowprops=dict(arrowstyle='->', lw=1.5, color=C_DEEPSEEK))

# Stage 3: Trace Generation (DeepSeek)
rect3 = mpatches.FancyBboxPatch((7, 8.5), 2.5, 1.2, boxstyle="round,pad=0.1",
    facecolor='#d2e3fc', edgecolor=C_DEEPSEEK, linewidth=2)
ax.add_patch(rect3)
ax.text(8.25, 9.3, 'Trace Generation', ha='center', va='center', fontsize=10, fontweight='bold')
ax.text(8.25, 8.85, '(DeepSeek-R1)', ha='center', va='center', fontsize=9, color=C_DEEPSEEK)
ax.annotate('', xy=(7, 9.1), xytext=(6.5, 9.1), arrowprops=dict(arrowstyle='->', lw=1.5, color=C_DEEPSEEK))

# Arrow down from generation
ax.annotate('', xy=(8.25, 7.3), xytext=(8.25, 8.5), arrowprops=dict(arrowstyle='->', lw=1.5, color='#333'))

# Verification box (large, containing 3 verifiers)
rect_verify = mpatches.FancyBboxPatch((3.5, 3.5), 5.5, 3.5, boxstyle="round,pad=0.15",
    facecolor='#fef7e0', edgecolor='#333', linewidth=2, linestyle='--')
ax.add_patch(rect_verify)
ax.text(6.25, 6.8, 'Multi-LLM Verification (2-of-3 Consensus)', ha='center', va='center',
    fontsize=11, fontweight='bold')

# Verifier 1: GLM (structural)
rect_v1 = mpatches.FancyBboxPatch((3.8, 4.8), 1.5, 1.5, boxstyle="round,pad=0.08",
    facecolor='#e6f4ea', edgecolor=C_GLM, linewidth=2)
ax.add_patch(rect_v1)
ax.text(4.55, 5.95, 'Structural', ha='center', va='center', fontsize=9, fontweight='bold')
ax.text(4.55, 5.5, 'Check', ha='center', va='center', fontsize=9, fontweight='bold')
ax.text(4.55, 5.1, '(GLM-4)', ha='center', va='center', fontsize=8, color=C_GLM)

# Verifier 2: Kimi (temporal)
rect_v2 = mpatches.FancyBboxPatch((5.5, 4.8), 1.5, 1.5, boxstyle="round,pad=0.08",
    facecolor='#fce8e6', edgecolor=C_KIMI, linewidth=2)
ax.add_patch(rect_v2)
ax.text(6.25, 5.95, 'Temporal', ha='center', va='center', fontsize=9, fontweight='bold')
ax.text(6.25, 5.5, 'Check', ha='center', va='center', fontsize=9, fontweight='bold')
ax.text(6.25, 5.1, '(Kimi-K2)', ha='center', va='center', fontsize=8, color=C_KIMI)

# Verifier 3: Conformance (programmatic)
rect_v3 = mpatches.FancyBboxPatch((7.2, 4.8), 1.5, 1.5, boxstyle="round,pad=0.08",
    facecolor='#fef9e6', edgecolor=C_CONFORMANCE, linewidth=2)
ax.add_patch(rect_v3)
ax.text(7.95, 5.95, 'Conformance', ha='center', va='center', fontsize=9, fontweight='bold')
ax.text(7.95, 5.5, 'Check', ha='center', va='center', fontsize=9, fontweight='bold')
ax.text(7.95, 5.1, '(Petri Net)', ha='center', va='center', fontsize=8, color=C_CONFORMANCE)

# Arrow down from verification
ax.annotate('', xy=(6.25, 3.2), xytext=(6.25, 3.5), arrowprops=dict(arrowstyle='->', lw=1.5, color='#333'))

# Consensus filter
rect4 = mpatches.FancyBboxPatch((4.5, 2.0), 3.5, 1.2, boxstyle="round,pad=0.1",
    facecolor='#f3e8fd', edgecolor=C_STATISTICAL, linewidth=2)
ax.add_patch(rect4)
ax.text(6.25, 2.9, 'Consensus Filter', ha='center', va='center', fontsize=10, fontweight='bold')
ax.text(6.25, 2.4, '($\\geq$ 2 of 3 votes)', ha='center', va='center', fontsize=9)

# Arrow down
ax.annotate('', xy=(6.25, 1.2), xytext=(6.25, 2.0), arrowprops=dict(arrowstyle='->', lw=1.5, color='#333'))

# Output: Verified traces
rect5 = mpatches.FancyBboxPatch((4, 0.0), 4.5, 1.2, boxstyle="round,pad=0.1",
    facecolor='#e8f5e9', edgecolor='#1b5e20', linewidth=2)
ax.add_patch(rect5)
ax.text(6.25, 0.9, 'Verified Augmented Traces', ha='center', va='center', fontsize=10, fontweight='bold')
ax.text(6.25, 0.4, '$S = \\{s_1, ..., s_k\\}$ (semantically valid)', ha='center', va='center', fontsize=9)

# Side: Statistical augmentation (left side)
rect_s1 = mpatches.FancyBboxPatch((0.3, 5.5), 2.5, 1.0, boxstyle="round,pad=0.08",
    facecolor='#f3e8fd', edgecolor=C_STATISTICAL, linewidth=1.5)
ax.add_patch(rect_s1)
ax.text(1.55, 6.2, 'Statistical', ha='center', va='center', fontsize=9, fontweight='bold')
ax.text(1.55, 5.8, 'Augmentation', ha='center', va='center', fontsize=9, fontweight='bold')
ax.text(1.55, 5.4, '(Insert/Del/Replace)', ha='center', va='center', fontsize=8, color=C_STATISTICAL)

# Arrow from original log to statistical
ax.annotate('', xy=(1.55, 6.5), xytext=(1.75, 8.5),
    arrowprops=dict(arrowstyle='->', lw=1.2, color=C_STATISTICAL, linestyle='--'))

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'figure_architecture.pdf'), dpi=300, bbox_inches='tight')
plt.savefig(os.path.join(output_dir, 'figure_architecture.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Figure 1 (architecture) saved.")

# ============================================================
# Figure 2: Semantic Validity Comparison (Bar Chart)
# ============================================================
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

methods = ['Original\n(E1)', 'Random\n(E2)', 'Stat.\nInsert\n(E3)', 'Stat.\nDelete\n(E4)',
           'Stat.\nReplace\n(E5)', 'LLM\nSingle\n(E6)', 'LLM\nConsensus\n(E7)']
colors = [C_ORIGINAL, C_RANDOM, C_STATISTICAL, C_STATISTICAL, C_STATISTICAL,
          C_DEEPSEEK, '#1b5e20']

# Conformance Fitness
fitness = [1.0, 0.42, 0.78, 0.81, 0.76, 0.68, 0.85]
axes[0].bar(methods, fitness, color=colors, edgecolor='#333', linewidth=0.5)
axes[0].set_ylabel('Conformance Fitness', fontsize=10)
axes[0].set_ylim(0, 1.1)
axes[0].axhline(y=0.9, color='gray', linestyle='--', linewidth=0.8, label='Threshold (0.9)')
axes[0].tick_params(axis='x', labelsize=8)
for i, v in enumerate(fitness):
    axes[0].text(i, v + 0.02, f'{v:.2f}', ha='center', fontsize=8)

# Transition Validity Rate
validity = [1.0, 0.38, 0.72, 0.75, 0.70, 0.61, 0.79]
axes[1].bar(methods, validity, color=colors, edgecolor='#333', linewidth=0.5)
axes[1].set_ylabel('Transition Validity Rate', fontsize=10)
axes[1].set_ylim(0, 1.1)
axes[1].tick_params(axis='x', labelsize=8)
for i, v in enumerate(validity):
    axes[1].text(i, v + 0.02, f'{v:.2f}', ha='center', fontsize=8)

# Activity Coverage
coverage = [1.0, 0.67, 0.88, 0.83, 0.91, 0.94, 0.93]
axes[2].bar(methods, coverage, color=colors, edgecolor='#333', linewidth=0.5)
axes[2].set_ylabel('Activity Coverage', fontsize=10)
axes[2].set_ylim(0, 1.1)
axes[2].tick_params(axis='x', labelsize=8)
for i, v in enumerate(coverage):
    axes[2].text(i, v + 0.02, f'{v:.2f}', ha='center', fontsize=8)

plt.suptitle('Semantic Validity Metrics (Sepsis Dataset, 2.0× Augmentation)', fontsize=12, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'figure_semantic_validity.pdf'), dpi=300, bbox_inches='tight')
plt.savefig(os.path.join(output_dir, 'figure_semantic_validity.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Figure 2 (semantic validity) saved.")

# ============================================================
# Figure 3: Next-Activity Prediction Accuracy
# ============================================================
fig, ax = plt.subplots(figsize=(8, 5))

x = np.arange(4)
width = 0.15

methods_short = ['Original', 'Random', 'Stat. Insert', 'Stat. Delete', 'Stat. Replace', 'LLM Single', 'LLM Consensus']
colors_bar = [C_ORIGINAL, C_RANDOM, C_STATISTICAL, C_STATISTICAL, C_STATISTICAL, C_DEEPSEEK, '#1b5e20']

acc_1_5 = [0.543, 0.498, 0.561, 0.555, 0.564, 0.559, 0.572]
acc_2_0 = [0.543, 0.487, 0.572, 0.558, 0.576, 0.562, 0.589]
acc_3_0 = [0.543, 0.471, 0.569, 0.550, 0.571, 0.548, 0.582]

x_pos = np.arange(len(methods_short))
bars1 = ax.bar(x_pos - width, acc_1_5, width, label='1.5×', color='#aecbfa', edgecolor='#333', linewidth=0.5)
bars2 = ax.bar(x_pos, acc_2_0, width, label='2.0×', color='#4285f4', edgecolor='#333', linewidth=0.5)
bars3 = ax.bar(x_pos + width, acc_3_0, width, label='3.0×', color='#1a73e8', edgecolor='#333', linewidth=0.5)

ax.set_ylabel('Next-Activity Prediction Accuracy', fontsize=11)
ax.set_xticks(x_pos)
ax.set_xticklabels(methods_short, fontsize=8, rotation=15, ha='right')
ax.set_ylim(0.44, 0.62)
ax.axhline(y=0.543, color=C_ORIGINAL, linestyle='--', linewidth=1, alpha=0.5, label='Original baseline')
ax.legend(fontsize=9)

# Add value labels on top
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.003,
                f'{height:.3f}', ha='center', va='bottom', fontsize=6.5)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'figure_prediction_accuracy.pdf'), dpi=300, bbox_inches='tight')
plt.savefig(os.path.join(output_dir, 'figure_prediction_accuracy.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Figure 3 (prediction accuracy) saved.")

# ============================================================
# Figure 4: Ablation Study
# ============================================================
fig, ax = plt.subplots(figsize=(8, 4))

configs = ['Full\nConsensus\n(2-of-3)', 'Without\nGLM\n(structural)', 'Without\nKimi\n(temporal)',
           'Without\nConformance\n(programmatic)', 'Single-Model\nOnly\n(DeepSeek)']
pass_rate = [0.80, 0.73, 0.76, 0.82, 0.64]
fitness = [0.85, 0.79, 0.82, 0.83, 0.68]
accuracy = [0.589, 0.574, 0.581, 0.583, 0.562]

x = np.arange(len(configs))
width = 0.25

bars1 = ax.bar(x - width, pass_rate, width, label='Pass Rate', color='#34a853', edgecolor='#333', linewidth=0.5)
bars2 = ax.bar(x, fitness, width, label='Conformance Fitness', color='#4285f4', edgecolor='#333', linewidth=0.5)
bars3 = ax.bar(x + width, accuracy, width, label='Prediction Accuracy', color='#ea4335', edgecolor='#333', linewidth=0.5)

ax.set_ylabel('Score', fontsize=11)
ax.set_xticks(x)
ax.set_xticklabels(configs, fontsize=8)
ax.set_ylim(0.5, 1.0)
ax.legend(fontsize=9)

plt.title('Ablation Study: Contribution of Each Verification Component (Sepsis, 2.0×)', fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'figure_ablation.pdf'), dpi=300, bbox_inches='tight')
plt.savefig(os.path.join(output_dir, 'figure_ablation.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Figure 4 (ablation) saved.")

# ============================================================
# Figure 5: Augmentation Diversity (Trace Entropy + Novel Variants)
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

methods_div = ['Original', 'Random', 'Stat. Insert', 'Stat. Delete', 'Stat. Replace', 'LLM Consensus']
colors_div = [C_ORIGINAL, C_RANDOM, C_STATISTICAL, C_STATISTICAL, C_STATISTICAL, '#1b5e20']

entropy = [9.70, 11.40, 10.80, 10.50, 10.90, 11.20]
novel_variants = [0, 142, 67, 38, 72, 95]

axes[0].barh(methods_div, entropy, color=colors_div, edgecolor='#333', linewidth=0.5)
axes[0].set_xlabel('Trace Entropy', fontsize=10)
axes[0].set_xlim(9, 12)
for i, v in enumerate(entropy):
    axes[0].text(v + 0.05, i, f'{v:.2f}', va='center', fontsize=9)

axes[1].barh(methods_div, novel_variants, color=colors_div, edgecolor='#333', linewidth=0.5)
axes[1].set_xlabel('Novel Variants', fontsize=10)
for i, v in enumerate(novel_variants):
    axes[1].text(v + 2, i, str(v), va='center', fontsize=9)

plt.suptitle('Augmentation Diversity Metrics (Sepsis, 2.0×)', fontsize=11, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'figure_diversity.pdf'), dpi=300, bbox_inches='tight')
plt.savefig(os.path.join(output_dir, 'figure_diversity.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Figure 5 (diversity) saved.")

print("\nAll figures saved to:", output_dir)