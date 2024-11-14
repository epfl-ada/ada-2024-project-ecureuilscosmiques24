# Gender Representation in Movie Over Time

## Abstract
Gender equality and representation has been a core issue since the 20th and 21th century.
Those centuries are characterised by a lot of movement and progress towards women's rights, for example in France the legalisation of abortion in 1975.
Therefore the question of gender representation is directly linked to the movie industry,
because it is the main vision of the woman and the one that is shown to everybody. One may assume that in the cinema industry women are under-represented.
They also might be younger than men. Those two parameters could also change from country to country because more are conservatives while the others are progressive.
Therefore an analysis should be done to assess those parameters and to understand to what extent those propositions are true and what are their substantive causes.
With the evolution of mentalities it could be interesting to analyse those different parameters against time.

## Research questions
1. How has the gender distribution across different movie genres evolved over decades ?
2. Do certain genres have historically been more male or female-dominated ? Can we link it to different historical/societal events ?
3. Is the actor's age influenced by the movie genre ? Does age influence the movie success (box office revenue for identical genres) ?
4. Are there specific regions where women are under or over represented in the movie industry ? If yes, does it change with time ?
5. Does the proportion of women per country of production correspond to the demography of that country ?
6. Does a balanced or unbalanced representation of gender lead to more successful movies ?
7. What biases are present ?
8. Can we predict the proportion of women using all the parameters that were used for the analysis with an ML model ?

For all those questions the cause may be identified and with the results some variable could be coupled. For example we could look at the evolution of representation of women in a certain type of movie in a specific region.

## Proposed additional datasets

- *name-dataset*: As gender is at the heart of our analysis, we have to address missing gender information. To do so, we use an additional dataset sourced from GitHub. This dataset, available at [this repository](https://github.com/philipperemy/name-dataset) and as a python library, contains information about the gender of the first name and comes from a Facebook leak. It allows us to infer the likely gender of actors based on their first names, providing a probable classification as male or female and thus removing some uncertainty.
The dataset is in the form of a python library that can be installed with the following line in the prompt with pip installer: “pip install names_dataset”
- [Population & Demography Data Explorer - Our World in Data](https://ourworldindata.org/explorers/population-and-demography?Metric=Population&Sex=Male&Age+group=Total&Projection+Scenario=None&country=USA~GBR~RUS~FRA~IND~DEU~AUS~CAN~POL~JPN~HKG~KOR~HUN~ESP~PAK~ITA~FIN~ZAF~MEX~IRL~TUR~DNK~SWE~NOR~PHL~BRA~BIH~CZE~NLD~CHE~KHM~PRT~BEL~THA~AUT~GRC~ISL~PRI~MYS~CHN~IDN~SVK~UKR~VEN~SGP~TWN~MLT~URY~IRN~ROU~PRK~IMN~MNE~PER~NPL~COL~VIR~HRV~KEN~EGY~ISR~NZL~JAM~BGR~SRB~EST~UZB~BGD~CUB~LKA~VNM~MKD~ARG~LUX~JOR~CHL~BHS~ALB~LTU~NGA~BOL~ARE~AFG~PSE~ARM~CRI~LBN~SEN~CYP~GEO~DZA~BTN): To study the demography of the different countries and the link to the representation in the films produced in these countries, we will use a dataset with the number of women, number of men for the selected countries (we choose the one that are interesting for our data) from 1950 to 2023. Integrate demographic data to provide country-level gender population distributions. This dataset will help us measure how movie industry gender representation aligns with actual demographic distributions by country.

## Methods & Tasks

### Task 1 : Data understanding - cleaning - reconstruction
1. As the first task is always understanding the data, we started by describe it and do a rough analysis to reveal outlier, missing values or whatever seems strange about it. This was done by merging both dataset, and then treat it to manage different data types. 
2. This basic analysis leads us to the cleaning part, where we have to filter incoherent values, as an example, we can cite the fact that there is actors measuring up to 510m high, or movie duration up to 1.9 years. So we decided to filter the data, based on common outliers on Earth, such as the talles man on Earth. 
3. After this cleaning part, the reconstruction part starts and we did reconstruct actor gender based on the Facebook leak mentionned above. We also treated NaN values at this point. 
4. Finally, an other rough analysis is needed to check what changed in the data during cleaning and reconstruction, and if the data treated are representative of the original rough data.

### Task 2 : Research questions & naive analysis - visualisations
1. Now that we understand well the data, and that we have a useable dataset, we devl into the research questions, and develop more on what data story we want to tell. 
2. This also leads us to a first analysis were we analyze our data globally, using two variables, the proportion of women and time. This allows to create plot and conduct statistical tests (such as t-tests) to see if there has been any change.
3. Next we could conduct a more specific analysis by breaking it down into certain categories, such as the evolution of the proportion of women over time by region or by film genre and then conduct statistical tests. 

### Task 3 : Matching and balancing data 
1. Subsequently, our data are likely biassed, so we could perform linear regressions with as many covariates as possible, in order to calcultate the propensity score, which allow us to compute a similarity index. We would have then two categories, men and women, which could need to be matched. 
2. Next, we need to check is the covariates are balances between the two groups, which can be done using histograms and boxplots. If the balance is confirmed, the analysis can be conducted; is not, the process previous point should re-run and adjust certain variables in the matching process to end up with a balanced dataset.

### Task 4 : Final conclusions and prediction
1. Finally, a more global analysis followed by specific analysis of certain parameters can be performed, similarly to the initial naive analysis conducted in Task 2. Again, plots and statistical tests can be conducted to draw unbiased conclusions. 
2. As a cherry on top, we can try to build an ML model using regression to predict the future proportion of women in movie depending on its characteristics. Cross-Validation will be performed at this stage to test the quality of our model, and ROC curves can be used to assess the performance of the model. 


## Proposed timeline & Organization

#### Until 10.11.24
- Task 1:
    - 1.1: Baptiste & Etienne 
    - 1.2: Adélaide & Thomas
    - 1.3: Baptiste
    - 1.4: Léo
#### Until 15.11.24
- Milestone P2:
    - Readme: Baptiste, Etienne & Adélaide
- Task 2:
    - 2.1: All
    - 2.2: Thomas & Adélaide
    - 2.3: Etienne


## Questions for TAs

- We didn’t find any information in the readme about which genre is the principal genre, we only have a list of genres, can we assume that the first genre of the list is the main genre to do our analysis?
- We think that the ethnicity of the actors may induce some biases for our analysis, but there are a lot of missing values for the ethnicity. 
