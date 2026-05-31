"""
Generate Petri net TikZ figures for all 6 datasets.
Reads DFGs from dataset_configs.py and converts to Petri net representations.
Outputs a combined figure and individual TikZ files.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dataset_configs import DATASETS, DATASET_ORDER, DATASET_COLORS
from collections import defaultdict

output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figures')
os.makedirs(output_dir, exist_ok=True)


def dfg_to_petri_net(dfg, start_activities, end_activities, activity_list):
    """
    Convert a DFG to a Petri net structure suitable for TikZ layout.
    Returns a layered graph representation.
    """
    # Build adjacency
    successors = defaultdict(list)
    predecessors = defaultdict(list)
    for src, dst in dfg:
        successors[src].append(dst)
        predecessors[dst].append(src)

    all_activities = set()
    for s, d in dfg:
        all_activities.add(s)
        all_activities.add(d)

    # Topological layering
    layers = []
    visited = set()
    # Layer 0: start activities
    current = set(start_activities)
    while current:
        layers.append(sorted(current))
        visited.update(current)
        next_layer = set()
        for act in current:
            for succ in successors[act]:
                if succ not in visited:
                    # Check if all predecessors are in earlier layers
                    preds_done = all(p in visited for p in predecessors[succ])
                    if preds_done:
                        next_layer.add(succ)
        current = next_layer

    # Add any stragglers
    remaining = all_activities - visited
    if remaining:
        layers.append(sorted(remaining))

    return layers, successors, predecessors


def make_tikz_petri(dataset_key, scale=1.0):
    """Generate TikZ code for a single dataset's Petri net."""
    ds = DATASETS[dataset_key]
    dfg = ds["dfg"]
    starts = ds["start_activities"]
    ends = ds["end_activities"]
    activities = ds["activity_list"]

    layers, successors, predecessors = dfg_to_petri_net(dfg, starts, ends, activities)

    # Short labels
    label_map = {}
    for act in activities:
        short = act.replace("ER ", "").replace("Registration", "Reg.")
        short = short.replace("Sepsis Triage", "Seps.Triage")
        short = short.replace("Admission ", "Adm.")
        short = short.replace("Release ", "Rel.")
        short = short.replace("Return ER", "Ret.ER")
        short = short.replace("Antibiotics", "Abx.")
        short = short.replace("Lactic Acid", "Lac.Acid")
        short = short.replace("Leucocytes", "Leuc.")
        short = short.replace("Liquid", "Liq.")
        short = short.replace("Insert Fine Notification", "Ins.Fine Notif.")
        short = short.replace("Insert Date Appeal to Prefecture", "Ins.Date Appeal")
        short = short.replace("Send Appeal to Prefecture", "Send Appeal")
        short = short.replace("Receive Result Appeal from Prefecture", "Recv.Result")
        short = short.replace("Notify Result Appeal to Offender", "Notify Result")
        short = short.replace("Appeal to Judge", "Appeal Judge")
        short = short.replace("Send for Credit Collection", "Send Cr.Col.")
        short = short.replace("Create Fine", "Create")
        short = short.replace("Send Fine", "Send")
        short = short.replace("Add penalty", "Add Penalty")
        short = short.replace("Payment", "Pay")
        short = short.replace("Request ", "Req.")
        short = short.replace("Additional info requested", "Add.Info Req.")
        short = short.replace("Info provided", "Info Prov.")
        short = short.replace("Permit ", "Perm.")
        short = short.replace("Decision made", "Decision")
        short = short.replace("Request closed", "Closed")
        short = short.replace("Request cancelled", "Cancelled")
        short = short.replace("Consultation", "Consult")
        short = short.replace("Approval requested", "Appr.Req.")
        short = short.replace("Approval granted", "Appr.Grant")
        short = short.replace("Approval denied", "Appr.Deny")
        short = short.replace("Document uploaded", "Doc.Upload")
        short = short.replace("Document verified", "Doc.Verify")
        short = short.replace("Document rejected", "Doc.Reject")
        short = short.replace("Notification sent", "Notif.Sent")
        short = short.replace("Reminder sent", "Remind.Sent")
        short = short.replace("Fine issued", "Fine Issued")
        short = short.replace("Objection submitted", "Obj.Submit")
        short = short.replace("Objection reviewed", "Obj.Review")
        short = short.replace("Inspection scheduled", "Insp.Sched.")
        short = short.replace("Inspection completed", "Insp.Comp.")
        short = short.replace("Report generated", "Report Gen.")
        short = short.replace("Payment handled", "Pay.Handle")
        short = short.replace("Request reviewed", "Review")
        short = short.replace("Request forwarded", "Forward")
        short = short.replace("Request submitted", "Submit")
        short = short.replace("Request received", "Receive")
        short = short.replace("Concept Modified", "Concept Mod.")
        short = short.replace("CEBA Submittal", "CEBA Submit")
        short = short.replace("CEBA Approved", "CEBA Approve")
        short = short.replace("CEBA Rejected", "CEBA Reject")
        short = short.replace("Decision Submitted", "Dec.Submit")
        short = short.replace("Decision Finalized", "Dec.Final")
        short = short.replace("A_Create Application", "Create Appl")
        short = short.replace("A_Submitted", "Submitted")
        short = short.replace("A_Concept", "Concept")
        short = short.replace("A_Accepted", "Accepted")
        short = short.replace("A_Validating", "Validating")
        short = short.replace("A_Complete", "Complete")
        short = short.replace("A_Pending", "Pending")
        short = short.replace("A_Cancelled", "Cancelled")
        short = short.replace("A_Denied", "Denied")
        short = short.replace("O_Create Offer", "Create Offer")
        short = short.replace("O_Sent (web)", "Sent (web)")
        short = short.replace("O_Sent", "Sent")
        short = short.replace("O_Returned", "Returned")
        short = short.replace("O_Accepted", "O-Accept")
        short = short.replace("O_Cancelled", "O-Cancel")
        short = short.replace("W_Call after offers", "Call Offers")
        short = short.replace("W_Complete application", "Compl.Appl")
        short = short.replace("W_Handle leads", "Handle Lead")
        short = short.replace("W_Personal loan collection", "Loan Coll.")
        short = short.replace("W_Shortened completion", "Short Compl.")
        short = short.replace("W_Validate application", "Valid.Appl")
        short = short.replace("NEW", "New")
        short = short.replace("BILLED", "Billed")
        short = short.replace("PAYMENT", "Pay")
        short = short.replace("REJECTED", "Reject")
        short = short.replace("APPEALED", "Appeal")
        short = short.replace("APPROVED", "Approve")
        short = short.replace("DENIED", "Deny")
        short = short.replace("REVIEW", "Review")
        short = short.replace("RELEASE", "Release")
        short = short.replace("REOPEN", "Reopen")
        short = short.replace("QUERY", "Query")
        short = short.replace("RESPONSE", "Response")
        short = short.replace("ADJUST", "Adjust")
        short = short.replace("WRITEOFF", "Writeoff")
        short = short.replace("CODE", "Code")
        short = short.replace("CANCEL", "Cancel")
        short = short.replace("MOD", "Modify")
        short = short.replace("Other", "Other")
        label_map[act] = short

    # Determine grid dimensions
    max_layer_len = max(len(l) for l in layers) if layers else 1
    n_layers = len(layers)

    x_spacing = 1.8 * scale
    y_spacing = 1.0 * scale
    total_width = n_layers * x_spacing

    lines = []
    lines.append("  % Petri net for " + ds["short_name"])

    # Assign coordinates per activity
    coords = {}
    for layer_idx, layer_acts in enumerate(layers):
        x = layer_idx * x_spacing
        n = len(layer_acts)
        y_start = -(n - 1) * y_spacing / 2
        for act_idx, act in enumerate(layer_acts):
            y = y_start + act_idx * y_spacing
            coords[act] = (x, y)

    # Draw transitions (activities) FIRST - must be defined before arcs reference them
    for act in activities:
        if act in coords:
            x, y = coords[act]
            idx = activities.index(act)
            label = label_map.get(act, act[:12])
            is_start = act in starts
            is_end = act in ends
            fill_color = "startcolor" if is_start else "endcolor" if is_end else "transitioncolor"
            lines.append(f"  \\node[transition, fill={fill_color}] (t_{dataset_key}_{idx}) at ({x}, {y}) {{\\tiny {label}}};")

    # Start place -> start activities
    start_y = coords[starts[0]][1]
    lines.append(f"  \\node[place, label=above:{{\\tiny $i$}}] (p_start_{dataset_key}) at ({-x_spacing}, {start_y}) {{}};")
    for sa in starts:
        if sa in coords:
            sx, sy = coords[sa]
            lines.append(f"  \\draw[post, stealth-] (t_{dataset_key}_{activities.index(sa)}.west) -- node[above, font=\\tiny] {{}} (p_start_{dataset_key});")

    # End activities -> end place
    end_ys = [coords[ea][1] for ea in ends if ea in coords]
    if end_ys:
        end_y = sum(end_ys) / len(end_ys)
    else:
        end_y = 0
    lines.append(f"  \\node[place, label=below:{{\\tiny $o$}}] (p_end_{dataset_key}) at ({n_layers * x_spacing}, {end_y}) {{}};")
    for ea in ends:
        if ea in coords:
            ex, ey = coords[ea]
            lines.append(f"  \\draw[post, -stealth] (t_{dataset_key}_{activities.index(ea)}.east) -- (p_end_{dataset_key});")

    # Draw places between transitions
    place_counter = 0
    drawn_places = {}
    for src, dst in dfg:
        if src in coords and dst in coords:
            sx, sy = coords[src]
            dx, dy = coords[dst]
            pkey = f"{src}_{dst}"
            if pkey not in drawn_places:
                px = (sx + dx) / 2
                py = (sy + dy) / 2
                pname = f"p_{dataset_key}_{place_counter}"
                place_counter += 1
                lines.append(f"  \\node[place] ({pname}) at ({px}, {py}) {{}};")
                drawn_places[pkey] = pname

            pn = drawn_places[pkey]
            src_idx = activities.index(src) if src in activities else -1
            dst_idx = activities.index(dst) if dst in activities else -1
            lines.append(f"  \\draw[post, -stealth] (t_{dataset_key}_{src_idx}.east) -- ({pn});")
            lines.append(f"  \\draw[post, -stealth] ({pn}) -- (t_{dataset_key}_{dst_idx}.west);")

    return "\n".join(lines)


