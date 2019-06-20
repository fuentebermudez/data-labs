import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from Extractor import ExtractRings
from Transformer import TransformRings
from Analyzer import AnalyzeRings

if __name__=='__main__':
    er=ExtractRings()
    tr=TransformRings()
    an=AnalyzeRings()

    raw_data=er.Extract (path='../data/spai067-1.rwl',encoding='UTF-8')

    data_frame=tr.Transform(raw_data)

    result = an.statistics(data_frame=data_frame)




