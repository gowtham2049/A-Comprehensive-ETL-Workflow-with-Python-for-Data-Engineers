# A-Comprehensive-ETL-Workflow-with-Python-for-Data-Engineers

### 1. **Data Acquisition**
- Download dataset:  
  `wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip`
- Unzip files:  
  `unzip source.zip -d ./unzipped_folder`

### 2. **Setup & Dependencies**
- **Libraries**: `glob`, `pandas`, `xml.etree.ElementTree`, `datetime`
- **File Paths**:
  - Logs: `log_file.txt`
  - Output: `transformed_data.csv`

### 3. **ETL Functions**
#### **Extract**
- File-specific functions: 
  - CSV → DataFrame
  - JSON → DataFrame
  - XML → DataFrame
- Master function merges data from all formats.

#### **Transform**
- Unit conversions:
  - Height: Inches → Meters (`height * 0.0254`)
  - Weight: Pounds → Kilograms (`weight * 0.453592`)

#### **Load**
- Save transformed data to `transformed_data.csv`.

#### **Logging**
- Timestamped logs for tracking ETL phases (start/end of extraction, transformation, loading).

### 4. **Execution Flow**
1. **Extract**: Combine data from CSV/JSON/XML files into a single DataFrame.
2. **Transform**: Apply unit standardization.
3. **Load**: Export transformed data to CSV.
4. **Log**: Record all phases with timestamps in `log_file.txt`.
