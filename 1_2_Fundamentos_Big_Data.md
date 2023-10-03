# 02. Fundamentos de Big Data

En esta sección vamos a entender: 

* Qué es el Big Data.
* Qué problemas soluciona.


# 02.1 ¿Qué es Big Data?

Aunque no hay ninguna definición que se acepte de forma "oficial", hay una definición que personalmente me gusta mucho:

_Big Data es el conjunto de herramientas y estrategias que permiten adquirir, almacenar y explotar una determinada información, que por diversas circunstancias, no se puede hacer con las técnicas o herramientas tradicionales._

Big Data es un proceso caro, pensemos que necesitaremos:
* Herramientas software especializadas.
* Hardware especialidado
* Personal con experiencia capacitado para hacer la tarea correctamente. 

Por lo tanto aunque Big Data e IA, están muy de moda, deberemos de asegurarnos de que es realmente necesario acudir al Big Data. En definitiva podemos caer el típico problma de un sobrecoste y sobreesfuerzo por intentar matar moscas a cañonazos.

Fijémonos en la siguiente imagen:
![Bloques del módulo](/images/02/tam.png)




* Una película HD en 1080 que ocupase un Zettabyte , duraría 36 millones de años
* El total del video en streaming ya supera los 4 zettabytes
* En los dos ultimos años se ha creado más datos que en toda la humanidad anterior.
* Amazon usa más de 2 Petabytes de datos diarios para recomendar productos a sus clientes, optimizar precios y gestionar inventarios.
* Google procesa más de 20 petabytes de datos al día para ofrecer sus servicios de búsqueda, publicidad, correo electrónico, mapas, traducción y otros.
* Twitter genera más de 12 terabytes de datos al día con los mensajes, imágenes y vídeos que comparten sus usuarios, y los utiliza para analizar tendencias, sentimientos y opiniones.
* Facebook almacena más de 300 petabytes de datos en su plataforma, que incluyen los perfiles, las publicaciones, los comentarios, los likes y las interacciones de sus más de 2.800 millones de usuarios activos al mes.

Un ejemplo de consumo podemos verlo en la siguiente gráfica
![Bloques del módulo](/images/02/tam2.png)

Podemos entender a partir de esta información que Big Data es un problema Grande, y nunca mejor dicho. ¿Como podríamos calcular una media de edad en un conjunto de datos de 1 terabyte? ¿Cuánta RAM necesito? ¿Cuánto tiempo se puede tardar en condiciones normales? ¿ Y un petabyte?

Por ejemplo BERT que es primo muy pequeño de ChatGPT4, se entrenó con unos 3.300 millones de palabras y requirió unos 1.843.200 Teraflops por segundo, donde un TeraFlop es un billón de instrucciones en coma flotante por segundo.


# 02.1 Pero.... ¿Porqué se necesitan tantos datos? 

Desde pequeños hemos aprendido que si tenemos una función podemos generar infinitos valores para la misma, pero qué ocurre cuando no tenemos la función y tenemos que obtener una aproximación a la misma mediante datos? Es decir, ¿Qué ocurre cuando tenemos justo el problema inverso? Tengo una serie de puntos y necesito obtener la función. 

![Bloques del módulo](/images/02/regresion_lineal.png)

Si lo pensamos, sería increible poder tener una función que me dijera exáctamente qué va a subir y a bajar en la bolsa. El que tuviera esa función sería multi-multi... millonario, por tanto, ¿Porqué no intentar conseguirla?.

El problema es que no es sencillo, el mero hecho de un humano tomando una decisión en un momento, puede hacer que acciones bajen o que suban, es decir, los parámetros del modelo de predicción son tantos, que es imposible eliminar la incertidumbre en este problema. 

De cualquier forma no es lo mismo tener 3 puntos e intentar calcular la recta que hemos visto antes, que tener mil puntos.

Fijaos en la siguiente imagen, en la que intentamos predecir la recta de regresión del ejemplo anterior pero con pocos puntos: 


![Regresión Lineal Pocos Puntos](/images/02/regresion_lineal2.png)

Cómo podéis observar cuantos más puntos, más sencillo va a ser obtener la mejor recta posible. Pensad en el caso de que únicamente tuviéramos un único punto, tendríamos infinitas rectas!!!, con lo que la única forma de alejarnos del infinito y acercarnos a la precisión es tener más punto. 

Aunque los ejemplos se basan en una regresión lineal sencilla, podéis entender que las redes neuronales se basan en lo mismo, ... Ostras! igual no es descabellado que Ellon compre twitter y se hunda en bolsa!!, que pasa con los datos que ha adquirido.... Uhm..... Hay veces que únicamente necesitamos datos!



![Data Meme](/images/02/data_every.png)

# 03. Ciclo de Vida

En la siguiente imagen podemos observar que el big data es un conjunto de áreas, cada una de las cuales puede tener unas capcidades técnicas: 

