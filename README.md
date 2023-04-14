# RPGanalysis
Using a webscraper for a popular PC game storefront (Steam), collected data of 10,000+ RPG games. The collected attributes includes:
- name,
- tags,
- number of reviews and positive reviews,
- release date
- url (mostly for debugging).
Here, tags are descriptive keywords assigned to each game by developers, Steam moderators, and most importantly users. Since these are user-defined, it provides a more user-oriented and organic way of classifying games beyond already existing genres. Thus, by analysing tags, we aim to investigate into possible sub-genres of RPG games.

## Methodology
The analysis breaks down into the following steps:
- preprocessing - for successful tag-based analysis, we focus on games with enough  to ensure the tags are 
- PCA - of course, there are redundancies in tags (for example, Action and Action RPG) and to remove this, we perform PCA on vectorized the tag lists.
- K-Means - to see if there is any obvious clustering, we then perform K-Means on PCA scores.
