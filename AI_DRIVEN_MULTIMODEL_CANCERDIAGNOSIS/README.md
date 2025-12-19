# Capstone Project
🧠 **AI-Driven Multi-Modal Data Fusion for Early Cancer Diagnosis**

---

## 📘 Overview
This research project develops an AI-driven model integrating clinical and genomic data from the **MMIST-ccRCC** dataset to predict early-stage clear-cell renal cell carcinoma (ccRCC) survival outcomes.  

The project focuses on **multi-modal data fusion**, comparing:

- **Early Fusion:** Combining clinical and genomic features before model training.  
- **Late Fusion:** Combining predictions from separate models trained on each modality.  

The goal is to demonstrate how integrating complementary data modalities improves prediction accuracy and interpretability compared to unimodal approaches.

---

## 🎯 Objectives
- Train and evaluate machine learning models using clinical and genomic data.  
- Implement and compare **early fusion** and **late fusion** strategies.  
- Assess model performance using **Accuracy, Precision, Recall, F1-score, and ROC-AUC**.  
- Visualize feature importance and contributions from each modality.

---

## 🧩 Dataset
**Dataset Name:** MMIST-ccRCC (Multi-Modal Imaging and Clinical Dataset for ccRCC)  

**Data Used:**
- `clinical.csv` – Patient demographics, lab results, and clinical features.  
- `genomic_split.csv` – Gene expression and mutation data.  

> ⚠️ Note: Imaging data (CT/MRI/WSI) is excluded in this study.  

**Data Source:**  
Mota, Tiago et al. *“MMIST-ccRCC: A Real-World Medical Dataset for the Development of Multi-Modal Systems.”*  
[Dataset Website](https://multi-modal-ist.github.io/datasets/ccRCC/)

---

## ⚙️ Methodology

### 1. Data Preprocessing
- Handle missing values and normalize features.  
- Encode categorical clinical variables.  
- Merge datasets on patient identifiers (`case_id`).  
- Split into **training (70%)**, **validation (15%)**, and **test (15%)** sets.  

### 2. Modeling Approaches
**Classical ML Models:**  
- Logistic Regression  
- Random Forest  

**Deep Learning Models:**  
- Feed-Forward Neural Networks (FFNN / MLP) for each modality.  

**Fusion Strategies:**  
- **Early Fusion:** Concatenate feature spaces of clinical + genomic data.  
- **Late Fusion:** Combine predictions from modality-specific models using ensemble averaging or meta-learning.

### 3. Evaluation Metrics
- **Accuracy**  
- **Precision / Recall / F1-Score**  
- **ROC-AUC (Area Under Curve)**  
- **Confusion Matrix and ROC Curve Visualization**  

---

## 📊 Expected Outcomes
- Cleaned and preprocessed multi-modal dataset.  
- Trained early and late fusion models.  
- Comparative charts showing performance improvements over unimodal approaches.  
- Visualizations of feature importance and modality contributions.  
- Insights on model interpretability and clinical applicability.

---

## 💻 Usage

1. **Clone the repository**
```bash
git clone https://github.com/Harikas07/Capstone_Project.git
cd Capstone_Project
