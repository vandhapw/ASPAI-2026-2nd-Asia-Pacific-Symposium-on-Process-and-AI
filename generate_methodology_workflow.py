"""
Generate the Research Methodology Workflow diagram as a standalone LaTeX TikZ figure.
This creates a comprehensive workflow showing Steps 1-3, evaluation metrics, and research questions.
"""

import os

output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figures')
os.makedirs(output_dir, exist_ok=True)

tikz_code = r"""
\begin{figure*}[t]
\centering
\begin{tikzpicture}[
    node distance=0.5cm and 0.6cm,
    % Step header bars
    stepbar/.style={rectangle, rounded corners=4pt, draw=#1!60!black, fill=#1!10,
        minimum width=14.5cm, minimum height=0.7cm, align=center,
        font=\footnotesize\bfseries, line width=1pt},
    % Main process boxes
    box/.style={rectangle, rounded corners=3pt, draw=#1!60!black, fill=#1!12,
        minimum width=2.6cm, minimum height=0.9cm, align=center,
        font=\scriptsize\bfseries, line width=0.8pt},
    % Small verifier/metric boxes
    sbox/.style={rectangle, rounded corners=2pt, draw=#1!60!black, fill=#1!15,
        minimum width=2.2cm, minimum height=0.85cm, align=center,
        font=\tiny, line width=0.7pt},
    % Wide boxes
    widebox/.style={rectangle, rounded corners=3pt, draw=#1!60!black, fill=#1!12,
        minimum width=5.5cm, minimum height=0.9cm, align=center,
        font=\scriptsize\bfseries, line width=0.8pt},
    % Arrows
    arr/.style={-{Stealth[length=4pt]}, line width=0.8pt, color=#1},
    % Labels
    lbl/.style={font=\tiny\itshape, text=black!60},
]

% ============================================================
% ROW 1: INPUT DATA
% ============================================================
\node[stepbar=deepseekblue] (header1) at (0, 0) {Input: Six Public Event Logs};

\node[box=deepseekblue, below=0.3cm of header1.south west, xshift=0.4cm, anchor=north west] (load)
    {Load \& Parse\\{\tiny pm4py XES}};
\node[box=deepseekblue, right=0.4cm of load] (discover)
    {Discover Models\\{\tiny DFG + Petri Net}};
\node[box=deepseekblue, right=0.4cm of discover] (extract)
    {Extract Context\\{\tiny Alphabet + Variants}};
\node[box=deepseekblue, right=0.4cm of extract] (split)
    {Split Data\\{\tiny 80/20 Temporal}};

\draw[arr=deepseekblue!60] (load) -- (discover);
\draw[arr=deepseekblue!60] (discover) -- (extract);
\draw[arr=deepseekblue!60] (extract) -- (split);

% ============================================================
% ROW 2: AUGMENTATION APPROACHES
% ============================================================
\node[stepbar=kimired, below=0.8cm of header1] (header2)
    {Step 1: Augmentation Approaches};

% Left: Statistical branch
\node[widebox=statpurple, below=0.3cm of header2.south west, xshift=1.0cm,
      anchor=north west, minimum height=1.5cm] (stat)
    {Statistical Baseline\\[2pt]
     {\tiny SiamSA-PPM: Insert / Delete / Replace}};

% Right: LLM branch
\node[widebox=deepseekblue, below=0.3cm of header2.south east, xshift=-1.0cm,
      anchor=north east, minimum height=1.5cm] (llm)
    {LLM-Based Generation\\[2pt]
     {\tiny DeepSeek-R1 $\cdot$ Temperature 0.7}};

% Arrows from preprocessing to both branches
\draw[arr=deepseekblue!50] (split.south) -- ++(0,-0.25) -| (stat.north);
\draw[arr=deepseekblue!50] (split.south) -- ++(0,-0.25) -| (llm.north);

% ============================================================
% ROW 3: VERIFICATION (for LLM path only)
% ============================================================
\node[stepbar=glmgreen, below=0.7cm of header2] (header3)
    {Step 2: Multi-LLM Consensus Verification (2-of-3 Voting)};

% Three verifiers centered under LLM branch
\node[sbox=glmgreen, below=0.3cm of header3.south, xshift=-3.0cm] (v1)
    {Structural\\[-1pt]{\tiny GLM-4 ($\tau{=}0.1$)}};
\node[sbox=kimired, right=0.3cm of v1] (v2)
    {Temporal\\[-1pt]{\tiny Kimi-K2 ($\tau{=}0.3$)}};
\node[sbox=conforange, right=0.3cm of v2] (v3)
    {Conformance\\[-1pt]{\tiny Petri Net Replay}};

% Arrows: LLM -> verifiers
\draw[arr=deepseekblue!60] (llm.south) -- ++(0,-0.2) -| (v1.north);
\draw[arr=deepseekblue!60] (llm.south) -- ++(0,-0.2) -| (v2.north);
\draw[arr=deepseekblue!60] (llm.south) -- ++(0,-0.2) -| (v3.north);

% Consensus box below verifiers
\node[box=statpurple, below=0.45cm of v2, minimum width=4.5cm] (consensus)
    {Consensus: $\geq$ 2 of 3 Accept};

\draw[arr=glmgreen!60]  (v1.south) -- (v1.south |- consensus.north);
\draw[arr=kimired!60]   (v2.south) -- (consensus.north);
\draw[arr=conforange!60] (v3.south) -- (v3.south |- consensus.north);

% ============================================================
% ROW 4: OUTPUT & EVALUATION
% ============================================================
\node[stepbar=darkgreen, below=0.8cm of header3] (header4)
    {Step 3: Evaluation \& Downstream Prediction};

% Three data sources
\node[box=statpurple, below=0.35cm of header4.south west, xshift=0.6cm,
      anchor=north west, minimum width=3.8cm] (src_stat)
    {Statistical\\Augmented Data};

\node[box=consensusgreen, below=0.35cm of header4.south, anchor=north,
      minimum width=3.8cm] (src_llm)
    {LLM Consensus\\Augmented Data};

\node[box=origgray, below=0.35cm of header4.south east, xshift=-0.6cm,
      anchor=north east, minimum width=3.8cm] (src_orig)
    {Original Data\\(No Augmentation)};

% Arrows to data sources
\draw[arr=statpurple!60] (stat.south) -- ++(0,-0.2) -| (src_stat.north);
\draw[arr=consensusgreen!60] (consensus.south) -- ++(0,-0.2) -| (src_llm.north);
\draw[arr=deepseekblue!40] (split.south) -- ++(0,-0.2) -| (src_orig.north);

% Metrics for Statistical
\node[sbox=statpurple, below=0.35cm of src_stat, minimum width=3.2cm] (m1)
    {Semantic Validity};
\node[sbox=statpurple, below=0.12cm of m1, minimum width=3.2cm] (m2)
    {Trace Diversity};
\node[sbox=statpurple, below=0.12cm of m2, minimum width=3.2cm] (m3)
    {Prediction Accuracy};

% Metrics for LLM Consensus
\node[sbox=consensusgreen, below=0.35cm of src_llm, minimum width=3.2cm] (m4)
    {Conformance Fitness};
\node[sbox=consensusgreen, below=0.12cm of m4, minimum width=3.2cm] (m5)
    {Novel Variant Rate};
\node[sbox=consensusgreen, below=0.12cm of m5, minimum width=3.2cm] (m6)
    {Next-Activity Acc.};

% Metrics for Original
\node[sbox=origgray, below=0.35cm of src_orig, minimum width=3.2cm] (m7)
    {Baseline Accuracy};
\node[sbox=origgray, below=0.12cm of m7, minimum width=3.2cm] (m8)
    {Ablation Study};
\node[sbox=origgray, below=0.12cm of m8, minimum width=3.2cm] (m9)
    {Consensus Rate};

% Arrows from sources to first metric
\draw[arr=statpurple!60] (src_stat.south) -- (m1.north);
\draw[arr=consensusgreen!60] (src_llm.south) -- (m4.north);
\draw[arr=origgray!60] (src_orig.south) -- (m7.north);

% ============================================================
% ROW 5: RESEARCH QUESTIONS
% ============================================================
\node[rectangle, rounded corners=5pt, draw=black!60, fill=yellow!8, line width=0.9pt,
      minimum width=14.5cm, minimum height=1.2cm, align=center, font=\footnotesize,
      below=0.5cm of m2] (rq) {
    \textbf{Research Questions}\\[2pt]
    \textbf{H1:} Multi-LLM consensus $\,>\,$ statistical baselines on semantic validity?
    \hspace{0.4cm}
    \textbf{H2:} Augmented data improves downstream prediction accuracy?
    \hspace{0.4cm}
    \textbf{H3:} Heterogeneous consensus $\,>\,$ single-model verification?
};

% Connect metrics to RQs
\draw[arr=black!30] (m3.south)  -- ++(0,-0.2) -| (rq.north -| m3.south);
\draw[arr=black!30] (m6.south)  -- ++(0,-0.2) -| (rq.north);
\draw[arr=black!30] (m9.south)  -- ++(0,-0.2) -| (rq.north -| m9.south);

% Side connection: statistical path bypasses verification -> direct to evaluation
\draw[arr=statpurple!40, dashed] (stat.east) --
    ++(1.2cm, 0) |-
    ([yshift=1.0cm]consensus.east) --
    (consensus.east);
\node[font=\tiny\itshape, text=statpurple!70!black, align=center]
    at ([xshift=2.0cm, yshift=-0.8cm]stat.east)
    {Statistical path bypasses\\LLM verification stage};

\end{tikzpicture}
\caption{Research methodology workflow. The pipeline processes six event logs through preprocessing and model discovery, applies both statistical and LLM-based augmentation, verifies LLM-generated traces via 2-of-3 multi-model consensus, and evaluates augmented data on semantic validity, diversity, and downstream prediction accuracy against three research hypotheses.}
\label{fig:methodology_workflow}
\end{figure*}
"""

# Write the TikZ code to a standalone file
workflow_path = os.path.join(output_dir, 'figure_methodology_workflow.tex')
with open(workflow_path, 'w') as f:
    f.write(tikz_code)

print(f"Workflow TikZ code written to: {workflow_path}")
print("\nTo include in main.tex, add before \\end{document}:")
print("  \\input{figures/figure_methodology_workflow.tex}")