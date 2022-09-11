#include<stdio.h>
#pragma warning(disable:4996)

int ar[10];

int function(int N);

int main()
{
	int N, T;
	int result;
	int t;

	scanf("%d", &T);
	for (t = 0; t < T; t++)
	{
		scanf("%d", &N);
		result = function(N);
		printf("%d\n", result);
	}


	return 0;
}
int function(int N)
{
	
	if (N < 0) return 0;
	if (N <= 1)	return 1;
	if (ar[N])	return ar[N];
	return ar[N] = function(N - 3) + function(N - 2) + function(N - 1);
}