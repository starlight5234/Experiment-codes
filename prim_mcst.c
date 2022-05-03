#include <stdio.h>
#include <stdlib.h>

#define INF 999999

void prim(int ad_mat[10][10], int dim){
    int visited[10] = {0};
    int noOfEdgesVisited = 1, min_cost=0;
    int min, a,b;
    visited[1]=1;

    while(noOfEdgesVisited < dim){
        min = INF;
        for(int i=1; i<=dim; i++){
            for(int j=1; j<=dim; j++){
                if(ad_mat[i][j]<min){
                    if(visited[i] != 0){
                        min = ad_mat[i][j];
                        a = i;
                        b = j;
                    }
                }
            }
        }

        printf("MST Path:\n");
        if(visited[b]==0){
            printf("%d to %d cost = %d\n",a,b,min);
            min_cost = min_cost + min;
            noOfEdgesVisited++;
        }

        visited[b] = 1;
        ad_mat[a][b] = ad_mat[b][a] = INF;
    }

    printf("\nMST Minimum cost is %d\n",min_cost);
}

int main(){

    int ad_mat[10][10];
    int dim;

    printf("Enter the number of vertices: ");
    scanf("%d", &dim);

    printf("Enter cost in the form of adjacency matrix: " );
    for(int i=1; i<=dim; i++){
        for(int j=1; j<=dim; j++){
            scanf("%d", &ad_mat[i][j]);
            if(ad_mat[i][j] == 0){
                ad_mat[i][j] = INF;
            }
        }
    }

    prim(ad_mat, dim);
    return 0;
}

