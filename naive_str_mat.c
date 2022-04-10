#include <stdio.h>
#include <string.h>

#define max 20

void search(char* pat, char* txt)
{
	int M = strlen(pat);
	int N = strlen(txt);

	for (int i = 0; i <= N - M; i++) {
		int j;

		for (j = 0; j < M; j++)
			if (txt[i + j] != pat[j])
				break;

		if (j == M)
			printf("Pattern found at index %d \n", i);
	}
}

int main()
{
	char txt[max], pat[max];
	printf("Enter text string: ");
	scanf("%s", txt);

	printf("Enter pattern to search: ");
	scanf("%s",pat);
	
	search(pat, txt);
	return 0;
}

