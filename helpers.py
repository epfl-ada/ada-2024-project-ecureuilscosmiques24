from names_dataset import NameDataset
import numpy as np
import pandas as pd
import ast
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt


#We create an instance of the NameDataset class
nd = NameDataset()


def string2dict(data: str) -> dict:
    """Convert a string representation of a dictionary to a dictionary
    Args:
        data (str): The string representation of a dictionary
    Returns:
        dict: The dictionary
    """
    return ast.literal_eval(data)


def extract_all_genres(data: str) -> list:
    """Extract all genres from a string representation of a dictionary
    Args:
        data (str): The string representation of a dictionary
    Returns:
        list: The list of genres"""
    data_list = []
    for key,value in string2dict(data).items():
        data_list.append(value)
    return data_list


#We create a function to extract the first name of an actor
def split_name(full_name : str) -> str:
    """Extract the first name from the full name of an actor
    Args:
        full_name (str): The full name of the actor
    Returns:
        f_name (str): The first name of the actor
        """
    parts = full_name.strip().split()
    
    f_name = parts[0] if parts else ''
    return f_name


#We create a function to deduce the gender based on the actor's first name
def get_gender(name : str) -> str:
    """Get the dominant gender(85 percent) associated to a name 
    Args:
        name (str): The name of the actor
    Returns
        gender (str): The gender of the name(M/F/Unknown)
    """
    f_name = split_name(name)
    temp = nd.search(f_name)

    if temp['first_name'] is not None : 
        prob_male = temp['first_name']['gender'].get('Male',0)
        prob_female = temp['first_name']['gender'].get('Female',0)

        #We use a threshold of 85% of confidence about the gender. 
        #When 85% of the time, the name considered is associated to a specific gender, 
        #we decide that this is the correct genre.
        if prob_male > 0.85:
            gender = 'M'
        elif prob_female > 0.85:
            gender ='F'
        else :
            gender = 'Unknown' #when there is a doubt on the gender, we replace it by unknown.

        return gender
    

def country_to_region(country):
    """
    Associate a defined region to a country
    Input:
    country: string
    Output:
    region: string
    """
    # Define lists for each region
    north_america = ["united states of america", "canada", "puerto rico", "mexico", "bahamas", "costa rica"]
    south_america = ["argentina", "brazil", "venezuela", "peru", "bolivia", "chile", "colombia", "cuba"]
    western_europe = ["united kingdom", "france", "germany", "west germany", "weimar republic",
                    "netherlands", "switzerland", "portugal", "belgium", "austria", "finland",
                    "denmark", "sweden", "norway", "iceland", "ireland", "luxembourg", "greece", 
                    "spain", "italy", "england","wales", "cyprus"]
    eastern_europe = ["soviet union", "poland", "hungary", "yugoslavia", "bosnia and herzegovina",
                    "czech republic", "slovakia", "slovenia", "romania", "ukraine", "bulgaria",
                    "republic of macedonia", "lithuania", "albania", "georgia", "armenia","turkey",
                    "slovak republic", "croatia", "estonia", "serbia"]
    asia = ["india", "japan", "hong kong", "south korea", "pakistan", "thailand", "malaysia",
            "china", "indonesia", "taiwan", "iran", "nepal", "korea", "israel", "vietnam",
            "sri lanka", "cambodia", "bangladesh", "uzbekistan", "bhutan", "russia", "lebanon", 
            "united arab emirates", "singapore"]
    oceania = ["australia", "new zealand", "isle of man", "philippines", "jamaica"]
    africa = ["south africa", "egypt", "nigeria", "algeria", "senegal", "afghanistan"]

    # List of "dead" countries
    dead_countries = ["german democratic republic", "czechoslovakia", "kingdom of great britain",
                    "socialist federal republic of yugoslavia", "federal republic of yugoslavia",
                    "nazi germany", "mandatory palestine", "palestinian territories", "serbia and montenegro", "burma"]

    # Merge all regional lists into one dictionary
    country_region_map = {**{country: "North America" for country in north_america},
                          **{country: "South America" for country in south_america},
                          **{country: "West Europa" for country in western_europe},
                          **{country: "East Europa" for country in eastern_europe},
                          **{country: "Asia" for country in asia},
                          **{country: "Oceania" for country in oceania},
                          **{country: "Africa" for country in africa},
                          **{country: "Dead country" for country in dead_countries}}

    # We make the function insensitive to the case
    country = country.strip().lower()

    # Return the region or a default message if the country is not found
    return country_region_map.get(country, "Unknown region")


def extract_numerical_categorical_features(data:pd.DataFrame, exclude_col:list):
    """
    Extract the categorical and numerical features of a dataset whith some excluded columns
    Args:
    data: the dataframe
    label: the label we do not want to import
    """
    numerical_features = [key for key, value in data.dtypes.items() if value=="float64" and key not in exclude_col]
    print(f"Numerical features: {numerical_features}")

    #categorical_features = [key for key, value in data.dtypes.items() if value=="object" and key!=label]
    categorical_features = [col for col in data.columns if col not in (numerical_features+exclude_col)]
    print(f"Categorical features: {categorical_features}")
    
    return numerical_features, categorical_features


def plot_sse(features_X, start=2, end=10):
    """
    Plot the sum of the squared errors

    Input:
    features
    start: min k values
    end: maximum k value

    Output:
    matplotlib.object
    """
    sse = []
    for k in range(start, end):
        # Assign the labels to the clusters
        kmeans = KMeans(n_clusters=k, random_state=10).fit(features_X)
        sse.append({"k": k, "sse": kmeans.inertia_})

    sse = pd.DataFrame(sse)
    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(sse.k, sse.sse)
    ax.set_xlabel("K")
    ax.set_ylabel("Sum of Squared Errors")
    ax.set_title("Sum of squared error depending on k")
    plt.show()
    return ax


def min_max_scaling(data):
    """
    Set the maximum of the data to 1 and the minimum to 0
    Args:
    data: the data we want to scale
    Returns
    scaled_data
    """
    data_max = np.max(data)
    data_min = np.min(data)
    scaled_data = (data-data_min)/(data_max-data_min)
    return scaled_data


def computediff(prop1,prop2): 
    return np.abs(prop1-prop2)


def compute_similarity(prop1,prop2):
    return 1-np.abs(prop1-prop2)