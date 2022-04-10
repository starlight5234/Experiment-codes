#include<stdio.h>
#include<stdlib.h>

#define V 6
#define INF 999999

void printSolution(int dist[][V])
{
	for (int i = 0; i < V; i++){
		for (int j = 0; j < V; j++){
			if (dist[i][j] >= (INF%10))
				printf("%7s", "INF");
			else
				printf ("%7d", dist[i][j]);
		}
		printf("\n");
	}
}

void floydWarshall (int graph[][V]){
	int dist[V][V], i, j, k;

	for (i = 0; i < V; i++)
		for (j = 0; j < V; j++)
			dist[i][j] = graph[i][j];

	for (k = 0; k < V; k++){
		for (i = 0; i < V; i++){
			for (j = 0; j < V; j++){
				if (dist[i][k] + dist[k][j] < dist[i][j])
					dist[i][j] = dist[i][k] + dist[k][j];
			}
		}
	}

	printSolution(dist);
}

int main(){
    /* Testcase 1 */
    int graph[V][V] = {
           {0, INF, INF, INF, -1, INF},
	   {1, 0, INF, 2, INF, INF},
	   {INF, 2, 0, INF, INF, -8},
           {-4, INF, INF, 0, 3, INF},
           {INF, 7, INF, INF, 0, INF},
           {INF, 5, 10, INF, INF, 0}
	};

    /* Testcase 2
    int graph[V][V] = {
           {0, 8, 5},
	   {2, 0, INF},
	   {INF, 1, 0},
	};
    */

    printf("Given graph matrix is: \n");
    printSolution(graph);

    printf("\nShortest path matrix using Floyd Warshall's algorithm is: \n");
    floydWarshall(graph);
	return 0;
}

