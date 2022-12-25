#include <stdio.h>

int main(){
	int answer = 0;
	for (int i = 0; i < 5; i++){
		int v; scanf("%d", &v);
		answer += (v%10) * (v%10);
	}

	printf("%d", answer%10);

	return 0;
}
