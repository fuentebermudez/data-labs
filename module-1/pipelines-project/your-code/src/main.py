import matplotlib
matplotlib.use('TkAgg')


import matplotlib.pyplot as plt

from Extractor import ExtractRings
from Transformer import TransformRings


er=ExtractRings()
tr=TransformRings()

raw_data=er.Extract (path='../data/spai067-1.rwl',encoding='UTF-8')

data_frame=tr.Transform(raw_data)

primera_serie=data_frame[:0]

years=primera_serie.index
measurements=primera_serie.values

plt.interactive(False)
plt.plot(years,measurements)
plt.show(block=True)
data_frame.plot()
#print(data_frame)



