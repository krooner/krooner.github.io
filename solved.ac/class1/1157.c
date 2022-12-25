#include <stdio.h>
int main(){
	char arr[1000000]; scanf("%s", arr);
	char cnt[26] = {0,};
	int idx = 0,  max = 0;
	while (1) {
		if (arr[idx] == '\0') {
			break;
		}
		int cidx = (int)arr[idx] - 97;
		if (cidx < 0) {
			cidx += 32;
		}
		cnt[cidx] += 1;
		if (max < cnt[cidx]) {
			max = cnt[cidx];
		}
		idx += 1;
	}
	idx = -1;
	int repeat = 0, max_idx = 0;
	for (int i = 0; i < 26; i++){
		if (cnt[i] == max){
			repeat += 1;
			max_idx = i;	
		}
	}
	
	if (repeat > 1) printf("?");
	else printf("%c", max_idx+65);
	return 0;
}	
