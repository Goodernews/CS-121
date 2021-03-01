def eligible(in_path, write_path):
  in_file = open(in_path, "r").readlines()
  in_file = [x.strip("\n").split(", ") for x in in_file]
  in_file = [", ".join(y) for y in in_file if float(y[1])>=18]
  in_file = [in_file[z] + "\n" for z in range(0,len(in_file))] 
  out_file = open(write_path, "w")
  out_file.writelines(in_file)
  out_file.close()