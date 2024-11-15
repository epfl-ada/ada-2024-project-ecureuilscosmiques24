from names_dataset import NameDataset
import numpy as np
import pandas as pd
import ast

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