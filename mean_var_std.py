import numpy as np

def calculate(list):
    if len(list) != 9: # the list must be 9
        raise ValueError("List must contain nine numbers.")
    
    # Convert list to 3x3 NumPy array
    reshaped_list = np.array(list).reshape(3, 3)
    
    # Build dictionary with all required calculations
    calculations = {
        'mean': [reshaped_list.mean(axis=0).tolist(),
                 reshaped_list.mean(axis=1).tolist(),
                 reshaped_list.mean()]
    }



    return calculations