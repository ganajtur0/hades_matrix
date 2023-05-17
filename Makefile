run: matrix
	jar fu hades.jar hades/
	wmname "LG3D" && java -jar hades.jar
matrix: Matrix.java Matrix.sym
	javac -cp hades.jar Matrix.java
	cp Matrix.class Matrix.sym hades/models/io/
bazsiled: BazsiLED.java Bazsiled.sym
	javac -cp hades.jar BazsiLED.java
	cp BazsiLED.class BazsiLED.sym hades/models/io/
