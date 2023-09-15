import openpyxl

def get_cell_data(path,sheet,row,col):
    try:
        wb=openpyxl.load_workbook(path)
        v=wb[sheet].cell(row,col).value
        return v
    except:
        return ""

p=get_cell_data("../test_data/input.xlsx","Sheet1",1,1)
print(p)