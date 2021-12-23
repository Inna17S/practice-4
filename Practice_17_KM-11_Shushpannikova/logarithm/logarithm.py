from math import log as logarithm

def log(a,b):
    if a>0 and a!=1 and b>0:
        return round(logarithm(b,a),4)
    else:
        return "invalid inputing" 

def lg(b):
    return round(logarithm(b,10),4) if b>0 else "invalid inputing"

def ln(b):
    return round(logarithm(b),4) if b>0 else "invalid inputing"