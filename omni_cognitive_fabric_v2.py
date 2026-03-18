"""
OmniCognitiveFabric v2.0
────────────────────────────────────────────────────────────────
พัฒนาจาก Demo Prototype โดยรวม:
  1. Streamlit Real-Time Dashboard  (แท็บ 1)
  2. NetworkX Network Topology      (แท็บ 2)
  3. SimPy Discrete-Event Simulation (แท็บ 3)

ติดตั้ง dependencies:
  pip install streamlit plotly networkx simpy numpy pandas

รัน:
  streamlit run omni_cognitive_fabric_v2.py
  
  or
  
  python -m streamlit run omni_cognitive_fabric_v2.py
────────────────────────────────────────────────────────────────
"""

import math
import random
import time

import numpy as np
import pandas as pd
import simpy
import networkx as nx
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import streamlit as st

# ══════════════════════════════════════════════════════════════
# ── 0. PAGE CONFIG & THEME ────────────────────────────────────
# ══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="OmniCognitiveFabric v2",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Rajdhani:wght@400;600;700&display=swap');
  html, body, [class*="css"] { font-family: 'Rajdhani', sans-serif; }
  code, pre, .metric-value { font-family: 'Share Tech Mono', monospace; }

  /* Dark panel cards */
  .stMetric { background: #0d1117; border: 1px solid #30363d;
               border-radius: 8px; padding: 12px; }
  .stTabs [data-baseweb="tab"] { font-family: 'Share Tech Mono', monospace;
                                  font-size: 13px; letter-spacing: 1px; }
  h1, h2, h3 { font-family: 'Rajdhani', sans-serif; font-weight: 700;
                color: #58a6ff; letter-spacing: 1px; }
  .block-container { padding-top: 1.5rem; }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# ── 1. CORE SIMULATION ENGINE ─────────────────────────────────
# ══════════════════════════════════════════════════════════════

class OmniCognitiveFabric:
    """
    สี่ Layer ของเครือข่าย พร้อมสูตรคณิตศาสตร์ที่ชัดเจน
    """

    def __init__(self, env_noise: float, bio_concentration: float = 100.0):
        self.env_noise = env_noise
        self.bio_concentration = bio_concentration

    # ── Layer 1 ──────────────────────────────────────────────
    def biological_bridge_layer(self, distance: float) -> dict:
        """
        สูตร: Signal(d) = C₀ · e^(−α · d)
          C₀  = ความเข้มข้นเริ่มต้น
          α   = 0.05 + noise·0.1   (attenuation coefficient)
          d   = ระยะทาง (หน่วย: cm)
        """
        alpha = 0.05 + self.env_noise * 0.1
        signal = self.bio_concentration * math.exp(-alpha * distance)
        snr = signal / (self.env_noise * 10 + 1e-9)   # Signal-to-Noise Ratio
        return {
            "alpha": alpha,
            "signal_strength": signal,
            "snr_db": 10 * math.log10(snr) if snr > 0 else 0,
        }

    # ── Layer 2 ──────────────────────────────────────────────
    def reality_adaptive_ai_layer(self, signal_strength: float) -> dict:
        """
        สูตร: Stability = clamp( S/C₀ − η + Δ, 0, 1 )
          S   = signal_strength
          η   = env_noise
          Δ   = AI correction ∈ [0.1, 0.4]   (PID-like controller)
        """
        delta = random.uniform(0.1, 0.4)
        stability = (signal_strength / self.bio_concentration) - self.env_noise + delta
        stability = max(0.0, min(1.0, stability))
        return {
            "ai_correction": delta,
            "stability_score": stability,
        }

    # ── Layer 3 ──────────────────────────────────────────────
    def quantum_transmission_backbone(self, stability: float) -> dict:
        """
        สูตร: Fidelity F = e^(−λ·(1 − S))
          λ = decoherence rate (default 0.5)
          Latency = 0 ms  ถ้า F ≥ 0.85
                  = Uniform(1.5, 10) ms  ถ้า F < 0.85
        Throughput = F · B_max
          B_max = 10 Gbps (theoretical max)
        """
        lam = 0.5
        fidelity = math.exp(-lam * (1.0 - stability))
        latency = 0.0 if fidelity >= 0.85 else random.uniform(1.5, 10.0)
        throughput_gbps = fidelity * 10.0
        return {
            "fidelity": fidelity,
            "latency_ms": latency,
            "throughput_gbps": throughput_gbps,
        }

    # ── Layer 4 ──────────────────────────────────────────────
    def neural_interface_layer(self, fidelity: float) -> dict:
        """
        สูตร: CognLoad = L_base + (1 − F) · 100
          L_base = 15% (baseline cognitive overhead)
          Access = FULL    ถ้า CognLoad < 60%
                 = RESTRICTED  ถ้า CognLoad ≥ 60%
        Bandwidth efficiency = F · 100%
        """
        base_load = 15.0
        cog_load = base_load + (1.0 - fidelity) * 100
        access = "FULL ACCESS" if cog_load < 60 else "RESTRICTED"
        bw_efficiency = fidelity * 100
        return {
            "cognitive_load": cog_load,
            "access_status": access,
            "bandwidth_efficiency": bw_efficiency,
        }

    def run_cycle(self, distance: float) -> dict:
        """รัน 1 รอบ และรวม metrics ทั้งหมด"""
        l1 = self.biological_bridge_layer(distance)
        l2 = self.reality_adaptive_ai_layer(l1["signal_strength"])
        l3 = self.quantum_transmission_backbone(l2["stability_score"])
        l4 = self.neural_interface_layer(l3["fidelity"])
        return {**l1, **l2, **l3, **l4}


# ══════════════════════════════════════════════════════════════
# ── 2. SIMPY QUEUE SIMULATION ─────────────────────────────────
# ══════════════════════════════════════════════════════════════

class NetworkQueueSimulation:
    """
    M/M/1 Queue Model สำหรับ Quantum Network Nodes
    ─────────────────────────────────────────────
    Arrival  rate λ (packets/s)
    Service  rate μ (packets/s)
    Utilization ρ = λ/μ  (ต้องน้อยกว่า 1 เพื่อ stability)
    Avg queue length  Lq = ρ² / (1 − ρ)
    Avg wait time     Wq = ρ / (μ(1 − ρ))
    """

    def __init__(self, arrival_rate: float, service_rate: float, num_users: int, sim_time: float = 100):
        self.lam = arrival_rate
        self.mu = service_rate
        self.num_users = num_users
        self.sim_time = sim_time
        self.results: list[dict] = []

    def _packet_source(self, env, server, user_id):
        """สร้าง packet ตาม Poisson Process"""
        while True:
            yield env.timeout(random.expovariate(self.lam))
            arrival = env.now
            with server.request() as req:
                yield req
                wait = env.now - arrival
                service_time = random.expovariate(self.mu)
                yield env.timeout(service_time)
                self.results.append({
                    "user_id": f"Node-{user_id:02d}",
                    "arrival_time": round(arrival, 3),
                    "wait_time_ms": round(wait * 1000, 3),
                    "service_time_ms": round(service_time * 1000, 3),
                    "total_time_ms": round((wait + service_time) * 1000, 3),
                })

    def run(self) -> pd.DataFrame:
        env = simpy.Environment()
        server = simpy.Resource(env, capacity=1)
        for uid in range(self.num_users):
            env.process(self._packet_source(env, server, uid))
        env.run(until=self.sim_time)
        return pd.DataFrame(self.results)

    @property
    def rho(self):
        return self.lam / self.mu

    @property
    def theoretical_lq(self):
        r = self.rho
        return (r ** 2) / (1 - r) if r < 1 else float("inf")

    @property
    def theoretical_wq_ms(self):
        r = self.rho
        return (r / (self.mu * (1 - r))) * 1000 if r < 1 else float("inf")


# ══════════════════════════════════════════════════════════════
# ── 3. NETWORK TOPOLOGY BUILDER ───────────────────────────────
# ══════════════════════════════════════════════════════════════

def build_topology(num_users: int, fidelity: float, stability: float) -> go.Figure:
    """
    สร้าง Graph แสดง Topology ของเครือข่าย
    Node สีขึ้นกับ cognitive_load, Edge สีขึ้นกับ fidelity
    """
    G = nx.Graph()

    # Central quantum hub
    G.add_node("Q-HUB", layer="hub")
    # Layer nodes
    layers = ["BIO-BRIDGE", "AI-CTRL", "Q-BACKBONE", "NEURAL-IF"]
    for ln in layers:
        G.add_node(ln, layer="layer")
        G.add_edge("Q-HUB", ln)

    # User nodes
    for i in range(num_users):
        uid = f"USR-{i:02d}"
        G.add_node(uid, layer="user")
        target = random.choice(layers)
        G.add_edge(uid, target)

    # Layout
    pos = nx.spring_layout(G, seed=42, k=2.5)

    # Edge traces – สีตาม fidelity
    edge_color = f"rgba({int(255*(1-fidelity))},{int(255*fidelity)},100,0.7)"
    edge_x, edge_y = [], []
    for u, v in G.edges():
        x0, y0 = pos[u]; x1, y1 = pos[v]
        edge_x += [x0, x1, None]; edge_y += [y0, y1, None]

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y, mode="lines",
        line=dict(width=1.5, color=edge_color),
        hoverinfo="none", name="Links"
    )

    # Node traces
    node_colors = {
        "hub": "#f0a500", "layer": "#58a6ff", "user": "#3fb950"
    }
    node_x, node_y, node_text, node_color, node_size = [], [], [], [], []
    for node in G.nodes():
        x, y = pos[node]
        ltype = G.nodes[node]["layer"]
        node_x.append(x); node_y.append(y)
        node_text.append(node)
        node_color.append(node_colors[ltype])
        node_size.append(28 if ltype == "hub" else 20 if ltype == "layer" else 14)

    node_trace = go.Scatter(
        x=node_x, y=node_y, mode="markers+text",
        marker=dict(size=node_size, color=node_color,
                    line=dict(width=1, color="#21262d")),
        text=node_text, textposition="top center",
        textfont=dict(size=9, color="#c9d1d9"),
        hoverinfo="text", name="Nodes"
    )

    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            title=dict(text=f"Network Topology  |  Fidelity {fidelity:.1%}  |  Stability {stability:.2f}",
                       font=dict(color="#58a6ff", size=14)),
            showlegend=False,
            paper_bgcolor="#0d1117", plot_bgcolor="#0d1117",
            font=dict(color="#c9d1d9"),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            margin=dict(l=20, r=20, t=50, b=20),
            height=480,
        )
    )
    return fig


