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
1. How has the gender distribution across different movie genres evolved over decades ? Do certain genres have historically been more male or female-dominated ?
2. Is the actor's age influenced by the movie genre ? Does age influence the movie success (box office revenue for identical genres) ?
3. Are there specific regions where women are under or over represented in the movie industry ? If yes, does it change with time ?
4. Does the proportion of women per country of production correspond to the demography of that country ?
5. Does a balanced or unbalanced representation of gender lead to more successful movies ?
6. What biases are present ?
7. Can we predict the proportion of women using all the parameters that were used for the analysis with an ML model ?

## Proposed additional datasets

- *name-dataset*: To address missing gender information,
we use the `names-dataset` Python library, sourced from a GitHub repository ([here](https://github.com/philipperemy/name-dataset)).
Based on a Facebook leak, it provides likely gender classifications for first names,
helping us infer actors' genders as male or female. Install it via: `pip install names-dataset`

- To analyze country-level gender representation in films,
we use demographic data from the [Our World in Data Population & Demography Explorer](https://ourworldindata.org/explorers/population-and-demography).
This dataset provides the male and female population for selected countries from 1950 to 2023,
enabling us to compare movie industry gender representation with actual demographic distributions. 



## Methods & Tasks

### Task 1 : Data understanding - cleaning - reconstruction
1. As the first task is always understanding the data, we start by describing it and do a rough analysis to reveal outliers,
missing values or whatever seems strange about it. This was done by merging both datasets (movies+characters),
and then treating it to manage different data types.
2. This basic analysis leads us to the cleaning part, where we have to filter incoherent values.
For example, we can cite the fact that there are actors measuring up to 510m high,
or movie duration up to 1.9 years. So we decided to filter the data, based on common outliers,
such as the tallest man on Earth. 
3. After this cleaning part, the reconstruction part starts and we reconstruct actor gender based on the Facebook leak mentioned above.
We also treated NaN values at this point. 
4. Finally, another rough analysis is needed to check what changed in the data during cleaning and reconstruction,
and if the treated data are representative of the original rough data.

### Task 2 : Research questions & naive analysis - visualizations
1. Now that we understand the data well, and that we have a usable dataset,
we go deeper into the research questions, and develop more on what data story we want to tell. 
2. This also leads us to a first analysis where we analyze our data globally,
using two variables, the proportion of women and time.
This allows us to create plots and conduct statistical tests (such as t-tests) to see if there has been any change.
3. Next we conduct a more specific analysis by exploring changes into certain categories,
such as the evolution of the proportion of women over time by region or by film genre and then conduct statistical tests. 

### Task 3 : Matching and balancing data 
1. Subsequently, our data are likely biased, so we could perform linear regressions with as many covariates as possible,
in order to calculate the propensity score, which allows us to compute a similarity index.
We would have then two categories, men and women, which could need to be matched.
This way we deal with the observable covariates which makes our analysis unbiased (except unobservable covariates). 
2. Next, we need to check if the covariates are balanced between the two groups,
which can be done using histograms and boxplots. If the balance is confirmed,
the analysis can be conducted; if not,
the process in the previous point should re-run and adjust certain variables in the matching process to end up with a balanced dataset.

### Task 4 : Final conclusions and prediction
1. Finally, we repeat initial naive analysis conducted in Task 2,
but with unbiased and balanced data, this will lead to unbiased conclusions. 
2. As a cherry on top, we can try to build an ML model using regression to predict the future proportion of women in movies depending on its characteristics.
Cross-Validation will be performed at this stage to test the quality of our model,
and ROC curves can be used to assess the performance of the model. 


## Proposed timeline & Organization

#### Until 10.11.24
- Task 1:
    - 1.1: Baptiste & Etienne 
    - 1.2: Adélaïde & Thomas
    - 1.3: Baptiste
    - 1.4: Léo
#### Until 15.11.24
- Milestone P2:
    - Readme: Baptiste, Etienne & Adélaïde
- Task 2:
    - 2.1: All
    - 2.2: Thomas & Adélaïde
    - 2.3: Etienne
#### Until 20.12.24
- Task 3:
    - 3.1: Etienne & Baptiste
    - 3.2: Léo, Thomas & Adélaïde
- Task 4: All

## Questions for TAs

- We didn’t find any information in the readme about which genre is the principal genre,
we only have a list of genres, can we assume that the first genre of the list is the main genre to do our analysis?
- We think for e.g. that ethnicity of the actors may induce some biases, but there are a lot of missing values for the ethnicity.
Is it mandatory to drop the NaN for these features ? Or is it possible to keep these values for the analysis ?
