# Reto 4:Grupo 21

Los proveedores de equipo de cómputo, normalmente identifican los bienes que tienen para la venta en un catálogo mediante parejas <código_estandar:valor> en **formato JSON**.
<br><br>
Una empresa va a adquirir varios equipos de cómputo de varias marcas (servidores, estaciones de trabajo, computadores de escritorio, portátiles, tabletas, enrutadores, switches, Access points), para todas sus sedes. Y hace una licitación publicando una relación de los equipos que requiere, identificados mediante de códigos estándar de una letra.
<br><br>
Uno de los proveedores de equipo requiere un programa para **cruzar la lista de equipos solicitados por licitación contra su propio catalogo** ya que quiere saber cuáles equipos puede ofrecer y cuál sería el valor total de la oferta, si de cada equipo se compra una unidad.
<br><br>
Entrada:<br>
*  parejas <código_estandar:valor> en formato JSON del catálogo del proveedor
*   Relación total de letras que identifican los equipos solicitados por licitación. En este caso los equipos se identifican por letras del alfabeto, separados por espacio.
<br>

Salida:
*   valor total de los equipos solicitados y que el proveedor puede ofrecer, representado por un número entero.
*   relación de códigos que identifican los equipos que el proveedor puede ofrecer y que son solicitados en la licitación.

Ejemplo:

|Entrada|Salida|
|---|---|
|{"v": 45, "s": 32, "c": 45, "g": 29, "z": 45, "d": 46}|168|
|s v c d y f t|s v c d|