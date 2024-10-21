def hashable_objects():
    tt = (1, 2, (30, 40))
    print(hash(tt))
    t1 = (1, 2, [30, 40])
    print(hash(t1))
    tf = (1, 2, frozenset([30, 40]))
    print(hash(tf))
    

hashable_objects()