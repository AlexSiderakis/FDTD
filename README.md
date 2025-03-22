# Finite-Difference Time-Domain (FDTD) Method Simulation

## Overview

This project simulates electromagnetic wave propagation using the **Finite-Difference Time-Domain (FDTD)** method. The simulation is performed on a **100 × 100** grid in the **xy-plane**, where a **Drude material** is placed in the region **y = 40 to y = 70**. A sinusoidal pulse source is positioned at **(x, y) = (50, 25)**. The simulation incorporates **Mur’s second-order absorbing boundary conditions** to prevent wave reflections at the edges.

## Key Concepts

- **Electromagnetic Wave Propagation**: The simulation models the behavior of an electromagnetic pulse interacting with a dispersive material.
- **FDTD Method**: Discretizes Maxwell’s equations in both space and time.
- **Drude Model**: A material model accounting for frequency-dependent permittivity.
- **Mur Absorbing Boundary Conditions**: Applied at the edges to minimize wave reflections.

## Simulation Implementation

The FDTD method is implemented in **Python** using `numpy` for numerical calculations and `matplotlib` for visualization.

### Dependencies

```bash
pip install numpy matplotlib
```

### Running the Simulation

Execute the following command to run the simulation:

```bash
python fdtd_simulation.py
```

## Expected Results
Outside the material, wave propagation follows standard Maxwell’s equations. Upon reaching the Drude material, part of the wave is transmitted, and part is reflected. The expected behavior is a lens-like effect, where the pulse converges and then re-emerges.  The expected behavior is a **lens-like effect**, where the wave converges and then re-emerges. The simulation captures wave evolution at different time steps (50, 100, 200, ..., 700 steps).

## Visualizations

Snapshots of the **Ez field** are generated at different time steps (50, 100, 200, ..., 700).

---
![Figure_50](https://github.com/user-attachments/assets/860ff1d4-8ce7-4a28-8924-c225cc8ee4ea)
![Figure_100](https://github.com/user-attachments/assets/d777a84d-7ef5-4230-880f-258ab6ac6e67)
![Figure_200](https://github.com/user-attachments/assets/700e1a32-7307-4d22-bdd5-7c9a84b9f151)
![Figure_300](https://github.com/user-attachments/assets/d3e0801c-7654-4c50-8f3d-a6399293b651)
![Figure_400](https://github.com/user-attachments/assets/456283b5-ebc4-4c97-9085-bb2b6a58eca5)
![Figure_500](https://github.com/user-attachments/assets/cdf020d8-1308-4826-b773-cf4457f1cba9)
![Figure_600](https://github.com/user-attachments/assets/1ad4357e-1897-4445-8c6c-c2d9c7197c2c)
![Figure_700](https://github.com/user-attachments/assets/3991f4ce-feb7-499e-8da9-d93f50e8987b)


