#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int pat_f = 0;

void KMP(char* X, char* Y, int m, int n){
	if (*Y == '\0' || n == 0)
		printf("The pattern occurs with length zero");

	if (*X == '\0' || n > m)
		printf("Pattern not found");

	int next[n + 1];

	for (int i = 0; i < n + 1; i++) 
		next[i] = 0;

	for (int i = 1; i < n; i++){
		int j = next[i + 1];

		while (j > 0 && Y[j] != Y[i])
			j = next[j];

		if (j > 0 || Y[j] == Y[i])
			next[i + 1] = j + 1;
	}

	for (int i = 0, j = 0; i < m; i++){
		if (*(X + i) == *(Y + j)){
			if (++j == n) {
				pat_f = 1;
				printf("The pattern occurs with index %d\n", i - j + 1);
			}
		}else if (j > 0){
			j = next[j];
			i--;
		}
	}
	
	if(pat_f != 1)
		printf("The pattern could not be found\n");
}

int main(){
	char text[50],pattern[25];

	printf("Enter the main text: ");
	scanf("%[^\n]%*c",text);

	printf("Enter the pattern text you want to search: ");
	scanf("%[^\n]%*c",pattern);

	KMP(text, pattern, strlen(text), strlen(pattern));
	return 0;
}
