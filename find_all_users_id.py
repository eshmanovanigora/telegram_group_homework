from read_data import read_data

def find_all_users_id(data: dict) -> list:
    """ 
    This function finds all user IDs from the provided data dictionary.

    Parameters:
        data (dict): Dictionary containing the data of the JSON file
    
    Returns:
        list: List containing all user IDs
    """
    lst = []
    for message in data["messages"]:
            if "id" in message:
                lst.append(message["id"])
    return lst

# Load the data and find all user IDs
data = read_data('data/result.json')
print(find_all_users_id(data))