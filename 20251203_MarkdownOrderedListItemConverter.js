** start of script.js **

function convertListItem(markdown) {
  markdown = markdown.trim();

  // Create function to check for digit
  function isDigit(char) {
    return /\d/.test(char)
  };

  //Check for number eligibility
  if (!isDigit(markdown[0])) {
    console.log("Invalid format")
    return("Invalid format")
  } else if (markdown[1] !== ".") {
    console.log("Invalid format")
    return("Invalid format")
  };

  // Strip the first two then clean
  markdown = `<li>${markdown.slice(2).trim()}</li>`;

  console.log(markdown);
  return(markdown)
}

convertListItem("1. My item")
convertListItem(" 1.  Another item")
convertListItem("1 . invalid item")
convertListItem("2. list item text")
convertListItem(". invalid again")
convertListItem("A. last invalid")



** end of script.js **

