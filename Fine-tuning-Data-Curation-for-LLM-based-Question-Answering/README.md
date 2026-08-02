# Fine-tuning Data Curation for LLM-based Question-Answering Using LoRA/QLoRA for a Specific Domain

This repository contains the INFO 621 final project of Our (Pineapple Programmers) team, which includes three team members: Xiaoqin Fu, Subhrajeet Ghosh, and Usama Ahmed. In this project, we develop a fine-tuning data curation method for answering questions of a specific domain: building energy.

## Directory Structure
```
.
├── data/
│   ├── processed/  (Cleaned and formatted data)
│   └── raw/  (Original data)
├── experiments/  (Experimential Results)
├── notebooks/
│   ├── exploratory/  (Initial data analysis)
│   └── reproducibility/  (Code for replication)
├── src/
│   └── config/  (LoRA and QLoRA fine-tuning config)
├── video/ (The videos demonstrating the execution of various programs on the server)
├── environment.yml (The environment file)
├── README.md
├── INFO_621_Final_Project_Report.pdf (The project report)
└── requirements.txt (The requirements of dependencies)
```
   
## Install Requirements
  * Python  
  * Conda environment (for Jupyter Notebooks) 
  * (NVIDIA H100) GPUs    
  * Dependencies listed in requirements.txt 
  * OpenAI API key
  * Hugging Face Token
  
## Part 1: Data Preparation

### Step 1.1: Parsing PDF document (raw data)

- Locally run notebooks/exploratory/PDFToTxt.ipynb to parse the PDF document "data/raw/EngineeringReference.pdf" to generate the parsed (unstructured) text file "data/processed/EngineeringReference.txt". 
 
### Step 1.2: Improving the text

- Upload the unstructured text file "data/processed/EngineeringReference.txt" to Google Drive.
- Upload notebooks/exploratory/GPT4ImproveTxt.ipynb to Google Colab.
- On your google colab, run GPT4ImproveTxt.ipynb to improve the parsed (unstructured) text file "EngineeringReference.txt" to generated the improved (structured) text file "data/processed/EngineeringReference1_5.txt".

### Step 1.3: Geneating Fine-tuning Training Data

- Upload notebooks/exploratory/GPT4TxtToQA.ipynb to Google Colab.
- On Google Colab, run GPT4ImproveTxt.ipynb to generate many (193) question-answer pairs and to save them in the text file "EngineeringReference1_5_QAGPT4.txt".
- From Google Colab, download the text file "EngineeringReference1_5_QAGPT4.txt" to a local folder, such as data/processed/.
- Locally run TxtToJSON.py to transfer the improve text file "EngineeringReference1_5_QAGPT4.txt" to the JSON file "EngineeringReference1_5_QAGPT4.json", as the training data.

### Step 1.4: Geneating Fine-tuning Testing Data

- Upload notebooks/exploratory/GPT4TxtToQA_testdata.ipynb to Google Colab.
- On Google Colab, run GPT4ImproveTxt.ipynb to generate a few (17) and different question-answer pairs and to save them in the text file "EngineeringReference1_5_TESTQAGPT4omini.txt".
- From Google Colab, download the text file "EngineeringReference1_5_TESTQAGPT4omini.txt" to a local folder, such as data/processed/.
- Locally run TxtToJSON.py to transfer the improve text file "EngineeringReference1_5_TESTQAGPT4omini.txt" to the JSON file "EngineeringReference1_5_TESTQAGPT4omini.json", as the testing data.

## Part 2: LLM Execution 

### Step 2.1: Fine-tuning and Testing 

- Upload the traning data “EngineeringReference1_5_QAGPT4.json“ and the testing data "EngineeringReference1_5_TESTQAGPT4omini.json" to a folder (such as /srv/data1/fuxiaoqin/Downloads/) in the server with a conda environment and (three 80 GB NVIDIA H100) GPUs.

#### Step 2.1.1: Fine-tuning and Testing Llama 3.2 1B

- Upload notebooks/reproducibility/LoRAQLoRA_FinetuneLlama_1B.ipynb to the server.
- Run LoRAQLoRA_FinetuneLlama_1B.ipynb.
- Upload generated metric files (i.e., Metrics_LM32_1B_Before.csv, Metrics_LM32_1B_QA_LoRA.csv, Metrics_LM32_1B_QA_QLoRA.csv) and result files (i.e., Results_LM32_1B_Before.csv, Results_LM32_1B_QA_LoRA.csv, Results_LM32_1B_QA_QLoRA.csv) from the server to Google Colab.
(Note: *_Before.csv files mean for the foundation model (base) before the fine-tuning.)

