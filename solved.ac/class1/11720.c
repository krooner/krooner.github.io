#include <stdio.h>

int main(){
	
	int n; scanf("%d", &n);
	char arr[n+1];
	scanf("%s", arr);
	int answer = 0;
	for (int i = 0; i < n; i++){
		int v = (int)arr[i] - 48;
		answer += v;
	}

	printf("%d", answer);
	return 0;
}
