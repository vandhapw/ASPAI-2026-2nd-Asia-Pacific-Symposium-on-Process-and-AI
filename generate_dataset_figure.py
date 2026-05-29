import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patches as patches
import numpy as np
import os

output_dir = '/mnt/d/AI-LLM/workspaces/Claude-projects/research-grounding/ASPAI-2026-2nd-Asia-Pacific-Symposium-on-Process-and-AI/figures'

# Colors
C_REG = '#4285f4'    # ER Registration
C_TRI = '#34a853'    # ER Triage
C_SEP = '#fbbc04'    # ER Sepsis Triage
C_IV  = '#ea4335'    # IV Liquid / IV Antibiotics
C_ADM = '#9334e6'    # Admission
C_TST = '#ff6d01'    # CRP / Lactic Acid / Leucocytes
C_REL = '#1b5e20'    # Release
C_RET = '#5f6368'    # Return ER

activity_colors = {
    'ER Registration': C_REG,
    'ER Triage': C_TRI,
    'ER Sepsis Triage': C_SEP,
    'IV Liquid': C_IV,
    'IV Antibiotics': C_IV,
    'Admission NC': C_ADM,
    'Admission IC': C_ADM,
    'CRP': C_TST,
    'Lactic Acid': C_TST,
    'Leucocytes': C_TST,
    'Release A': C_REL,
    'Release B': C_REL,
    'Release C': C_REL,
    'Release D': C_REL,
    'Release E': C_REL,
    'Return ER': C_RET,
}

# ============================================================
# Figure: Sepsis Dataset Illustration
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# ---- Panel A: What is an Event Log? ----
ax = axes[0][0]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('(a) Event Log Structure', fontsize=12, fontweight='bold', pad=10)

