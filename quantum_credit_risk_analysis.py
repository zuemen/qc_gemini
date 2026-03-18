
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit_algorithms import IterativeAmplitudeEstimation, EstimationProblem

class QuantumCreditRiskSystem:
    """
    Quantum Credit Risk Analysis System
    Using Iterative Amplitude Estimation (IAE) to estimate Expected Loss (EL).
    """
    
    def __init__(self, p_defaults, lgd):
        self.p_defaults = p_defaults
        self.lgd = lgd
        self.n_assets = len(p_defaults)
        self.max_loss = sum(lgd)
        self.qc = None
        self.uncertainty_model = None

    def build_uncertainty_model(self):
        """Constructs the Bernoulli distribution for asset defaults."""
        qc = QuantumCircuit(self.n_assets, name="Uncertainty")
        for i, p in enumerate(self.p_defaults):
            theta = 2 * np.arcsin(np.sqrt(p))
            qc.ry(theta, i)
        self.uncertainty_model = qc
        return qc

    def build_full_circuit(self):
        """Constructs the full pricing circuit including LGD encoding."""
        num_qubits = self.n_assets + 1
        qc = QuantumCircuit(num_qubits, name="CreditRisk")
        
        # Load uncertainty model
        qc.append(self.build_uncertainty_model(), range(self.n_assets))
        qc.barrier()
        
        # Encode Loss Given Default (LGD) into the objective qubit
        for i in range(self.n_assets):
            angle = 2 * np.arcsin(np.sqrt(self.lgd[i] / self.max_loss))
            qc.cry(angle, i, self.n_assets)
        
        self.qc = qc
        return qc

    def visualize_circuit(self, filename='quantum_circuit.png'):
        """Generates and saves a visualization of the quantum circuit."""
        print(f"[系統] 正在繪製量子電路圖...")
        if self.qc is None:
            self.build_full_circuit()
        
        # Use matplotlib to draw the circuit
        fig = self.qc.draw(output='mpl', style='iqp')
        fig.savefig(filename)
        print(f"量子電路圖已儲存至: {filename}")

    def run_analysis(self, epsilon=0.01):
        """Executes the Quantum Amplitude Estimation."""
        print("\n--- 啟動量子信用風險核心分析 ---")
        if self.qc is None:
            self.build_full_circuit()
            
        problem = EstimationProblem(
            state_preparation=self.qc,
            objective_qubits=[self.n_assets]
        )

        sampler = StatevectorSampler()
        ae = IterativeAmplitudeEstimation(
            epsilon_target=epsilon,
            alpha=0.05,
            sampler=sampler
        )
        
        print(f"[量子計算] 使用 StatevectorSampler 進行振幅估計 (epsilon={epsilon})...")
        result = ae.estimate(problem)
        
        quantum_el = result.estimation * self.max_loss
        classical_el = sum(p * l for p, l in zip(self.p_defaults, self.lgd))
        
        self._print_results(quantum_el, classical_el)
        self._plot_comparison(quantum_el, classical_el)
        
        return quantum_el

    def _print_results(self, q_el, c_el):
        print("\n" + "="*50)
        print(f"{'分析維度':<20} | {'數值':<15}")
        print("-" * 50)
        print(f"{'量子估計預期損失':<20} | {q_el:.4f}")
        print(f"{'傳統理論預期損失':<20} | {c_el:.4f}")
        print(f"{'估計絕對誤差':<20} | {abs(q_el - c_el):.4f}")
        print("="*50)

    def _plot_comparison(self, q_el, c_el, filename='quantum_credit_risk_result.png'):
        plt.figure(figsize=(10, 6))
        bars = plt.bar(['Quantum (QAE)', 'Classical (Theoretical)'], [q_el, c_el], 
                       color=['#61affe', '#ff7675'], edgecolor='black', alpha=0.8)
        
        plt.ylabel('Expected Loss ($)', fontsize=12)
        plt.title('Quantum Credit Risk Analysis: Comparison Study', fontsize=14, fontweight='bold')
        
        # Add value labels
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01, f'{yval:.4f}', ha='center', va='bottom', fontweight='bold')
            
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.savefig(filename)
        print(f"對比分析圖表已儲存至: {filename}")

if __name__ == "__main__":
    # 配置參數
    PD_LIST = [0.15, 0.25, 0.10]  # 資產違約機率
    LGD_LIST = [1.0, 2.0, 1.5]     # 資產違約損失
    
    system = QuantumCreditRiskSystem(PD_LIST, LGD_LIST)
    
    # 執行流程
    system.visualize_circuit()
    system.run_analysis(epsilon=0.02)
    
if __name__ == "__main__":
    run_quantum_credit_risk()
    
if __name__ == "__main__":
    run_quantum_credit_risk()