# Generate the combined figure
combined_tikz = r"""
\begin{figure*}[t]
\centering
\begin{tikzpicture}[
    transition/.style={rectangle, rounded corners=2pt, draw=black, fill=white,
        minimum width=1.2cm, minimum height=0.55cm, align=center, font=\tiny,
        inner sep=1pt, line width=0.4pt},
    place/.style={circle, draw=black, fill=white,
        minimum size=0.28cm, inner sep=0pt, line width=0.4pt},
    post/.style={line width=0.35pt, draw=black!60},
    scale=0.85,
]
\colorlet{startcolor}{green!25}
\colorlet{endcolor}{red!20}
\colorlet{transitioncolor}{white}
"""

ds_short = {
    "sepsis": "Sepsis", "bpic2011": "BPIC 2011", "bpic2017": "BPIC 2017",
    "bpic2020": "BPIC 2020", "hospital_billing": "Hospital Billing",
    "road_traffic_fines": "Road Traffic Fines",
}

# Layout positions for 6 sub-petri-nets in 3x2 grid
# Each Petri net is drawn in its own scope with a shift
grid_cols = 3
grid_rows = 2
cell_width = 7.0
cell_height = 4.5

for idx, dk in enumerate(DATASET_ORDER):
    col = idx % grid_cols
    row = idx // grid_cols
    x_off = col * cell_width
    y_off = -row * cell_height

    combined_tikz += f"\n  % ---- {ds_short[dk]} ----\n"
    combined_tikz += f"  \\begin{{scope}}[shift={{({{{x_off}}}, {{{y_off}}})}}]\n"
    combined_tikz += make_tikz_petri(dk)
    combined_tikz += f"\n  \\node[font=\\footnotesize\\bfseries] at ({{2.5}}, {{1.6}}) {{{ds_short[dk]}}};"
    combined_tikz += "\n  \\end{scope}\n"