# Table header
headers = ['Case ID', 'Activity', 'Timestamp', 'Resource']
x_positions = [0.5, 2.5, 5.0, 7.5]
for x, h in zip(x_positions, headers):
    ax.text(x, 9.3, h, ha='center', va='center', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#e8f0fe', edgecolor='#4285f4'))

# Sample data rows
rows = [
    ['1', 'ER Registration',   '09:00', 'Nurse A'],
    ['1', 'ER Triage',        '09:15', 'Nurse A'],
    ['1', 'ER Sepsis Triage', '09:30', 'Dr. X'],
    ['1', 'IV Antibiotics',    '09:45', 'Dr. X'],
    ['1', 'Admission IC',     '10:00', 'Dr. X'],
    ['2', 'ER Registration',  '10:30', 'Nurse B'],
    ['2', 'ER Triage',        '10:45', 'Nurse B'],
    ['2', 'IV Liquid',        '11:00', 'Dr. Y'],
    ['2', 'Admission NC',     '11:15', 'Dr. Y'],
    ['3', 'ER Registration',  '08:00', 'Nurse C'],
]

row_colors = ['#ffffff', '#f8f9fa'] * 5
for i, row in enumerate(rows):
    y = 8.8 - i * 0.85
    bg_color = '#e8f5e9' if row[0] == '1' else '#fff3e0' if row[0] == '2' else '#e3f2fd'
    for x, val in zip(x_positions, row):
        ax.text(x, y, val, ha='center', va='center', fontsize=8,
                bbox=dict(boxstyle='round,pad=0.2', facecolor=bg_color, edgecolor='#ddd', linewidth=0.5))

# Trace bracket
ax.annotate('', xy=(9.5, 9.0), xytext=(9.5, 5.4),
            arrowprops=dict(arrowstyle='<->', color='#1a73e8', lw=1.5))
ax.text(9.7, 7.2, 'Trace 1', fontsize=8, color='#1a73e8', rotation=90, va='center')

ax.annotate('', xy=(9.5, 5.0), xytext=(9.5, 3.7),
            arrowprops=dict(arrowstyle='<->', color='#ea4335', lw=1.5))
ax.text(9.7, 4.35, 'Trace 2', fontsize=8, color='#ea4335', rotation=90, va='center')

# Label
ax.text(5.0, 0.5, 'Each row = 1 event. Each trace = sequence of events for 1 patient.',
         ha='center', fontsize=8, style='italic', color='#5f6368')

# ---- Panel B: Trace Variants (Why Diversity Matters) ----
ax = axes[0][1]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('(b) Trace Variants in Sepsis Log', fontsize=12, fontweight='bold', pad=10)

# Draw 4 sample traces as horizontal flow
traces = [
    ['ER Reg.', 'Triage', 'Sepsis\nTriage', 'IV Liq.', 'Adm. NC', 'CRP', 'Rel. A'],
    ['ER Reg.', 'Triage', 'Sepsis\nTriage', 'IV Abx.', 'Adm. IC', 'Lac.\nAcid', 'Rel. C'],
    ['ER Reg.', 'Triage', 'Sepsis\nTriage', 'IV Liq.', 'Adm. IC', 'Leuc.', 'Rel. E'],
    ['ER Reg.', 'Triage', 'Sepsis\nTriage', 'IV Abx.', 'Adm. NC', 'CRP', 'Rel. B'],
]

trace_colors_short = [C_REG, C_TRI, C_SEP, C_IV, C_ADM, C_TST, C_REL]

for t_idx, trace in enumerate(traces):
    y_base = 9.0 - t_idx * 2.2
    for a_idx, activity in enumerate(trace):
        x = 0.5 + a_idx * 1.25
        color = trace_colors_short[a_idx]
        rect = mpatches.FancyBboxPatch((x-0.45, y_base-0.45), 0.9, 0.9,
            boxstyle="round,pad=0.05", facecolor=color, edgecolor='white', linewidth=1.5, alpha=0.85)
        ax.add_patch(rect)
        ax.text(x, y_base, activity, ha='center', va='center', fontsize=5.5, color='white', fontweight='bold')
        # Arrow between activities
        if a_idx < len(trace) - 1:
            ax.annotate('', xy=(x+0.55, y_base), xytext=(x+0.55, y_base),
                       arrowprops=dict(arrowstyle='->', color='#333', lw=0.8))

    ax.text(0.0, y_base, f't{t_idx+1}', ha='center', va='center', fontsize=8, fontweight='bold', color='#333')

ax.text(5.0, 0.3, '830 variants from only 1,050 cases = high variability',
         ha='center', fontsize=8, style='italic', color='#ea4335', fontweight='bold')

# ---- Panel C: Data Scarcity Problem ----
ax = axes[1][0]
ax.set_title('(c) Data Scarcity: Sepsis vs Typical DL Dataset', fontsize=12, fontweight='bold', pad=10)

datasets_names = ['ImageNet\n(CV)', 'WikiText\n(NLP)', 'BPIC 2017\n(PM, Large)', 'BPIC 2012\n(PM, Med)', 'Sepsis\n(PM, Small)']
dataset_sizes = [14_000_000, 4_000_000, 59_148, 13_087, 1_050]
colors_bar = ['#e8f0fe', '#e8f0fe', '#fce8e6', '#fce8e6', '#ea4335']

bars = ax.barh(datasets_names, dataset_sizes, color=colors_bar, edgecolor='#333', linewidth=0.5)
ax.set_xscale('log')
ax.set_xlabel('Number of Cases (log scale)', fontsize=9)

# Add value labels
for bar, val in zip(bars, dataset_sizes):
    if val >= 1_000_000:
        label = f'{val/1_000_000:.0f}M'
    elif val >= 1_000:
        label = f'{val/1_000:.0f}K'
    else:
        label = str(val)
    ax.text(bar.get_width() * 1.3, bar.get_y() + bar.get_height()/2, label,
            va='center', fontsize=9, fontweight='bold')

# Arrow highlighting the gap
ax.annotate('', xy=(59000, 2.5), xytext=(59000, 4.3),
            arrowprops=dict(arrowstyle='<->', color='#ea4335', lw=2))
ax.text(80000, 3.4, '3 orders\nof magnitude', fontsize=8, color='#ea4335', fontweight='bold', ha='center')

ax.text(0.5, -0.15, 'Sepsis has 1,000x fewer cases than typical DL training sets',
        fontsize=8, style='italic', color='#ea4335', fontweight='bold',
        transform=ax.transAxes, ha='center')

# ---- Panel D: Augmentation Challenge ----
ax = axes[1][1]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('(d) The Augmentation Challenge', fontsize=12, fontweight='bold', pad=10)

# Valid trace
valid_trace = ['ER Reg.', 'Triage', 'Sepsis\nTriage', 'IV Liq.', 'Adm.\nNC', 'CRP', 'Rel. A']
y_valid = 8.5
for i, act in enumerate(valid_trace):
    x = 0.5 + i * 1.25
    color = trace_colors_short[i]
    rect = mpatches.FancyBboxPatch((x-0.45, y_valid-0.45), 0.9, 0.9,
        boxstyle="round,pad=0.05", facecolor=color, edgecolor='white', linewidth=1.5, alpha=0.85)
    ax.add_patch(rect)
    ax.text(x, y_valid, act, ha='center', va='center', fontsize=5.5, color='white', fontweight='bold')

ax.text(0.0, y_valid, 'Valid', ha='center', va='center', fontsize=8, fontweight='bold', color='#34a853')

# Random augmentation (invalid)
invalid_trace = ['ER Reg.', 'Rel. C', 'Sepsis\nTriage', 'IV Abx.', 'Adm.\nIC']
y_invalid = 5.5
invalid_colors = [C_REG, C_REL, C_SEP, C_IV, C_ADM]
for i, (act, color) in enumerate(zip(invalid_trace, invalid_colors)):
    x = 0.5 + i * 1.25
    rect = mpatches.FancyBboxPatch((x-0.45, y_invalid-0.45), 0.9, 0.9,
        boxstyle="round,pad=0.05", facecolor=color, edgecolor='#ea4335', linewidth=2, alpha=0.5)
    ax.add_patch(rect)
    ax.text(x, y_invalid, act, ha='center', va='center', fontsize=5.5, color='white', fontweight='bold')

# X mark on invalid transition
ax.text(3.75, 7.2, 'X', fontsize=30, color='#ea4335', fontweight='bold', ha='center')
ax.text(3.75, 6.8, 'Invalid!', fontsize=7, color='#ea4335', ha='center')

ax.text(0.0, y_invalid, 'Invalid', ha='center', va='center', fontsize=8, fontweight='bold', color='#ea4335')

# Explanation
ax.text(5.0, 3.5, 'Random augmentation breaks\nprocess semantics:', ha='center', fontsize=9,
        fontweight='bold', color='#ea4335')
ax.text(5.0, 2.5, '"Release" cannot happen\nbefore "Admission" + "Tests"', ha='center', fontsize=8,
        style='italic', color='#5f6368')

# Our solution box
sol_rect = mpatches.FancyBboxPatch((1.0, 0.3), 8.0, 1.5, boxstyle="round,pad=0.15",
    facecolor='#e8f5e9', edgecolor='#1b5e20', linewidth=2)
ax.add_patch(sol_rect)
ax.text(5.0, 1.05, 'Our Solution: Multi-LLM Consensus', ha='center', fontsize=9,
        fontweight='bold', color='#1b5e20')
ax.text(5.0, 0.6, 'Generate with reasoning + Verify with 3 independent checks', ha='center', fontsize=7,
        color='#1b5e20')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'figure_dataset_illustration.pdf'), dpi=300, bbox_inches='tight')