![Data Meme](/images/02/ciclo_vida.png)

* Business Case. Todo comienza con un problema, ... Tenemos un problema o queremos obtener un beneficio de algo y necesitamos resolverlo. 

* Data Collection. Como hemos visto, el primer paso, es almacenar la información. Este proceso no es tan sencillo como parece:
  * Bases de datos distintas
  * DataSources diferentes, por ejemplo, ¿y si sacamos información de los videos de youtube??
  * Velocidad en la generación de datos, IOT
  * Capacidad de almacenamiento. ¿Como almacenará netflix toda esa información=, y ¿Spotify?
  * Durabilidad. Hay datos que nunca se pueden perder!
  * ...


* Data Modeling. De todas las fuentes de datos, podrían ocurrir que para algo que semánticamente signifique lo mismo, pudiera ser que distintos equipos, departamentos, empresas o indivíduos, tengan un concepto distinto y lo guarden de forma diferente. ¿Cómo se unifica toda la información en un único dato que representa la información verídica?
  
* Data Processing. Obviamente si tenemos toda esa cantidad de DATOS, es porque en algún momento tenemos que obtener INFORMACIÓN de ellos, ... Uhmm, no es lo mismo... Pues no, tenemos que realizar un proceso de transformación (al menos uno).
  
* Data Visualization. En este punto hemos hecho una cantidad ingente de trabajo, definiendo el problema, adquiriendo datos, procesando datos, ... Para poder tener, en muchas ocasiones un PowerPoint que será lo que vea el cliente y experto en negocio y nos dirá si todo ha merecido la pena o tenemos que modificar algo. La visualización de datos es algo sencillo e intuitivo que la gente no IT, es decir Bussiness, pueda entender y sacar sus conclusiones, es decir, cuadros de mando como por ejemplo Power Bi. Al final si lo pensamos, ... mucho de nuestro trabajo es para obtener la información lo más sencilla posible y necesaria para que los expertos en negocio, sepan que decisión tomar, o al menos que les ayude a eliminar ese concepto tan molesto,... La incertidumbre.

En el útimo momento vemos que hay una flecha... Vaya, volvemos a empezar? Sí, o no, si al final lo que hemos obtenido no elimina la incertidumbre y Bussiness sigue sin saber que decisión tomar, necesitaremos volver a replantear el problema y modificar lo que haga falta para que ellos topen la decisión correcta. Pensemos que vivimos en una economía voraz, en la que determinadas informaciones pueden hacer que nos destaquemos o que vayamos a quiebra. **Ese es nuestro trabajo, indagar en los datos para poder ayudar las tomas de decisiones complejas del mundo que nos rodea.**

# 04. Las V's del Big Data.

No sólo Big Data es un problema por la gran cantidad de datos, ya que si lo pensamos, hasta hace relativamente poco, los bancos no usaban las tecnologías actuales de Big Data y siempre han trabajado con muchísimos datos. Entonces? Qué es Big Data.

Podríamos decir, de una manera simplificada que tenemos un problema de Big Data cuando al menos se dan 3 de las 4 V's del Big data que son: 

![Data Meme](/images/02/uves.png)


* **Velocity**:
  * Los datos son generados a gran velocidad, muchas veces además de forma ininterrumpida.
  
* **Volume**: 
  * Se refiere a cuando tenemos una gran cantidad de datos.

* **Variety**: 
  * No tenemos únicamente datos en forma de tabla, como ocurría antes, actualmente tenemos distintos tipos de información:
    * Estructurada: La que se representa de forma estricta, como son los formatos tabulares. DataFrames, SQL, ... Es lo que usaban los bancos y la más sencilla de trabajar, puesto que los datos son **estáticos**, o mejor dicho, sus estructuras.
  
    * Semi-Estructurada: Con el fin de romper la rigidez en la estructura de los datos, apareció JSON, aunque es un formato que tiene cierta estructura podemos cambiar mucha de la información gracias a su flexibildad. Como podemos comprender, es más complicada de gestionar que algo que sé que siempre va a tener unos nombres, tipos, tamaños,... Como en el formato estructurado.
  
    * Desestructurado: Aquello que se aleja de la estructura computacional y se acerca a la de los humanos, como es el audio, el video, el texto,... Para trabajar con este tipo de información necesitaremos conocimientos específicos del área, como puede ser NLP o Natural Language Programming, por ejemplo.


**Veracidad**:
  * Algo que nos puede llamar la atención es que en BD los datos **pueden** no ser consistentes.
    * Hay veces que cuando tenemos bases de datos distribuidas, cuando guardamos un dato no se guarde en todas las bases de datos a la vez, sino que se guardan en una y luego se manda una orden de actualización al resto, lo que provoca que durante un tiempo, haya varios valores para el mismo dato (sharding).
    * Hay otras en las que tenemos valores distintos para el mismo dato, porque tenemos muchas fuentes de información y o lo han cogido de forma diferente, o bien lo han interpretado de forma distinta.
    * Por ello, necesitaríamos, y de hecho es uno de los primeros pasos que tenemos que hacer, el tener un único centro de la verdad, es decir algún sitio centralizado donde ese sea nuestro valor verdadero.


