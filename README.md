# HexSoftwares_Project_EDA

Clean the data of electric vehicle population, handle missing values, and perform basic statistical analysis. Visualize data distributions, correlations, and key patterns using charts and graphs. Tools: Python (Pandas, Matplotlib, Seaborn, Scikit-learn)

## Project Overview

This project performs Exploratory Data Analysis (EDA) on Electric Vehicle Population Data, including:
- Data loading and preprocessing
- Handling missing values
- Feature engineering
- Logistic regression classification model
- Model evaluation with confusion matrix, accuracy, and precision metrics
- Visualization of results including ROC curve

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the main analysis script:

```bash
python ev_analysis.py
```

**Note:** The script expects the dataset at `/content/sample_data/Electric_Vehicle_Population_Data.csv.zip`. Please ensure the data file is available at this location or modify the `file_path` variable in the script accordingly.

## Features

- **Data Loading:** Reads Electric Vehicle Population Data from CSV/ZIP file
- **Feature Selection:** Uses Model Year, Electric Range, and Base MSRP as features
- **Target Variable:** Predicts Clean Alternative Fuel Vehicle (CAFV) Eligibility
- **Model Training:** Implements Logistic Regression classifier
- **Evaluation Metrics:** Calculates accuracy, precision, and confusion matrix
- **Visualizations:**
  - Confusion Matrix heatmap
  - Accuracy bar chart
  - ROC Curve with AUC score

## Requirements

- Python 3.7+
- pandas
- scikit-learn
- matplotlib
- numpy
