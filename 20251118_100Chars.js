** start of script.js **

function oneHundred(chars) {
  let finalChar = "";

  while (finalChar.length < 100) {
    finalChar += chars;
  }    
  
  finalChar = finalChar.slice(0, 100);

  console.log(finalChar)
  return finalChar;
}

oneHundred("One hundred ")

** end of script.js **

