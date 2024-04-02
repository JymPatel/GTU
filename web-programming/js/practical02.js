function validateForm() {
  // Get form elements
  let checkboxChecked = document.getElementById("checkboxInput").checked;
  let dateValue = document.getElementById("dateInput").value;
  let emailValue = document.getElementById("emailInput").value;
  let passwordValue = document.getElementById("passwordInput").value;
  let radioOption1Checked = document.getElementById("radioOption1").checked;
  let radioOption2Checked = document.getElementById("radioOption2").checked;
  let fileValue = document.getElementById("fileInput").value;

  let emailRegex = /^[a-zA-Z0-9+._]+@[0-9a-zA-Z]+\.[a-zA-Z]{2,3}$/;

  // Perform validation checks

  if (dateValue === "") {
    alert("Please select a date");
    return false;
  }

  console.log(1);
  if (!emailRegex.test(emailValue)) {
    alert("Please enter a valid email");
    return false;
  }
  console.log(1);

  if (passwordValue.length < 8) {
    alert("Minimum 8 characters are required in Password");
    return false;
  }
  console.log(1);

  if (!radioOption1Checked && !radioOption2Checked) {
    alert("Please select a radio option");
    return false;
  }
  console.log(1);

  if (fileValue === "") {
    alert("Please select a file");
    return false;
  }
  console.log(1);

  if (!checkboxChecked) {
    alert("Please accept Terms and Conditions to continue");
    return false;
  }
  console.log(1);

  // If all checks pass, form submission is valid
  if (confirm("Continue with: " + emailValue + ", " + passwordValue)) {
    alert(emailValue, passwordValue);
  } else {
    alert("Submission rejected by user!");
  }
  console.log(1);

  return true;
}