#### Step 2.1.2: Fine-tuning and Testing Llama 3.2 3B

- Upload notebooks/reproducibility/LoRAQLoRA_FinetuneLlama_3B.ipynb to the server.
- Run LoRAQLoRA_FinetuneLlama_3B.ipynb.
- Upload generated metric files (i.e., Metrics_LM32_3B_Before.csv, Metrics_LM32_3B_QA_LoRA.csv, Metrics_LM32_3B_QA_QLoRA.csv) and result files (i.e., Results_LM32_3B_Before.csv, Results_LM32_3B_QA_LoRA.csv, Results_LM32_3B_QA_QLoRA.csv) from the server to Google Colab.
(Note: *_Before.csv files mean for the foundation model (base) before the fine-tuning.)

### Step 2.2: Evaluation

- Upload the evaluation program notebooks/exploratory/GPT4GradeQAs.ipynb to Google Colab.

#### Step 2.2.1: Evaluating Llama 3.2 1B Results

- In notebooks/exploratory/GPT4GradeQAs.ipynb, find two lines:
  + csvFile = pandas.read_csv('/content/drive/MyDrive/Results_LM32_1B_Before.csv', sep=',', header=0, encoding='utf-8')
  + output_name = "Results_LM32_1B_Before_Scores_"+str(times+1)+".csv"
- Update the file name (Results_LM32_1B_Before) to your testing result file (Results_LM32_1B_Before) before fine-tuning and then run GPT4GradeQAs.ipynb.
- Update the file name (Results_LM32_1B_Before) to your testing result file (Results_LM32_1B_QA_LoRA) after LoRA fine-tuning and then run GPT4GradeQAs.ipynb.
- Update the file name (Results_LM32_1B_QA_LoRA) to your testing result file (Results_LM32_1B_QA_QLoRA) after LoRA fine-tuning and then run GPT4GradeQAs.ipynb.

#### Step 2.2.2: Evaluating Llama 3.2 3B Results

- In notebooks/exploratory/GPT4GradeQAs.ipynb, find two lines:
  + csvFile = pandas.read_csv('/content/drive/MyDrive/Results_LM32_1B_QA_LoRA.csv', sep=',', header=0, encoding='utf-8')
  + output_name = "Results_LM32_1B_QA_LoRA_Scores_"+str(times+1)+".csv"
- Update the file name (Results_LM32_1B_QA_LoRA) to your testing result file (Results_LM32_3B_Before) before fine-tuning and then run GPT4GradeQAs.ipynb.
- Update the file name (Results_LM32_3B_Before) to your testing result file (Results_LM32_3B_QA_LoRA) after LoRA fine-tuning and then run GPT4GradeQAs.ipynb.
- Update the file name (Results_LM32_3B_Before) to your testing result file (Results_LM32_3B_QA_LoRA) after LoRA fine-tuning and then run GPT4GradeQAs.ipynb.
- 
### Step 2.3: Analysis and Visualization

- Download all metric files (i.e., Metrics_LM32_1B_Before.csv, Metrics_LM32_1B_QA_LoRA.csv, Metrics_LM32_1B_QA_QLoRA.csv, Metrics_LM32_3B_Before.csv, Metrics_LM32_3B_QA_LoRA.csv, Metrics_LM32_3B_QA_QLoRA.csv) and result files (i.e., Results_LM32_1B_Before.csv, Results_LM32_1B_QA_LoRA.csv, Results_LM32_1B_QA_QLoRA.csv, Results_LM32_3B_Before.csv, Results_LM32_3B_QA_LoRA.csv, Results_LM32_3B_QA_QLoRA.csv) from the server to a folder (e.g., experiments/) in your local computer.
- Locally perform notebooks/reproducibility/CompareMetrics.ipynb to compare the metrics of the foundational models (bases) and LoRA/QLoRA fine-tund models of Llama 3.2 1B and 3B.
- Locally perform notebooks/reproducibility/get_questions_answers_scores.ipynb to generate a csv file (i.e., QAS_1B3B.csv) the results and corresponding evluation scores of the foundational models (bases) and LoRA/QLoRA fine-tund models of Llama 3.2 1B and 3B.

### Step 2.4: Loading Fine-tuned LLMs from Hugging Face (Optional)
- Upload notebooks/reproducibility/Fine-tuned_Llama_1B_results.ipynb and notebooks/reproducibility/Fine-tuned_Llama_3B_results.ipynb to the server.
- Run Fine-tuned_Llama_1B_results.ipynb and Fine-tuned_Llama_3B_results.ipynb, respectively.
