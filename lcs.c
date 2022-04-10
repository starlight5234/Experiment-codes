#include<stdio.h>
#include<string.h>

#define MAX 20
char B[MAX][MAX];

void print_lcs(char *X,char *Y,int i,int j)
{

if(i==0 || j==0)
return;

if(B[i][j]=='d')
{
print_lcs(X,Y,i-1,j-1);
printf("%c",X[i-1]);
}
else if(B[i][j]=='u')
print_lcs(X,Y,i-1,j);
else
print_lcs(X,Y,i,j-1);

}

void lcs( char *X, char *Y, int m, int n )
{
int C[m+1][n+1];
int i,j;

for(i=0;i<=m;i++)
C[i][0]=0;

for(i=0;i<=n;i++)
C[0][i]=0;

for(i=1;i<=m;i++)
for(j=1;j<=n;j++)
{
if(X[i-1]==Y[j-1])
{
C[i][j]=C[i-1][j-1]+1;
B[i][j]='d';
}
else if(C[i-1][j]>=C[i][j-1])
{
C[i][j]=C[i-1][j];
B[i][j]='u';
}
else

{
C[i][j]=C[i][j-1];
B[i][j]='l';
}
}

printf("LCS of %s and %s is ",X,Y);
print_lcs(X,Y,m,n);
printf("\n");
}

int main()
{
char X[MAX],Y[MAX];
int m,n;

printf("Enter 1st sequence:");
scanf("%s",X);

printf("Enter 2nd sequence:");
scanf("%s",Y);

m = strlen(X);
n = strlen(Y);

lcs(X, Y, m, n);

return 0;
}
