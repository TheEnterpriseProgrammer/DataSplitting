# DataSplitting
This is a python library for splitting object graphs in a Excel worksheet cell into a Excel sheet

# Dependencies
This project requires the following dependencies

* pandas
* xlrd
* openpyxl

Install dependencies using the following command
```
py -m pip install {packageName} --user
```

# Input File Requirements
The input file requires the following constraints
1. The file must be located in the same directory as the python script.
2. The file must be named InputFile.xlsx
3. The file must have a sheet named Results that contains the column where object graph data resides.
4. The column the object graph data resides in must have a heading titled Data

Please see the example input file located in the src directory
