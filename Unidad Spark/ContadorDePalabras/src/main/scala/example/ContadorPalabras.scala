import org.apache.spark.sql.SparkSession

object ContadorPalabras {
  def main(args: Array[String]): Unit = {
    // Inicializa SparkSession
    val spark = SparkSession.builder
      .appName("Contador de Palabras")
      .master("local[*]") // Ejecuta localmente con todos los núcleos disponibles
      .getOrCreate()

    // SparkContext se utiliza para interactuar con RDDs
    val sc = spark.sparkContext

    // Lee el archivo de texto como un RDD
    val texto = sc.textFile("libro.txt")

    // Realiza la operación de conteo de palabras
    val conteoPalabras = texto.flatMap(linea => linea.split("\\W+")) // "\\W+" divide por cualquier carácter no alfabético
                              .filter(palabra => palabra.nonEmpty) // Filtra palabras vacías
                              .map(palabra => (palabra.toLowerCase, 1)) // Convierte a minúsculas y mapea cada palabra a un par (palabra, 1)
                              .reduceByKey(_ + _) // Reduce los pares por clave (palabra) sumando los valores

    // Imprime el conteo de palabras
    conteoPalabras.collect().foreach(println)

    // Detiene la SparkSession
    spark.stop()
  }
}
