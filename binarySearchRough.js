function binarySearch(arr, n){
  let start = 0;
  let end = arr.length -1;
  let mid = Math.floor((start + end)/2);

  while(arr[mid] !== n && start <= end){
    if(arr[mid] < n){
      start = mid + 1;
    } else if(arr[mid] > n){
      end = mid - 1;
    };

    mid = Math.floor((start + end)/2);
  }

  if(arr[mid] == n){
    return mid;
  }

  return -1;
}