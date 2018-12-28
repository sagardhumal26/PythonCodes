
def merge_list(left,right):
    result = []
    left_idx,right_idx=0,0
    while left_idx<len(left) and right_idx<len(right):
        if left[left_idx]<right[right_idx]:
            result.append(left[left_idx])
            left_idx+=1
        else:
            result.append(right[right_idx])
            right_idx+=1
            
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result
            

def mergeSort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    
    left=mergeSort(left)
    right=mergeSort(right)
    return merge_list(left,right)

def printList(arr):
    for item in arr:
        print(item,end=" ")
    print()

if  __name__=='__main__':
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr=mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
