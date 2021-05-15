#include <stdio.h>
#include <stdlib.h>


int main (void)
{
	FILE *fp;
	int *ptr;
	int summ = 0;

	ptr = (int *) malloc(100 * sizeof(int));
	fp = fopen("data.txt", "r");

	if(fp == NULL)
   	{
      		printf("Error, please check");
      		exit(1);
   	}
	fscanf(fp,"%d" ,ptr );

	while(fscanf(fp,"%d" ,ptr ) != EOF )
	{
		printf("%d \n", *ptr);
		summ = summ + *ptr;
	}
	printf("%d \n", summ);

	fclose(fp);
	free(ptr);
	fp = fopen("result.txt", "w+");
	fprintf(fp ,"%d \n", summ);
	fclose(fp);
}
