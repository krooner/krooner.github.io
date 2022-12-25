#include <stdio.h>

int main(){

	
	int arr[42] = {0,};
	int answer = 0;
	for (int i = 0; i < 10; i++){
		int a; scanf("%d", &a);
		arr[a%42] += 1;
		if (arr[a%42] == 1)
			answer += 1;
	}
	printf("%d", answer);

	return 0;
}
