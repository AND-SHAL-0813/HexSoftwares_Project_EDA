"""
QUICK START GUIDE - Electric Vehicle Population EDA
====================================================

This guide shows you how to quickly get started with the EDA tools.

STEP 1: Install Dependencies
-----------------------------
Run this in your terminal:
    pip install -r requirements.txt

STEP 2: Prepare Your Data
--------------------------
Make sure you have your Electric Vehicle dataset in CSV format.
See DATASET_STRUCTURE.md for expected column names.

STEP 3: Choose Your Approach
-----------------------------

OPTION A: Use the Python Script
================================

from ev_population_eda import EVPopulationEDA

# Initialize the EDA object
eda = EVPopulationEDA()

# Load your data (replace with your file path)
eda.load_data('your_ev_data.csv')

# Run the complete EDA pipeline
eda.run_complete_eda()

# This will:
# 1. Show initial data exploration
# 2. Identify and handle missing values
# 3. Detect outliers
# 4. Perform statistical analysis
# 5. Generate all visualizations
# 6. Create a comprehensive report

# Output files created:
# - distributions.png
# - correlation_heatmap.png
# - categorical_analysis.png
# - boxplots.png
# - eda_report.txt


OPTION B: Use the Jupyter Notebook
===================================

1. Open Jupyter:
   jupyter notebook EV_Population_EDA.ipynb

2. Update the data path in cell under "2. Load the Dataset":
   data_path = 'your_ev_data.csv'

3. Run all cells or execute step by step

4. Follow the PROMPTS in each section for guidance


OPTION C: Step-by-Step Custom Analysis
=======================================

from ev_population_eda import EVPopulationEDA

# Initialize
eda = EVPopulationEDA()
eda.load_data('ev_data.csv')

# Step 1: Explore the data
eda.initial_exploration()

# Step 2: Check for missing values
missing_info = eda.check_missing_values()

# Step 3: Handle missing values (choose strategy)
# Options: 'auto', 'drop', 'fill_mean', 'fill_median', 'fill_mode', or custom dict
eda.handle_missing_values(strategy='auto')

# Step 4: Detect outliers
outliers = eda.detect_outliers(method='iqr')  # or method='zscore'

# Step 5: Perform statistical analysis
eda.statistical_analysis()

# Step 6: Create visualizations
eda.visualize_distributions()
eda.visualize_correlations()
eda.visualize_categorical(top_n=15)
eda.visualize_boxplots()

# Step 7: Generate final report
eda.generate_report()


UNDERSTANDING THE PROMPTS
==========================

The tools include helpful PROMPTS throughout:

1. When you load data:
   ✓ Shows dataset shape and memory usage
   
2. When checking missing values:
   ⚠ Highlights columns with missing data
   
3. When handling missing values:
   ✓ Confirms which strategy was applied
   
4. When detecting outliers:
   ⚠ Shows columns with outliers and percentages
   
5. In statistical analysis:
   • Shows skewness (left/right/symmetric)
   • Displays correlation strengths
   
6. For visualizations:
   ✓ Saves files with descriptive names
   

CUSTOMIZATION EXAMPLES
======================

Example 1: Custom Missing Value Strategy
-----------------------------------------
# Handle different columns differently
custom_strategy = {
    'Electric Range': 'median',      # Use median for ranges
    'Base MSRP': 'mean',             # Use mean for prices
    'County': 'mode',                # Use mode for categories
    'Legislative District': 'drop'   # Drop rows with missing district
}
eda.handle_missing_values(strategy=custom_strategy)


Example 2: Focus on Specific Visualizations
--------------------------------------------
# Only create correlation and distribution plots
eda.visualize_correlations()
eda.visualize_distributions()


Example 3: Analyze Top Categories
----------------------------------
# Show top 20 instead of default 10
eda.visualize_categorical(top_n=20)


SAMPLE DATA DOWNLOAD
====================

If you don't have data yet, you can download sample datasets from:

1. Washington State Electric Vehicle Population Data:
   https://data.wa.gov/Transportation/Electric-Vehicle-Population-Data/f6w7-q2d2
   
2. Download as CSV and save locally

3. Update the file path in your code


TROUBLESHOOTING
===============

Issue: "ModuleNotFoundError: No module named 'pandas'"
Solution: Run: pip install -r requirements.txt

Issue: "File not found"
Solution: Check your file path is correct and file exists

Issue: "No numeric columns to visualize"
Solution: Ensure your dataset has numeric columns (Model Year, Electric Range, etc.)

Issue: Visualizations not showing
Solution: If running in script, ensure you have display capability or save to files


NEXT STEPS
==========

After running the EDA:

1. Review the generated reports and visualizations
2. Identify data quality issues to address
3. Note interesting patterns and correlations
4. Use insights for:
   - Further data cleaning
   - Feature engineering
   - Predictive modeling
   - Stakeholder presentations
   - Dashboard development


QUESTIONS?
==========

Refer to:
- README.md for comprehensive documentation
- DATASET_STRUCTURE.md for data format details
- The code comments in ev_population_eda.py
- The prompts in EV_Population_EDA.ipynb


Happy Analyzing! 📊🚗⚡
"""

if __name__ == "__main__":
    print(__doc__)
