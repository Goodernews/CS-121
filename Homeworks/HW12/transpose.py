def transpose(in_path, write_path):
  in_file = open(in_path, "r").readlines()
  in_file = [x.strip("\n").split(" ") for x in in_file]
  in_file = [ [int(z) for z in y] for y in in_file]
  dim = in_file[0]
  in_file = in_file[1:]
  in_file = [ [in_file[b][a] for b in range(0,dim[0])] for a in range(0,dim[1])]
  in_file = [ [str(z) for z in y] for y in in_file] #back to string
  in_file = [" ".join(y) for y in in_file] #join lines
  in_file = [in_file[z] + "\n" for z in range(0,len(in_file))] #adds returns
  in_file = [str(dim[1]) + " " + str(dim[0]) + "\n"] + in_file
  print(in_file)
  out_file = open(write_path, "w")
  out_file.writelines(in_file)
  out_file.close()