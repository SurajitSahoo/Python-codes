#include<stdio.h>


void display(int arr[], int size) {
    printf("Array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}


int insertion(int arr[], int size, int element, int capacity, int index) {
    if (size >= capacity) {
        return -1; l
    }

    
    for (int i = size - 1; i >= index; i--) {
        arr[i + 1] = arr[i];
    }

    
    arr[index] = element;
    return 1;

int main() {
    int arr[100] = {1, 4, 6, 8, 9};
    int size = 5, element = 3, index = 2;

    display(arr, size); 
    insertion(arr, size, element, 100, index); 
    size += 1; 
    display(arr, size); 
    return 0;
}