#include <stdio.h>

int main(){

	int arr[8];
	for (int i = 0; i < 8; i++) {
		scanf("%d", &arr[i]);
	}

	if (arr[0] == 1 && arr[1] == 2){
		for (int i = 2; i < 8; i++){
			if (arr[i] != i+1){
				printf("mixed"); return 0;
			}
		}
		printf("ascending");
	
	}

	else if (arr[0] == 8 && arr[1] == 7){
		for (int i = 2; i < 8; i++){
			if (arr[i] != 8 - i){
				printf("mixed"); return 0;
			}	
		}
		printf("descending");
	}
	
	else{
		printf("mixed");
	}

	return 0;
}
