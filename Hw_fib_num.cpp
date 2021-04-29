#include <stdio.h>

int numberFibonacci(int number)
{
	int sum = 0;
	if (number >= 0)
	{
	int num1 = 0;
	int num2 = 1;
	int temp = 0;
	while ( num2 <= number )
	{
		sum = num2 + sum;
		temp = num1 + num2;
		num1 = num2;
		num2 = temp;		
	}
	printf ("The sum of all Fibonacci numbers less than %d is equal to %d \n",number, sum);
	}else{
		printf ("The number is not valid\n");
	}

	return sum;


}

int conv_to_bin (int n)
{
	int i = 0;
	printf ("the binary representation of %d is :\n", a);
	for (int b = sizeof(int) * 8 - 1; b >= 0; b--){
		i = a % 2;
		a = a >> 1;
		if (i & 1){
			printf ("1");
		} else {
			printf ("0");
		}
	}
	printf("\n");
}


int main()
{
	int inpt;
	printf ("Enter your number: ");
	scanf("%d", &inpt);
	printf ("Inputed number is %d\n" , inpt);
	int fibnum = numberFibonacci(inpt);
	printf("The binary representation of our number is ");
	conv_to_bin(fibnum);
	printf("\n");
}

