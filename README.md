# RPG Analysis
Using a webscraper for a popular PC game storefront (Steam), collected data of 10,000+ RPG games. The collected attributes includes:
- name,
- tags,
- number of reviews and positive reviews,
- release date
- url (mostly for debugging).
Here, tags are descriptive keywords assigned to each game by developers, Steam moderators, and most importantly users. Since these are user-defined, it provides a more user-oriented and organic way of classifying games beyond already existing genres. Thus, by analysing tags, we aim to investigate into possible sub-genres of RPG games.

## Methodology
The analysis breaks down into the following steps:
- preprocessing - for successful tag-based analysis, we focus on games with enough user data (reviews) and tags. 
- PCA - of course, there are redundancies in tags (for example, Action and Action RPG) and to remove this, we perform PCA on vectorized the tag lists. MCA would have been a more orthodox option as the tags are categorical variables, however for some reason PCA on centerred data returned better results.
- K-Means - to see if there is any obvious clustering, we then perform K-Means on PCA scores.

## Clustering
After looking at both inertia and sihouette score, we chose 14 as the number of clusters.
<img src="images/cluster-pie.png">

These clusters presents a finer classification of the RPG games (Action RPG, Adventure RPG, Casual, JRPG, Party-based RPG, Roguelike, Strategy RPG). For example, by looking at clusters with "action" tags, we obtain a finer classification of Action RPG games into following sub-categories: Action-Roguelike, Action-Adventure, Action-Platformer, Action-MMORPG, Action-FPS. Here, each bar shows the percentage of 15 most common tags for each cluster with a representative game in the title.

<img src="images/action-tags.png" width=80% height=80%>

Especially since tags provide more information than information contained in the RPG subgenres listed above, we obtain clusters that are more than just combination of the subgenres. Cluster 1 and Cluster 12 are best examples of this. Even if these two clusters contain games with "action" tag and "adventure" tag, Cluster 1 contains fantasy themed games (for example, Hogwarts Legacy) whereas Cluster 12 contains sci-fi themed FPS games (for example, Prey).

Similarly, there are two clutsers for roguelike RPG games of different nature. In the following plot, Cluster 0 shows Action-Roguelike games such as Binding of Issac and Cluster 3 shows Roguelike-Strategy games such as Slay the Spire or Darkest Dungeon.

<img src="images/roguelike-tags.png" width=80% height=80%>

## Trend Analysis
Of course, each clusters shows different trend in their publications. The prime example of this is shown in the following plots which tracks the number of pulication from each quarter from past decade. Although both plots shows increase in the publication of both clusters, it is evident that Cluster 

<img src="images/trend-quarterly-roguelike.png" width=80% height=80%>

The difference becomes more evident when we compare their yearly publication from past two decades:
<img src="images/trend-yearly-roguelike.png" width=80% height=80%>

