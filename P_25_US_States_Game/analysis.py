import pandas as pd 

data = pd.read_csv("50_states.csv")         # Reading CSV File

# print(data)

states_list = data["state"].to_list()       # List of State Names
# print(states_list)

def state_info(state_name) :                # Method to return State coordinates w.r.t. State Name
    
    state_data = data[data["state"] == state_name]
    state_data = [state_data["x"].item(), state_data["y"].item()]
    
    return state_data

def save_states(list,location):
    data_csv = pd.DataFrame(list)
    data_csv.to_csv(location)