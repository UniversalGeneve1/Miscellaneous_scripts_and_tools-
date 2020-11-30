// PYRAMID PROBLEM:
// ITERATIVE:

function pyramid_iter(n){
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

//RECURSIVE:
// A prime example that recursion doesn't always mean better or simpler.
function pyramid_recr(n, row=0, level='') {
  //base case: stop when we've completed n number rows
  if(row===n) {
    return;
  }
  /*if length of string is same as num cols, print out
    and begin recursing on next row */
  if(level.length===((2 * n) - 1)) {
    console.log(level);
    return pyramid_recr(n, row+1)
  }
  //the main functional part
  const midpoint = Math.floor (((2 * n) - 1) / 2);
  //this will hold the character needed to be added to level:
  let char_to_add;
  //
  if(midpoint - row <= level.length && midpoint + row >= level.length) {
    char_to_add = '#';
  } else {
    char_to_add = ' ';
  }
  // move on to next column. this is why we check with level.length
  pyramid_recr(n, row, level + char_to_add)
}
