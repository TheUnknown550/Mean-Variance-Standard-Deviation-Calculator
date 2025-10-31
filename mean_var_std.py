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
                 reshaped_list.mean()],
        'variance': [reshaped_list.var(axis=0).tolist(),
                     reshaped_list.var(axis=1).tolist(),
                     reshaped_list.var()],
        'standard deviation': [reshaped_list.std(axis=0).tolist(),
                               reshaped_list.std(axis=1).tolist(),
                               reshaped_list.std()]
    }



    return calculations