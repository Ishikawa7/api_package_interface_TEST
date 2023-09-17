import requests
import pandas as pd
from io import StringIO

def autoCM_fit(dataset : pd.DataFrame) -> pd.DataFrame:
    url = "https://us-central1-davidesemeion.cloudfunctions.net/function-1"
    df_json = dataset.to_json()
    response = requests.post(url, json = df_json)
    # check status code
    print("Status response: " + str(response.status_code))
    assert response.status_code == 200
    df_result = pd.read_json(StringIO(response.json()))
    return df_result
