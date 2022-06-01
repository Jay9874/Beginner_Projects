//Program for Matrix Multiplication

#include<stdio.h>

#include<math.h>

int mat_input(int arr[][100], int r)

{

	int i, j;	

	for(i=0; i<r; i++)

	{

		printf("\nEnter the elements in the %dth row.\n\n", i+1);

		for(j=0;j<r; j++)

		{

			printf("Enter the element in the %dth column.", j+1);

			scanf("%d", &arr[i][j]);

		}

	}

}

int mat_display(int arr[][100], int r)

{

	int i, j;

	

	for(i=0; i<r; i++)

	{

		for(j=0;j<r; j++)

		{

			printf("\t%d  ", arr[i][j]);

		}

		printf("\n");

	}

}

int mat_multip(int arr1[][100], int arr2[][100], int arr6[][100], int r)

{

	int i, j, k;

	

	for(k=0;k<r;k++)

	{

		for(i=0;i<r;i++)

		{

			for(j=0;j<r;j++)

			{

				arr6[k][i] += arr1[k][j] *arr2[j][i];

			}

 		}

	}

	printf("\nThe multiplication of both the matrices is\n");

	mat_display(arr6, r);

}

int main()

{

	int x[100][100], y[100][100], res[100][100], i, j, r;

	

	printf("What is the order of all the square matrices?: ");

	scanf("%d", &r);

	printf("Enter all the elements of first matrix.");

	mat_input(x, r);

	printf("\nEnter all the elements of second matrix.");

	mat_input(y, r);

	mat_multip(x, y, res, r);

}