combined_tikz += r"""
\end{tikzpicture}
\caption{Petri net representations of the six event logs used in this study, discovered via the Inductive Miner.
Transitions represent activities, places represent process states, and arcs denote causal dependencies.
Green transitions are start activities, red transitions are end activities.
The Petri nets illustrate the range of process complexity: from the simple, linear structure of Road Traffic Fines (4 variants) to the highly branching structure of BPIC 2017 (21,500 variants).}
\label{fig:petri_nets}
\end{figure*}
"""

# Write the combined figure
fig_path = os.path.join(output_dir, "figure_petri_nets.tex")
with open(fig_path, "w") as f:
    f.write(combined_tikz)
print(f"Combined Petri net figure written to: {fig_path}")

# Also write individual figures for standalone use
for dk in DATASET_ORDER:
    ds = DATASETS[dk]
    tikz_body = make_tikz_petri(dk)
    short_name = ds["short_name"]
    cases = ds["cases"]
    acts = ds["activities_count"]
    vars_ = ds["variants"]
    individual = (
        "\\begin{figure}[t]\n"
        "\\centering\n"
        "\\begin{tikzpicture}[\n"
        "    transition/.style={rectangle, rounded corners=2pt, draw=black, fill=white,\n"
        "        minimum width=1.2cm, minimum height=0.55cm, align=center, font=\\tiny,\n"
        "        inner sep=1pt, line width=0.4pt},\n"
        "    place/.style={circle, draw=black, fill=white,\n"
        "        minimum size=0.28cm, inner sep=0pt, line width=0.4pt},\n"
        "    post/.style={line width=0.35pt, draw=black!60},\n"
        "]\n"
        "\\colorlet{startcolor}{green!25}\n"
        "\\colorlet{endcolor}{red!20}\n"
        "\\colorlet{transitioncolor}{white}\n"
        + tikz_body + "\n"
        "\\node[font=\\footnotesize] at (current bounding box.north) {" + short_name + "};\n"
        "\\end{tikzpicture}\n"
        "\\caption{Petri net representation of the " + short_name + " event log ("
        + str(cases) + " cases, " + str(acts) + " activities, "
        + str(vars_) + " variants).}\n"
        "\\label{fig:petri_" + dk + "}\n"
        "\\end{figure}\n"
    )
    ind_path = os.path.join(output_dir, f"figure_petri_{dk}.tex")
    with open(ind_path, "w") as f:
        f.write(individual)
    print(f"  Individual Petri net written to: {ind_path}")

print("\nTo include in main.tex, add before \\end{document}:")
print("  \\input{figures/figure_petri_nets.tex}")
