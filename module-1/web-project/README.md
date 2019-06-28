![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Objetivo
El objetivo de este proyecto es:
* Realizar una extracción de todas las leyes promulgadas por el congreso de los diputados desde el año 1977.
* Aplicar técnicas de minería de textos a los títulos de las leyes para obtener unos datos sobre los que poder aplicar otras técnicas de minería de textos.
* Una vez obtenidos y normalizados los datos se pretendía aplicar algún criterio de clasificación que permitiera saber si estas leyes eran de corte progresista o conservador.

# Proceso

Se ha aplicado un ptrón ETL en el que se ha creado un módulo para agrupar todas las funciones que se han necesiado para realizar webscrapping de la página del congreso ya que no existe ninguna API que permita la extracción de estos datos.

Para continuar con el patrón se ha creado otro módulo en el que se han agrupado las funciones creadas para transformar el texto. La transformación del texto tiene como resultado un data frame en el que se han agrupado las leyes por años y sobre las que se han aplicado métodos de limpieza propios de la minería de texto.

Por último para completar la fase de análisis se ha creado un Notebook de Jupiter sobre el que se ha implementado el análisis de los datos.

# Resultados

No se ha conseguido hacer la clasificación del texto, en lugar de eso se han creado nubes de palabras para cada uno de los años para visualizar que asuntos han sido más relevantes desde el punto de vista legislativo para cada uno de los años.

