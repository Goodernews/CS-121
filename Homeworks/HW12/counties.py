import math

mean = lambda x : sum(x)/len(x)
std = lambda y : (sum([(z-mean(y))**2 for z in y])/(len(y)-1))**0.5
e_dist = lambda x, y : sum([(x[z]-y[z])**2 for z in range(0,len(x))])**0.5

class County:
    def __init__(self, name, values):
        self.name = name
        self.values = values
    def distance(self, othervals):
        dist = 0
        for i in range(len(self.values)):
            dist += abs(self.values[i]-othervals[i])
        return dist

class Cluster:
    def __init__(self):
        self.centroid = []
        self.contents = []
    def updateCentroid(self):
        if self.contents!=[]:
          self.centroid = [mean([y.values[x] for y in self.contents]) for x in range(0,len(self.centroid))]
    def names(self):
        names = ""
        for c in self.contents:
            names += c.name + "; "
        return names
    def clear(self):
        self.contents = []

def readData(filename):
  in_file = open(filename, "r").readlines()
  in_file = [x.strip("\n").split(";") for x in in_file]
  header = in_file[0]
  in_file = in_file[1:]
  county_names = [y[0] for y in in_file]
  county_info = [[float(z[a]) for a in range(2,19)] for z in in_file]
  county_info = [[rows[b] if b!=1 else rows[1]/rows[16] for b in range(0,16)] for rows in county_info]
  counties = [County(county_names[n], county_info[n]) for n in range(0,len(county_names))]
  return counties

def normalizeCounties(counties):
  mean = lambda x : sum(x)/len(x)
  std = lambda y : (sum([(z-mean(y))**2 for z in y])/(len(y)))**0.5
  rot_df = [[y.values[x] for y in counties] for x in range (0,16)]
  global_means = [mean(z) for z in rot_df]
  global_stds = [std(a) for a in rot_df]
  rot_df = [[(c-global_means[b])/global_stds[b] for c in rot_df[b]] for b in range (0,16)]
  for d in range(0, len(counties)):
    counties[d].values = [rot_df[e][d] for e in range(0,16)]
  counties[:] = counties

def initClusters(counties, num):
    clusters = []
    for i in range(num):
        newcluster = Cluster()
        newcluster.centroid = counties[i].values[:]
        clusters.append(newcluster)
    return clusters

def placeCounties(counties, clusters):
    cluster_centers = [y.centroid for y in clusters]
    for x in counties:
      e_dist = lambda y : sum([abs(x.values[z]-y[z]) for z in range(0,len(x.values))])
      clusters[cluster_centers.index(min(cluster_centers, key=e_dist))].contents.append(x) # find closest
    clusters[:] = clusters

def updateCentroids(clusters):
    for c in clusters:
        c.updateCentroid()

def clearClusters(clusters):
    for c in clusters:
        c.clear()

def writeOutput(clusters, filename):
  #your code here (replace "pass" with code)
  output = []
  for x in range(0,len(clusters)):
    cluster = clusters[x]
    output.append("Cluster " + str(x+1) + "\n")
    output.append("size: " + str(len(cluster.contents)) + "\n")
    output.append(cluster.names() + "\n")
    output.append("\n")
  out_file = open(filename, "w")
  out_file.writelines(output)
  out_file.close()

def kmeans(infile, outfile, k, cycles):
    counties = readData(infile)
    normalizeCounties(counties)
    clusters = initClusters(counties, k)
    for i in range(cycles):
        clearClusters(clusters)
        placeCounties(counties, clusters)
        updateCentroids(clusters)
    writeOutput(clusters, outfile)

# You can use the line below to test your kmeans code once you've
# completed the coding for all five exercises.  Compare the text file
# "output.txt" produced by the code below against the sample output
# file called "output30x120.txt" included in this folder.
#
# Please comment out this line when you hand in your code for each
# exercise, otherwise our tests might time out, taking too long to
# load your code. (Our tests use other means to verify your code.)
#

#kmeans("counties.txt", "output.txt", 30, 120)
