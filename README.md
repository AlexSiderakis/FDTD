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
![Figure_50](https://github.com/user-attachments/assets/00595934-9562-441b-9876-a300306b5bc7)
![Figure_100](https://github.com/user-attachments/assets/0bde84ee-6b98-49b9-94c6-df75ff4445e0)
![Figure_200](https://github.com/user-attachments/assets/26052309-c2df-492a-a8ac-30e20786d99d)
![Figure_300](https://github.com/user-attachments/assets/d2a5cd03-338e-4427-a068-9193a7fb8f81)
![Figure_400](https://github.com/user-attachments/assets/e1305fbe-a6da-443f-8c44-fbabcc5ec6e5)
![Figure_500](https://github.com/user-attachments/assets/6548d369-9c2e-4bd3-a184-9b1a99be3c24)
![Figure_600](https://github.com/user-attachments/assets/37fe38e7-bf99-4c2b-b423-049f011f7a92)
![Figure_700](https://github.com/user-attachments/assets/56f64a9f-ddd0-4ba6-9957-69e99c94262b)



