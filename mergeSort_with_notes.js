// Merges two already sorted arrays
function merge(arr1, arr2){
    let results = [];
    let i = 0;
    let j = 0;
    while(i < arr1.length && j < arr2.length){ // while we're not at the end of both arrays, perform comparisons.
        if(arr2[j] > arr1[i]){
            results.push(arr1[i]);
            i++;
        } else {
            results.push(arr2[j])
            j++;
        }
    }
    while(i < arr1.length) {                  // these are for cases when one array is exhausted already.
        results.push(arr1[i])
        i++;
    }
    while(j < arr2.length) {
        results.push(arr2[j])
        j++;
    }
    return results;
}

//MERGE SORT:
function mergeSort(arr) {
  if(arr.length <=1) return arr;             // base case for recursion
  let mid = Math.floor(arr.length/2);
  let left = mergeSort(arr.slice(0,mid));
  let right = mergeSort(arr.slice(mid));
  return merge(left, right); 
}


/*NOTES ON MERGESORT:
- mergeSort, in our case consists of two functions.
- the `merge` function is exclusively responsible for the sorting of the array
- the `mergeSort` function is responsible for the "orientating" of the elements to be handled by merge, 
  as well as the strategic invoking of merge.
*/

//TEST:
//merge([100,200], [1,2,3,5,6])


                   