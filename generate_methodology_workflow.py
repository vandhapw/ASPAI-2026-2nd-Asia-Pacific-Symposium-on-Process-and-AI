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
\resizebox{\textwidth}{!}{%
\begin{tikzpicture}[
    node distance=0.6cm and 0.8cm,
    % Style definitions
    stepbox/.style={rectangle, rounded corners=6pt, draw=#1, fill=#1!8, line width=1.5pt,
        minimum width=14.5cm, minimum height=1cm, align=center},
    subbox/.style={rectangle, rounded corners=3pt, draw=#1, fill=#1!12, line width=0.8pt,
        minimum width=3.2cm, minimum height=1.4cm, align=center, font=\scriptsize},
    tinybox/.style={rectangle, rounded corners=2pt, draw=#1!70!black, fill=#1!15, line width=0.6pt,
        minimum width=2.8cm, minimum height=0.8cm, align=center, font=\tiny},
    metricbox/.style={rectangle, rounded corners=2pt, draw=#1!70!black, fill=#1!15, line width=0.6pt,
        minimum width=2.2cm, minimum height=0.65cm, align=center, font=\tiny\bfseries},
    arr/.style={-{Stealth[length=5pt]}, line width=1pt, color=#1},
    darr/.style={-{Stealth[length=5pt]}, line width=0.8pt, color=#1, dashed},
]

% ============================================================
% ORIGINAL EVENT LOGS
% ============================================================
\node[stepbox=deepseekblue] (logs) at (0, 0) {
    \textbf{Original Event Logs} \quad
    {\footnotesize Sepsis \(\cdot\) BPIC 2011 \(\cdot\) BPIC 2017 \(\cdot\) BPIC 2020 \(\cdot\) Hospital Billing \(\cdot\) Road Traffic Fines}
};

% ============================================================
% STEP 1: PREPROCESSING
% ============================================================
\node[stepbox=glmgreen, below=0.7cm of logs] (step1) {
    \textbf{Step 1: Preprocessing}
};

\node[subbox=glmgreen, below=0.4cm of step1.south west, xshift=0.3cm, anchor=north west] (load) {
    \textbf{Load Event}\\
    \textbf{Logs (pm4py)}
};

\node[subbox=glmgreen, right=0.3cm of load] (discover) {
    \textbf{Discover Process}\\
    \textbf{Models (DFG/Petri)}
};

\node[subbox=glmgreen, right=0.3cm of discover] (extract) {
    \textbf{Extract Frequent}\\
    \textbf{Patterns \& Context}
};

\node[subbox=glmgreen, right=0.3cm of extract] (split) {
    \textbf{Split}\\
    \textbf{Train/Test Sets}
};

% Arrows inside step 1
\draw[arr=glmgreen!70!black] (load) -- (discover);
\draw[arr=glmgreen!70!black] (discover) -- (extract);
\draw[arr=glmgreen!70!black] (extract) -- (split);

% Arrow from logs to step1
\draw[arr=deepseekblue!70!black] (logs.south) -- ++(0,-0.25) -| (step1.north);

% ============================================================
% STEP 2: AUGMENTATION APPROACHES
% ============================================================
\node[stepbox=kimired, below=0.8cm of step1] (step2) {
    \textbf{Step 2: Augmentation Approaches}
};

% Statistical baselines (left side)
\node[subbox=statpurple, below=0.4cm of step2.south west, xshift=0.3cm, anchor=north west, minimum width=4cm, minimum height=2.2cm] (stat) {
    \textbf{Statistical Baselines}\\
    \textbf{(SiamSA-PPM)}
};

\node[tinybox=statpurple, below=0.15cm of stat.south] (ops) {
    Insert \(\cdot\) Delete \(\cdot\) Replace
};

\draw[arr=statpurple!70!black] (stat.south) -- (ops.north);

% LLM augmentation (right side)
\node[subbox=kimired, right=0.5cm of stat, minimum width=9.5cm, minimum height=2.2cm] (llm) {
};

% LLM sub-label
\node[font=\scriptsize\bfseries, text=kimired!70!black] at ([yshift=-0.15cm]llm.north) {LLM-Based Augmentation};

% Generator
\node[tinybox=deepseekblue, below=0.2cm of llm.north, minimum width=3cm] (gen) {
    \textbf{DeepSeek-R1}\\
    {\tiny Generator}
};

% Three verifiers
\node[tinybox=glmgreen, below=0.3cm of gen.south west, xshift=0.1cm, anchor=north west, minimum width=2.5cm] (v_glm) {
    \textbf{GLM-4}\\
    {\tiny Structural Verifier}
};

\node[tinybox=kimired, right=0.2cm of v_glm, minimum width=2.5cm] (v_kimi) {
    \textbf{Kimi-K2}\\
    {\tiny Temporal Verifier}
};

\node[tinybox=conforange, right=0.2cm of v_kimi, minimum width=2.5cm] (v_conf) {
    \textbf{Conformance}\\
    {\tiny Check (Petri Net)}
};

% Arrows in LLM box
\draw[arr=deepseekblue!70!black] (gen.south) -- ++(0,-0.15) -| (v_glm.north);
\draw[arr=deepseekblue!70!black] (gen.south) -- ++(0,-0.15) -| (v_kimi.north);
\draw[arr=deepseekblue!70!black] (gen.south) -- ++(0,-0.15) -| (v_conf.north);

% Arrow from step1 to step2
\draw[arr=glmgreen!70!black] ([xshift=-3cm]step1.south) -- ++(0,-0.25) -| (stat.north);
\draw[arr=glmgreen!70!black] ([xshift=3cm]step1.south) -- ++(0,-0.25) -| (llm.north);

% ============================================================
% STEP 3: MULTI-LLM CONSENSUS VERIFICATION
% ============================================================
\node[stepbox=consensusgreen, below=1.2cm of step2] (step3) {
    \textbf{Step 3: Multi-LLM Consensus Verification}
};

% Trace candidates
\node[tinybox=deepseekblue, below=0.3cm of step3] (candidates) {
    \textbf{LLM Trace Candidates}
};

\draw[arr=deepseekblue!70!black] (step3.south) -- (candidates.north);

% Three verifier boxes
\node[tinybox=glmgreen, below=0.35cm of candidates.south west, xshift=0.6cm, anchor=north, minimum width=2.5cm] (v_glm2) {
    \textbf{GLM-4}\\
    {\tiny Structural}
};

\node[tinybox=kimired, right=0.3cm of v_glm2, minimum width=2.5cm] (v_kimi2) {
    \textbf{Kimi-K2}\\
    {\tiny Temporal}
};

\node[tinybox=conforange, right=0.3cm of v_kimi2, minimum width=2.5cm] (v_conf2) {
    \textbf{Conformance}\\
    {\tiny Check}
};

\draw[arr=black] (candidates.south) -- ++(0,-0.12) -| (v_glm2.north);
\draw[arr=black] (candidates.south) -- ++(0,-0.12) -| (v_kimi2.north);
\draw[arr=black] (candidates.south) -- ++(0,-0.12) -| (v_conf2.north);

% 2-of-3 consensus
\node[tinybox=statpurple, below=0.4cm of v_kimi2, minimum width=4.5cm, minimum height=0.9cm, font=\small\bfseries] (voting) {
    2-of-3 Consensus (Majority Voting)
};

\draw[arr=glmgreen!70!black] (v_glm2.south) -- (voting.north -| v_glm2.south);
\draw[arr=kimired!70!black] (v_kimi2.south) -- (voting.north);
\draw[arr=conforange!70!black] (v_conf2.south) -- (voting.north -| v_conf2.south);

% Verified traces
\node[tinybox=consensusgreen, below=0.35cm of voting, minimum width=4.5cm, minimum height=0.9cm, font=\small\bfseries] (verified) {
    Verified Semantic Traces
};

\draw[arr=consensusgreen!70!black] (voting.south) -- (verified.north);

% Arrow from step2 to step3 (LLM path)
\draw[arr=kimired!70!black] ([xshift=2cm]step2.south) -- ++(0,-0.3) -| (step3.north -| step3.west);

% ============================================================
% OUTPUT: AUGMENTED DATA + EVALUATION
% ============================================================
\node[stepbox=randorange, below=1cm of step3, minimum height=1cm] (eval) {
    \textbf{Evaluation \& Downstream Prediction}
};

% Three output branches
\node[tinybox=statpurple, below=0.5cm of eval.south west, xshift=0.5cm, anchor=north, minimum width=3.2cm, minimum height=0.9cm] (stat_out) {
    \textbf{Statistical}\\
    \textbf{Augmented Data}
};

\node[tinybox=consensusgreen, below=0.5cm of eval.south, anchor=north, minimum width=3.2cm, minimum height=0.9cm] (llm_out) {
    \textbf{LLM Consensus}\\
    \textbf{Augmented Data}
};

\node[tinybox=origgray, below=0.5cm of eval.south east, xshift=-0.5cm, anchor=north, minimum width=3.2cm, minimum height=0.9cm] (orig_out) {
    \textbf{Original Data}\\
    \textbf{(No Augmentation)}
};

\draw[arr=statpurple!70!black] (eval.south -| stat_out.north) -- (stat_out.north);
\draw[arr=consensusgreen!70!black] (eval.south) -- (llm_out.north);
\draw[arr=origgray] (eval.south -| orig_out.north) -- (orig_out.north);

% Evaluation metrics
\node[metricbox=deepseekblue, below=0.5cm of stat_out, yshift=-0.1cm] (m1) {Semantic Validity};
\node[metricbox=statpurple, below=0.15cm of m1] (m2) {Trace Diversity};
\node[metricbox=kimired, below=0.15cm of m2] (m3) {Prediction Accuracy};

\node[metricbox=deepseekblue, below=0.5cm of llm_out, yshift=-0.1cm] (m4) {Conformance Fitness};
\node[metricbox=statpurple, below=0.15cm of m4] (m5) {Novel Variants};
\node[metricbox=kimired, below=0.15cm of m5] (m6) {Next-Activity Acc.};

\node[metricbox=origgray, below=0.5cm of orig_out, yshift=-0.1cm] (m7) {Baseline Accuracy};
\node[metricbox=statpurple, below=0.15cm of m7] (m8) {Ablation Study};
\node[metricbox=conforange, below=0.15cm of m8] (m9) {Consensus Rate};

% Research questions
\node[rectangle, rounded corners=4pt, draw=black, fill=yellow!10, line width=0.8pt,
      minimum width=14.5cm, minimum height=1.6cm, align=center, font=\small,
      below=0.4cm of m2] (rq) {
    \textbf{Research Questions:}\\[2pt]
    \textbf{H1:} Multi-LLM consensus $>$ Statistical baselines on semantic validity? \quad
    \textbf{H2:} Augmented data improves downstream prediction accuracy? \quad
    \textbf{H3:} Heterogeneous consensus $>$ Single-model verification?
};

% Arrows from metrics to research questions
\draw[arr=black!50] (m3.south) -- ++(0,-0.15) -| (rq.north -| m3.south);
\draw[arr=black!50] (m6.south) -- ++(0,-0.15) -| (rq.north);
\draw[arr=black!50] (m9.south) -- ++(0,-0.15) -| (rq.north -| m9.south);

% Arrows from stat and llm paths to step3
\draw[darr=statpurple!70!black] (stat.south) -- ++(0,-0.3) -| ([xshift=-4cm]eval.north);
\draw[arr=consensusgreen!70!black] (verified.south) -- ++(0,-0.3) -| (eval.north -| eval.west);

\end{tikzpicture}
}%
\caption{Research methodology workflow. Step~1 preprocesses event logs and discovers process models. Step~2 applies statistical baselines and LLM-based augmentation with three verification mechanisms. Step~3 applies 2-of-3 majority voting consensus filtering. Augmented data is evaluated against original and statistical baselines on semantic validity, diversity, and downstream prediction accuracy.}
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