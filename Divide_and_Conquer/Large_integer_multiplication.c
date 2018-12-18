#include <stdio.h>
#include <stdlib.h>

/*Multiplication of large integers, represented as strings for simplicity*/

int divide_and_conquer_mult(int num1, int num2)
{
	//For small numbers, use the basic algorithm
	//Now taking small as 2-digit numbers
	if(strlen(num1) < 3 || strlen(num2) < 3)
	{
		return num1 * num2;
	}
	//Divide each number in half
	num1_1 = 


void main(int argc, char *argv[])
{
	if(argc != 3)
	{
		printf("Usage: lim num1, num2\n");
		return;
	}
	int res = divide_and_conquer_mult(argv[1], argv[2]);

	printf("%d\n", res);

	return;
}

