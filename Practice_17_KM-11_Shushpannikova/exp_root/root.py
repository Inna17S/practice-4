def root2(n):
    if n<0:
        return 'number should be natural.'
    else:
        from math import sqrt
        return round(sqrt(n), 4)


def root3(n):
    return round(-((-n) ** (1/3)), 4) if n < 0 else round(n ** (1/3), 4)