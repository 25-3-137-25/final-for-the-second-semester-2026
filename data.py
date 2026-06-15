from typing import Dict, List, Set
import pandas as pd

# Константы типов нагрузки
K1: str = "магистрант 1 курса"
K2: str = "магистрант 2 курса"
KD: str = "диплом магистра"
B3: str = "бакалавр 3 курса"

# Списки нагрузок (заполняются строго из файлов)
ly: List[Dict[str, str]] = []
cy: List[Dict[str, str]] = []

# Загрузка данных из Варианта №2
df_var2 = pd.read_csv("var2.xlsx")
# Загрузка данных из Варианта №15
df_var15 = pd.read_csv("var15.xls")

# Объединяем данные из обоих файлов
combined_df = pd.concat([df_var2, df_var15], ignore_index=True)

# Парсинг строк в структуру проекта
for index, row in combined_df.dropna(subset=['ФИО', 'Дисциплина']).iterrows():
    student_name = str(row.get('Группы', '')).strip()
    teacher_name = str(row['ФИО']).strip()
    load_type = str(row['Вид нагрузки']).strip()
    
    record = {"t": teacher_name, "s": student_name, "k": load_type}
    
    if "19" in str(row.get('Группы', '')):
        ly.append(record)
    else:
        cy.append(record)

# Множества и словари для main.py (заполни их актуальными данными из файлов или логикой)
done2: Set[str] = {"Пантелеева"}
act: Set[str] = {"Пантелеева", "Кочугуров"}
chg: Dict[str, str] = {}