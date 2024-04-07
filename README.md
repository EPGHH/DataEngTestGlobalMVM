# DataEngTestGlobalMVM
Repository for Data Engineering Technical Test - Global MVM

# Introducción
El presente repositorio resuelve la prueba técnica para Global MVM de Ing de Datos

# Punto 1

Paso 1: Se cre una primera versión del diagrama de solución, al identificar que cada uno de los desafíos corresponde a una 
        parte del proceso de ingesta de datos, para éste caso se identifica como ELT, en donde se realiza la extracción y carga
        a una base de datos própia para posteriormente transformarlos explotarlos en análisis. 
        a los datos.

## Desafío 1

Paso 1: Se diseña un diagrama ER sobre el cual se puede proceder a construir el código que generará la data de acuerdo a éste.
        Se agrega una columna last_modified_date para tener un registro de cuando fue agregado cada uno de los datos.

Paso 2: Se implementa el código para generar la data.
        El cual se piensa de la siguiente forma: 