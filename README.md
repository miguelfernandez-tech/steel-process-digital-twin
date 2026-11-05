# Process Digital Twin: Continuous Casting & Rolling Mill Synchronization
### Operational Optimization at ArcelorMittal Gijón

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![SimPy](https://img.shields.io/badge/SimPy-4.1.1-green.svg)
![Domain](https://img.shields.io/badge/Domain-Industrial%20Engineering%20%7C%20Operations%20Research-orange.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

---

## 1. Executive Summary & Problem Formulation

In integrated steel manufacturing facilities such as **ArcelorMittal Gijón (Veriña, Spain)**, a critical operational bottleneck occurs at the interface between the **Continuous Casting Machine (CCM)** and the **Hot Rolling Mill (RM)**.

* **Rigid Upstream Process:** Continuous casting solidifies molten steel into semi-finished billets at a continuous rate. Halting the caster abruptly leads to thermal shocks, severe refractory wear, and yield loss.
* **Stochastic Downstream Disruptions:** Hot rolling mills operate as discrete finishing systems subject to operational disruptions, such as mechanical micro-stoppages, cobbles, and guide adjustments.
* **The Thermal Penalty ($D_{cold}$):** Direct hot charging (introducing hot billets directly into the reheat furnace/rolling mill) minimizes natural gas consumption. However, when mill breakdowns occur and the intermediate holding buffer saturates ($B(t) \ge C_{max}$), billets must be diverted to an outdoor cold yard. Cold billets lose all thermal inertia, requiring extensive reheating, increasing specific fuel consumption (GJ/ton), and elevating Work-In-Process (WIP) holding costs.

This repository implements an operational **Process Digital Twin (DES)** using Python and **SimPy** to model shop-floor dynamics and evaluate a prescriptive pacing control policy.

---

## 2. Process Topology & Control Strategy

```text
+-----------------------+        +--------------------------+        +----------------------+
|  Continuous Casting   | -----> | Intermediate Hot Buffer  | -----> | Hot Rolling Mill     |
|  (Upstream Generator) |        | Capacity: C_max = 12     |        | (Single Server)      |
+-----------------------+        +--------------------------+        +----------------------+
                                               |
                                    If Buffer Level >= C_max
                                               v
                                 +--------------------------+
                                 | Cold Stacking Yard       |
                                 | (Thermal Loss Penalty)   |
                                 +--------------------------+
