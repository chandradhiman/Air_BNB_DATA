import pandas as pd
import numpy as NP

file_path = 'airbnb_contacts.xlsx'
rank = pd.read_excel("airbnb_contacts.xlsx")
print(rank.head())

rank_agg=rank.pivot_table(index='id_guest',values='n_messages',aggfunc='sum').reset_index().sort_values(by='n_messages',ascending=False)
print(rank_agg)

rank_agg['rank'] = rank_agg['n_messages'].rank(ascending=False,method='dense')
rank_agg.head(10)


# data = {
#     'Men' : ['A1men', 'B1men', 'C1men', 'D1Men', 'E1Men'],
#     'Women':['A1', 'B1', 'C1', 'D1', 'E1'],
#     'child' :[1,4,3,2,5 ]
# }

# df = pd.DataFrame(data)

# pivot = df.pivot_table(values = 'child', index = 'Men', columns= 'Women', aggfunc= 'sum')
# print(pivot)


