plt.savefig(os.path.join(output_dir, 'figure_dataset_illustration.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Dataset illustration saved.")

# ============================================================
# Also create a standalone Sepsis process flow diagram
# ============================================================
fig, ax = plt.subplots(figsize=(14, 5))
ax.set_xlim(-0.5, 14)
ax.set_ylim(-1.5, 3.5)
ax.axis('off')

# Sepsis process flow (simplified DFG)
nodes = {
    'ER Registration':      (0, 1),
    'ER Triage':           (2, 1),
    'ER Sepsis Triage':    (4, 1),
    'IV Liquid':           (6, 2),
    'IV Antibiotics':      (6, 0),
    'Admission NC':        (8, 2),
    'Admission IC':        (8, 0),
    'CRP':                (10, 2.5),
    'Lactic Acid':         (10, 1),
    'Leucocytes':         (10, -0.5),
    'Release A':          (12, 2.5),
    'Release B':          (12, 2.0),
    'Release C':          (12, 1.0),
    'Release D':          (12, 0.5),
    'Release E':          (12, -0.5),
    'Return ER':          (12, -1.0),
}

node_colors = {
    'ER Registration': C_REG, 'ER Triage': C_TRI, 'ER Sepsis Triage': C_SEP,
    'IV Liquid': C_IV, 'IV Antibiotics': C_IV,
    'Admission NC': C_ADM, 'Admission IC': C_ADM,
    'CRP': C_TST, 'Lactic Acid': C_TST, 'Leucocytes': C_TST,
    'Release A': C_REL, 'Release B': C_REL, 'Release C': C_REL,
    'Release D': C_REL, 'Release E': C_REL, 'Return ER': C_RET,
}

edges = [
    ('ER Registration', 'ER Triage'),
    ('ER Triage', 'ER Sepsis Triage'),
    ('ER Sepsis Triage', 'IV Liquid'),
    ('ER Sepsis Triage', 'IV Antibiotics'),
    ('IV Liquid', 'Admission NC'),
    ('IV Liquid', 'Admission IC'),
    ('IV Antibiotics', 'Admission NC'),
    ('IV Antibiotics', 'Admission IC'),
    ('Admission NC', 'CRP'),
    ('Admission NC', 'Lactic Acid'),
    ('Admission NC', 'Leucocytes'),
    ('Admission IC', 'CRP'),
    ('Admission IC', 'Lactic Acid'),
    ('Admission IC', 'Leucocytes'),
    ('CRP', 'Release A'),
    ('CRP', 'Release B'),
    ('Lactic Acid', 'Release C'),
    ('Lactic Acid', 'Release D'),
    ('Leucocytes', 'Release E'),
    ('Release A', 'Return ER'),
    ('Return ER', 'ER Triage'),
]

# Draw edges
for src, dst in edges:
    sx, sy = nodes[src]
    dx, dy = nodes[dst]
    ax.annotate('', xy=(dx-0.45, dy), xytext=(sx+0.45, sy),
               arrowprops=dict(arrowstyle='->', color='#bbb', lw=1.2, connectionstyle='arc3,rad=0.05'))

# Draw nodes
for name, (x, y) in nodes.items():
    color = node_colors.get(name, '#ddd')
    rect = mpatches.FancyBboxPatch((x-0.5, y-0.35), 1.0, 0.7,
        boxstyle="round,pad=0.08", facecolor=color, edgecolor='white', linewidth=1.5, alpha=0.9)
    ax.add_patch(rect)
    # Shorten label
    label = name.replace('ER ', '').replace('Sepsis ', 'S.').replace('Admission ', 'Adm.').replace('Release ', 'Rel.').replace('Lactic Acid', 'Lac. Acid').replace('Leucocytes', 'Leuc.').replace('Return ', 'Ret. ')
    ax.text(x, y, label, ha='center', va='center', fontsize=7, color='white', fontweight='bold')

# Title
ax.text(6.5, 3.2, 'Sepsis Treatment Process (Simplified DFG)', ha='center', fontsize=13, fontweight='bold', color='#333')

# Legend
legend_items = [
    ('Registration', C_REG), ('Triage', C_TRI), ('Sepsis Triage', C_SEP),
    ('IV Treatment', C_IV), ('Admission', C_ADM), ('Lab Tests', C_TST),
    ('Release', C_REL), ('Return ER', C_RET),
]
for i, (label, color) in enumerate(legend_items):
    x = 0.5 + i * 1.6
    rect = mpatches.FancyBboxPatch((x-0.3, -1.3), 0.6, 0.4,
        boxstyle="round,pad=0.05", facecolor=color, edgecolor='white', linewidth=0.5)
    ax.add_patch(rect)
    ax.text(x, -1.1, label, ha='center', va='center', fontsize=5.5, color='white', fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'figure_sepsis_process_flow.pdf'), dpi=300, bbox_inches='tight')
plt.savefig(os.path.join(output_dir, 'figure_sepsis_process_flow.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Sepsis process flow saved.")