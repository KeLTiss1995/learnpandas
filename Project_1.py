import pandas as pd
from datetime import datetime
df = pd.read_csv('C:/Users/Администратор/Desktop/data.csv')
#print(df.shape)
#print(df.tail())
#print(df.dtypes)
#print(df.describe())
#print(df[['customer_id', 'amount']].head())
#print(df.customer_id)
all_amount = df.amount.sum()
#print(df.groupby('mcc_code', as_index=False).aggregate({'amount': 'sum'}).sort_values('amount', ascending=False))
amount_by_type = df\
    .groupby(['mcc_code', 'tr_type'], as_index=False)\
    .aggregate({'amount': 'sum', 'customer_id': 'count'})\
    .sort_values('amount', ascending=False)\
    .rename(columns={'customer_id': 'count_id'})
#print(amount_by_type.amount.sum())
#print(all_amount)
#amount_by_type.to_csv('amount_by_type.csv', index=False)
today_day = datetime.today().strftime('%Y-%m-%d')
file_name = 'amount_by_type_{}.csv'
file_name = file_name.format(today_day)
if int(amount_by_type.amount.sum())== int(all_amount):
    print('OK! File {} is written.'.format(file_name))
    amount_by_type.to_csv(file_name, index=False)
else:
    print('ERROR!!!!')
