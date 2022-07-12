import pandas as pd

class CSVReader:

    @classmethod
    def read_csv(cls, path: str, data_format: str):
        data = pd.read_csv(path).to_dict(data_format)
        return data