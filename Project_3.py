#Импортируйте библиотеку pandas как pd. Загрузите два датасета user_data и logs. Проверьте размер таблицы, типы переменных, наличие пропущенных значений, описательную статистику.import pandas as pd
import pandas as pd
user_data = pd.read_csv('C:/Users/Администратор/Desktop/PycharmProjects/Project2/user_data.csv')
logs = pd.read_csv('C:/Users/Администратор/Desktop/PycharmProjects/Project2/logs.csv')
print(user_data.dtypes)
print()
print(user_data.shape)
print()
print(user_data.isna().sum())
print()
print(user_data.describe())
print()
print(logs.dtypes)
print()
print(logs.shape)
print()
print(logs.isna().sum())
print()
print(logs.describe())
print()

#Какой клиент совершил больше всего успешных операций? (success == True)
success_number = logs.query('success == True')\
      .groupby('client', as_index=False)\
      .agg({'platform': 'count'})\
      .rename(columns={'platform': 'success_number'})\
      .sort_values('success_number', ascending=False)
maximum_success = success_number.success_number.max()
successful_clients = success_number.query('success_number == @maximum_success')\
      .sort_values('client')\
      .client\
      .tolist()
print(', '.join([str(client) for client in successful_clients]))
print()
success_number_2 = logs\
      .groupby('client', as_index=False)\
      .agg({'success': 'sum'})\
      .rename(columns={'success': 'success_number'})\
      .sort_values('success_number', ascending=False)
print(success_number_2.head())
print()
print(success_number.head())
print()
maximum_success_2 = success_number_2.success_number.max()
successful_clients_2 = success_number_2.query('success_number == @maximum_success')\
      .sort_values('client')\
      .client\
      .tolist()
print(maximum_success_2, successful_clients_2)
print()
#С какой платформы осуществляется наибольшее количество успешных операций?
print(logs.query('success == True').platform.value_counts().idxmax())
print()
#Какую платформу предпочитают премиумные клиенты?
data = user_data.merge(logs)
print(data.query('premium == True').platform.value_counts().idxmax())
print()
#Визуализируйте распределение возраста клиентов в зависимости от типа клиента (премиум или нет)
import seaborn as sns
import matplotlib.pyplot as plt
#fig, ax = plt.subplots(nrows=2, ncols=1)
#print(sns.distplot(data.query('premium == False').age, ax=ax[0], color='green'))
#print(sns.distplot(data.query('premium == True').age, ax=ax[1], color='red'))
client_vs_success_number = data.groupby('client')\
      .agg({'success':'sum'})
#print(sns.distplot(client_vs_success_number, kde=False))
print(client_vs_success_number.success.value_count())
age_vs_success_number = data.query('platform == "computer"')\
      .groupby('age')\
      .agg({'success':'sum'})
print(age_vs_success_number)