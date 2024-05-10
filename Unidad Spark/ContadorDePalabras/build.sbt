import Dependencies._

ThisBuild / scalaVersion     := "2.13.12"
ThisBuild / version          := "0.1.0-SNAPSHOT"
ThisBuild / organization     := "com.daviscientist"
ThisBuild / organizationName := "deivit"


// sbt new scala/scala-seed.g8
lazy val root = (project in file("."))
  .settings(
    name := "ContadorPalabras", // Cambia el nombre del proyecto si lo deseas
    libraryDependencies ++= Seq(
      "org.apache.spark" %% "spark-core" % "3.5.1", // Reemplaza con la versión de Spark que estás utilizando
      "org.apache.spark" %% "spark-sql" % "3.5.1"   // Reemplaza con la versión de Spark que estás utilizando
    )
  )
// See https://www.scala-sbt.org/1.x/docs/Using-Sonatype.html for instructions on how to publish to Sonatype.
