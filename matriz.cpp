// matriz.cpp: define el punto de entrada de la aplicación de consola.
//

#include "stdafx.h"
#include <stdio.h>
#include <conio.h>

int main()
{
	int matriz[100][100], filas, columnas, i, j;
	printf_s("Digite el numero de filas: ");
	scanf_s("%i", &filas);
	printf_s("Digite el numero de columnas: ");
	scanf_s("%i", &columnas);

	printf_s("\n\n");

	for (i = 0; i < filas; i++) {
		for (j = 0; j < columnas; j++) {
			printf_s("Digite el numero de la matriz[%i][%i]", i+1, j+1);
			scanf_s("%i", &matriz[i][j]);
		}
	}
	printf_s("\n\n");
	for (i = 0; i < filas; i++) {
		printf_s("/");
		for (j = 0; j < columnas; j++) {
			printf_s(" %i ", matriz[i][j]);

		}
		printf_s("/ \n");
	}
	printf_s("\n\n La matriz tanspuesta es:\n");
	for (i = 0; i < filas; i++) {
		printf_s("/");
		for (j = 0; j < columnas; j++) {
			printf_s(" %i ", matriz[j][i]);
		}
		printf_s("/ \n");
	}
	



    return 0;
}

