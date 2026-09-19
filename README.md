# Public Sector Corruption Analytics — Bribe Reporting Study

An investigative data analytics project analyzing citizen-reported corruption records to uncover systemic patterns, most affected public departments, and geographic bribe concentrations.

[![Kaggle Notebook](https://img.shields.io/badge/Kaggle-Notebook-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/code/lazer999/exposing-the-most-corrupt-departments)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Field](https://img.shields.io/badge/Field-Exploratory%20Data%20Analysis%20/%20Civic%20Analytics-brightgreen)](#)

---

## Table of Contents
- [Project Overview](#project-overview)
- [Key Highlights & Results](#key-highlights--results)
- [System Architecture & Workflow](#system-architecture--workflow)
- [Repository Structure](#repository-structure)
- [Quickstart & Reproduction](#quickstart--reproduction)
- [Dataset Details](#dataset-details)
- [Author & Acknowledgments](#author--acknowledgments)

---

## Project Overview

This repository provides the complete, production-structured implementation of the **[Public Sector Corruption Analytics — Bribe Reporting Study](https://www.kaggle.com/code/lazer999/exposing-the-most-corrupt-departments)** project originally published on Kaggle. 

The primary focus of this work is translating complex data into actionable machine learning solutions using disciplined data engineering, rigorous validation strategies, and clean, leak-free preprocessing pipelines.

---

## Key Highlights & Results

- Cleaned and normalized thousands of crowd-sourced citizen reports on public bribery.
- Rank-ordered departments by bribery frequency and total financial extortion (Police, Municipal, Transport, Revenue).
- Geographical breakdown mapping reports across states and major metropolitan centers.
- Analyzed citizen engagement: correlation between transaction scale and report readership.

---

## System Architecture & Workflow

The pipeline follows a structured, modular execution path:

```mermaid
flowchart LR
    A[Citizen Bribe Reports] --> B[Amount Parsing & Categorical Cleansing]
    B --> C[Departmental Frequency & Value Ranking]
    B --> D[Geographic State & City Mapping]
    C --> E[Department vs Amount Profiling]
    D --> E
    E --> F[Civic Transparency Report]
```

---

## Repository Structure

```plaintext
public-sector-corruption-analysis/
├── notebooks/
│   └── public-sector-corruption-analysis.ipynb      # Original Jupyter notebook with full exploratory visuals
├── src/
│   └── main.py                # Modular, executable Python pipeline
├── .gitignore                 # Standard Python/Jupyter ignores
├── LICENSE                    # MIT License
├── README.md                  # Human-friendly documentation
└── requirements.txt           # Verified Python dependencies
```

---

## Quickstart & Reproduction

### 1. Clone the Repository
```bash
git clone https://github.com/musaoc/public-sector-corruption-analysis.git
cd public-sector-corruption-analysis
```

### 2. Set Up a Virtual Environment
```bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the Pipeline
You can run the end-to-end script directly:
```bash
python src/main.py
```

Or open and run the interactive notebook:
```bash
jupyter lab notebooks/public-sector-corruption-analysis.ipynb
```

---

## Dataset Details

- **Dataset / Competition**: [I Paid a Bribe Dataset](https://www.kaggle.com/datasets/lazer999/corruption)
- **Origin Platform**: Kaggle
- For automated dataset downloading via Kaggle CLI:
  ```bash
  kaggle datasets download -d lazer999/corruption
  ```

---

## Author & Acknowledgments

- **Author**: **Muhammad Musa Khan** (Kaggle Master)
- **Kaggle Profile**: [@lazer999](https://www.kaggle.com/lazer999)
- **GitHub**: [@musaoc](https://github.com/musaoc)
- **Original Kaggle Solution**: [Public Sector Corruption Analytics — Bribe Reporting Study](https://www.kaggle.com/code/lazer999/exposing-the-most-corrupt-departments)

If you found this project helpful or insightful, please consider starring the repository ⭐!
