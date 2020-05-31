
function selectionSort(arr){
  //swap function to remove the need for temp variable:
  const swap = (arr, idx1, idx2) =>
  ([arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]]);
  //array loop:
  for(let i = 0; i < arr.length; i++){
    let lowest = i;
    //positional loop:
    for(let j = i+1; j < arr.length; j++){
      if(arr[lowest] > arr[j]){
        lowest = j;
      }
    }
    if (i !== lowest){
		swap(arr, i, lowest)
	} else {
		return arr;
	}
  }  
}

