#include <stdio.h>

int main(){
	int h, m; scanf("%d %d", &h, &m);

	m -= 45;
	
	if (m >= 0){
		printf("%d %d", h, m);
	} else {
		if (h-1 >= 0)
			printf("%d %d", h-1, 60+m);
		else {
			printf("%d %d", 23, 60+m);
		}

	}


	return 0;
}
