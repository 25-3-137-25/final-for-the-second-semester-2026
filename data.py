from typing import Dict, List, Set
import pandas as pd

# Константы типов нагрузки
K1: str = "магистрант 1 курса"
K2: str = "магистрант 2 курса"
KD: str = "диплом магистра"
B3: str = "бакалавр 3 курса"

# Инициализируем списки пустыми значениями, чтобы данные читались строго из файлов
ly: List[Dict[str, str]] = []
cy: List[Dict[str, str]] = []

try:
    # Читаем файлы Excel напрямую. 
    # sheet_name=0 означает, что берется первая вкладка (лист) в каждом файле.
    df_var2 = pd.read_excel("var2.xlsx", sheet_name=0)
    df_var15 = pd.read_excel("var15.xls", sheet_name=0)
    
    # Объединяем данные
    combined_df = pd.concat([df_var2, df_var15], ignore_index=True)
    
    # Очищаем заголовки колонок от случайных пробелов по краям
    combined_df.columns = combined_df.columns.str.strip()
    
    dynamic_ly = []
    dynamic_cy = []
    
    # Проверяем наличие ключевой колонки
    if 'ФИО' in combined_df.columns:
        # Удаляем строки, где нет преподавателя
        df_clean = combined_df.dropna(subset=['ФИО'])
        
        for index, row in df_clean.iterrows():
            teacher_name = str(row['ФИО']).strip()
            
            # Определяем колонку с группой (Группы или Группа)
            group_col = 'Группы' if 'Группы' in combined_df.columns else ('Группа' if 'Группа' in combined_df.columns else '')
            student_name = str(row[group_col]).strip() if group_col else ""
            
            # Определяем колонку с типом нагрузки
            load_col = 'Вид нагрузки' if 'Вид нагрузки' in combined_df.columns else ('Дисциплина' if 'Дисциплина' in combined_df.columns else '')
            load_type = str(row[load_col]).strip() if load_col else ""
            
            # Пропускаем пустые или сервисные строки
            if not teacher_name or "Итог" in teacher_name or teacher_name == "nan":
                continue
                
            record = {"t": teacher_name, "s": student_name, "k": load_type}
            
            # Разносим по спискам: прошлый год (ly) и текущий год (cy)
            if "19" in student_name or "2019" in student_name:
                dynamic_ly.append(record)
            else:
                dynamic_cy.append(record)
                
        # Если списки заполнились, обновляем глобальные переменные
        if dynamic_ly:
            ly = dynamic_ly
        if dynamic_cy:
            cy = dynamic_cy

except Exception as e:
    print(f"Ошибка при чтении или обработке файлов Excel: {e}")

# Дополнительные структуры данных для работы алгоритма переноса
done2: Set[str] = {"Пантелеева"}
act: Set[str] = {"Пантелеева", "Кочугуров"}
chg: Dict[str, str] = {}