from fastapi import FastAPI

import logging
import pickle
import numpy as np

# it can't take a dash in the module name
from dataobjectsmodule.dataobjects import Flower


# using a logger as the print statements 
# do not come on the console
# using JavaScript naming conventions as opposed to python
logger = logging.getLogger("uvicorn.error")
logger.setLevel(logging.DEBUG)


app = FastAPI()

# this is a pre-trained model for Iris flower classification
# done via jupyter notebooks
irisClassificationModelFile  = open("models/iris_classification_model.pickle", "rb") 

# this doesn't need to be cast to the actual model used
# load it only once for the  instance and keep in memory
irisModel = pickle.load(irisClassificationModelFile)

# hardcoding for now TODO load from a JSON file
irisModelFlowerLabels = ["setosa", "versicolor", "virginica"]



@app.get("/")
def read_root():
    logger.debug("Root request served")
    return {"status": "The service is setup and running"}


@app.post("/predictflower/")
def predictFlower(flowerInstance: Flower):
    
    # TODO find out how to write this in separate line
    logger.debug(f"Flower instance: {flowerInstance}")

    flowerDetails = np.array([
        [
            flowerInstance.sepalLength,         
            flowerInstance.sepalWidth,
            flowerInstance.petalLength,
            flowerInstance.petalWidth
         ]]
        )
    
    logger.debug(f"Input array value: {flowerDetails}")

    # this returns an array with one value
    prediction = irisModel.predict(flowerDetails)

    # take the first value TODO null check
    predictionValue = prediction[0]
    logger.debug(f"Predicted value: {predictionValue}")

    # convert the number to text using labels
    predictedFlower = irisModelFlowerLabels[predictionValue]
    logger.debug(f"Predicted flower: {predictedFlower}")

    response = {"flower": predictedFlower}

    return response
