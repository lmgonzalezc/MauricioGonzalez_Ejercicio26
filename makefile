all: euler.dat rk4.dat leapfrog.dat

%.dat: MauricioGonzalez_Ejercicio26.x
	./MauricioGonzalez_Ejercicio26.x

MauricioGonzalez_Ejercicio26.x: MauricioGonzalez_Ejercicio26.cpp
	c++ MauricioGonzalez_Ejercicio26.cpp -o MauricioGonzalez_Ejercicio26.x

clean:
	rm -rf *.x *.dat
