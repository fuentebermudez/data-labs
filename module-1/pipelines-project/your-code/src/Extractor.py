import pandas as pd

class Extractor:
    def Extract(self):
        pass

class ExtractRings(Extractor):
    #Extrae las mediciones de los añillos del archivo con los datos en bruto.
    def Extract(self,path,encoding):
        df_tree_rings=pd.read_csv(path,encoding=encoding)
        return df_tree_rings
