// PYRAMID PROBLEM:
// ITERATIVE:

function pyramid(n){
  // calculate midpoint
  // midpoint is Math.floor(((2*n)-1)/2)
  const midpoint = Math.floor (((2 * n) - 1) / 2);
  
  //for each row
  for(let row=0; row < n; row++){
    var level = ''; //make empty string

    //for each column in row:
    for(let column=0; column < (2*n)-1; column++){
      //the column relation to n is (2*n)-1
      if(midpoint-row <= column && midpoint+row >= column){
        level += "#";
      } else {
        level += " ";
      }
    }

    console.log(level);    
  }
}
