# RPG Analysis
Using a webscraper for a popular PC game storefront (Steam), collected data of 10,000+ RPG games. The collected attributes includes:
- name,
- tags,
- number of reviews and positive reviews,
- release date,
- url (mostly for debugging).

Here, tags are descriptive keywords assigned to each game by developers, Steam moderators, and most importantly users. Tags usually contains more information about a game than genres ascribed to games. Also, being user-defined, it provides a more user-oriented description of games. The goal of this project is to acheive a finer, more user-oriented classification of RPG games using the tags.

## Methodology
The analysis breaks down into the following steps:
- preprocessing - For successful tag-based analysis, we focus on games with enough user data (measured by number of reviews) and tags. 
- PCA - To remove redundancies in tags (for example, Action and Action RPG), we perform PCA on vectorized the tag lists. Of course, MCA would have been a more orthodox option as the tags are categorical variables, however for some reason PCA on centerred data returned better results.
- K-Means - To see if there is any obvious clustering, we then perform K-Means on PCA scores.

## Clustering
After looking at both inertia and sihouette score, we chose 14 as the number of clusters.
<img src="images/cluster-pie.png">

Currently, there are seven subgenres of RPG games presented on the online storefront: Action RPG, Adventure RPG, Casual, JRPG, Party-based RPG, Roguelike, Strategy RPG. The returned clusters present a finer classification than these subgenres. For example, by looking at clusters with Action tags, we obtain the following sub-categories of Action RPG games: Cluster 4 (Action, Adventure, Fantasy), Cluster 8 (Action, Roguelike), Cluster 9 (Action, Platformer, Metrovania), and Cluster 10 (Action, Adventure, Sci-Fi). Here, each bar shows the percentage for each of the 15 most common tags and the titles shows the cluster number along with the names of representative games (i.e. selected with ) in each cluster.

<img src="images/action-tags.png" width=80% height=80%>

Especially since tags provide more information than information contained in the RPG subgenres listed above, we obtain clusters that are more than just combination of the subgenres. Cluster 4 and Cluster 10 are best examples of this. Even if these two clusters contain games with "action" tag and "adventure" tag, Cluster 4 contains fantasy themed games (for example, The Witcher or Hogwarts Legacy) whereas Cluster 10 contains sci-fi themed FPS games (for example, Prey or S.T.A.L.K.E.R series) as seen above.

As another example, Cluster 2 and Cluster 8 samples Rogulike games of different flavors. It can be checked in the following plots that Cluster 2 consists of Roguelike-Strategy games such as Slay the Spire or Darkest Dungeon whereas Cluster 8 consists of Action-Roguelike games such as Binding of Issac and Hades.

<img src="images/roguelike-tags.png" width=80% height=80%>

Plots for all 14 clusters can be found in the [Jupyter notebook](RPG_Clustering_and_Analysis.ipynb) or in [images](images).

## Trend Analysis
Of course, each clusters follows different pulicaton trends. The prime example of this is shown in the following plots which tracks the number of pulication from each quarter from past decade. Although both clusters exhibit increase in the number of publication per quarter during the past decade, Cluster 2 does not exhibit the rapid growth in 2022 as Cluster 8 does.

<img src="images/roguelike-quarterly-trends.png" width=80% height=80%>

The difference can be observed from their yearly publication from past two decades as well.
<img src="images/roguelike-yearly-trends.png" width=80% height=80%>

Again, plots for all 14 clusters can be found in the [Jupyter notebook](RPG_Clustering_and_Analysis.ipynb) or in [images](images).
