function binarySearch(arr, n){
    let start = 0;
    var end = arr.length - 1;
    var middle = Math.floor((start + end) / 2);
    while(arr[middle] !== n && start <= end) {

        if(n < arr[middle]) end = middle - 1;
        else start = middle + 1;

        middle = Math.floor((start + end) / 2);

    }
    return arr[middle] === n ? middle : -1;
}
