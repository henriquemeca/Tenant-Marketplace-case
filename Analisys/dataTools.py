import imp
from importlib.resources import path
from xml.etree.ElementInclude import include
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

def explore(data):
    print('----Data Sample----')
    print(data.head())
    print('----About the columns----')
    print(data.info())
    print('----Unique values in columns----')
    print(data.nunique())
    print('----Numeric columns statistics----')
    print(data.describe())
    print('')

def plots(data):
    print('----Columns Histogram----')
    """
        function1: general plots
            correlations(heatmap) ,Cluster
        function2: column analyser
            histogram, boxplot,valuecounts pie, violin plot
        function3: specific plots 2 variables
            Pareto, Ogiva, density(with mean and meadian on the chart), scatter
        function4: plot grids
            seaborn scater plot grids / pairplot / relplot / distplot / cat plot

        CRISP DM method
        - Barry | Business Understading
        - Drove | Data Understanding
        - Directly to the | Data Prep
        - Medical | Modeling
        - Emergency | Evaluation
        - Department | Deployment
    """
    
    # for (columnName, columnData) in data.iteritems():
    #     graph = data[columnName].plot

        
# class dataExplorer: 
#     def __init__(self,data) -> None:
#         if not isinstance(data, pd.DataFrame):
#             raise ValueError('Insert a pandas DataFrame')
#         self.data=data
