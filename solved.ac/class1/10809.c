#include <stdio.h>

int main(){

	char arr[100]; scanf("%s", arr);
	int cnt[26];
	for (int i = 0; i < 26; i++)
		cnt[i] = -1;	
	int i = 0;
	while (1){
		if (arr[i] == '\0')
			break;
		int idx = (int)(arr[i]) - 97;
		if (cnt[idx] == -1)
			cnt[idx] = i;
		i += 1;
	}

	for (int i = 0; i < 26; i++)
		printf("%d ", cnt[i]);

	return 0;
}
