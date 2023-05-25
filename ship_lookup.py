import requests
import json

def sw_lookup(type, id):
    """
    Using the StarWars API, look up the provided type and (optionally) specific ID
    Input:
        type = String
        id = String
    Output:
        List/Dict of results of the API call
    """
    pass

def results_parse(lookup):
    """
    Take in the results of the 'sw_lookup' function and filter to the pre-defined parameters
    1. Provide a list of all ships that have pilots.
    2. Provide a second list of all pilots that have used a starship.

    Input:
        lookup = List
    Output:
        Dict of lists (list one is focused on the ship, while list two is focused on the pilots)
    """
    pass

def print_results(filtered_list):
    """
    Take the provided dict of lists and iterate through the items and print them in a human readable way

    Input:
        filtered_list = Dict of lists
    Output:
        None
    """
    pass

if __name__ == "__main__":
    print("Hello World")