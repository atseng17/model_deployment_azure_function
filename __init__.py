import json
import logging
import os
from typing import Union

import azure.functions as func
import joblib
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split

# if you need to load model weights
# clf = joblib.load('XXX.pkl')
connection: Union[str, None] = os.getenv("SQLConnectionString")
# cnxn = pyodbc.connect(connection)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    data = req.get_json()
    data = json.loads(data)

    if data is not None:
        # importing data
        housing_data = datasets.fetch_california_housing()
        feature_names = housing_data["feature_names"]

        # Get feature/target and train test split
        feature_df = pd.DataFrame(data=housing_data["data"])
        feature_df.rename(
            columns={
                0: feature_names[0],
                1: feature_names[1],
                2: feature_names[2],
                3: feature_names[3],
                4: feature_names[4],
                5: feature_names[5],
                6: feature_names[6],
                7: feature_names[7],
            },
            inplace=True,
        )
        target_df = pd.DataFrame(data=housing_data["target"])
        target_df.rename(columns={0: "Target"}, inplace=True)
        housing = pd.concat([feature_df, target_df], axis=1)
        X_train, X_test, y_train, y_test = train_test_split(
            housing.loc[:, housing.columns != "Target"],
            housing["Target"],
            random_state=66,
        )

        # Create linear regression object
        regr = linear_model.LinearRegression()
        regr.fit(X_train, y_train)

        importance = regr.coef_.tolist()
        results_dict = {"pred_label": importance, "dummy connection string": connection}

        return json.dumps(results_dict)

    else:
        return func.HttpResponse(
            "Please pass a properly formatted JSON object to the API", status_code=400
        )
