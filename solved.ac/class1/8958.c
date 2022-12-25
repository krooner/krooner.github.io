#include <stdio.h>

int main(){
	
	int n; scanf("%d", &n);
	for (int i = 0; i < n; i++){
		char arr[80]; scanf("%s", arr);
		int j = 0;
		int streak = 0;
		int score = 0;
		while (1){
			if (arr[j] == '\0')
				break;
			if (arr[j] == 'X')
				streak = 0;
			else {
				score += 1 + streak;
				streak += 1;
			}
			j += 1;
		}			
		printf("%d\n", score);
	}

	return 0;
}
