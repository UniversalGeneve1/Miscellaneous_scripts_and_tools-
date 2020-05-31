function fizzBuzz(n, fz = 3, bz = 5){
  
  for(let i = 1; i <= n; i++){

    let result = '';
    let counter = 0;

    if(i % 3 === 0){
      counter += 1;
      result = result + 'Fizz';
    };

    if(i % 5 === 0){
      counter += 1;
      result = result + 'Buzz';
    }

    if(counter === 0){
      result = i;
    }

    console.log(result);

  };

};

