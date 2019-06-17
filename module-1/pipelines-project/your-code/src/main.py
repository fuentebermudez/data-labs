import pandas as pd

class Extractor:
    def Extract(self):
        pass
class Transformer:
    def Transform(self):
        pass


class ExtractRings(Extractor):
    def Extract(self,path,encoding):
        df_tree_rings=pd.read_csv(path,encoding=encoding)
        return df_tree_rings

class TransformRings(Transformer):
    def Transform(self):
        pass

    def get_observaciones(self,data_frame):
        er=ExtractRings()
        data_frame = er.Extract(path='../data/spai067-1.rwl',encoding='UTF-8')

        data_frame = df[df.columns[0]][2:]
        data_frame = list(data_frame.replace("\s{3}", ";", regex=True))

        observaciones = []
        for fila in data_frame:
            elementos = fila.split(";")
            year = elementos[0][-4:]
            tree = elementos[0][:-4]
            measurements = elementos[1:]
            years_measurements = self.fill_series(year, measurements)

            years_serie = years_measurements[0]
            measurements_serie = years_measurements[1]

            observacion = [tree, years_serie, measurements_serie]
            observaciones.append(observacion)
        return observaciones

    def fill_series(self,year,measurements):
        year = int(year)
        resto = divmod(int(year), 10)
        n_measurements = len(measurements)
        l_zeros = [0] * resto[1]
        r_zeros=[0] * (10-(n_measurements+len(l_zeros)))
        years = [year for year in range(year-len(l_zeros), year + (n_measurements + len(r_zeros)))]
        measurements=l_zeros+measurements+r_zeros
        measurements_year =[years,measurements]

        return measurements_year

    def get_years(self,observaciones):
        years = []
        for observacion in observaciones:
            for year in observacion[1]:
                years.append(year)

        return years

    def max_year_series(self,observaciones):
        years=self.get_years(observaciones)
        return max(years)

    def min_year_series(self,observaciones):
        years=self.get_years(observaciones)
        return min(years)

    def get_trees(self,observaciones):
        trees = [observacion[0] for observacion in observaciones]
        return list(set(trees))

    def get_measuresYears_by_tree(self,observaciones):
        arboles=self.get_trees(observaciones)
        arbol_dict_medidas = []
        for arbol in arboles:
            dict_measurements_year = {}
            for observacion in observaciones:
                if observacion[0] == arbol:
                    dict_measurements_year.update(dict(zip(observacion[1], observacion[2])))
            arbol_dict_medidas.append([arbol, dict_measurements_year])
        return arbol_dict_medidas

er=ExtractRings()
tr=TransformRings()

df=er.Extract (path='../data/spai067-1.rwl',encoding='UTF-8')
observaciones=tr.get_observaciones(data_frame=df)


max_year=tr.max_year_series(observaciones)
min_year=tr.min_year_series(observaciones)
arboles=tr.get_trees(observaciones)
arboles=set(arboles)

arbol_dict_medidas=tr.get_measuresYears_by_tree(observaciones)

complete_years_series=[]
for arbol in arbol_dict_medidas:
    complete_years_serie=[]
    for year in range(min_year,max_year):

        measurement_years=arbol[1]
        try:
            measurement=measurement_years[year]
        except KeyError as error:
            measurement=0
        complete_years_serie.append(measurement)
    complete_years_series.append(complete_years_serie)
    print(complete_years_serie)




#print(arbol_dict_medidas)
