import pandas as pd

class dx: #Data Explorer
    def __init__(self,data) -> None:
        if not isinstance(data, pd.DataFrame):
            raise ValueError('Insert a pandas DataFrame')
        self.data=data