# HexSoftwares_Project_EDA

## Electric Vehicle Population - Exploratory Data Analysis

This project provides comprehensive tools and prompts for performing EDA (Exploratory Data Analysis) on Electric Vehicle Population datasets. Clean the data of electric vehicle population, handle missing values, and perform basic statistical analysis. Visualize data distributions, correlations, and key patterns using charts and graphs.

**Tools:** Python (Pandas, Matplotlib, Seaborn, NumPy, SciPy)

---

## 📋 Features

- **Data Loading and Exploration**: Load CSV data and perform initial exploration
- **Missing Value Analysis**: Identify, visualize, and handle missing values
- **Data Cleaning**: Multiple strategies for handling missing data and outliers
- **Statistical Analysis**: Comprehensive statistical metrics, distributions, correlations
- **Outlier Detection**: IQR and Z-score methods for outlier identification
- **Rich Visualizations**: 
  - Distribution plots
  - Correlation heatmaps
  - Box plots for outlier detection
  - Categorical variable analysis
- **Automated Reporting**: Generate comprehensive EDA reports
- **Interactive Notebook**: Jupyter notebook for step-by-step analysis

---

## 🚀 Quick Start

### 1. Installation

First, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2. Using the Python Script

```python
from ev_population_eda import EVPopulationEDA

# Initialize the EDA class
eda = EVPopulationEDA()

# Load your dataset
eda.load_data('path/to/your/ev_data.csv')

# Run complete EDA pipeline
eda.run_complete_eda()
```

### 3. Using the Jupyter Notebook

Open the interactive notebook:

```bash
jupyter notebook EV_Population_EDA.ipynb
```

Follow the step-by-step prompts in the notebook to perform your analysis.

---

## 📊 Dataset Structure

The tools are designed to work with Electric Vehicle Population datasets, typically containing columns such as:

- **VIN (Vehicle Identification Number)**: Unique identifier for each vehicle
- **County**: County where the vehicle is registered
- **City**: City where the vehicle is registered
- **State**: State where the vehicle is registered
- **Postal Code**: ZIP code
- **Model Year**: Year the vehicle was manufactured
- **Make**: Vehicle manufacturer (e.g., Tesla, Nissan, Chevrolet)
- **Model**: Vehicle model name
- **Electric Vehicle Type**: BEV (Battery Electric Vehicle) or PHEV (Plug-in Hybrid)
- **CAFV Eligibility**: Clean Alternative Fuel Vehicle eligibility
- **Electric Range**: Range in miles on electric power
- **Base MSRP**: Manufacturer's Suggested Retail Price
- **Legislative District**: District number
- **DOL Vehicle ID**: Department of Licensing ID
- **Vehicle Location**: Geographic coordinates
- **Electric Utility**: Utility provider
- **2020 Census Tract**: Census tract information

---

## 🔧 Usage Examples

### Example 1: Complete EDA Pipeline

```python
from ev_population_eda import EVPopulationEDA

# Initialize and load data
eda = EVPopulationEDA('electric_vehicle_data.csv')
eda.load_data()

# Run complete analysis
eda.run_complete_eda()
```

### Example 2: Step-by-Step Analysis

```python
from ev_population_eda import EVPopulationEDA

# Initialize
eda = EVPopulationEDA()
eda.load_data('ev_data.csv')

# Individual analysis steps
eda.initial_exploration()
eda.check_missing_values()
eda.handle_missing_values(strategy='auto')
eda.detect_outliers(method='iqr')
eda.statistical_analysis()

# Generate visualizations
eda.visualize_distributions()
eda.visualize_correlations()
eda.visualize_categorical(top_n=15)
eda.visualize_boxplots()

# Generate report
eda.generate_report()
```

### Example 3: Custom Missing Value Handling

```python
# Custom strategy for specific columns
custom_strategy = {
    'Electric Range': 'median',
    'Base MSRP': 'mean',
    'County': 'mode',
    'City': 'mode'
}

eda.handle_missing_values(strategy=custom_strategy)
```

---

## 📁 Project Structure

```
HexSoftwares_Project_EDA/
├── ev_population_eda.py      # Main Python script with EDA class
├── EV_Population_EDA.ipynb   # Interactive Jupyter notebook
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

---

## 🎯 Key Analysis Areas

### 1. Data Quality Assessment
- Missing value identification and handling
- Duplicate detection
- Data type validation
- Unique value analysis

### 2. Statistical Analysis
- Descriptive statistics (mean, median, std, etc.)
- Distribution metrics (skewness, kurtosis)
- Correlation analysis
- Outlier detection

### 3. Visualizations
- **Distribution Plots**: Histograms for numeric features
- **Correlation Heatmap**: Relationships between numeric variables
- **Box Plots**: Outlier visualization
- **Bar Charts**: Categorical variable analysis

### 4. Key Insights
- EV adoption patterns by geographic location
- Temporal trends in EV registration
- Popular manufacturers and models
- Electric range distribution
- Vehicle type distribution (BEV vs PHEV)

---

## 🔍 Example Questions to Answer

The EDA tools help answer questions such as:

1. **Distribution Patterns:**
   - What is the distribution of electric vehicles by make and model?
   - Which EV types are most common (BEV vs PHEV)?

2. **Geographic Insights:**
   - Which counties/cities have the highest EV adoption?
   - Are there geographic clusters?

3. **Temporal Trends:**
   - How has EV adoption changed over the years?
   - What is the distribution of model years?

4. **Technical Specifications:**
   - What is the average electric range?
   - How does range vary by manufacturer?

5. **Data Quality:**
   - Which features have the most missing data?
   - Are there any data quality issues to address?

---

## 📝 Output Files

After running the EDA, the following files will be generated:

- `distributions.png` - Distribution plots for numeric columns
- `correlation_heatmap.png` - Correlation matrix visualization
- `categorical_analysis.png` - Categorical variable analysis
- `boxplots.png` - Box plots for outlier detection
- `eda_report.txt` - Comprehensive text report
- `ev_population_cleaned.csv` - Cleaned dataset (from notebook)
- `eda_summary_report.txt` - Summary report (from notebook)

---

## 🛠️ Requirements

- Python 3.7+
- pandas >= 1.3.0
- numpy >= 1.21.0
- matplotlib >= 3.4.0
- seaborn >= 0.11.0
- scipy >= 1.7.0
- jupyter >= 1.0.0 (for notebook)
- notebook >= 6.4.0 (for notebook)

---

## 📚 Documentation

### Main Class: `EVPopulationEDA`

#### Methods:

- `load_data(data_path)` - Load CSV dataset
- `initial_exploration()` - Display dataset overview and structure
- `check_missing_values()` - Analyze missing values
- `handle_missing_values(strategy)` - Handle missing data
- `detect_outliers(method)` - Detect outliers using IQR or Z-score
- `statistical_analysis()` - Perform statistical analysis
- `visualize_distributions()` - Create distribution plots
- `visualize_correlations()` - Create correlation heatmap
- `visualize_categorical(top_n)` - Visualize categorical variables
- `visualize_boxplots()` - Create box plots
- `generate_report()` - Generate comprehensive report
- `run_complete_eda()` - Run entire EDA pipeline

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📄 License

This project is open source and available under the MIT License.

---

## 👥 Authors

**HexSoftwares Team**

---

## 📞 Support

For questions or issues, please open an issue on the GitHub repository.

---

## 🎓 Learning Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [EDA Best Practices](https://towardsdatascience.com/exploratory-data-analysis-8fc1cb20fd15)

---

**Happy Analyzing! 📊🚗⚡**
