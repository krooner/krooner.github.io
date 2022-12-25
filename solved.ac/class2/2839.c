#include <stdio.h>

int rec(int remainder);

int main(){

	int n; scanf("%d", &n);
	printf("%d", rec(n));

	return 0;
}

