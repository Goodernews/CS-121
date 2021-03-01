def  list_overlap(a, b):
    holder = []
    compare = b
    for x in a:
      if x in b:
        holder.append(x)
        b.pop(b.index(x))
    return holder