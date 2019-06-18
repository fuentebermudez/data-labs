import pandas as pd


class Transformer:
    def Transform(self):
        pass

class TransformRings(Transformer):
    def Transform(self,raw_data):
        #Toma los valores extraídos y los transforma en un data frame.
        observaciones=self.get_observaciones(raw_data)
        data_frame=self.genera_data_frame_observaciones(observaciones)
        self.delete_zero_columns(data_frame)
        self.remove_precission(data_frame)
        data_frame=self.to_numeric(data_frame)
        return data_frame

    def remove_header(self,raw_data):
        #Quita las primeras líneas que contienen información referente al punto de muestreo
        raw_data=raw_data[raw_data.columns[0]][2:]
        return raw_data

    def get_observaciones(self,raw_data):
        '''
        Toma los datos brutos y los transforma en una lista cuyo primer elemento es el ID del árbol y el segundo
        una lista con las mediciones en las que se ha rellenado con ceros los valores que faltan.
        :param raw_data:
        :return:
        '''

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
        #Rellena los valores que faltan para una decada.
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
        #Obtiene la serie de años asociada a un conjunto de mediciones.
        years = []
        for observacion in observaciones:
            for year in observacion[1]:
                years.append(year)

        return years

    def max_year_series(self,observaciones):
        #Obtiene el último año para el que hay mediciones
        years=self.get_years(observaciones)
        return max(years)

    def min_year_series(self,observaciones):
        #Devuelve el primer año para el que hay mediciones
        years=self.get_years(observaciones)
        return min(years)

    def get_trees(self,observaciones):
        #Obtiene el id del árbol asociaodo a un conjunto de mediciones.
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

    def delete_zero_columns(self,data_frame):
        #Eliminamos los años que no tienen un mínimo de 30 mediciones.
        for column in data_frame.columns:
            values=list(data_frame[column].values)
            zeros=values.count(0)
            n_measures=len(data_frame[column])
            if (n_measures-zeros)<30:
                data_frame.drop(column,inplace=True,axis=1)

    def remove_precission(self,data_frame):
        #Substituye el valor 999 que indica la precisión de las medidas
        data_frame.replace("999", 0, inplace=True)

    def to_numeric(self,data_frame):
        #Aseguramos que el tipo de las columnas del data_frame es el correcto
        data_frame = data_frame.astype(int)
        return data_frame
