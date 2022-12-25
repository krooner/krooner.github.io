#include <stdio.h>

int main(){
	
	int n; scanf("%d", &n);
	double arr[n];
	double max = -1.0;
	for (int i = 0; i < n; i++){
		double v; scanf("%lf", &v);
		arr[i] = v;
		if (v > max)
			max = v;
	}
	double avg = 0.0;
	for (int i = 0; i < n; i++){
		avg += (arr[i]/max)*(double)100;
	}

	printf("%lf", avg/(double)n);


	return 0;
}
