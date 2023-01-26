import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv('simulated_data_clustered.csv', index_col=0)
df_clusters = df[['y_KMeans', 'y_KShape',
                  'y_FCluster_complete', 'y_FCluster_ward']].copy()



cluster_names = ['y_KMeans', 'y_KShape',
                 'y_FCluster_complete', 'y_FCluster_ward']


cluster_selector = 0  # cluster can be changed here <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

current_cluster = cluster_names[cluster_selector]
cluster_names.pop(cluster_selector)


df = df.drop(cluster_names, axis=1)

first_column = df.pop(current_cluster)
df.insert(0, current_cluster, first_column)



gb = df.groupby(current_cluster)

dataframe_list = []

plt.style.use('seaborn-darkgrid')
fig, axes = plt.subplots(nrows=3, ncols=4)

for i in [gb.get_group(x) for x in gb.groups]:
    
    i = i.drop(current_cluster, axis=1)
    i = i.T
    #print(i.head(10))
    #sns.relplot(data=i, x=list(range(0, len(i))), y=i[]  kind='line')
    dataframe_list.append(i)


k = 0
for i in range(0, 3):
    for j in range(0, 4):
        dataframe_list[k].plot(ax=axes[i, j], legend=None, title='cluster ' + str(k))
        k = k + 1

plt.suptitle('Clusters using ' + current_cluster)
plt.show()
'''

sns.relplot(data=dataframe_list[0], kind='line')
sns.relplot(data=dataframe_list[1], kind='line')



#plt.show()


fig = px.line(df, facet_col=df.loc[current_cluster], facet_col_wrap = 4)
fig.show()
'''
