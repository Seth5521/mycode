import pandas
data = pandas.read_excel('movies4.xls')
data = data.drop(['Unnamed: 0'],axis=1)

data.to_excel('movies5.xls')
                            
