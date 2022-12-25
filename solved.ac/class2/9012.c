#include <stdio.h>
#include <string.h>

int check(char arr[]){
	char spare[100] = {0,};
	int cnt = 0;

	for (int i = 0; i < strlen(arr); i++){
		if (arr[i] == '(') {
			spare[cnt] = '(';
			cnt++;
		}
		else {
			if (cnt <= 0 || spare[cnt-1] == ')')
				return 0;
			cnt -= 1; 
		}
	}

	if (cnt == 0) return 1;
	else return 0;
	
	

}

int main(){
	int n; scanf("%d", &n);
	for (int i = 0; i < n; i++){
		char arr[100]; scanf("%s", arr);
		if (check(arr) == 0) printf("NO\n");
		else printf("YES\n");
	}



	return 0;
}
