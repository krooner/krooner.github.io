#include <stdio.h>

int main(){
	int n; scanf("%d", &n);
	int gap = 1;
	int lb = 0;
	int answer = 1;
	while (1){
		//printf("%d, %d\n", lb, lb+gap);
		if (lb < n && n <= lb+gap)
			break;
		lb += gap;
		if (answer == 1)
			gap *= 6;
		else
			gap += 6;
		answer += 1;
	}

	printf("%d\n", answer);

	return 0;
}
