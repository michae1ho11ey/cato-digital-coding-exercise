import requests
import json

def sw_lookup(type):
    """
    Using the StarWars API, look up the provided type
    Input:
        type = String
    Output:
        A dictionary with the results of the API call
    """
    results = json.loads(requests.get(f'https://swapi.dev/api/{type}').text)
    #TODO: The results are in 10 ship chunks, the call needs to use a pagination marker to move through all pages and append them to the results
    return results

def results_parse(lookup):
    """
    Take in the results of the 'sw_lookup' function and filter to find piloted ship names and their pilots

    Input:
        lookup = List
    Output:
        Dict of lists (list one is focused on the ship, while list two is focused on the pilots)
    """
    pass
    #TODO: 
    # Create a list (piloted_ships[]) outside of any loop
    # Loop through lookup.results[] and search the 'pilots' key for the non-empty values
    # Add the ship name ('name') and the pilot(s) name(s) ('pilots') to a dictionary (piloted_ship{})
    # Add the piloted_ship{} dictionary to the piloted_ships[] list
    # Loop through piloted_ships[] looking for duplicates, and if present, create a new list with all unique ship names, and then combine the pilot list into a single ship entry
    # Return the list piloted_ships[]

def print_results(filtered_list):
    """
    Take the provided dict of lists and iterate through the items and print them in a human readable way

    Input:
        filtered_list = Dict of lists
    Output:
        None
    """
    pass
    #TODO:
    # Print out header information (StarWars Piloted Ship List) and stats of the number of found ships
    # Loop through the filtered_list[] and print out ship name and comma separated list of pilots like this:
    # Ship: {ship-name} -- Pilot(s): {pilot-one}, {pilot-two}
    # If only one pilot is found, then don't print a comma after the pilot's name

if __name__ == "__main__":
    ship_list = sw_lookup('starships')
    filtered_list = results_parse(ship_list)
    print_results(filtered_list)
