const form = document.querySelector("#loginForm");

async function login() {
  // Associate the FormData object with the form element
  const formData = new FormData(form);

  try {
    const response = await fetch("/login", {
      method: "POST",
      // Set the FormData instance as the request body
      body: formData,
    });

    let status = await response.status

    if (status === 200){
        window.location.replace("/");
    }

    else if (status === 401){
        $("#loginAlert").removeClass("d-none")
        $("#loginAlert").addClass("alert-danger")
        $("#loginAlert").html("You must have an Administrator profile to log in")
        $("input[name='password']")[0].value = '';
        $("input[name='username']")[0].value = '';   
    }

    else{
        $("#loginAlert").removeClass("d-none")
        $("#loginAlert").addClass("alert-danger")
        $("#loginAlert").html("Wrong username or password")
        $("input[name='password']")[0].value = '';     
    }

    console.log(await response.status);
  } catch (e) {
    console.error(e);
  }
}

// Take over form submission
form.addEventListener("submit", (event) => {
  event.preventDefault();
  login();
});