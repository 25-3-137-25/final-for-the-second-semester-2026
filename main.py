from data import K1, K2, KD, act, chg, cy, done2, ly


def tr(a, b, d2, ac, cg):
    p = {}
    for x in a:
        if x["k"] == K1:
            p[x["s"]] = x["t"]
    for s, t in cg.items():
        p[s] = t

    b[:] = [x for x in b if x["k"] not in (K2, KD) or x["s"] in ac or x["s"] in cg]

    r = []
    for s, t in p.items():
        if s not in ac and s not in cg:
            continue
        r.append({"t": t, "s": s, "k": K2})

    has_k2 = {x["s"] for x in r if x["k"] == K2}
    for s, t in p.items():
        if s in d2 and s in has_k2:
            r.append({"t": t, "s": s, "k": KD})

    for x in b:
        if x["k"] in (K2, KD) and x["s"] in p:
            continue
        r.append(x)

    u = {}
    for x in r:
        u[(x["t"], x["s"], x["k"])] = x

    return list(u.values())


def db(a, b, d2, ac, cg):
    return tr(a, b, d2, ac, cg)


if __name__ == "__main__":
    r = db(ly, cy, done2, act, chg)
    for i in r:
        print(i)
