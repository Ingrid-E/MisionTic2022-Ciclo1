# Reto #5

#### Solución #1 realizada por: [@g1alexander](https://github.com/g1alexander)

 <!-- #### Solución #2 realizada por: [@santigp258](https://github.com/santigp258) -->

---

La tienda oficial de la Universidad Nacional decide crear una librería que le permite a la persona que atiende interactuar mucho más rápido con los usuarios que para van a comprar láminas del álbum de la chocolatina Jet. Esta librería debe permitirle a la persona que atiende poder filtrar láminas repetidas de un usuario, validar un tipo de lámina de un conjunto de láminas, verificar cuales láminas no se tienen en comparación con otro grupo de láminas y obtener el número de láminas que se pueden intercambiar de entre dos grupos. Se le ha pedido a usted que construya la librería para la tienda universitaria que tenga las cuatro (4) funciones mencionadas anteriormente. Nota: Esta librería no debe pedir entradas ni retornar valores de salida ya que estas se colocan como parámetros y retornos de las funciones.

- Función # 1: filtrar_laminas: A partir de una lista de láminas, retorna una nueva con los números de las láminas que solo se encuentras una vez.

  | Entrada                                                | Salida             |
  | ------------------------------------------------------ | ------------------ |
  | [3, 4, 6, 2, 1, 3, 3, 1, 1, 6, 6, 4, 1, 5, 5, 2, 5, 4] | [3, 4, 6, 2, 1, 5] |

- Función # 2: validar_tipo: Dada una lista de índices, una lista de láminas, y un tipo de láminas, retorna la lista de índices filtrada en donde se dejan los índices en donde coincida en la lista de láminas el tipo de lámina que se busca.
  | Entrada | Salida |
  | ------------------------------------------------------ | ------------------ |
  | [13, 10, 17, 0, 6, 18, 16, 3, 2] #indices | [10, 6, 16] |
  | [1, 5, 4, 1, 2, 4, 3, 3, 1, 1, 3, 1, 1, 1, 1, 4, 3, 5, 2] | |
  | #laminas | |
  | 3 # tipo | |

- Función # 3: listar_faltantes: Dadas la lista del usuario y la lista de intercambiables de la tienda, la función debe retornar una lista con las láminas que no estén dentro de la lista de intercambiables de la tienda.
  | Entrada | Salida |
  | ------------------------------------------------------ | ------------------ |
  | [16, 6, 0, 14, 8, 5, 22, 19, 25, 26, 9, 13] # lista_usuario | [16, 0, 5, 22, 26, 9] |
  | [25, 14, 7, 3, 4, 1, 8, 17, 6, 19, 13] # lista_intercambiables | |

- Función # 4: numero_intercambiables: Dadas las listas de un usuario y la lista de intercambiables de la tienda, la función debe decir el número de láminas que puede se pueden intercambiar entre el usuario y la tienda (Puede ayudarse de la función listar_faltantes).
  | Entrada | Salida |
  | ------------------------------------------------------ | ------------------ |
  | [3, 4, 19, 11, 1, 16, 0, 6, 17, 9]| 5|
  | [5, 6, 1, 14, 4, 20, 13, 12] | |
