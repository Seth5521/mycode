import pandas
data = pandas.read_excel('movies2.xls')
data = data.drop(['Facebook Likes - Director'],axis=1)

data.to_excel('movies3.xls')
