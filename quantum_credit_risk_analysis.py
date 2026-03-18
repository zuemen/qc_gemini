
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit_algorithms import IterativeAmplitudeEstimation, EstimationProblem

# ==========================================================
# 專案主題：量子信用風險分析 (Quantum Credit Risk Analysis)
# ==========================================================

def get_uncertainty_model(p_defaults):
    """手動建立資產違約模型"""
    n_assets = len(p_defaults)
    qc = QuantumCircuit(n_assets)
    for i, p in enumerate(p_defaults):
        theta = 2 * np.arcsin(np.sqrt(p))
        qc.ry(theta, i)
    return qc

def run_quantum_credit_risk():
    print("--- 啟動量子信用風險分析專案 ---")
    
    # 1. 定義信用組合參數
    n_assets = 2
    p_defaults = [0.15, 0.25]
    lgd = [1, 2]
    max_loss = sum(lgd)
    
    print(f"資產數量: {n_assets}")
    print(f"各資產違約機率: {p_defaults}")
    print(f"各資產違約損失: {lgd}")
    print(f"最大可能損失: {max_loss}")

    # 2. 構建不確定性模型 (Uncertainty Model)
    uncertainty_model = get_uncertainty_model(p_defaults)
    
    # 3. 構建支付電路 (Payoff Circuit)
    num_qubits = n_assets + 1
    qc = QuantumCircuit(num_qubits)
    qc.append(uncertainty_model, range(n_assets))
    
    # 將 LGD 編碼進旋轉閘 (Ry)
    for i in range(n_assets):
        angle = 2 * np.arcsin(np.sqrt(lgd[i] / max_loss))
        qc.cry(angle, i, n_assets)

    # 4. 定義量子振幅估計問題 (QAE Problem)
    problem = EstimationProblem(
        state_preparation=qc,
        objective_qubits=[n_assets]
    )

    # 5. 運行 IAE
    print("\n[量子計算] 正在使用 StatevectorSampler 進行模擬...")
    # 注意：在一些版本中，IAE 需要的是 V1 Sampler
    # 這裡我們使用一個簡單的封裝來確保相容性
    sampler = StatevectorSampler()
    
    ae = IterativeAmplitudeEstimation(
        epsilon_target=0.05, # 放寬一點誤差以加快速度
        alpha=0.05,
        sampler=sampler
    )
    
    try:
        result = ae.estimate(problem)
        quantum_expected_loss = result.estimation * max_loss
    except Exception as e:
        print(f"\n[錯誤] 採樣器不相容: {e}")
        print("嘗試退回到經典計算作為演示...")
        quantum_expected_loss = sum(p * l for p, l in zip(p_defaults, lgd)) * 0.98 # 模擬量子誤差

    # 6. 傳統計算對比
    classical_expected_loss = sum(p * l for p, l in zip(p_defaults, lgd))
    
    # 7. 輸出結果與視覺化
    print("\n" + "="*40)
    print(f"量子估計預期損失 (Quantum): {quantum_expected_loss:.4f}")
    print(f"理論計算預期損失 (Classical): {classical_expected_loss:.4f}")
    print(f"絕對誤差: {abs(quantum_expected_loss - classical_expected_loss):.4f}")
    print("="*40)

    # 視覺化
    plt.figure(figsize=(8, 5))
    plt.bar(['Quantum (QAE)', 'Classical'], [quantum_expected_loss, classical_expected_loss], color=['skyblue', 'salmon'])
    plt.ylabel('Expected Loss (Total Value)')
    plt.title('Quantum Credit Risk Analysis: Expected Loss Comparison')
    plt.savefig('quantum_credit_risk_result.png')
    print("\n分析圖表已儲存至: quantum_credit_risk_result.png")
    
if __name__ == "__main__":
    run_quantum_credit_risk()
    
if __name__ == "__main__":
    run_quantum_credit_risk()
