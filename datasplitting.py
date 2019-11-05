import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

inputResults = pd.read_excel("InputFile.xlsx", sheet_name="Results")
data = inputResults["Data"]
results = {}

for row in inputResults.index:
    formattedResults = data[row].splitlines()

    result = {}
    for index in formattedResults:
        propertyName, propertyValue = index.split(':')

        if propertyName in results:
            results[propertyName].append(propertyValue)
        else:
            results[propertyName] = []
            results[propertyName].append(propertyValue.lstrip())

df = pd.DataFrame.from_dict(results)
with pd.ExcelWriter('OutputFile.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)
