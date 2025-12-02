** start of script.js **

function toSnake(camel) {
  let newString = "";

  // Need to write the logic for upper checks first
  function isUpper(char) {
    // Return True only if the character is not its lowercase ver and also is their uppercase ver (to prevent digits)
    return char !== char.toLowerCase() && char === char.toUpperCase();
  };


  for (let i = 0; i < camel.length; i ++) {
    if (isUpper(camel[i])) {
      newString += `_${camel[i].toLowerCase()}`
    } else {
      newString += camel[i]
    }
  };

  console.log(newString);
  return newString;
}

toSnake("helloWorld")
toSnake("myVariableName")

** end of script.js **

