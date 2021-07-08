function partition(arr) {
    let pivot = arr[0];
    let leftItems = 0;

    for(let i = 0; i < arr.length; i++) {
        console.log("i", i);
        console.log("arr[i]", arr[i]);
        console.log("leftItems", leftItems);
        console.log("in front of left", arr[leftItems + 1]);
        if(arr[i] > pivot) {
            continue;
        } else {
            if(leftItems < i) {
                let tmp = arr[leftItems + 1];
                arr[leftItems + 1] = arr[i];
                arr[i] = tmp;
                leftItems++;
            } else {
                leftItems++
            }
        }
    }

    let tmp = pivot;
    arr[0] = arr[leftItems];
    arr[leftItems] = tmp;

    return arr;
}
x = [6, 4, 2, 3, 9, 8, 9, 4, 7, 6, 1]
console.log(partition(x));