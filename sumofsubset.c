#include<stdio.h>
#define TRUE 1
#define FALSE 0

int inc[50], w[50], sum, n, set_found=0;

void sumset(int,int,int);

int promising(int i,int wt,int total) {
	return(((wt+total)>=sum)&&((wt==sum)||(wt+w[i+1]<=sum)));
}

int main() {
	int i,j,n,temp,total=0;
	printf("Enter how many numbers: ");
	scanf("%d",&n);
	printf("\nEnter %d numbers to the set: ",n);
	for (i=0;i<n;i++) {
		scanf("%d",&w[i]);
		total+=w[i];
	}
	printf("\nInput the sum value to create sub set: ");
	scanf("%d",&sum);
	for (i=0;i<=n;i++)
		for (j=0;j<n-1;j++)
			if(w[j]>w[j+1]){
				temp=w[j];
				w[j]=w[j+1];
				w[j+1]=temp;
			}

	if((total < sum)){
		printf("\nSubset construction is not possible.\n");
	}else{
		for (i=0;i<n;i++)
			inc[i]=0;
		sumset(-1,0,total);
		if(set_found == 0)
			printf("No feasible set solution.\n");
		else
			printf("\n");
	}
	return 0;
}
void sumset(int i,int wt,int total) {
	int j;
	if(promising(i,wt,total)) {
		if(wt != sum) {
			inc[i+1]=TRUE;
			sumset(i+1,wt+w[i+1],total-w[i+1]);
			inc[i+1]=FALSE;
			sumset(i+1,wt,total-w[i+1]);
		} else {
			if(set_found == 0)
				printf("The solution using backtracking is: ");
			else
				printf(", ");
			
			printf("{ ");
			for (j=0;j<=i;j++)
				if(inc[j])
					printf("%d ",w[j]);
			printf("}");
			set_found = 1;
		}
	}
}
