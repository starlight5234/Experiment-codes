#include <stdio.h>
#include <stdlib.h>

void printArray(int array[], int size);
void merge(int array[], int low, int mid, int high);
void MergeSort(int array[], int low, int high);

int main(){
    int array[5] = {5, 4, 3, 2 ,1};
    int size = sizeof(array)/sizeof(array[0]);

    MergeSort(array, 0, size-1);

    printf("This is the sorted array: \n");
    printArray(array, size);
}

void printArray(int array[], int size) {
  for (int i = 0; i < size; ++i) {
    printf("%d  ", array[i]);
  }
  printf("\n");
}

void MergeSort(int array[], int low, int high){
    if(low < high){
        int mid = low + (high - low)/2;

        MergeSort(array, low, mid);
        MergeSort(array, mid+1, high);

        merge(array, low, mid, high);
    }
}

void merge(int array[], int low, int mid, int high){

    int Lsize = mid - low + 1;
    int Rsize = high - mid;

    int LeftArr[Lsize], RightArr[Rsize];

    for(int i=0; i < Lsize; i++){
        LeftArr[i] = array[low + i];
    }

    for(int i=0; i < Rsize; i++){
        RightArr[i] = array[mid + 1 + i];
    }

    int l_idx=0, r_idx=0;
    
    int main_idx=low;
    
    while(l_idx < Lsize && r_idx < Rsize){
        
        if(LeftArr[l_idx] > RightArr[r_idx]){
            
            array[main_idx] = RightArr[r_idx];
            r_idx++;
        
        } else {
            
            array[main_idx] = LeftArr[l_idx];
            l_idx++;
        }
        main_idx++;
    }

    while(l_idx < Lsize){
        array[main_idx] = LeftArr[l_idx];
        l_idx++;
        main_idx++;
    }

    while(r_idx < Rsize){
        array[main_idx] = RightArr[r_idx];
        r_idx++;
        main_idx++;
    }
}