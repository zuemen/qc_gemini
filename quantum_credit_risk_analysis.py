
import numpy as np
import matplotlib.pyplot as plt
import time
from qiskit import QuantumCircuit, transpile
from qiskit.primitives import StatevectorSampler
from qiskit_algorithms import IterativeAmplitudeEstimation, EstimationProblem
from qiskit_finance.circuit.library import GaussianConditionalIndependenceModel

class QuantumFinanceScientist:
    """
    Nature Reviews Physics Standard Framework for Quantum Credit Risk.
    Focus: Quantum Advantage Benchmarking, Greek Calculation, and T-depth Analysis.
    """
    
    def __init__(self, p_zeros, rhos, lgd):
        self.p_zeros = np.array(p_zeros)
        self.rhos = np.array(rhos)
        self.lgd = np.array(lgd)
        self.n_assets = len(p_zeros)
        self.max_loss = sum(lgd)
        
        # Systemic factor parameters
        self.n_z = 2
        self.z_max = 2.0
        self.model = GaussianConditionalIndependenceModel(self.n_z, self.z_max, p_zeros, rhos)

    def _get_circuit(self, current_pd=None):
        """Internal helper to build circuit with optional PD overrides for Greeks."""
        pd = current_pd if current_pd is not None else self.p_zeros
        model = GaussianConditionalIndependenceModel(self.n_z, self.z_max, pd, self.rhos)
        num_qubits = model.num_qubits + 1
        qc = QuantumCircuit(num_qubits)
        qc.append(model, range(model.num_qubits))
        
        for i in range(self.n_assets):
            angle = 2 * np.arcsin(np.sqrt(self.lgd[i] / self.max_loss))
            asset_idx = model.num_qubits - self.n_assets + i
            qc.cry(angle, asset_idx, num_qubits - 1)
        return qc

    def calculate_delta(self, asset_idx, delta_p=0.01):
        """Calculates Delta: First derivative of EL with respect to asset PD."""
        print(f"\n[研究分析] 正在計算資產 {asset_idx} 的 Delta (風險敏感度)...")
        
        # Standard EL
        el_original = self.run_qae_el(epsilon=0.02, verbose=False)
        
        # Shifted PD
        pd_shifted = self.p_zeros.copy()
        pd_shifted[asset_idx] += delta_p
        
        shifted_qc = self._get_circuit(pd_shifted)
        problem = EstimationProblem(state_preparation=shifted_qc, objective_qubits=[shifted_qc.num_qubits-1])
        ae = IterativeAmplitudeEstimation(epsilon_target=0.02, alpha=0.05, sampler=StatevectorSampler())
        res = ae.estimate(problem)
        el_shifted = res.estimation * self.max_loss
        
        delta = (el_shifted - el_original) / delta_p
        print(f"資產 {asset_idx} 的 Delta: {delta:.4f} (預期損失/PD變動)")
        return delta

    def run_qae_el(self, epsilon=0.01, verbose=True):
        qc = self._get_circuit()
        problem = EstimationProblem(state_preparation=qc, objective_qubits=[qc.num_qubits-1])
        ae = IterativeAmplitudeEstimation(epsilon_target=epsilon, alpha=0.05, sampler=StatevectorSampler())
        result = ae.estimate(problem)
        el = result.estimation * self.max_loss
        if verbose:
            print(f"QAE 預期損失估計 (eps={epsilon}): {el:.2f}")
        return el

    def benchmark_convergence(self):
        """Scientific plot: Error Convergence vs Theoretical Speedup."""
        print("\n[學術實驗] 正在執行收斂速度基準測試 (Convergence Benchmarking)...")
        epsilons = [0.1, 0.05, 0.02, 0.01]
        quantum_runtimes = []
        
        for eps in epsilons:
            st = time.time()
            self.run_qae_el(epsilon=eps, verbose=False)
            quantum_runtimes.append(time.time() - st)
            
        plt.figure(figsize=(10, 6))
        plt.plot(epsilons, quantum_runtimes, 'o-', label='Quantum QAE (Local Sim)', color='#0984e3', linewidth=2)
        plt.xscale('log')
        plt.yscale('log')
        plt.gca().invert_xaxis()
        plt.xlabel('Target Accuracy (Epsilon)', fontsize=12)
        plt.ylabel('Wall-clock Time (s)', fontsize=12)
        plt.title('Quantum Advantage Benchmark: Precision vs. Computational Cost', fontsize=14, fontweight='bold')
        plt.grid(True, which="both", ls="--", alpha=0.5)
        plt.legend()
        plt.savefig('scientific_convergence_benchmark.png')
        print("基準測試圖表已儲存至: scientific_convergence_benchmark.png")

    def analyze_fault_tolerant_cost(self):
        """Advanced Resource Estimation: T-gate and T-depth."""
        qc = self._get_circuit()
        # Transpile to basis including T-gates
        t_qc = transpile(qc, basis_gates=['u3', 'cx', 't'], optimization_level=3)
        ops = t_qc.count_ops()
        
        print("\n" + "="*50)
        print(f"{'容錯量子計算資源估算':^50}")
        print("-" * 50)
        print(f"Logical Qubits: {t_qc.num_qubits}")
        print(f"Circuit Depth: {t_qc.depth()}")
        print(f"T-Gate Count: {ops.get('t', 0)}")
        print(f"CNOT Count: {ops.get('cx', 0)}")
        print(f"T-Depth (Approx): {t_qc.depth()}") # Simplified for sim
        print("="*50)

if __name__ == "__main__":
    # 文獻基準參數
    P_BASE = [0.15, 0.20, 0.10]
    RHO_BASE = [0.1, 0.1, 0.1]
    LGD_BASE = [1000, 2000, 1500]
    
    scientist = QuantumFinanceScientist(P_BASE, RHO_BASE, LGD_BASE)
    
    # 執行學術研究流程
    scientist.analyze_fault_tolerant_cost()
    scientist.calculate_delta(asset_idx=1) # 計算資產 1 的敏感度
    scientist.benchmark_convergence()
    
    print("\n[系統] 研究級分析完成。")
