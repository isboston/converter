import openpyxl

file_exel = openpyxl.open('book.xlsx', read_only=True)
sheet = file_exel.active
print(sheet[2][4].value)
for row in range(2, 5):
    degree_value = sheet[row][4].value
    degree = degree_value.split('°')
    minutes = degree[1].split("'")
    seconds = degree[1].split("'")
    decimal_degrees = int(degree[0]) + int(minutes[0]) / 60 + int(minutes[1]) / 3600
    print(row, degree_value, '%.6f' % decimal_degrees)

output_file = openpyxl.load_workbook('my_book.xlsx')
output_sheet = output_file.active
output_sheet.title = 'degrees'

output_sheet['A6'] = 2345
output_sheet['B6'] = 'td'
output_file.save('my_book.xlsx')
