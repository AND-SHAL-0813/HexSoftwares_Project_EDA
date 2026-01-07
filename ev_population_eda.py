"""
Electric Vehicle Population - Exploratory Data Analysis (EDA)
=============================================================

This script provides a comprehensive framework for performing EDA on 
Electric Vehicle Population datasets.

Tools Used: Python (Pandas, Matplotlib, Seaborn, NumPy)

Author: HexSoftwares
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Set visualization style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


class EVPopulationEDA:
    """
    A comprehensive class for performing EDA on Electric Vehicle Population data.
    """
    
    def __init__(self, data_path=None):
        """
        Initialize the EDA class with optional data path.
        
        Parameters:
        -----------
        data_path : str, optional
            Path to the CSV file containing EV population data
        """
        self.data_path = data_path
        self.df = None
        self.numeric_cols = []
        self.categorical_cols = []
        
    def load_data(self, data_path=None):
        """
        Load the Electric Vehicle Population dataset.
        
        Parameters:
        -----------
        data_path : str, optional
            Path to the CSV file
            
        Returns:
        --------
        pd.DataFrame : Loaded dataset
        """
        path = data_path or self.data_path
        if path is None:
            print("PROMPT: Please provide a data path to load the dataset")
            print("Example: eda.load_data('path/to/ev_population.csv')")
            return None
            
        try:
            self.df = pd.read_csv(path)
            print(f"✓ Data loaded successfully!")
            print(f"  Shape: {self.df.shape[0]} rows × {self.df.shape[1]} columns")
            return self.df
        except FileNotFoundError:
            print(f"✗ Error: File not found at {path}")
            return None
        except Exception as e:
            print(f"✗ Error loading data: {str(e)}")
            return None
    
    def initial_exploration(self):
        """
        Perform initial data exploration to understand the dataset structure.
        
        This includes:
        - Display first and last few rows
        - Show dataset info (dtypes, memory usage)
        - Display basic statistics
        - Identify numeric and categorical columns
        """
        if self.df is None:
            print("PROMPT: Load data first using load_data() method")
            return
        
        print("\n" + "="*80)
        print("INITIAL DATA EXPLORATION")
        print("="*80)
        
        print("\n📊 First 5 rows of the dataset:")
        print(self.df.head())
        
        print("\n📊 Last 5 rows of the dataset:")
        print(self.df.tail())
        
        print("\n📋 Dataset Information:")
        print(f"  • Total rows: {self.df.shape[0]:,}")
        print(f"  • Total columns: {self.df.shape[1]}")
        print(f"  • Memory usage: {self.df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        
        print("\n📋 Column Data Types:")
        print(self.df.dtypes)
        
        # Identify numeric and categorical columns
        self.numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        self.categorical_cols = self.df.select_dtypes(include=['object', 'category']).columns.tolist()
        
        print(f"\n📊 Numeric Columns ({len(self.numeric_cols)}): {self.numeric_cols}")
        print(f"📊 Categorical Columns ({len(self.categorical_cols)}): {self.categorical_cols}")
        
        print("\n📊 Statistical Summary:")
        print(self.df.describe())
        
        if len(self.categorical_cols) > 0:
            print("\n📊 Categorical Columns Summary:")
            print(self.df[self.categorical_cols].describe())
    
    def check_missing_values(self):
        """
        Analyze missing values in the dataset.
        
        Returns:
        --------
        pd.DataFrame : Summary of missing values by column
        """
        if self.df is None:
            print("PROMPT: Load data first using load_data() method")
            return None
        
        print("\n" + "="*80)
        print("MISSING VALUES ANALYSIS")
        print("="*80)
        
        missing_df = pd.DataFrame({
            'Column': self.df.columns,
            'Missing_Count': self.df.isnull().sum(),
            'Missing_Percentage': (self.df.isnull().sum() / len(self.df) * 100).round(2),
            'Data_Type': self.df.dtypes
        })
        
        missing_df = missing_df[missing_df['Missing_Count'] > 0].sort_values(
            'Missing_Percentage', ascending=False
        ).reset_index(drop=True)
        
        if len(missing_df) == 0:
            print("✓ No missing values found in the dataset!")
        else:
            print(f"⚠ Found missing values in {len(missing_df)} columns:\n")
            print(missing_df.to_string(index=False))
            
            # Visualize missing values
            if len(missing_df) > 0:
                plt.figure(figsize=(10, 6))
                plt.barh(missing_df['Column'], missing_df['Missing_Percentage'])
                plt.xlabel('Missing Percentage (%)')
                plt.title('Missing Values by Column')
                plt.tight_layout()
                plt.show()
        
        return missing_df
    
    def handle_missing_values(self, strategy='auto'):
        """
        Handle missing values using specified strategy.
        
        Parameters:
        -----------
        strategy : str or dict
            - 'auto': Automatically choose strategy based on data type
            - 'drop': Drop rows with missing values
            - 'fill_mean': Fill numeric columns with mean
            - 'fill_median': Fill numeric columns with median
            - 'fill_mode': Fill categorical columns with mode
            - dict: Custom strategy per column {column_name: strategy}
        
        Returns:
        --------
        pd.DataFrame : Cleaned dataset
        """
        if self.df is None:
            print("PROMPT: Load data first using load_data() method")
            return None
        
        print("\n" + "="*80)
        print("HANDLING MISSING VALUES")
        print("="*80)
        
        initial_missing = self.df.isnull().sum().sum()
        
        if strategy == 'auto':
            # Fill numeric with median, categorical with mode
            for col in self.numeric_cols:
                if self.df[col].isnull().sum() > 0:
                    self.df[col].fillna(self.df[col].median(), inplace=True)
                    print(f"✓ Filled '{col}' with median")
            
            for col in self.categorical_cols:
                if self.df[col].isnull().sum() > 0:
                    self.df[col].fillna(self.df[col].mode()[0], inplace=True)
                    print(f"✓ Filled '{col}' with mode")
                    
        elif strategy == 'drop':
            self.df.dropna(inplace=True)
            print(f"✓ Dropped rows with missing values")
            
        elif strategy == 'fill_mean':
            self.df[self.numeric_cols] = self.df[self.numeric_cols].fillna(
                self.df[self.numeric_cols].mean()
            )
            print(f"✓ Filled numeric columns with mean")
            
        elif strategy == 'fill_median':
            self.df[self.numeric_cols] = self.df[self.numeric_cols].fillna(
                self.df[self.numeric_cols].median()
            )
            print(f"✓ Filled numeric columns with median")
            
        elif strategy == 'fill_mode':
            for col in self.df.columns:
                if self.df[col].isnull().sum() > 0:
                    self.df[col].fillna(self.df[col].mode()[0], inplace=True)
            print(f"✓ Filled all columns with mode")
            
        elif isinstance(strategy, dict):
            for col, method in strategy.items():
                if col in self.df.columns and self.df[col].isnull().sum() > 0:
                    if method == 'mean':
                        self.df[col].fillna(self.df[col].mean(), inplace=True)
                    elif method == 'median':
                        self.df[col].fillna(self.df[col].median(), inplace=True)
                    elif method == 'mode':
                        self.df[col].fillna(self.df[col].mode()[0], inplace=True)
                    elif method == 'drop':
                        self.df.dropna(subset=[col], inplace=True)
                    print(f"✓ Handled '{col}' with {method}")
        
        final_missing = self.df.isnull().sum().sum()
        print(f"\n📊 Missing values: {initial_missing} → {final_missing}")
        
        return self.df
    
    def detect_outliers(self, method='iqr'):
        """
        Detect outliers in numeric columns.
        
        Parameters:
        -----------
        method : str
            - 'iqr': Interquartile Range method
            - 'zscore': Z-score method (threshold: 3)
        
        Returns:
        --------
        dict : Dictionary with outlier information per column
        """
        if self.df is None:
            print("PROMPT: Load data first using load_data() method")
            return None
        
        print("\n" + "="*80)
        print("OUTLIER DETECTION")
        print("="*80)
        
        outliers_dict = {}
        
        for col in self.numeric_cols:
            if method == 'iqr':
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                outliers = self.df[(self.df[col] < lower_bound) | (self.df[col] > upper_bound)][col]
                
            elif method == 'zscore':
                z_scores = np.abs(stats.zscore(self.df[col].dropna()))
                outliers = self.df[col][z_scores > 3]
            
            if len(outliers) > 0:
                outliers_dict[col] = len(outliers)
                print(f"⚠ '{col}': {len(outliers)} outliers ({len(outliers)/len(self.df)*100:.2f}%)")
        
        if len(outliers_dict) == 0:
            print("✓ No significant outliers detected")
        
        return outliers_dict
    
    def statistical_analysis(self):
        """
        Perform comprehensive statistical analysis on the dataset.
        
        Includes:
        - Distribution analysis
        - Skewness and kurtosis
        - Correlation analysis
        - Unique value counts
        """
        if self.df is None:
            print("PROMPT: Load data first using load_data() method")
            return
        
        print("\n" + "="*80)
        print("STATISTICAL ANALYSIS")
        print("="*80)
        
        print("\n📊 Distribution Metrics (Numeric Columns):")
        for col in self.numeric_cols:
            skew = self.df[col].skew()
            kurt = self.df[col].kurtosis()
            print(f"\n  {col}:")
            print(f"    • Mean: {self.df[col].mean():.2f}")
            print(f"    • Median: {self.df[col].median():.2f}")
            print(f"    • Std Dev: {self.df[col].std():.2f}")
            print(f"    • Skewness: {skew:.2f} {'(Right-skewed)' if skew > 0 else '(Left-skewed)' if skew < 0 else '(Symmetric)'}")
            print(f"    • Kurtosis: {kurt:.2f}")
        
        print("\n📊 Unique Values Count:")
        for col in self.df.columns:
            unique_count = self.df[col].nunique()
            unique_pct = (unique_count / len(self.df)) * 100
            print(f"  • {col}: {unique_count:,} unique values ({unique_pct:.1f}%)")
        
        if len(self.numeric_cols) > 1:
            print("\n📊 Correlation Analysis:")
            print("  (Correlation coefficients between numeric variables)\n")
            corr_matrix = self.df[self.numeric_cols].corr()
            print(corr_matrix.round(3))
    
    def visualize_distributions(self):
        """
        Create distribution plots for numeric columns.
        """
        if self.df is None:
            print("PROMPT: Load data first using load_data() method")
            return
        
        print("\n" + "="*80)
        print("VISUALIZING DISTRIBUTIONS")
        print("="*80)
        
        if len(self.numeric_cols) == 0:
            print("No numeric columns to visualize")
            return
        
        n_cols = len(self.numeric_cols)
        n_rows = (n_cols + 2) // 3
        
        fig, axes = plt.subplots(n_rows, 3, figsize=(15, 5*n_rows))
        axes = axes.flatten() if n_cols > 1 else [axes]
        
        for idx, col in enumerate(self.numeric_cols):
            if idx < len(axes):
                axes[idx].hist(self.df[col].dropna(), bins=30, edgecolor='black', alpha=0.7)
                axes[idx].set_title(f'Distribution of {col}')
                axes[idx].set_xlabel(col)
                axes[idx].set_ylabel('Frequency')
                axes[idx].grid(alpha=0.3)
        
        # Hide extra subplots
        for idx in range(n_cols, len(axes)):
            axes[idx].set_visible(False)
        
        plt.tight_layout()
        plt.savefig('distributions.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("✓ Distribution plots saved as 'distributions.png'")
    
    def visualize_correlations(self):
        """
        Create correlation heatmap for numeric columns.
        """
        if self.df is None:
            print("PROMPT: Load data first using load_data() method")
            return
        
        if len(self.numeric_cols) < 2:
            print("Need at least 2 numeric columns for correlation analysis")
            return
        
        print("\n" + "="*80)
        print("CORRELATION HEATMAP")
        print("="*80)
        
        plt.figure(figsize=(12, 10))
        corr_matrix = self.df[self.numeric_cols].corr()
        
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
                    square=True, linewidths=1, fmt='.2f')
        plt.title('Correlation Matrix - Electric Vehicle Population', fontsize=16, pad=20)
        plt.tight_layout()
        plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("✓ Correlation heatmap saved as 'correlation_heatmap.png'")
    
    def visualize_categorical(self, top_n=10):
        """
        Create visualizations for categorical columns.
        
        Parameters:
        -----------
        top_n : int
            Number of top categories to display
        """
        if self.df is None:
            print("PROMPT: Load data first using load_data() method")
            return
        
        if len(self.categorical_cols) == 0:
            print("No categorical columns to visualize")
            return
        
        print("\n" + "="*80)
        print("CATEGORICAL DATA VISUALIZATION")
        print("="*80)
        
        n_cols = len(self.categorical_cols)
        n_rows = (n_cols + 1) // 2
        
        fig, axes = plt.subplots(n_rows, 2, figsize=(15, 5*n_rows))
        axes = axes.flatten() if n_cols > 1 else [axes]
        
        for idx, col in enumerate(self.categorical_cols):
            if idx < len(axes):
                value_counts = self.df[col].value_counts().head(top_n)
                axes[idx].barh(range(len(value_counts)), value_counts.values)
                axes[idx].set_yticks(range(len(value_counts)))
                axes[idx].set_yticklabels(value_counts.index)
                axes[idx].set_title(f'Top {top_n} Categories: {col}')
                axes[idx].set_xlabel('Count')
                axes[idx].invert_yaxis()
                
                # Add value labels
                for i, v in enumerate(value_counts.values):
                    axes[idx].text(v, i, f' {v:,}', va='center')
        
        # Hide extra subplots
        for idx in range(n_cols, len(axes)):
            axes[idx].set_visible(False)
        
        plt.tight_layout()
        plt.savefig('categorical_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("✓ Categorical analysis saved as 'categorical_analysis.png'")
    
    def visualize_boxplots(self):
        """
        Create box plots to visualize distributions and outliers.
        """
        if self.df is None:
            print("PROMPT: Load data first using load_data() method")
            return
        
        if len(self.numeric_cols) == 0:
            print("No numeric columns to visualize")
            return
        
        print("\n" + "="*80)
        print("BOX PLOTS (Outlier Detection)")
        print("="*80)
        
        n_cols = len(self.numeric_cols)
        n_rows = (n_cols + 2) // 3
        
        fig, axes = plt.subplots(n_rows, 3, figsize=(15, 5*n_rows))
        axes = axes.flatten() if n_cols > 1 else [axes]
        
        for idx, col in enumerate(self.numeric_cols):
            if idx < len(axes):
                axes[idx].boxplot(self.df[col].dropna())
                axes[idx].set_title(f'Box Plot: {col}')
                axes[idx].set_ylabel(col)
                axes[idx].grid(alpha=0.3)
        
        # Hide extra subplots
        for idx in range(n_cols, len(axes)):
            axes[idx].set_visible(False)
        
        plt.tight_layout()
        plt.savefig('boxplots.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("✓ Box plots saved as 'boxplots.png'")
    
    def generate_report(self):
        """
        Generate a comprehensive EDA report.
        """
        if self.df is None:
            print("PROMPT: Load data first using load_data() method")
            return
        
        print("\n" + "="*80)
        print("COMPREHENSIVE EDA REPORT")
        print("="*80)
        
        report = f"""
