                                             # Library imports
import sklearn
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt


                                        #step 1, set example data
#500 points
num_points = 500

# generate 500 random points with x and y values between -100 and 350
data = np.random.uniform(low=-100, high=350, size=(num_points,2))
#__________________________________________________________________________________________________________________
                                        # step 2, cluster identification


# define the number of clusters(n_clusters) I want to identify (2)
kmeans = KMeans(n_clusters=2, random_state=0)

# if you want to identify a different amount of clusters just change the number following the parameter



#  step 2.1 (example)

#example with 3 clusters
#kmeans = KMeans(n_clusters =3, random_state=0)

#example with 5 clusters
#kmeans = KMeans(n_clusters =5, random_state=0)


#__________________________________________________________________________________________________________________

                                    # step 3, fit the data into the k-means model

#fitting the data to the model
kmeans.fit(data)
#__________________________________________________________________________________________________________________

                                        # step 4, set cluster labels

#setting cluster labels
labels = kmeans.labels_

#identify the coordinates of the two centroids
centroids = kmeans.cluster_centers_

print("Cluster labels: ", labels)
print("Centroid coordinates: ", centroids)
#__________________________________________________________________________________________________________________
                                                # step 5, set up plot parameters
# figure size
plt.figure(figsize=(8,8))

# put each point on a scatter plot using a loop

for i in range(kmeans.n_clusters):
    # choose the points that belong to the current cluster
    cluster_points = data[labels==i]
    #plottign cluster 1 (0) and cluster 2 (1)
    # take note, if you change the amount of clusters to a value different than 2 you have to edit this section
    # "label =.." denotes which point is associated to which cluster
    plt.scatter(cluster_points[:,0], cluster_points[:,1], label = f'Cluster {i+1}')


# plot the centroids

#color is red
#marker is the shape of an x
#s=100 adjust the size of the marker
# each marker is labeled 'centroids'
plt.scatter(centroids[:,0], centroids[:,1], color= 'red', marker = 'o', s=100, label='Centroids')



#__________________________________________________________________________________________________________________

                                            # step 6, show plot

#create the plot
plt.title('K-Means Clustering Test Trial') # plot title
plt.xlabel('X-axis') #x-axis title
plt.ylabel('Y-axis') #y-axis title
plt.legend(bbox_to_anchor=(1,1)) #moves legend to the upper right, outside of the plot
plt.grid(True)#shows the grid lines on the plot

plt.show()#actually shows the plot