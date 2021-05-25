# Импортируйте библиотеку pandas как pd. Загрузите датасет bookings.csv с разделителем ;. Проверьте размер таблицы, типы переменных, а затем выведите первые 7 строк, чтобы посмотреть на данные.
import pandas as pd
bookings = pd.read_csv('C:/Users/Администратор/Desktop/PycharmProjects/Project2/bookings.csv', sep=';')
print("В таблице", bookings.shape[0], "строк и", bookings.shape[1], "столбец")
print()
print(bookings.head(7))
print()
print("Типы переменных:")
print(bookings.dtypes.value_counts())
print()

# Приведите названия колонок к нижнему регистру и замените пробелы на знак нижнего подчеркивания.
def to_lower_underscore(name):
    name = name.lower().replace(' ', '_')
    return name
bookings =  bookings.rename(columns=to_lower_underscore)
print(bookings.columns)
print()

# Пользователи из каких стран совершили наибольшее число успешных бронирований? Укажите топ-5.
print("Список стран, совершивших наибольшее число успешных бронирований:")
print(bookings.query('is_canceled == 0')\
      .country\
      .value_counts()[:5])
print()

# На сколько ночей в среднем бронируют отели разных типов?
print(bookings.groupby('hotel')\
    .agg({'stays_total_nights': 'mean'})\
    .round(decimals=2))
print()

# Иногда тип номера, полученного клиентом (assigned_room_type), отличается от изначально забронированного (reserved_room_type). Такое может произойти, например, по причине овербукинга. Сколько подобных наблюдений встретилось в датасете?
print(bookings.query('reserved_room_type != assigned_room_type'))
print()

# Проанализируйте даты запланированного прибытия.
# – На какой месяц чаще всего успешно оформляли бронь в 2016? Изменился ли самый популярный месяц в 2017?
print("Список успешно оформлявших бронь в 2016 г.:")
print(bookings.query('arrival_date_year == 2016')\
    .arrival_date_month\
    .value_counts())
print()
print("Список успешно оформлявших бронь в 2017 г.:")
print(bookings.query('arrival_date_year == 2017')\
    .arrival_date_month\
    .value_counts())
print()

# – Сгруппируйте данные по годам и проверьте, на какой месяц бронирования отеля типа City Hotel отменялись чаще всего в каждый из периодов
print(
    (
    bookings
     .query('(hotel == "City Hotel") and (is_canceled == 1)')
     .groupby('arrival_date_year')
     .arrival_date_month
     .value_counts()
     )
)
print()

#Посмотрите на числовые характеристики трёх переменных: adults, children и babies. Какая из них имеет наибольшее среднее значение?
print(bookings[['adults', 'children', 'babies']].describe())
print()

#Создайте колонку total_kids, объединив children и babies. Отели какого типа в среднем пользуются большей популярностью у клиентов с детьми?
bookings['total_kids'] = bookings['children'] + bookings['babies']
print(
    (
bookings
    .groupby('hotel')
    .agg({'total_kids': 'mean'})
    .round(decimals=2)
    .max()
    )
)
print()

#Создайте переменную has_kids, которая принимает значение True, если клиент при бронировании указал хотя бы одного ребенка (total_kids), в противном случае – False. Посчитайте отношение количества ушедших пользователей к общему количеству клиентов, выраженное в процентах (churn rate). Укажите, среди какой группы показатель выше.
bookings['has_kids'] = bookings.total_kids > 0
no_kids_churn = bookings.query('(is_canceled == 1) and (has_kids == False)').shape[0] / bookings.query('has_kids == False').shape[0]
no_kids_churn = round(no_kids_churn * 100, 2)
print("Отношение количества ушедших пользователей к общему количеству клиентов без детей равно", no_kids_churn,"%")
print()
yes_kids_churn = bookings.query('(is_canceled == 1) and (has_kids == True)').shape[0] / bookings.query('has_kids == True').shape[0]
yes_kids_churn = round(yes_kids_churn * 100, 2)
print("Отношение количества ушедших пользователей к общему количеству клиентов с детьми равно", yes_kids_churn,"%")