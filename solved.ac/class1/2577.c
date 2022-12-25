#include <stdio.h>

int main(){

	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	a = a*b*c;

	int arr[10] = {0,};

	while (1){
		int q = a/10, r = a%10;
		if (q+r == 0)
			break;
		arr[r] += 1;
		a /= 10;

	}

	for (int i = 0; i < 10; i++)
		printf("%d\n", arr[i]);

	return 0;
}
