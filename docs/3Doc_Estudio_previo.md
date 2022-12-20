[Anterior](2Doc_Objetivos_Requisitos) - [Índice](Doc) - [Siguiente](4Doc_Plan_Trabajo)

## 3. Estudio previo
### 3.1. Estado actual

El problema a resolver es la renovación de la infraestructura de RRSS del IES Gran Capitán.

Actualmente, la estructura de automatización que se estaba usando es compleja ya que requiere de la sincronización de diferentes aplicaciones alojadas en distintos servidores de __SAAS__[[1]](9Doc_Referencias_Bibliografia#1) __(Software as a Service)__.

En concreto utiliza los servicios de __Zappier__[ [2] ](9Doc_Referencias_Bibliografia#2), __Buffer__[[3]](9Doc_Referencias_Bibliografia#3) y __IFTTT__[[4]](9Doc_Referencias_Bibliografia#4).

Cada una de estas tres tecnologías requiere de una cuenta de servicio de pago.

La solución a la que se llegó fue la de usar varias cuentas con cuotas gratuitas. Este tipo de cuenta limita la funcionalidad, tanto en cantidad como en tamaño, por lo que cada tecnología deben hacer pocas y pequeñas operaciones, lo que limita la escalabilidad ya que requiere de demasiadas cuentas y servicios distintos para poder cubrir todas las necesidades de forma cómoda, efectiva y eficiente.

La infraestructura del sistema del profesorado es la siguiente:

    1. Un servicio de Zapier recibe las publicaciones de la aplicación Pocket.

![](img/old-proyect/pocket-zapier.gif)

    2. Un servicio de Zapier las publica en twitter a través de la aplicación Buffer.

![](img/old-proyect/zapier-twitter.gif)

    3. Un servicio de ifttt recibe las publicaciones de twitter.

![](img/old-proyect/twitter-ifttt.gif)

    4. Un servicio de ifttt las publica en telegram.

![](img/old-proyect/ifttt-telegram.gif)

Otro problema es la dependencia de esos servicios gratuitos, que pueden cambiar sus condiciones de uso en cualquier momento, por lo que la solución es inestable.

### 3.2. Estudio de soluciones existentes

Las solución existente es la descrita en el apartado anterior, que podría progresar mejorando las cuentas a cuotas de pago.

Existen otras aplicaciones como __n8n__[[5]](9Doc_Referencias_Bibliografia#5), __Hootsuite__[[6]](9Doc_Referencias_Bibliografia#6) o __Sprout Social__[[7]](9Doc_Referencias_Bibliografia#7), pero tienen los mismos inconvenientes que la solución actual con el añadido de que son herramientas cuyo uso es más complejo y requieren de una curva de aprendizaje más elevada.

Otra solución evidente sería usar manualmente las cuentas de las redes sociales, pero esto no es viable ya que el número de publicaciones es demasiado elevado.

[Anterior](2Doc_Objetivos_Requisitos) - [Índice](Doc) - [Siguiente](4Doc_Plan_Trabajo)
