#include<iostream>
int main()
{
    int arr[5]={5,4,3,2,1};
    int n=5; //number of elements
    //insertion sort code
    int i,j,temp;
    for(int i=1;i<n;i++)
    {
        j=i-1;//decrement to point value so that to compare
        temp=arr[i];
        while(j>=0 && arr[j]>temp)//until j has not reached array end and  also every value at  j is greater than temp 
        {
            arr[j+1]=arr[j];
            j--;
        }
        arr[j+1]=temp;//as j is decremented to check therefore incrementing it to place in appropriate position
    }
    for(i=0;i<n;i++)
    std::cout<<arr[i]<<std::endl;
    return 0;
}