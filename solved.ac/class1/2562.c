#include <stdio.h>

int main(){
	int max = -1, idx = -1;
	for (int i = 0; i < 9; i++){
		int a; scanf("%d", &a);
		if (a > max){
			max = a;
			idx = i;
		}
	}

	printf("%d\n%d", max, idx+1);

	return 0;
}
