# Electric Vehicle Population Dataset Structure

This document describes the expected structure of Electric Vehicle Population datasets for use with the EDA tools.

## Dataset Format

- **File Type**: CSV (Comma-Separated Values)
- **Encoding**: UTF-8
- **First Row**: Column headers

## Expected Columns

### Core Identification Fields

| Column Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| VIN (1-10) | String | First 10 characters of Vehicle Identification Number | "5YJ3E1EA1K" |
| DOL Vehicle ID | Integer | Department of Licensing Vehicle ID | 123456789 |

### Geographic Information

| Column Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| County | String | County of registration | "King" |
| City | String | City of registration | "Seattle" |
| State | String | State abbreviation | "WA" |
| Postal Code | String/Integer | ZIP code | "98101" |
| Legislative District | Integer | District number | 43 |
| 2020 Census Tract | Float | Census tract identifier | 53033005302.0 |
| Vehicle Location | String | Geographic coordinates | "POINT (-122.329 47.603)" |

### Vehicle Details

| Column Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| Model Year | Integer | Year manufactured | 2023 |
| Make | String | Manufacturer name | "TESLA" |
| Model | String | Model name | "MODEL 3" |
| Electric Vehicle Type | String | BEV or PHEV | "Battery Electric Vehicle (BEV)" |
| Electric Range | Integer | Miles on electric power | 353 |
| Base MSRP | Integer | Manufacturer's price | 44990 |

### Eligibility & Utility

| Column Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| Clean Alternative Fuel Vehicle (CAFV) Eligibility | String | CAFV eligibility status | "Clean Alternative Fuel Vehicle Eligible" |
| Electric Utility | String | Utility provider | "PUGET SOUND ENERGY INC" |

## Sample Data Structure

Here's an example of what the first few rows might look like:

```csv
VIN (1-10),County,City,State,Postal Code,Model Year,Make,Model,Electric Vehicle Type,CAFV Eligibility,Electric Range,Base MSRP,Legislative District,DOL Vehicle ID,Vehicle Location,Electric Utility,2020 Census Tract
5YJ3E1EA1K,King,Seattle,WA,98101,2023,TESLA,MODEL 3,Battery Electric Vehicle (BEV),Clean Alternative Fuel Vehicle Eligible,353,44990,43,123456789,POINT (-122.329 47.603),PUGET SOUND ENERGY INC,53033005302.0
5YJSA1E14H,Snohomish,Bothell,WA,98011,2022,TESLA,MODEL S,Battery Electric Vehicle (BEV),Clean Alternative Fuel Vehicle Eligible,405,94990,1,987654321,POINT (-122.206 47.762),PUGET SOUND ENERGY INC,53061051910.0
1N4AZ0CP0F,Pierce,Tacoma,WA,98403,2021,NISSAN,LEAF,Battery Electric Vehicle (BEV),Clean Alternative Fuel Vehicle Eligible,149,31600,27,456789123,POINT (-122.477 47.252),TACOMA PUBLIC UTILITIES,53053007900.0
```

## Data Quality Notes

### Missing Values
- Some columns may have missing values (empty fields)
- Typical columns with missing data:
  - Electric Range (for older models or PHEVs)
  - Base MSRP (not always reported)
  - Legislative District
  - 2020 Census Tract
  - Vehicle Location

### Data Types
- **Numeric**: Model Year, Electric Range, Base MSRP, Legislative District, DOL Vehicle ID
- **Categorical**: Make, Model, Electric Vehicle Type, CAFV Eligibility, County, City, State
- **Text**: VIN (1-10), Electric Utility, Vehicle Location

### Expected Value Ranges

| Column | Min | Max | Typical Range |
|--------|-----|-----|---------------|
| Model Year | 1997 | 2024 | 2015-2024 |
| Electric Range | 0 | 500 | 50-350 miles |
| Base MSRP | 10000 | 200000 | 30000-100000 |

## Common Data Issues

1. **Missing Values**: Handle using median (numeric) or mode (categorical)
2. **Outliers**: Some vehicles may have unusual ranges or prices
3. **Duplicates**: Check for duplicate VINs
4. **Inconsistent Formatting**: 
   - Make/Model names may have different capitalizations
   - State codes should be standardized
   - Postal codes may be numeric or string

## Data Sources

Typical sources for EV population data:
- Department of Licensing (DOL) databases
- Vehicle registration databases
- Clean Alternative Fuel Vehicle programs
- State transportation departments

## Usage with EDA Tools

To use your dataset with the provided EDA tools:

1. Ensure your CSV file matches the structure above (column names can vary slightly)
2. Save as UTF-8 encoded CSV
3. Load using: `eda.load_data('your_file.csv')`
4. The tools will automatically:
   - Detect numeric vs categorical columns
   - Identify missing values
   - Generate appropriate visualizations

## Example Datasets

Public datasets you can use:
- [Washington State EV Registration](https://data.wa.gov/Transportation/Electric-Vehicle-Population-Data/f6w7-q2d2)
- [California ZEV Sales](https://www.energy.ca.gov/data-reports/energy-insights/zero-emission-vehicle-and-infrastructure-statistics)

---

**Note**: The EDA tools are flexible and will work with datasets that don't have all these columns. The analysis will adapt based on the columns present in your data.
