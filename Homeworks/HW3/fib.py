def fibonacci3(x):
    list_fibs = [1,1,1]
    while len(list_fibs)<= x-1:
        list_fibs.append(sum(list_fibs[-3:]))
    return list_fibs[-1]