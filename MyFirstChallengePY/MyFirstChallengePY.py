# File link: "https://drive.google.com/file/d/18fz_LXV6ySdo4tpvQb0CQS4Jy6gBe1Ll/view?usp=sharing"
# step 1; import my database to python
import pandas as pd
table = pd.read_csv(r'C:\Users\welin\Downloads\telecom_users.csv')
display(table)
# step 2; view the database:
# understand what information is available;
# find errors in the database;
table = table.drop('Unnamed: 0', axis=1)
# axis=0 -> Line
# axis=1 -> column
display(table)
# step 3; database treatment:

# values ​​that are numbers but that python thinks are texts:
table['TotalGasto'] = pd.to_numeric(table['TotalGasto'], errors='coerce')

# delete useless information:
# empty columns;
table = table.dropna(how='all', axis=1)
# empty lines;
table = table.dropna(how='any', axis=0)
# all = completely empty columns;
# any = columns with at least 1 empty value;
print(table.info())


# exploratory analysis -> general analysis -> see how cancellations are doing;
display(table['Churn'].value_counts())
display(table['Churn'].value_counts(normalize=True))#.map("(:.1%)".format));
# step 4; looking at the columns in our database -> identify why customers cancel;

import plotly.express as px
column = 'FormaPagamento'
graphic = px.histogram(table, x=column, color='Churn')
graphic.show()
#   use for to display all 'table' graphics:
#   for coluna in tabela.columns:
#   print(coluna)
#   grafico = px.histogram(tabela, x=coluna, color='churn')
#   grafico.show
