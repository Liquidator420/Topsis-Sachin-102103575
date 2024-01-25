
# TOPSIS-Sachin-102103575

## Overview
for: Project-1 (UCS633) submitted by: Katinder Kaur Roll no: 101703283 Group: 3COE13

TOPSIS-102103575 is a Python-based implementation of the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) method. It is designed to analyze a given dataset and calculate TOPSIS scores and rankings based on user-provided weights and impacts.

## Usage
To use the TOPSIS-102103575 program, follow these steps:

1. **Install Dependencies:**
   Ensure you have the required dependencies installed. You can install them using the following command:

   ```
   pip install pandas numpy
   ```

2. **Run the Program:**
   Execute the program from the command line with the following command:

   ```
   python TOPSIS-102103575.py <InputDataFile> <Weights> <Impacts> <ResultFileName>
   ```

   Replace `<InputDataFile>`, `<Weights>`, `<Impacts>`, and `<ResultFileName>` with the appropriate values.

   - `<InputDataFile>`: The CSV file containing the input data.
   - `<Weights>`: Comma-separated weights for each column in the input data.
   - `<Impacts>`: Comma-separated impact signs ('+' or '-') for each column in the input data.
   - `<ResultFileName>`: The name of the CSV file to save the TOPSIS results.

3. **Review Results:**
   The program will analyze the data using the TOPSIS method and save the results in the specified CSV file. The results include TOPSIS scores and rankings.

## Input File Requirements
- The input CSV file should have more than two columns.
- All columns, except the first one, must contain numeric values.
- Weights, impacts, and the number of columns must be the same.

## Example
```bash
python TOPSIS-102103575.py input_data.csv 1,1,1,+,-,+ result_output.csv
```

## Author
- Your Name

## License
This project is licensed under the [MIT License](LICENSE).
