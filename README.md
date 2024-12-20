# Who's in the spotlight ?? 
### *Gender dynamics in movies over time.*

## Abstract
Gender equality and representation has been a core issue since the 20th and 21th century.
Those centuries are characterized by a lot of movement and progress towards women's rights,
for example in France the legalization of abortion in 1975.
Knowing that it is commonly said that “cinema is not only an art form but also a mirror of society”,
the question of gender representation is directly linked to the movie industry and it reflects how we perceive the world.
In the movie industry, a lot of norms exist and they could change from country to country because more are conservatives while the others are progressive.
Therefore an analysis should be done to assess those norms and to understand to what extent they impact movie creation and what are their potential causes.
Mentalities also evolve with time and analyzing those different standards of evolution is necessary.

## Research questions
1. How has the gender distribution evolved over decades ?
2. What are the biases present ?
3. Do certain movie genres have historically been more male or female-dominated ?
4. Are there specific regions where women are under or over represented in the movie industry ? If yes, does it change with time ?
5. Does the proportion of women per country of production correspond to the demography of that country ?
6. Which gender have greater chances to be selected multiple times in movie casts ?
7. Does a balanced or unbalanced representation of gender lead to more successful movies ?

## Additional datasets

For this project we mainly used the [CMU Movie Summary Corpus](https://www.cs.cmu.edu/~ark/personas/), which contains 42,306 movie plot summaries, sourced from Wikipedia. It also provides metadata for each movie such as title, release years, box office revenue, etc. The dataset also includes characters' characteristics and actors' labels such as gender, age, ethnicity, etc.

In parallel, we also used the [names-dataset](https://github.com/philipperemy/name-dataset) Python library to reconstruct missing genres, as well as demographic data ([Our World in Data Population & Demography Explorer](https://ourworldindata.org/explorers/population-and-demography)) to analyze country-level representation in films. We also scaled the box office according to the value of the dollars at the year of interest based on the [Consumers Price Index](https://fred.stlouisfed.org/series/CPIAUCNS#0).
A dataset associating the country with its code (FRA for France, etc) is used for the interactive plot of the map of the world. It can be found on this [github](https://github.com/johan/world.geo.json/tree/master).



## Methods & Tasks

### Task 1 : Data understanding - cleaning - reconstruction (P2)
1. Data Understanding: We began by merging the movie and character datasets to explore the data and conduct a rough analysis. This step aimed to identify outliers, missing values, or other anomalies in the data.
2. Data Cleaning: During this analysis, we identified and filtered out incoherent values, such as actors with heights up to 510m or movies lasting 1.9 years. These "impossible" values were removed to ensure data integrity.
3. Data Reconstruction: Missing actor gender information was reconstructed using a gender inference process based on the Facebook dataset. By analyzing actor names, genders were associated with a certainty threshold of 0.85.  

### Task 2 : additionnal treatments of the data and first plots
1. We grouped the countries per region using the *county_to_region* function, that associates the country given to the region containing this country in its list for the spatial analysis.
2. Because of the large number of movie genres and the different genres associated to each movies, we did clustering to associate movies that have similar genres by "exploding" the genre list of each movie in a dataframe and treating them as features to cluster movies with close enough features together (the number of clusters was chosen according to the silouhette score and the SSE). A heatmap of the aggregated genres for each cluster was plotted to visualize which genres were dominant in each cluster. This allowed us to understand the distribution of genres across clusters.
3. The sizes of actors are rescaled for each gender based on the mean height of men and women respectively.
4. The box office is also rescaled in order to have comparable prices for different epochs. It was done by using the CPI dataset and the following formula : 
$ Price_{scaled} = \frac{Price_{X}}{CPI_X} CPI_{1984}$
5. We plot the proportion of male and female across the years to have a first idea about the evolution. 
6. With the new genres obtained by clustering, we plot the distribution of male and female per genre. 

### Task 3 : Spatial analysis
This section describes the spatial analysis conducted in the project. The analysis is based on two datasets:

**`data_cleaned_countries.csv` (df):**, derived from the original dataset.
**`female_population_prop.csv` (df2):** got from Our World in Data, containing the proportion of female actors in the population of a given country for each year from 1950 to 2020.

1. A column `Generation` is added to the `df` dataset to classify movies into generations. Generations are defined as 25-year periods starting from 1900 up to 2020 (last one spans only 20 years).
2. ISO codes are added to `df` using a JSON file containing a world country map. The JSON file is taken from the [Johan World GeoJSON GitHub repo](https://github.com/johan/world.geo.json/tree/master).
3. Using `df2`, the average proportion of females in the population (`F_prop_population`) is calculated for each country and generation by averaging the proportion over the years of the given generation.
4. Female proportions in movies (`F_prop_movies`) are computed for each generation and region/country using the `get_proportion()` function.
5. The datasets are merged to create a combined dataset with the following columns: `Country`, `ISO`, `F_prop_population`, `F_prop_movies`
6. A representativity index is calculated using the formula:
  \[
  \text{Representativity} = \left(\frac{\text{F_prop_movies}}{\text{F_prop_population}} - 1\right)
  \]
Positive index means overrepresentation of female actors in movies compared to their proportion in population while negative index means an underrepresentation.
7. For countries with sufficient data over three generations (1950–1975, 1975–2000, 2000–2020), the net evolution of representativity is calculated. It's the representativity of the last generation minus the one of the first generation.
8. Using the JSON file, a world map is plotted with four layers: one layer for each generation and one layer showing the net evolution of representativity.

### Task 4 : Biases analysis
1. In order to perform a logistic regression, we want to analyze the possible biases. Therefore, we illustrated some boxplots of characteristics that could be biases, separating for male and female, to see if there is a significative difference between the two groups. These boxplots work for the numerical values, such as the released year, the box office, the runtime, the actor height and the age. 
2. For categorical features, we already plotted the analysis per movie genre and per region, which allows us to consider them as biases.

### Task 5 : Matching and balancing genders 
1. Logistic Regression and Propensity Score Calculation: we build a logistic regression model using the *statsmodels* library to calculate propensity scores for each actor. The calculated propensity scores are stored.
2. Quantifying Uncertainty: we extract the model coefficients, p-values, standard errors, and confidence intervals to assess the significance of features. Coefficients with 95% CI are visualized to interpret the model results.
3. Grouping and matching by propensity score: actors are grouped by name, and the mean propensity score is calculated for each group. A subset of the data is sampled, and male and female actors are matched based on their propensity scores using a graph-matching algorithm.
4. Reconstructing features: after matching, the script reconstructs the dataset to include only matched actors. This ensures that the subsequent analysis is performed on balanced groups.
5. Visualization: Apparition Densities Before and After Matching: density plots are generated to compare apparition counts by gender before and after matching. These plots provide a visual representation of gender distribution changes due to matching.
6. Statistical testing for gender representation: A t-test is conducted to assess whether there is a statistically significant difference in apparition counts between male and female actors after matching.

### Task 6 : Matching and balancing movies with balanced and unbalanced casts in gender
1. Data Preparation:
- Feature selection: we identify the useful numerical and categorical features for this regression (movie features only).
- Dataset aggregation: we grouped the dataset by movie name, summing columns to calculate the proportion of male actors and restoring counts for each movie.
- Balanced classification: we created a new column "Balanced" to indicate whether the movie's gender proportion falls within a predefined range (±0.15 from 50%).
2. Logistic regression for propensity score calculation: we build a logistic regression model to compute propensity scores for movies based on selected features.
Extracted and visualized model coefficients, p-values, and confidence intervals to interpret feature importance.
3. Matching balanced and unbalanced movies: used a graph-based matching algorithm to pair balanced and unbalanced movies with similar propensity scores.
Evaluated matching quality by the number of successful matches.
4. Visualizing box office revenue distribution: 
- Before matching: Created density plots to compare box office revenues for balanced and unbalanced movies.
- After matching: Re-plotted box office revenue distributions for matched groups, ensuring comparable groups.


## Organization

- Thomas : final preprocessing of the data, biases analysis, merging notebook with coherence and clarity
- Etienne : analysis by genre, running tests, matching for genders number of roles
- Baptiste : clustering the genres, preparing the final presentation website 
- Léo : spatial analysis, interactive plots
- Adélaïde : gender proportion across time, matching for movies
All members have equally participate to the project and multiple meeting have been planned to discuss about each member's work. 
