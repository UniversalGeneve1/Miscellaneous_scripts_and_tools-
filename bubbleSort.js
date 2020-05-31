function bubbleSort(arr){
  let noSwaps;//to avoid relooping on the sorted array
  for(let i = arr.length; i > 0; i--){ //defines array length
    noSwaps = true; 
    for(let j = 0; j < i - 1; j++){ //defines position of comparison
      if(arr[j] > arr[j+1]){
        //SWAP
        let temp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = temp;
        noSwaps = false;
      }
    }
    if(noSwaps) break;
  }
  return arr;
} 