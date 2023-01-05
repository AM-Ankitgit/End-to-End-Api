import pickle
import json
import config
import numpy as np

## creating class
class Iris():
    # user input
    def __init__(self,sepal_width, petal_length, petal_width, species):
        self.sepal_width=sepal_width
        self.petal_length=petal_length
        self.petal_width=petal_width
        self.species="species_"+species
    # for load model
    def load_model(self):
        with open(iris_model_path,'rb') as file:
            self.model=pickle.load(file)
        with open(iris_json_path,'r') as file:
            self.json_data =json.load(file)
    def get_predicted_length(self):
        self.load_model()
        test_array=np.zeros(len(self.json_data['columns']))
        test_array[0]=self.sepal_width
        test_array[1]=self.petal_length
        test_array[2]=self.petal_width
        
        species_index =self.json_data['columns'].index(self.species)
        test_array[species_index]=1
        print("Test_array",test_array)
        lenght1= self.model.predict([test_array])
        return lenght1