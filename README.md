#### Descripción
Esta branch se creó desde el IDE de ***PyCharm***.

Hilos
--

Los ***hilos*** pueden ser llamados *procesos ligeros* o *subproceso* ya que es una secuencia de tareas que son encadenas, y a su vez pueden ser ejecutada por un sistema operativo.
 
Algo que distingue a los ***hilos*** es que su ejecución comparte los mismos recursos y sumados a otros recursos hacen un conjunto que se hace llamar como proceso, la ventaja de ocuparlos es que en cualquier ejecucion que se haga, comparten los recursos para poder hacer cualquier modificacion a ellos. 
**EJEMPLO**: cuando un hilo modifica un dato en la memoria, los otros hilos acceden a ese dato modificado inmediatamente.
Los hilos poseen un estado de ejecución y pueden sincronizarse entre ellos para evitar problemas de compartición de recursos. Generalmente, cada hilo tiene una tarea específica y determinada, como forma de aumentar la eficiencia del uso del procesador.



### Parse

*Python* facilita el uso del **JSON** de *JavaScript*.
Primero que nada, debe importarse la librería. La que principalmente parsea el JSON de archivos o strings. También parsea el JSON en un diccionario o en una lista en Python y viceversa, es decir, convierte los diccionarios y las listas de Python en cadenas JSON.

> r = requests.get('https://clandestina-hds.com/movies/title?search=shrek')
> data = r.json()


