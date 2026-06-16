from main import tr
from data import ly, cy, done2, act, chg

if __name__ == "__main__":
    print("=== Запуск переноса преемственности магистров ===")
    
    # Вызываем функцию автоматического распределения нагрузок
    updated_current_year = tr(ly, cy, done2, act, chg)
    
    print(f"\nУспешно обработано записей текущего года: {len(updated_current_year)}")
    print("\nРезультаты распределения:")
    for item in updated_current_year:
        print(f"Преподаватель: {item['t']:<15} | Студент/Группа: {item['s']:<12} | Нагрузка: {item['k']}")