**Value**
* Hay autores


# 05. Fases de procesamiento en Big Data

Desde los comienzos se han pasado por 3 fases: 

* 2003 hasta 2009 aproximadamente **Procesamiento Batch**:
  * Se caracterizaba por tener una gran cantidad de datos y no tener una prisa excesiva en realizar los cálculos. Por ejemplo si tenía que realizar la facturación antes de un día en concreto, me daba igual que tardase 20horas de procesamiento.
  * Si nos fijamos eran los problemas que tenían las grandes empresas que en un primer momento se plantearon obtener beneficio de los datos. Por ejemplo imaginad el caso en el que Ford con todos sus datos almacenados durante años se planteara aplicar machine learning a los datos. Probablemente les dará igual que la computación tarde horas o incluso días si van a obtener un benefició
  * Escalable  
  * Procesamiento distribuido en paralelo
  * Alta capacidad de tolerancia a fallos
  * Trabaja con grandes cantidades de datos estáticos
  * Sufren una gran latencia.
  
* 2010 a 2015 aproximadamente. ** Procesamiento Streaming** 
  * Durante esta época existe una gran revolución, a diferencia de lo que pasaba anteriormente, ahora los datos no son históricos que necesitan ser procesados sino que lo que ocurre ahora es que emergen multitud de empresas que generan datos en tiempo real, por lo cual necesito tener capacidad de cómputo para estas nuevas necesidades. Pensamos en Facebook, Amazon, Netflix...
  * El Stream Processing, se caracteríza precisamente porque los datos vienen en tiempo real ( o cerca del tiempo real), con lo que el tiempo de respuesta importa, ahora no puedo tardar en procesar algo en horas sino que necesito tiempos de respuesta mucho más rápidos.
    * Escalable
    * Procesamiento distribuido y paralelo
    * Alta capacidad de tolerancia a fallos
    * Los datos pueden cambiar de forma constante.
    * No tienen casi prácticamente latencia. 

* Actualidad. ** Arquitecturas híbridas**
  * Ahora estamos en un momento en el que si lo pensamos usamos las dos cosas anteriores. Las empresas como Ford que procesan datos históricos también generan datos de forma contínua y por tanto, necesitan hacer un mix de las dos arquitecturas. 
  * Pensemos en que por ejemplo quiero hacer una previsión en ventas para final de este año, y necesito un dato hoy, si solicito ese dato y tengo que computarlo es problable que tarde bastante y para hoy no lo tendría, pero un valor aproximado tampoco me viene mal. En lugar de tener una previsión de ventas con un incremtento del 5,43% respecto al año anterior, si tengo que va a ser superior al 5% me da practicamente la misma información. 
  * Las arquitecturas híbridas se caracterizan porque en lugar de tener una u otra, dependiendo de una selcción obtendré datos calculados en streaming o prodré procesar los históricos

![Data Meme](/images/02/hibridas.png)

  
Pensad en que la capacidad de hardware y las herramientas software deben de adaptarse para cada uno de los escenarios descritos anteriormente.

En la siguiente imagen podemos ver la evolución de los sistemas Big Data

![Data Meme](/images/02/evolucion.png)


# 05. Procesamiento Paralelo y Procesamiento Distribuido.
## 05.1 Procesamiento Paralelo vs Procesamiento lineal. 

Observemos la siguiente imagen:
![Data Meme](/images/02/procesamiento_lineal_paralelo.png)

* Procesamiento Lineal
  * Cada instrución, bloque, ... Es secuencial, lo que implica que se ejecuta algo, y posteriormente se ejecuta otra cosa. 
  * Imaginemos que tenemos una impresora y quiero imprimir 100 hojas. En este caso la persona que está esperando a que termine tendrá que ver como imprimo mis 100 copias. Esto es procesamiento lineal. 
  * Si pensamos de una manera más abstracta, nos daremos cuenta de que **siempre que se comparte un recurso** tenemos un bloqueo, y por tanto deberemos de esperar a que se termine de hacer lo que estamos haciendo para que comience lo siguiente. Por lo tanto la capcidad, y por tanto, la velocidad de procesamiento dependerá de la capacidad o velocidad del elemento bloqueante, o cuello de botella.
  
* Procesamiento en Paralelo
  * En este caso tenemos varias instancias del elemento bloqueante, por lo cual puedo ejecutar al mismo tiempo varias unidades de ejecución porque no comparten recurso.
  * Imaginemos en este caso que disponemos de 3 impore