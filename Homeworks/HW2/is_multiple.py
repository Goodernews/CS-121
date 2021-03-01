def is_multiple(a,b):
    if a==0:
        return True
    if b==0:
        return False
    return abs(a)%abs(b)==0