Electric Vehicle Population - EDA Report
{'='*80}

Dataset Overview:
-----------------
• Total Records: {self.df.shape[0]:,}
• Total Features: {self.df.shape[1]}
• Memory Usage: {self.df.memory_usage(deep=True).sum() / 1024**2:.2f} MB
• Numeric Columns: {len(self.numeric_cols)}
• Categorical Columns: {len(self.categorical_cols)}

Data Quality:
-------------
• Missing Values: {self.df.isnull().sum().sum():,} ({self.df.isnull().sum().sum() / (self.df.shape[0] * self.df.shape[1]) * 100:.2f}%)
• Duplicate Rows: {self.df.duplicated().sum():,}

Key Statistics:
---------------
"""
        for col in self.numeric_cols[:5]:  # Show top 5 numeric columns
            report += f"\n{col}:\n"
            report += f"  Mean: {self.df[col].mean():.2f}\n"
            report += f"  Median: {self.df[col].median():.2f}\n"
            report += f"  Std: {self.df[col].std():.2f}\n"
        
        print(report)
        
        # Save report to file
        with open('eda_report.txt', 'w') as f:
            f.write(report)
        print("\n✓ Report saved as 'eda_report.txt'")
    
    def run_complete_eda(self):
        """
        Run the complete EDA pipeline.
        """
        print("\n" + "="*80)
        print("RUNNING COMPLETE EDA PIPELINE")
        print("="*80)
        
        if self.df is None:
            print("⚠ No data loaded. Please load data first.")
            return
        
        # Step 1: Initial Exploration
        self.initial_exploration()
        
        # Step 2: Missing Values Analysis
        self.check_missing_values()
        self.handle_missing_values(strategy='auto')
        
        # Step 3: Outlier Detection
        self.detect_outliers(method='iqr')
        
        # Step 4: Statistical Analysis
        self.statistical_analysis()
        
        # Step 5: Visualizations
        self.visualize_distributions()
        self.visualize_correlations()
        self.visualize_categorical()
        self.visualize_boxplots()
        
        # Step 6: Generate Report
        self.generate_report()
        
        print("\n" + "="*80)
        print("✓ COMPLETE EDA FINISHED!")
        print("="*80)
        print("\nGenerated files:")
        print("  • distributions.png")
        print("  • correlation_heatmap.png")
        print("  • categorical_analysis.png")
        print("  • boxplots.png")
        print("  • eda_report.txt")


def main():
    """
    Main function demonstrating how to use the EDA class.
    
    PROMPT: Follow these steps to perform EDA on your Electric Vehicle data:
    
    1. Initialize the EDA object:
       eda = EVPopulationEDA()
    
    2. Load your dataset:
       eda.load_data('path/to/your/ev_data.csv')
    
    3. Run individual analyses or complete pipeline:
       
       Option A - Run complete EDA:
       eda.run_complete_eda()
       
       Option B - Run step by step:
       eda.initial_exploration()
       eda.check_missing_values()
       eda.handle_missing_values(strategy='auto')
       eda.detect_outliers()
       eda.statistical_analysis()
       eda.visualize_distributions()
       eda.visualize_correlations()
       eda.visualize_categorical()
       eda.visualize_boxplots()
       eda.generate_report()
    
    Expected dataset columns (typical EV population data):
    - VIN (Vehicle Identification Number)
    - County
    - City
    - State
    - Postal Code
    - Model Year
    - Make
    - Model
    - Electric Vehicle Type
    - Clean Alternative Fuel Vehicle (CAFV) Eligibility
    - Electric Range
    - Base MSRP
    - Legislative District
    - DOL Vehicle ID
    - Vehicle Location
    - Electric Utility
    - 2020 Census Tract
    """
    
    print(__doc__)
    print(main.__doc__)
    
    # Example usage
    print("\n" + "="*80)
    print("EXAMPLE USAGE")
    print("="*80)
    print("""
# Initialize EDA
eda = EVPopulationEDA()

# Load your data
eda.load_data('electric_vehicle_population.csv')

# Run complete EDA
eda.run_complete_eda()

# OR run individual steps
eda.initial_exploration()
eda.check_missing_values()
eda.handle_missing_values(strategy='auto')
eda.statistical_analysis()
eda.visualize_distributions()
eda.visualize_correlations()
    """)


if __name__ == "__main__":
    main()
