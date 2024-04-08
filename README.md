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
        El cual se piensa de la siguiente forma: Se implementa pensando principalmente en un colegio, desde su diseño, aunque luego se 
                                                 revisa que puede servir para muchas cosas más.

Paso 3: Se crea una interfáz gráfica que hace que el ingresar los datos sea un poco más amigable e interactiva.

## Desafío 2

Paso 1: Como se hizo en el diseño general, se va a llevar en archivos .csv a la nube, almacenandolo en un container para su posterior explotación.

Paso 2: Implementaciíon del código para conectarse con el storage remoto y hacer el envío de la información.

Paso 3: Se crea un contenedor en la cuenta de almacenamiento datalake storage gen 2  de azure, ésto para alojar allí los archivos con la información
        generada.

Paso 4: Se crea un Key vault para poder tener una mayor seguridad en las claves usadas para enviar la información, ésto hace que al ser un repositorio público
        no se tenga mayor vulnerabilidad a filtraciones no deseadas. (Éste paso se intenta y se crea el secreto, pero se presentaron errores inesperados y se decide avanzar
        para una implementación real y productiva es indispensable).

## Desafío 3

Paso 1: para ésto se creó un recurso de Azure Synapse, en el cual se van a hacer las implementaciones de ADF y del procesamiento que llegue a ser necesario.

Paso 2: Se integró GitHub con AZ synapse analitics, ésto para que todo lo desarrollado en dicha plataforma quede registrado y se pueda llevar una trazabilidad.
        Se tuvo que resolver varios inconvenientes con dicha integración, dejo la documentación encontrada para reolver el error:
        https://learn.microsoft.com/en-us/answers/questions/1180165/failed-to-load-one-or-more-resources-due-to-forbid
        https://stackoverflow.com/questions/75220412/azure-synapse-github-personal-access-token-is-invalid

Paso 3: Desarrollo de pipelines necesarios para el copiado de la data desde el continer de la data cruda hasta el caontainer en donde se va a almacenar y a transformar.



