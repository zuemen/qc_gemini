# Quantum Credit Risk Analysis 🚀

A professional implementation of **Quantum Amplitude Estimation (QAE)** for financial risk assessment, specifically focused on **Expected Loss (EL)** calculation for credit portfolios.

## 📌 Overview
Traditional Credit Risk Analysis often relies on Monte Carlo simulations, which can be computationally expensive. This project utilizes the **Iterative Amplitude Estimation (IAE)** algorithm from Qiskit to achieve a theoretical quadratic speedup in estimating the expected loss of a portfolio.

### Key Concepts
- **Bernoulli Distribution**: Models the default probability (PD) of individual assets.
- **LGD Encoding**: Encodes the Loss Given Default into the quantum state amplitudes.
- **QAE**: Estimates the expectation value of the loss without full state measurement.

## 🛠 Features
- **Quantum Circuit Visualization**: Automatically generates high-quality diagrams of the credit risk quantum circuits.
- **Statistical Benchmarking**: Compares Quantum results against Classical Theoretical baselines.
- **Scalable Architecture**: Object-oriented Python design allowing for easy expansion of asset portfolios.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Qiskit 1.0+
- Qiskit Algorithms
- Matplotlib & NumPy

### Installation
```bash
pip install qiskit qiskit-aer qiskit-algorithms matplotlib numpy
```

### Usage
Run the main analysis script:
```bash
python quantum_credit_risk_analysis.py
```

## 📊 Results & Visualization
Upon execution, the system generates two key artifacts:
1. `quantum_circuit.png`: A visual representation of the quantum gates used in the analysis.
2. `quantum_credit_risk_result.png`: A comparative chart showing the accuracy of the Quantum estimation vs. Classical calculation.

## 🏗 Project Structure
- `quantum_credit_risk_analysis.py`: Main system logic and algorithm implementation.
- `quantum_circuit.png`: (Generated) High-level quantum circuit diagram.
- `quantum_credit_risk_result.png`: (Generated) Final analysis report chart.

---
*Developed as a part of the Quantum Finance Research project.*
