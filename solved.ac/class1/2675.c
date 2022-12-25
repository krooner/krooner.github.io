#include <stdio.h>

int main(){

	int t; scanf("%d", &t);
	for (int i = 0; i < t; i++){
		int r; char s[20];
		scanf("%d %s", &r, s);
		char arr[160];
		int idx = 0;
		int arr_idx = 0;
		while (1){
			if (s[idx] == '\0')
				break;
			for (int j = 0; j < r; j++){
				arr[arr_idx] = s[idx];
				arr_idx += 1;
			}
			idx += 1;
		}
		arr[arr_idx] = '\0';
		
		printf("%s\n", arr);
	}

	return 0;
}
