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
	int i ;
	int a = 8;
	int bin[a];
	for(i = 7; i > 0; i--)
	{
		bin[i] = n % 2;
		n = n / 2;	
	}
	for(i = 0; i < 8; i++)
	{
		printf("%d", bin[i]);
	}
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