# ══════════════════════════════════════════════════════════════
# ── 4. STREAMLIT UI ───────────────────────────────────────────
# ══════════════════════════════════════════════════════════════

# ── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    st.title("🧠 OCF Control Panel")
    st.markdown("---")

    st.subheader("🔬 Layer Parameters")
    env_noise   = st.slider("Environmental Noise (η)", 0.1, 0.9, 0.4, 0.05)
    distance    = st.slider("Signal Distance (d) cm",   1.0, 30.0, 10.0, 0.5)
    bio_conc    = st.slider("Bio Concentration (C₀)",  50.0, 200.0, 100.0, 10.0)

    st.markdown("---")
    st.subheader("📡 SimPy Queue Config")
    num_users   = st.slider("Number of Users (Nodes)", 2, 20, 6)
    arrival_rate = st.slider("Arrival Rate λ (pkt/s)",  0.5, 8.0, 3.0, 0.5)
    service_rate = st.slider("Service Rate μ (pkt/s)",  1.0, 10.0, 5.0, 0.5)
    sim_time_val = st.slider("Simulation Time (s)",    10, 200, 60)

    st.markdown("---")
    st.subheader("🔄 Run Cycles")
    num_cycles  = st.slider("Historical Cycles", 10, 100, 30)

    run_btn = st.button("▶  Run Full Simulation", type="primary", use_container_width=True)

