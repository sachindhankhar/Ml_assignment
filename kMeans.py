import math
import matplotlib.pyplot as plt

def computeCentroids(cluster):
    centroids=[]
    for key in cluster:
        
        if(len(cluster[key])==0):   ##  boundary case-->if length of any cluster is ZERO
            centroids.append(key)  ## append that centroid's cordinates in the list
        else:
            i=0
            j=0
            for a,b in cluster[key]:
                i=i+a
                j=j+b
            centroids.append((i/len(cluster[key]),j/len(cluster[key]))) 
    return centroids


def assignCluster(inp,centroids):
    cluster={}
    for a,b in centroids:
        cluster[(a,b)]=[]
    
    for x,y in inp:
        a=0
        b=0
        distance =math.inf
        for i,j in centroids:
            if(math.sqrt(pow(x-i,2)+pow(y-j,2))<distance):
                distance=math.sqrt(pow(x-i,2)+pow(y-j,2))
                a=i
                b=j
        cluster[(a,b)].append((x,y))
    return cluster

def checkConvergence(centroids1,centroids2):
    for i in range(len(centroids1)):
        a,b=centroids1[i]
        c,d=centroids2[i]
        if(a!=c or b!=d):
            return 0
    return 1

def kMeans(k,inp):

    centroids=[(1,1),(2,2),(3,3),(10,10),(20,20)]   ## random centroids ,k will be used here to decide its length

    cluster=assignCluster(inp,centroids)
    newCentroids=computeCentroids(cluster)
    
    if(checkConvergence(centroids,newCentroids)):
        return cluster
    else:
        while(True):
            centroids=newCentroids
            cluster=assignCluster(inp,centroids)
            newCentroids=computeCentroids(cluster)
            if(checkConvergence(centroids,newCentroids)):
                return cluster
            

if __name__=="__main__":
    inp = [(-1.9,-1.5),(0,0),(0.11,1.35),(5.99,8.33),(11.1,11.2),(12.3,2.4),(10.1,10.2),(8.1,10.2),(25.1,30.2),(8.1,8.2),(5.1,5.2),(6.1,6.2),(4,5),(8,9),(20,23),(19,19)]
    for x,y in inp:
        plt.scatter(x,y+30,color='black')
    #plt.show()
    k=5
    colors=['red','blue','green','yellow','orange']
    i=0
    for li in kMeans(k,inp).values():
        for x,y in li:
            plt.scatter(x,y,color=colors[i])
        i=i+1
    

    plt.show()
    
    

    
