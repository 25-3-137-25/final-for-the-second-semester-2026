from main import tr
from data import ly, cy, done2, act, chg

if __name__ == "__main__":
    updated_load = tr(ly, cy, done2, act, chg)
    print("Распределение преемственности успешно перенесено:")
    for item in updated_load:
        print(item)