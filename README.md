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
By looking at both inertia and sihouette score, 14 has been selected as the number of clusters.
![](images/cluster-pie.png | width=100)

These clusters presents a finer classification of the RPG games (Action RPG, Adventure RPG, Casual, JRPG, Party-based RPG, Roguelike, Strategy RPG). For example, by looking at clusters with 'action' tags, we obtain a finer classification of Action RPG games into following sub-categories: action-roguelike, action-adventure, action-platformer, action-MMORPG, action-adventure (FPS). Here, each bar shows the percentage of 15 most common tags for each cluster with a representative game in the title.
![](images/action-tags.png | width=100)
Especially since tags provide more information than simply . This can be observed in . Even if these two clusters both show action-adventure RPG games, depending on its setting and subject matter, it further  into two genres: action-adventure games with fantasy theme and action-adventure games with sci-fi theme.

Also for the roguelike games,
<img source = "https://github.com/rnklee/RPGanalysis/tree/main/images/action-tags.png", "width" = 100>

## Trend Analysis
![](images/trend-quarterly-roguelike.png | width=100)
![](images/trend-yearly-roguelike.png | width=100)

