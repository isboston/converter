import openpyxl

output_file = openpyxl.load_workbook('my_copy.xlsx')
output_sheet = output_file.active
output_sheet.title = '4ww'

file_exel = openpyxl.open('book.xlsx', read_only=True)
sheet = file_exel.active
print(sheet[2][4].value)
for row in range(2, 21):
    degree_value = sheet[row][4].value
    degree = degree_value.split('°')
    minutes = degree[1].split("'")
    seconds = degree[1].split("'")
    decimal_degrees = int(degree[0]) + int(minutes[0]) / 60 + int(minutes[1]) / 3600
    print(row, degree_value, '%.6f' % decimal_degrees)
    output_sheet[row][2].value = '%.6f' % decimal_degrees
    print('%.6f' % decimal_degrees, 1)
    output_file.save('my_copy.xlsx')
