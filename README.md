# 量子信用風險分析研究實驗室 (Quantum Credit Risk Research Lab) 🚀

本專案是一個具備「工業級」與「科研級」標準的量子金融分析系統。本系統整合了 **Nature Reviews Physics**, **IEEE Transactions on Computers** 以及 **Entropy** 等國際頂尖期刊之研究方法，實作了基於量子振幅估計 (QAE) 的信用風險評估框架。

---

## 📌 核心研究功能

本系統不只是簡單的模擬器，它包含了以下具備學術深度的專業功能：

1.  **系統性風險建模 (Gaussian Conditional Independence Model)**
    *   參考 **Basel II** 標準，引入潛在市場因子 $Z$。
    *   模擬資產間的相關性 (Correlation)，而非單純的獨立違約。
2.  **關鍵風險指標計算 (Economic Capital & VaR)**
    *   計算 **預期損失 (Expected Loss, EL)**。
    *   利用量子演算法估算 **風險價值 (Value at Risk, VaR)** 與 **經濟資本 (Economic Capital, Ecap)**。
3.  **量子優勢基準測試 (Quantum Advantage Benchmarking)**
    *   自動對比量子 QAE 演算法與傳統蒙地卡羅 (CMC) 在不同精度下的收斂效率。
    *   實證量子演算法相對於經典算法的平方級加速 (Quadratic Speedup) 理論。
4.  **容錯量子資源評估 (Quantum Resource Estimation)**
    *   自動分析電路深度 (Depth)、邏輯位元數 (Qubits) 與 CNOT 閘數。
    *   提供未來在「容錯量子計算機 (Fault-Tolerant Hardware)」上執行的成本報告。

---

## 🛠 環境要求

啟動本專案前，請確保您的環境具備以下條件：

*   **Python 版本**: 3.8 或以上
*   **必要套件**:
    ```bash
    pip install qiskit qiskit-aer qiskit-finance qiskit-algorithms matplotlib numpy pandas pylatexenc
    ```

---

## 🚀 操作步驟：如何啟動

### 1. 取得專案
您可以直接下載本專案資料夾，或使用 Git 複製倉庫：
```bash
git clone https://github.com/zuemen/qc_gemini.git
cd qc_gemini
```

### 2. 執行分析系統
在終端機 (Terminal/PowerShell) 執行主程式：
```bash
python quantum_credit_risk_analysis.py
```

### 3. 查看研究報告
執行完成後，系統會自動在資料夾中生成以下專業產出：
*   **終端機輸出**: 詳細的資源分析報告、EL/VaR/Ecap 數值報告。
*   **`quantum_advantage_benchmark.png`**: 展示量子與經典算法效率對比的收斂曲線圖。
*   **`risk_profile_analysis.png`**: 視覺化資產組合的風險概況 (EL vs. VaR vs. Ecap)。
*   **`research_quantum_circuit.png`**: 系統自動繪製的高品質量子電路結構圖。

---

## 🏗 專案結構說明

*   `quantum_credit_risk_analysis.py`: 核心科研框架，採用物件導向設計 (OOP)。
*   `README.md`: 專案使用說明與學術背景。
*   `*.png`: 自動生成的實驗圖表與科研數據。

---

## 📚 學術參考文獻

本專案之設計嚴格參考以下頂尖科研文獻：
1.  **Herman et al. (2023)**, *Nature Reviews Physics* - Quantum computing for finance.
2.  **Egger et al. (2021)**, *IEEE Transactions on Computers* - Credit Risk Analysis Using Quantum Computers.
3.  **Dri et al. (2023)**, *Entropy* - A More General Quantum Credit Risk Analysis Framework.
4.  **Orús et al. (2019)**, *Reviews in Physics* - Quantum computing for finance: Overview and prospects.

---
*本專案由量子金融研究框架驅動，旨在展示量子計算在風險管理中的實務潛力。*
