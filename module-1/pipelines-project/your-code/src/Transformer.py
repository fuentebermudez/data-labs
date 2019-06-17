import pandas as pd


class Transformer:
    def Transform(self):
        pass

class TransformRings(Transformer):
    def Transform(self,raw_data):
        observaciones=self.get_observaciones(raw_data)
        data_frame=self.genera_data_frame_observaciones(observaciones)
        return data_frame

    def remove_header(self,raw_data):
        raw_data=raw_data[raw_data.columns[0]][2:]
        return raw_data

    def get_observaciones(self,raw_data):
        #er=ExtractRings()
        #data_frame = er.Extract(path='../data/spai067-1.rwl',encoding='UTF-8')

        raw_data = self.remove_header(raw_data)
        raw_data = list(raw_data.replace("\s{3}", ";", regex=True))

        observaciones = []
        for fila in raw_data:
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

    def genera_data_frame_observaciones(self,observaciones):

        max_year = self.max_year_series(observaciones)
        min_year = self.min_year_series(observaciones)

        arboles = self.get_trees(observaciones)
        arboles = set(arboles)

        arbol_dict_medidas = self.get_measuresYears_by_tree(observaciones)

        complete_years_series = []
        for arbol in arbol_dict_medidas:
            complete_years_serie = []
            for year in range(min_year, max_year):

                measurement_years = arbol[1]
                try:
                    measurement = measurement_years[year]
                except KeyError as error:
                    measurement = 0
                complete_years_serie.append(measurement)

            complete_years_series.append(complete_years_serie)

        return (pd.DataFrame(complete_years_series, index=arboles, columns=range(min_year, max_year)))
