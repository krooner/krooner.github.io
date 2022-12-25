#include <stdio.h>

int main(){
	
	char arr[1000000]; scanf("%[^\n]s", arr);
	int i = 0;
	int before = 1;
	int answer = 0;
	while (1){
		if (arr[i] == '\0')
		       break;
		if (arr[i] == ' ')
			before = 1;	
		else {
			if (before == 1){
				answer += 1;
				before = 0;
			}		
		}
		i += 1;

	}       
   	printf("%d", answer);	

	return 0;
}
