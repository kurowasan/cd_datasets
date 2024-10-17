import requests
import os
import json
import numpy as np
import time
import matplotlib.pyplot as plt
import pandas as pd

def main(verbose: bool = True) -> dict:
    venues = ['NeurIPS', 'ICLR', 'ICML', 'AISTATS', 'UAI', 'AAAI', 'CLEaR', 'JMLR']

    query_params = {'query': '"causal discovery" | "causal structure learning" | "DAG learning" | "DAG structure learning"',
                    'fields': 'title,year,venue,abstract,url',
                    'year': '2019-2024',
                    'venue': ",".join(venues)}

    # add your API key here. You can get one by signing up at https://api.semanticscholar.org/
    headers = {'x-api-key': 'XXX'}

    url = f"http://api.semanticscholar.org/graph/v1/paper/search/bulk"
    r = requests.get(url, params=query_params, headers=headers).json()
    if verbose:
        print(f"Found approx. {r['total']} papers")

    retrieved = 0
    all_papers = []

    # retrieve all papers, 1000 at a time
    while True:
        if "data" in r:
            retrieved += len(r["data"])
            if verbose:
                print(f"Retrieved {retrieved} papers...")
            all_papers.extend(r["data"])
        if "token" not in r or r["token"] is None:
            break
        query_params["token"] = r["token"]
        r = requests.get(url, params=query_params, headers=headers).json()

    if verbose:
        print(f"Done! Retrieved {retrieved} papers total")

    # save as JSON file
    with open(f"papers.json", "w") as f:
        json.dump(all_papers, f, indent=2)

    return all_papers

def format_short_name(df: pd.DataFrame) -> pd.DataFrame:
    short_names = {"AAAI Conference on Artificial Intelligence": "AAAI",
                   "International Conference on Learning Representations": "ICLR",
                   "International Conference on Artificial Intelligence and Statistics": "AISTATS",
                   "Conference on Uncertainty in Artificial Intelligence": "UAI",
                   "Neural Information Processing Systems": "NeurIPS",
                   "International Conference on Machine Learning": "ICML"}
    df.replace(short_names, inplace=True)
    return df


def save_as_csv(all_papers: dict):
    # use short names for venues
    df = pd.DataFrame(all_papers)
    df = format_short_name(df)
    df[["title", "year", "url", "venue"]].to_csv("raw_papers.csv", index=False)


if __name__ == "__main__":
    all_papers = main()
    save_as_csv(all_papers)
