import matplotlib as mp
import pandas as pd
import numpy as np

class Analyzer:
    def Analize(self):
        pass

class AnalyzeRings(Analyzer):
    def Analize(self):
        resume=self.statistics(data_frame=data_frame)

    def statistics(self,data_frame):
        #Generamos un dataframe resumen con los datos estadísticos asociados a la serie de medidas.
        average = data_frame.apply(axis=0, func=np.nanmean)
        min_grouth = data_frame.apply(axis=0, func=np.min)
        max_grouth = data_frame.apply(axis=0, func=np.max)
        std = data_frame.apply(axis=0, func=np.nanstd)

        statistics = pd.concat([average, std, min_grouth, max_grouth], axis=1, sort=False)
        statistics.columns=['Media','Desviacion tipica','Min','Max']
        return statistics

