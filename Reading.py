#import xlrd module
import xlrd

#Open excel file
workbook= xlrd.open_workbook("Baseline.xlsx")

#Open sheet
worksheet = workbook.sheet_by_index(0)

# Extracting all columns name
# For row 0 and column 0
worksheet.cell_value(0,0)

for i in range(worksheet.ncols):
    print(worksheet.cell_value(0,i))
    
    
