import imp
from importlib.resources import path
import pandas as pd
from os import listdir
import json 

def getJsons(folder)->list:
    """Get all Json files in Path as data frames"""
    if not folder.endswith('/'):
        folder += '/'

    paths = listdir(folder)
    paths = [folder+p for p in paths if p.endswith('.json')]
    files = {}
    for path in paths:
        with open(path,encoding='utf-8') as f:
            f = json.load(f)
            files[path.replace(folder,'').replace('.json','')] = f
    return files

class dataExplorer: 
    def __init__(self,data) -> None:
        if not isinstance(data, pd.DataFrame):
            raise ValueError('Insert a pandas DataFrame')
        self.data=data