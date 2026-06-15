from data import K1, K2, KD, act, chg, cy, done2, ly


def tr(a, b, d2, ac, cg):
    """Перенос преемственности руководства магистрами."""
    p = {}
    
    # собираем прошлогоднюю базу (1 курс)
    for x in a:
        if x["k"] == K1:
            p[x["s"]] = x["t"]
            
    # применяем изменения руководителей
    for s, t in cg.items():
        p[s] = t

    # очищаем текущий год от неактуальных записей K2/KD
    b[:] = [x for x in b if x["k"] not in (K2, KD) or x["s"] in ac or x["s"] in cg]

    r = []
    # назначаем 2 курс актуальным студентам
    for s, t in p.items():
        if s not in ac and s not in cg:
            continue
        r.append({"t": t, "s": s, "k": K2})

    # добавляем диплом (KD), если 2 курс завершен
    has_k2 = {x["s"] for x in r if x["k"] == K2}
    for s, t in p.items():
        if s in d2 and s in has_k2:
            r.append({"t": t, "s": s, "k": KD})

    # переносим остальные записи (например, бакалавров)
    for x in b:
        if x["k"] in (K2, KD) and x["s"] in p:
            continue
        r.append(x)

    # удаляем дубликаты
    u = {}
    for x in r:
        u[(x["t"], x["s"], x["k"])] = x

    return list(u.values())