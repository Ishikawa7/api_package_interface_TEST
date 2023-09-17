import requests
import pandas as pd
from io import StringIO

def autoCM_fit(dataset : pd.Dataframe) -> pd.DataFrame:
    url = "https://us-central1-davidesemeion.cloudfunctions.net/function-1"
    df_json = dataset.to_json()
    response = requests.post(url, json = df_json)
    df_result = pd.read_json(StringIO(response.json))
    return df_result