# ── Main Title ────────────────────────────────────────────────
st.title("⚡ OmniCognitiveFabric v2.0")
st.caption("Quantum Neural Network Simulation  ·  Dashboard + Topology + Queue Simulation")

# ── Run simulation data ───────────────────────────────────────
if "history" not in st.session_state or run_btn:
    fabric = OmniCognitiveFabric(env_noise, bio_conc)
    history = []
    for _ in range(num_cycles):
        metrics = fabric.run_cycle(distance)
        history.append(metrics)
    st.session_state["history"] = history
    st.session_state["env_noise"] = env_noise
    st.session_state["distance"] = distance
    st.session_state["num_users"] = num_users

history = st.session_state["history"]
latest  = history[-1]

# ── KPI Row ───────────────────────────────────────────────────
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("📶 Signal Strength", f"{latest['signal_strength']:.1f}%",
            delta=f"SNR {latest['snr_db']:.1f} dB")
col2.metric("⚖️ Stability Score",  f"{latest['stability_score']:.3f}",
            delta=f"+{latest['ai_correction']:.2f} AI correction")
col3.metric("🔮 Quantum Fidelity", f"{latest['fidelity']:.1%}",
            delta=f"{latest['throughput_gbps']:.1f} Gbps")
col4.metric("⏱️ Latency",          f"{latest['latency_ms']:.2f} ms",
            delta="Zero-Latency ✓" if latest['latency_ms'] == 0 else "⚠ Degraded")
