# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 16:29:11 2021

@author: Nikhil
"""

import json
import argparse
from pathlib import Path
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor

def _random_forest(args):

    # Open and reads file "data"
    with open(args.data) as data_file:
        data = json.load(data_file)
    
    # The excted data type is 'dict', however since the file
    # was loaded as a json object, it is first loaded as a string
    # thus we need to load again from such string in order to get 
    # the dict-type object.
    data = json.loads(data)

    x_train = data['x_train']
    y_train = data['y_train']
    x_test = data['x_test']
    y_test = data['y_test']
    
    # Initialize and train the model
    model = RandomForestRegressor()
    model.fit(x_train, y_train)

    # Get predictions
    y_pred = model.predict(x_test)
    
    # Get r2 score
    r2 = r2_score(y_test, y_pred)

    # Save output into file
    with open(args.r2, 'w') as accuracy_file:
        accuracy_file.write(str(r2))


if __name__ == '__main__':

    # Defining and parsing the command-line arguments
    parser = argparse.ArgumentParser(description='My program description')
    parser.add_argument('--data', type=str)
    parser.add_argument('--r2', type=str)

    args = parser.parse_args()

    # Creating the directory where the output file will be created (the directory may or may not exist).
    Path(args.r2).parent.mkdir(parents=True, exist_ok=True)
    
    _random_forest(args)
