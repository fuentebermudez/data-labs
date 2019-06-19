

# Aplicación de patrón ETL a datos dendrocronológicos.




## Introducción

Para la realización de este proyecto se ha elegido una fuente de datos que contiene datos referentes al crecimiento de los árboles. Estos datos se presentan como mediciones de los anillos de crecimiento, que se generan anualmente y se corresponden con el periodo de actividad vegetativa de los árboles.

![NOAA Logo](https://static01.nyt.com/images/2019/04/29/science/29SCI-TREE-RINGS-3/merlin_153311571_b3fdf7b9-c200-4890-9b82-9f12f185d579-articleLarge.jpg)

Se ha elegido está fuente de datos, por un lado por su interés en diversos campos como la arqueología, el estudio del cambio climático y la gestión mediambiental y por otro por ser datos normalizados para los que es interesante la creación de un procedimiento que los adapte a un interés concreto.

## Objetivo
El objetivo es implementar un patrón ETL que dé como resultado un resumen estadístico, además de transoformar los datos de tal manera que sea más sencillo su incorporación en otras herramientas o análisis.

## Procedimiento.

Como fuente de datos se acude a NOAA. Este organísmo estadounidense pone a disposición del público una base de datos de mediciones dendroconológicas para su descarga. 
Estos datos se proporcionan en archivos de texto plano con una estructura [definida](https://www1.ncdc.noaa.gov/pub/data/paleo/treering/treeinfo.txt).

Estos archivos se presenta como un conjunto de medidas agrupadas por arboles correspondiendose cada medida a un año determinado. Las mediciones se agrupan por décadas y no hay el mismo número de mediciones para todos los arboles.

El resultado final deseado es un data frame en el que aparezca una columna por añor y tantas filas como arboles.

Para obtener este dataframe primero hay que normalizar las series de mediciones rellenando los huecos.

Estas series normalizadas de mediciones se almacenan primero en una lista y luego, para facilitar su manejo se pasan a un diccionario cuyas claves serán los años.

Una vez se tienen los correspondientes diccionarios se procede a generar el data frame.

Sobre este data frame se realizan las últimas transformaciones de los datos.






