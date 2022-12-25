#include <stdio.h>
#include <math.h>

int prime(int num){
	if (num < 2) return 0;
	int boundary = (int) sqrt(num);
	// printf("num: %d, boundary: %d", num, boundary);
	for (int i = 2; i <= boundary; i++){
		if (num % i == 0) return 0;
	}
	return 1;
}

int main(){
	int n; scanf("%d", &n);
	int answer = 0;
	for (int i = 0; i < n; i++){
		int num;
		scanf("%d", &num);
		if (prime(num) == 1) {
	//		printf("prime number %d\n", num);
			answer += 1;
		}
	}

	printf("%d\n", answer);

	return 0;
}
