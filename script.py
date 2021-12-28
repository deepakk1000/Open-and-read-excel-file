import xlrd

loc = ("test.xls")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
header = []
for i in range(sheet.ncols):
    header.append(sheet.cell_value(0,i))
amount = header.index("amount")
print ("{:<8} {:<20} {:<20}".format(*header))

for row in range(1,sheet.nrows):
    row_items = []
    for column in range(sheet.ncols):
        if column ==amount:
            row_items.append("$"+str(sheet.cell_value(row,column)))
        else:
            row_items.append(sheet.cell_value(row,column))
    print ("{:<8} {:<20} {:<20}".format(*row_items))

