#include <stdio.h>
#include <stdlib.h>

void printArray(int array[], int size) {
  for (int i = 0; i < size; i++) {
    printf("%d ", array[i]);
  }
  printf("\n");
}

void insertionSort(int array[], int size) {
  for (int j = 1; j < size; j++) {
    int key = array[j];
    int i = j - 1;

    while (key < array[i] && i >= 0) {
      array[i + 1] = array[i];
      --i;
    }
    array[i + 1] = key;
  }
}

int main() {
    int size, *Arr;
    printf("Enter size of array: ");
    scanf("%d", &size);
    Arr = (int *) malloc(size * sizeof(int));
    printf("Enter element of array: ");
    for(int i=0; i < size; i++)
        scanf("%d", &Arr[i]);
    insertionSort(Arr, size);
    printf("Sorted array in ascending order:\n");
    printArray(Arr, size);
}
