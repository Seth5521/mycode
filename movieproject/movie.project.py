from random import seed
from random import randint
import xlrd

path = "movies.xls"

inputWorkbook = xlrd.open_workbook(path)
inputWorksheet = inputWorkbook.sheet_by_index(0)

title = []
year = []
genre = []
rating = []

for y in range(1, inputWorksheet.nrows):
    title.append(inputWorksheet.cell_value(y, 0))
    year.append(inputWorksheet.cell_value(y, 1))
    genre.append(inputWorksheet.cell_value(y, 2))
    rating.append(inputWorksheet.cell_value(y, 5))

def time_date():
    first_value = str(randint(0, 23))
    second_value = str(randint(0, 5))
    third_value = str(randint(0,9 ))
    fourth_value  = str(randint(0, 0))
    fifth_value = str(randint(1, 12))
    sixth_value = str(randint(1,31))
    print(first_value+":"+second_value + third_value, fifth_value+"/"+sixth_value)

#time_date()
print(title)
print(year)
print(genre)
print(rating)