col5.metric("🧠 Cognitive Load",   f"{latest['cognitive_load']:.1f}%",
            delta=latest['access_status'])

st.markdown("---")

# ── Tabs ──────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs([
    "📊  REAL-TIME DASHBOARD",
    "🌐  NETWORK TOPOLOGY",
    "📦  SIMPY QUEUE SIMULATION",
])

# ════════════════════════════════════════
# TAB 1 – Real-Time Dashboard
# ════════════════════════════════════════
with tab1:
    df = pd.DataFrame(history)
    df["cycle"] = range(1, len(df) + 1)

    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=(
            "Layer 1 – Bio Signal Strength (%)",
            "Layer 2 – Network Stability Score",
            "Layer 3 – Quantum Fidelity & Throughput",
            "Layer 4 – Cognitive Load (%)",
        ),
        vertical_spacing=0.14,
        horizontal_spacing=0.08,
    )

    # Panel 1: Signal Strength
    fig.add_trace(go.Scatter(
        x=df["cycle"], y=df["signal_strength"],
        mode="lines+markers", name="Signal",
        line=dict(color="#3fb950", width=2),
        fill="tozeroy", fillcolor="rgba(63,185,80,0.1)",
        marker=dict(size=4),
    ), row=1, col=1)

    # Panel 2: Stability
    fig.add_trace(go.Scatter(
        x=df["cycle"], y=df["stability_score"],
        mode="lines", name="Stability",
        line=dict(color="#58a6ff", width=2),
    ), row=1, col=2)
    fig.add_hline(y=0.5, line_dash="dot", line_color="rgba(255,200,0,0.5)",
                  annotation_text="Threshold", row=1, col=2)

    # Panel 3: Fidelity + Throughput
    fig.add_trace(go.Scatter(
        x=df["cycle"], y=df["fidelity"],
        mode="lines", name="Fidelity",
        line=dict(color="#d2a8ff", width=2),
    ), row=2, col=1)
    fig.add_trace(go.Bar(
        x=df["cycle"], y=df["throughput_gbps"],
        name="Throughput (Gbps)", opacity=0.4,
        marker_color="#f0a500",
    ), row=2, col=1)
    fig.add_hline(y=0.85, line_dash="dot", line_color="rgba(255,100,100,0.5)",
                  annotation_text="F≥0.85 Zero-Lat", row=2, col=1)

    # Panel 4: Cognitive Load
    fig.add_trace(go.Scatter(
        x=df["cycle"], y=df["cognitive_load"],
        mode="lines+markers", name="Cog Load",
        line=dict(color="#ff7b72", width=2),
        fill="tozeroy", fillcolor="rgba(255,123,114,0.1)",
        marker=dict(size=4),
    ), row=2, col=2)
    fig.add_hline(y=60, line_dash="dot", line_color="rgba(255,200,0,0.5)",
                  annotation_text="Overload 60%", row=2, col=2)

    fig.update_layout(
        height=540, showlegend=False,
        paper_bgcolor="#0d1117", plot_bgcolor="#161b22",
        font=dict(color="#c9d1d9", size=11),
        margin=dict(l=40, r=20, t=50, b=40),
    )
    fig.update_xaxes(gridcolor="#21262d", title_text="Cycle")
    fig.update_yaxes(gridcolor="#21262d")
    st.plotly_chart(fig, use_container_width=True)

    # Math formula reference
    with st.expander("📐 สูตรคณิตศาสตร์ที่ใช้ใน Dashboard"):
        st.markdown(r"""
| Layer | สูตร | ตัวแปร |
|-------|------|--------|
| **1 Biological Bridge** | $S(d) = C_0 \cdot e^{-\alpha d}$ | α = 0.05 + η·0.1, d = distance |
| **2 AI Controller** | $\text{Stability} = \text{clamp}\!\left(\tfrac{S}{C_0} - \eta + \Delta, 0, 1\right)$ | Δ ~ U(0.1, 0.4) |
| **3 Quantum Backbone** | $F = e^{-\lambda(1-\text{Stab})}$ | λ = 0.5 (decoherence rate) |
| **4 Neural Interface** | $CL = 15 + (1-F)\cdot 100$ | CL < 60% = FULL ACCESS |
        """)

