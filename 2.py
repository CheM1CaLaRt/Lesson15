import pandas as pd

# Загрузка данных из CSV файла (замените 'путь_к_вашему_файлу.csv' на путь к вашему файлу)
data = pd.read_csv('dz.csv')

# Вычисление средней зарплаты по городам
average_salary_by_city = data.groupby('City')['Salary'].mean()

# Вывод результатов
print("Средняя зарплата по городам:")
print(average_salary_by_city)