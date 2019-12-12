import requests
import json
import pandas as pd


def func(url):
    response = requests.get(url, "GET")
    if response.status_code == 200:
        json_object = json.loads(response.content)
        count = json_object['count']
        products = json_object['products']
        df = pd.DataFrame.from_dict(products.values())
        df['popularity'] = pd.to_numeric(df['popularity'])
        df.sort_values(['popularity'], inplace=True, ascending=False)
        return df[['title', 'price']]