# ════════════════════════════════════════
# TAB 2 – Network Topology
# ════════════════════════════════════════
with tab2:
    st.subheader("🌐 Live Network Topology")

    c1, c2 = st.columns([3, 1])
    with c1:
        topo_fig = build_topology(
            num_users=num_users,
            fidelity=latest["fidelity"],
            stability=latest["stability_score"],
        )
        st.plotly_chart(topo_fig, use_container_width=True)

    with c2:
        st.markdown("**Node Legend**")
        st.markdown("🟡 **Q-HUB** – Quantum Hub Central")
        st.markdown("🔵 **Layer Nodes** – 4 Processing Layers")
        st.markdown("🟢 **USR-XX** – User Brain Nodes")
        st.markdown("---")
        st.markdown("**Edge Color**")
        st.markdown(f"Current Fidelity: **{latest['fidelity']:.1%}**")
        # Gradient bar as reference
        grad_fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=latest["fidelity"] * 100,
            title={"text": "Fidelity %", "font": {"color": "#c9d1d9"}},
            gauge={
                "axis": {"range": [0, 100], "tickcolor": "#c9d1d9"},
                "bar": {"color": "#58a6ff"},
                "steps": [
                    {"range": [0, 50], "color": "#3d1a1a"},
                    {"range": [50, 85], "color": "#2d3a1a"},
                    {"range": [85, 100], "color": "#1a2d3a"},
                ],
                "threshold": {"line": {"color": "#3fb950", "width": 3}, "value": 85},
            }
        ))
        grad_fig.update_layout(
            height=200, paper_bgcolor="#0d1117",
            font=dict(color="#c9d1d9"), margin=dict(l=10, r=10, t=30, b=10)
        )
        st.plotly_chart(grad_fig, use_container_width=True)

        st.markdown("**Stability Score**")
        st.progress(latest["stability_score"])

