import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import pickle


df = pd.read_csv('simulated_data_clustered.csv', index_col=0)
df_clusters = df[['y_KMeans', 'y_KShape',
                  'y_FCluster_complete', 'y_FCluster_ward']].copy()

df = df.drop(['y_KMeans', 'y_KShape',
              'y_FCluster_complete', 'y_FCluster_ward'], axis=1)


pal = []

with open('n_clusters.pkl', 'rb') as pklfile:
    n_clusters = pickle.load(pklfile)

print(n_clusters)


for i in range(0, n_clusters):
    color_p = sns.color_palette("ch:s=" + str(3 * i/ n_clusters) + ",r=0,d=.65,l=.70", n_colors=(len(df)//n_clusters))
    pal.append(color_p.as_hex())


#pal = list(sns.color_palette(palette='Paired', n_colors=12).as_hex())

cluster_names = ['y_KMeans', 'y_KShape', 'y_FCluster_complete', 'y_FCluster_ward']


cluster_selector = 3 # cluster can be changed here <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


df = df.T


fig = go.Figure()

for i in range(0, len(df.columns)):
    fig.add_trace(go.Scatter(x=list(range(0, len(df))), y=df[i], 
                             name=str(i) + '-' + cluster_names[cluster_selector] +'-cluster-' + 
                             str(df_clusters[cluster_names[cluster_selector]][i]),
                             line_color=pal[df_clusters[cluster_names[cluster_selector]][i]][abs(i//n_clusters - 1)],
                             fill=None))


#fig.title('Clusters using ' + cluster_names[cluster_selector])
fig.show()
