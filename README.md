# ⚡ The Omni-Cognitive Quantum Fabric v2.0
### รายงานสถาปัตยกรรมและการจำลองระบบ

> **Computer Network Project**  
> Built with: `Python` · `Streamlit` · `Plotly` · `NetworkX` · `SimPy`



https://omnicognitivefabric.streamlit.app/


**MVP**
--  NotebookLM :: Video & Info graphic 
https://drive.google.com/drive/folders/1APCD3xz8SruWC_QnKQlT3RbLaOOyKSfj?usp=sharing4


 
 
---

## 📋 สารบัญ

1. [ภาพรวมของระบบ](#1-ภาพรวมของระบบ)
2. [สถาปัตยกรรมโค้ด](#2-สถาปัตยกรรมโค้ด)
3. [แบบจำลองทางคณิตศาสตร์ (4 Layers)](#3-แบบจำลองทางคณิตศาสตร์-4-layers)
4. [ทฤษฎีคิว M/M/1 (SimPy)](#4-ทฤษฎีคิว-mm1-simpy)
5. [Dashboard และการแสดงผล](#5-dashboard-และการแสดงผล)
6. [การติดตั้งและรันโปรแกรม](#6-การติดตั้งและรันโปรแกรม)
7. [ตาราง Metrics สรุป](#7-ตาราง-metrics-สรุป)

---

## 1. ภาพรวมของระบบ

ระบบ **Omni-Cognitive Quantum Fabric** จำลองเครือข่ายประสาท-ควอนตัม (Neural-Quantum Network) ที่ผสานการสื่อสารระดับโมเลกุล, การควบคุมด้วย AI แบบ Real-Time, ช่องสัญญาณควอนตัม และ Interface กับสมองมนุษย์ ไว้ใน Pipeline เดียวกัน

```
[สมอง/ผู้ใช้]
     │
     ▼
┌─────────────────────────────────────────────────────────┐
│  Layer 1: Biological Bridge   →  Bio-Molecular Signal   │
│  Layer 2: Reality-Adaptive AI →  Stability Controller   │
│  Layer 3: Quantum Backbone    →  Fidelity & Throughput  │
│  Layer 4: Neural Interface    →  Cognitive Load / QoE   │
└─────────────────────────────────────────────────────────┘
     │
     ▼
[Streamlit Dashboard + NetworkX Topology + SimPy Queue]
```

สัญญาณไหลเป็น **Cascade** จาก Layer 1 → 4 โดยผลลัพธ์ของแต่ละ Layer จะเป็น Input ของ Layer ถัดไปเสมอ ผ่านฟังก์ชัน `run_cycle(distance)` ใน class หลัก

---

## 2. สถาปัตยกรรมโค้ด

โปรแกรมแบ่งออกเป็น **4 Modules** หลัก:

### Module A — `class OmniCognitiveFabric`
หัวใจหลักของการคำนวณ ประกอบด้วย 4 เมธอดตาม Layer และ 1 เมธอดรวม:

```python
class OmniCognitiveFabric:
    def __init__(self, env_noise: float, bio_concentration: float = 100.0)
    def biological_bridge_layer(self, distance: float) -> dict
    def reality_adaptive_ai_layer(self, signal_strength: float) -> dict
    def quantum_transmission_backbone(self, stability: float) -> dict
    def neural_interface_layer(self, fidelity: float) -> dict
    def run_cycle(self, distance: float) -> dict   # ← เรียกใช้ทั้ง 4 Layer
```

**Output keys** ที่ได้จาก `run_cycle()`:

| Key | ประเภท | ความหมาย |
|-----|--------|----------|
| `alpha` | float | Attenuation coefficient (Layer 1) |
| `signal_strength` | float | ความแรงสัญญาณ % (Layer 1) |
| `snr_db` | float | Signal-to-Noise Ratio in dB (Layer 1) |
| `ai_correction` | float | ค่าชดเชย Δ จาก AI (Layer 2) |
| `stability_score` | float | เสถียรภาพ 0–1 (Layer 2) |
| `fidelity` | float | ความสมบูรณ์ควอนตัม 0–1 (Layer 3) |
| `latency_ms` | float | ความหน่วง ms (Layer 3) |
| `throughput_gbps` | float | อัตรารับส่งข้อมูล Gbps (Layer 3) |
| `cognitive_load` | float | ภาระสมอง % (Layer 4) |
| `access_status` | str | `FULL ACCESS` / `RESTRICTED` (Layer 4) |
| `bandwidth_efficiency` | float | ประสิทธิภาพ Bandwidth % (Layer 4) |

---

### Module B — `class NetworkQueueSimulation`
จำลอง M/M/1 Queue ด้วย SimPy:

```python
class NetworkQueueSimulation:
    def __init__(self, arrival_rate, service_rate, num_users, sim_time)
    def _packet_source(self, env, server, user_id)  # Poisson Process generator
    def run(self) -> pd.DataFrame                   # รัน simulation → DataFrame
    @property rho          # ρ = λ/μ
    @property theoretical_lq    # Lq = ρ²/(1-ρ)
    @property theoretical_wq_ms # Wq = ρ/μ(1-ρ) × 1000
```

---

### Module C — `def build_topology()`
สร้าง Network Graph ด้วย NetworkX + Plotly:

```python
def build_topology(num_users: int, fidelity: float, stability: float) -> go.Figure
```

โครงสร้าง Graph แบบ **Hub-and-Spoke**:
- **Q-HUB** (1 node) — ศูนย์กลางควอนตัม
- **Layer Nodes** (4 nodes) — BIO-BRIDGE, AI-CTRL, Q-BACKBONE, NEURAL-IF
- **User Nodes** (N nodes) — USR-00 ถึง USR-N เชื่อมเข้า Layer แบบสุ่ม

สีของ Edge คำนวณจาก Fidelity:  
`rgba( 255×(1−F), 255×F, 100, 0.7 )` → แดง (F=0) ถึง เขียว (F=1)

---

### Module D — Streamlit UI
```
Sidebar (Control Panel)
  ├── Layer Parameters   : env_noise, distance, bio_concentration
  ├── SimPy Queue Config : num_users, λ, μ, sim_time
  └── Run Cycles         : จำนวน Historical Cycles

Main Panel
  ├── KPI Row (5 Metrics)
  ├── Tab 1: Real-Time Dashboard (Plotly 4-panel)
  ├── Tab 2: Network Topology (NetworkX Interactive)
  └── Tab 3: SimPy Queue Simulation (M/M/1)
```

---

## 3. แบบจำลองทางคณิตศาสตร์ (4 Layers)

### Layer 1 — Biological Bridge Layer
**โมเดล:** Signal Attenuation (การลดทอนสัญญาณแบบ Exponential Decay)

$$S(d) = C_0 \cdot e^{-\alpha d}$$

| ตัวแปร | ความหมาย | ค่า/สูตร |
|--------|----------|---------|
| $S(d)$ | Signal Strength ณ ระยะทาง d | — |
| $C_0$ | Bio Concentration เริ่มต้น | ปรับได้: 50–200 |
| $\alpha$ | Attenuation Coefficient | $0.05 + \eta \cdot 0.1$ |
| $\eta$ | Environmental Noise | ปรับได้: 0.1–0.9 |
| $d$ | ระยะทาง (cm) | ปรับได้: 1–30 |

**นัยทางเครือข่าย:** เทียบเท่า **Path Loss** ในระบบสื่อสารไร้สาย  
**SNR** คำนวณเพิ่มเติมเป็น: $\text{SNR}_{dB} = 10 \log_{10}\!\left(\dfrac{S}{\eta \cdot 10}\right)$

```python
alpha = 0.05 + self.env_noise * 0.1
signal = self.bio_concentration * math.exp(-alpha * distance)
snr = signal / (self.env_noise * 10 + 1e-9)
snr_db = 10 * math.log10(snr)
```

---

### Layer 2 — Reality-Adaptive AI Control Layer
**โมเดล:** Adaptive Controller (PID-like Correction)

$$\text{Stability} = \text{clamp}\!\left(\frac{S}{C_0} - \eta + \Delta,\ 0,\ 1\right)$$

| ตัวแปร | ความหมาย | ค่า |
|--------|----------|-----|
| $S$ | Signal Strength จาก Layer 1 | — |
| $\eta$ | Environmental Noise | ค่าเดิมจาก Layer 1 |
| $\Delta$ | AI Correction Factor | $\sim U(0.1,\ 0.4)$ |
| $\text{clamp}(x, 0, 1)$ | จำกัดค่า 0–1 | `max(0, min(1, x))` |

**นัยทางเครือข่าย:** เปรียบเสมือน **Forward Error Correction (FEC)** หรือ **QoS Management** ใน Data Link / Network Layer

```python
delta = random.uniform(0.1, 0.4)
stability = (signal_strength / self.bio_concentration) - self.env_noise + delta
stability = max(0.0, min(1.0, stability))
```

---

### Layer 3 — Quantum Transmission Backbone
**โมเดล:** Quantum Decoherence (การสูญเสียสถานะควอนตัม)

$$F = e^{-\lambda(1 - \text{Stability})}$$

| ตัวแปร | ความหมาย | ค่า |
|--------|----------|-----|
| $F$ | Quantum Fidelity (0–1) | — |
| $\lambda$ | Decoherence Rate | `0.5` (fixed) |
| $\text{Stability}$ | ค่าจาก Layer 2 | — |

**Latency Model:**

$$\text{Latency} = \begin{cases} 0\ \text{ms} & \text{ถ้า } F \geq 0.85 \\ U(1.5,\ 10.0)\ \text{ms} & \text{ถ้า } F < 0.85 \end{cases}$$

**Throughput Model:**

$$\text{Throughput} = F \cdot B_{\max} \quad (B_{\max} = 10\ \text{Gbps})$$

```python
lam = 0.5
fidelity = math.exp(-lam * (1.0 - stability))
latency = 0.0 if fidelity >= 0.85 else random.uniform(1.5, 10.0)
throughput_gbps = fidelity * 10.0
```

---

### Layer 4 — Neural Interface Layer
**โมเดล:** Cognitive Load (ภาระการรับรู้ของสมอง)

$$CL = L_{\text{base}} + (1 - F) \cdot 100$$

| ตัวแปร | ความหมาย | ค่า |
|--------|----------|-----|
| $CL$ | Cognitive Load (%) | — |
| $L_{\text{base}}$ | Baseline Overhead | `15%` |
| $F$ | Fidelity จาก Layer 3 | — |

**Access Control:**

$$\text{Access} = \begin{cases} \text{FULL ACCESS} & \text{ถ้า } CL < 60\% \\ \text{RESTRICTED} & \text{ถ้า } CL \geq 60\% \end{cases}$$

**นัยทางเครือข่าย:** เมื่อ Packet Loss สูงหรือ Fidelity ต่ำ สมองต้องทำงานหนักขึ้นเพื่อประมวลผลข้อมูลที่ขาดหาย — เทียบเท่ากลไก **Congestion Control**

```python
base_load = 15.0
cog_load = base_load + (1.0 - fidelity) * 100
access = "FULL ACCESS" if cog_load < 60 else "RESTRICTED"
bw_efficiency = fidelity * 100
```

---

## 4. ทฤษฎีคิว M/M/1 (SimPy)

### โมเดล M/M/1 Queue

| สัญลักษณ์ | ความหมาย | สูตร |
|-----------|----------|------|
| $\lambda$ | Arrival Rate (pkt/s) | ปรับได้ผ่าน Sidebar |
| $\mu$ | Service Rate (pkt/s) | ปรับได้ผ่าน Sidebar |
| $\rho$ | Utilization | $\rho = \lambda / \mu$ |
| $L_q$ | Avg Queue Length | $L_q = \rho^2 / (1 - \rho)$ |
| $W_q$ | Avg Wait Time | $W_q = \rho / [\mu(1 - \rho)]$ |
| $L$ | Avg Packets in System | $L = \rho / (1 - \rho)$ |
| $W$ | Avg Time in System | $W = 1 / [\mu(1 - \rho)]$ |

> **เงื่อนไขเสถียรภาพ:** ระบบจะเสถียรก็ต่อเมื่อ $\rho < 1$  
> หาก $\rho \geq 1$ คิวจะยาวไม่สิ้นสุด → **Network Congestion**

### การจำลองด้วย SimPy (Event-Driven)

```
Simulation Flow:
  สร้าง SimPy Environment
       │
       ├── สร้าง Resource (Quantum Hub, capacity=1)
       │
       └── สร้าง N Packet Sources (1 ต่อ User)
                │
                └── แต่ละ source: loop ∞
                      ├── รอ inter-arrival time ~ Exp(λ)
                      ├── ขอใช้ Resource
                      ├── วัด wait_time
                      ├── ประมวลผล ~ Exp(μ)
                      └── บันทึก → results[]
```

**ค่าที่วัดและเปรียบเทียบ:**
- `theoretical_wq_ms` — คำนวณจากสูตร M/M/1
- `sim_avg_wait` — ค่าเฉลี่ยจริงจาก simulation
- ส่วนต่าง Δ แสดงความแม่นยำของโมเดล

---

## 5. Dashboard และการแสดงผล

### แท็บ 1 — Real-Time Dashboard

กราฟ 4 แผง (Plotly subplot 2×2):

| แผง | ข้อมูล | สี | Threshold |
|-----|--------|----|-----------|
| Top-Left | Bio Signal Strength (%) | เขียว + fill | — |
| Top-Right | Network Stability Score | ฟ้า | 0.5 (เส้นประ) |
| Bottom-Left | Quantum Fidelity + Throughput Bar | ม่วง + ส้ม | F = 0.85 |
| Bottom-Right | Cognitive Load (%) | แดง + fill | 60% (overload) |

### แท็บ 2 — Network Topology

- Layout: `nx.spring_layout(seed=42, k=2.5)`
- สีโหนด: 🟡 Hub · 🔵 Layer · 🟢 User
- สี Edge: `rgba(255×(1−F), 255×F, 100, 0.7)` — เปลี่ยนตาม Fidelity แบบ Real-time
- Gauge แสดง Fidelity % พร้อม threshold ที่ 85%

### แท็บ 3 — SimPy Queue Simulation

- **Box Plot** แสดง Wait Time distribution แยกรายโหนด
- **Theory Curve** กราฟ $W_q$ vs $\lambda$ เส้นทฤษฎี พร้อม marker ค่า λ ปัจจุบัน
- **KPI Row:** ρ, Lq, Wq (ทฤษฎี), Wq (จริง) + ส่วนต่าง

---

## 6. การติดตั้งและรันโปรแกรม

### ติดตั้ง Dependencies

```bash
pip install streamlit plotly networkx simpy numpy pandas
```

### รันโปรแกรม

```bash
streamlit run omni_cognitive_fabric_v2.py
```

เปิด Browser ไปที่ `http://localhost:8501`

### ทางเลือก (ถ้า streamlit ไม่พบ)

```bash
python -m pip install streamlit plotly networkx simpy numpy pandas
python -m streamlit run omni_cognitive_fabric_v2.py
```

### ตรวจสอบ Python

```bash
python --version   # ต้องการ Python 3.9+
```

---

## 7. ตาราง Metrics สรุป

### Layer Metrics

| Layer | Metric | ช่วงค่า | เกณฑ์วิกฤต |
|-------|--------|---------|------------|
| 1 Bio Bridge | Signal Strength | 0–100% | — |
| 1 Bio Bridge | SNR | dB | ยิ่งสูงยิ่งดี |
| 2 AI Control | Stability Score | 0.0–1.0 | < 0.5 = warning |
| 3 Quantum | Fidelity | 0.0–1.0 | < 0.85 = latency เพิ่ม |
| 3 Quantum | Latency | 0 / 1.5–10 ms | 0 = zero-latency mode |
| 3 Quantum | Throughput | 0–10 Gbps | สัดส่วนกับ Fidelity |
| 4 Neural | Cognitive Load | 15–115% | > 60% = RESTRICTED |

### Queue Metrics (M/M/1)

| Metric | เงื่อนไขดี | เงื่อนไขวิกฤต |
|--------|-----------|--------------|
| ρ (Utilization) | < 0.8 | ≥ 1.0 (ระบบล่ม) |
| Wq (Wait Time) | ต่ำ | พุ่งสูงเมื่อ ρ → 1 |
| Lq (Queue Length) | ต่ำ | พุ่งสูงเมื่อ ρ → 1 |

---

*OmniCognitiveFabric v2.0 · Computer Network Project*