# ════════════════════════════════════════
# TAB 3 – SimPy Queue Simulation
# ════════════════════════════════════════
with tab3:
    st.subheader("📦 M/M/1 Queue Simulation (SimPy)")

    rho = arrival_rate / service_rate
    if rho >= 1:
        st.error(f"⚠️ ρ = λ/μ = {rho:.2f} ≥ 1  →  ระบบไม่เสถียร (Queue จะยาวไม่สิ้นสุด)  กรุณาลด λ หรือเพิ่ม μ")
    else:
        with st.spinner("⚙️  Running SimPy simulation..."):
            qsim = NetworkQueueSimulation(arrival_rate, service_rate, num_users, sim_time_val)
            df_q = qsim.run()

        if df_q.empty:
            st.warning("ไม่มีข้อมูลจาก Simulation – ลองเพิ่ม Simulation Time")
        else:
            # Theoretical vs simulated
            sim_avg_wait = df_q["wait_time_ms"].mean()
            sim_avg_total = df_q["total_time_ms"].mean()

            kc1, kc2, kc3, kc4 = st.columns(4)
            kc1.metric("ρ  Utilization",           f"{rho:.3f}",
                       delta="Stable ✓" if rho < 0.8 else "⚠ High Load")
            kc2.metric("Lq  Avg Queue Length",     f"{qsim.theoretical_lq:.2f} pkts",
                       delta="Theoretical")
            kc3.metric("Wq  Theoretical Wait",     f"{qsim.theoretical_wq_ms:.2f} ms",
                       delta="M/M/1 Formula")
            kc4.metric("Wq  Simulated Avg Wait",   f"{sim_avg_wait:.2f} ms",
                       delta=f"Δ {sim_avg_wait - qsim.theoretical_wq_ms:+.2f} ms")

            # Wait time distribution
            fig_q = make_subplots(
                rows=1, cols=2,
                subplot_titles=(
                    "Wait Time Distribution per Node",
                    "Avg Wait vs Arrival Rate (Theory)",
                )
            )

            for uid in df_q["user_id"].unique():
                sub = df_q[df_q["user_id"] == uid]
                fig_q.add_trace(go.Box(
                    y=sub["wait_time_ms"], name=uid,
                    boxmean=True, marker_color="#58a6ff",
                    line_color="#30363d",
                ), row=1, col=1)

            # Theory curve: Wq vs λ (keep μ fixed)
            lam_range = np.linspace(0.1, service_rate * 0.99, 100)
            wq_theory = (lam_range / service_rate) / (service_rate * (1 - lam_range / service_rate)) * 1000
            fig_q.add_trace(go.Scatter(
                x=lam_range, y=wq_theory, mode="lines",
                name="Wq = ρ / μ(1-ρ)",
                line=dict(color="#f0a500", width=2),
            ), row=1, col=2)
            fig_q.add_vline(x=arrival_rate, line_dash="dot", line_color="#3fb950",
                            annotation_text=f"λ={arrival_rate}", row=1, col=2)

            fig_q.update_layout(
                height=400, showlegend=False,
                paper_bgcolor="#0d1117", plot_bgcolor="#161b22",
                font=dict(color="#c9d1d9"),
                margin=dict(l=40, r=20, t=50, b=40),
            )
            fig_q.update_xaxes(gridcolor="#21262d")
            fig_q.update_yaxes(gridcolor="#21262d")
            st.plotly_chart(fig_q, use_container_width=True)

            with st.expander("📋 Raw Simulation Data (first 100 rows)"):
                st.dataframe(
                    df_q.head(100).style.background_gradient(
                        subset=["wait_time_ms", "total_time_ms"],
                        cmap="RdYlGn_r"
                    ),
                    use_container_width=True,
                )

            with st.expander("📐 สูตร M/M/1 Queue ที่ใช้"):
                st.markdown(r"""
| สัญลักษณ์ | ความหมาย | สูตร |
|-----------|----------|------|
| **ρ** | Utilization | $\rho = \lambda / \mu$ |
| **Lq** | Avg queue length | $L_q = \rho^2 / (1-\rho)$ |
| **Wq** | Avg waiting time | $W_q = \rho / \big(\mu(1-\rho)\big)$ |
| **L** | Avg in system | $L = \rho / (1-\rho)$ |
| **W** | Avg time in system | $W = 1 / \big(\mu(1-\rho)\big)$ |

> Inter-arrival time ~ **Exponential(λ)**,  Service time ~ **Exponential(μ)**
                """)

# ── Footer ────────────────────────────────────────────────────
st.markdown("---")
st.caption(
    "OmniCognitiveFabric v2.0  ·  "
    "Built with Streamlit · Plotly · NetworkX · SimPy  ·  "
    "Computer Network Project"
)