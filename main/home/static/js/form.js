console.log("Hello World!!")
// Form Validation  
    //First Name

const firstName = document.getElementById("firstName")
const mobile = document.getElementById("mobile")
const age = document.getElementById("age")
const weight = document.getElementById("weight")
const height = document.getElementById("height")
const city = document.getElementById("city")

let validName = false;
let validNumber = false;
let validAge = false;
let validWeight = false;
let validHeight = false;
let validCity = false;

// function printerror(id){
//     error = document.getElementById(id)
//     error.innerHTML = "Please re-check"
// }
                                //Validation for Name
firstName.addEventListener('blur', function(){
    console.log("Name is blurred")
    let exp = /^[a-zA-Z]+$/
    const str = firstName.value;
    console.log(exp, str)
    if(exp.test(str)){
        console.log("Name is valid")
        let success = document.getElementById("name-alert");
        firstName.classList.remove("is-invalid")
        firstName.classList.add("is-valid")
        success.innerHTML = "That looks Good!!"
        success.style.color = 'green';
        validName = true;
    }
    else{
        console.log("It's in-valid")
        firstName.classList.add("is-invalid")
        let error = document.getElementById("name-alert")
        error.innerHTML = "Please Enter a valid name!"
        error.style.color = 'red';
        validName = false;
    }
})

                                        //Validaion for Mobile Number
mobile.addEventListener('blur', function(){
    console.log("Mobile Number is blurred")
    let exp = /^[0-9]{10}$/
    const str = mobile.value;
    console.log(str, exp);

    if(exp.test(str)){
        console.log("Mobile No. is valid")
        mobile.classList.remove("is-invalid")
        mobile.classList.add("is-valid")
        let success = document.getElementById("mobile-alert")
        success.innerHTML = "That's look Good!!"
        success.style.color = 'green';
        validNumber = true;
    }
    else{
        console.log("Mobile no. is invalid")
        mobile.classList.add("is-invalid")
        let error = document.getElementById("mobile-alert");
        error.style.color = 'red';
        error.innerHTML = "Please Enter a Valid Mobile Number!"
        validNumber = false;
    }
})

                                            // Validation for Age
age.addEventListener('blur', function(){
    console.log("age is Blurred")
    let exp = /^[0-9]+$/
    const str = age.value;
    console.log(str)
    if(exp.test(str)){
        console.log("Age is Valid")
        if(str < 17){
            console.log("You are not eligible")
            // let success = document.getElementById("age-alert");
            // success.style.color = 'red'
            // success.innerHTML = "You are not Eligible!"
            age.classList.add("is-invalid")
            validAge = false;
        }
        else{
            console.log("You're eligible.")
            // let success = document.getElementById("age-alert")
            // success.style.color = 'green';
            // success.innerHTML = "Good!! :)"
            age.classList.remove("is-invalid")
            age.classList.add("is-valid")
            validAge = true;
        }
    }
    else{
        console.log("Age is invalid.")
        let error = document.getElementById('age-alert')
        // error.style.color = 'red'
        // error.innerHTML = "Please Enter a Valid Age";
        age.classList.add("is-invalid")
        validAge = false;
    }

})

// Validate Weight
weight.addEventListener('blur', function(){
    console.log("Weight Blurred!")
    let exp = /[0-9]+$/
    const str = weight.value;
    console.log(str)

    if(exp.test(str)){
        console.log("Valid Weight")
        weight.classList.remove("is-invalid")
        weight.classList.add("is-valid")
        // let success = document.getElementById("weight-alert");
        // weight.innerHTML = "Good!"
        validWeight = true;
    }
    else{
        console.log("Invalid Weight")
        weight.classList.add("is-invalid")
        //let failure = document.getElementById("weigth-alert")
        //failure.innerHTML = "Enter a valid weigth"
        //failure.style.color = 'red'
        validWeight = false;
    }
})

// Validate Weight
height.addEventListener('blur', function(){
    console.log("Height Blurred!")
    let exp = /[0-9]+$/
    const str = height.value;
    console.log(str)

    if(exp.test(str)){
        console.log("Valid Height")
        height.classList.remove("is-invalid")
        height.classList.add("is-valid")
        validHeight = true;

    }
    else{
        console.log("Invalid Height")
        height.classList.add("is-invalid")
        let failure = document.getElementById("height-alert")
        failure.innerHTML = "Enter a valid height"
        failure.style.color = 'red'
        validHeight = false;
    }
})

city.addEventListener('blur', function(){
    console.log("City is blurred")
    let exp = /^[a-zA-Z]+$/
    const str = city.value;
    if(exp.test(str)){
        console.log("Valid City")
        city.classList.add("is-valid")
        city.classList.remove("is-invalid")
        validCity = true;
    }
    else{
        console.log("Invalid City")
        city.classList.add("is-invalid")
        validCity = false;
    }
})



const inpFile = document.getElementById("inpFile");
const previewContainer = document.getElementById("image-preview")
const previewImage = previewContainer.querySelector(".image-preview__image");
const previewDefaultText = previewContainer.querySelector("image-preview__default-text");

let validFile = false;

inpFile.addEventListener("change", function() {
    const file = this.files[0];
    console.log(file);

    console.log(file.name)

    pic = document.getElementById("image-preview__default-text")
    pic.innerHTML = "You have uploaded " + file.name
    // const reader = new FileReader();

    // previewDefaultText.style.display = "none";
    // previewImage.style.display = "block";

    // reader.addEventListener("load", function(){
    //     previewImage.setAttribute("src", this.result);
    // })

    // console.log(this)
    
    // reader.readAsDataURL(file);
    if(file.name != null){
        validFile = true;
    }
    else{
        validFile = false;
    }
    console.log(validFile)
})










// BUTTON
button = document.getElementById('button')
button.addEventListener('click', function(e){
    e.preventDefault();
    console.log("submt button is pressed")
    if(validCity && validName && validNumber && validWeight && validHeight && validAge && validFile){
        console.log("The form is ready to submit")
        success = document.getElementById("alert-success")
        success.innerHTML = "<strong>Well Done!</strong> You have successfully submitted the form."
        success.classList.add("alert-success")
        success.classList.remove("alert-danger")
        success.classList.add("show")

        body = document.getElementById("body")
        body.style.background = "lightgreen";
        
        //body.style.background = "rgb(100, 248, 132)";

        title = document.getElementById("title")
        title.style.color = 'white';
    }
    else{
        console.log("Please re-check")
        console.log(validName, validAge, validHeight, validHeight, validNumber, validFile, validCity)
        failure = document.getElementById("alert-success")
        failure.classList.add("show")
        failure.innerHTML = "<strong>Invalid Form!</strong> Please re-check the form."
        failure.classList.add("alert-danger")
        failure.classList.remove("alert-success")

        body = document.getElementById("body")
        body.style.background = "rgb(255, 171, 163)";

        title = document.getElementById("title")
        title.style.color = 'white';
    }
})




