//Es opcional

const validateSector = (sector) => {
  
  let lengthValid = sector.trim().length <= 100;
  
  return lengthValid;
}

const validatePhone = (phone) => {
  
  let lengthValid = phone.trim().length == 13;
  let re = /^\+569\.\d{8}$/;
  let formatValid = re.test(phone);
  
  return lengthValid && formatValid;
}




//obligatorio
const validateSelect = (select) => {
  if(!select) return false;
  return true
}

const validateName = (name) => {
  if(!name) return false;
  //let lengthValid = name.trim().length >= 3;
  
  return true;
}

const validateEmail = (email) => {
  if (!email) return false;
  let lengthValid = email.length < 100;

  // validamos el formato
  let re = /^[\w.]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
  let formatValid = re.test(email);

  // devolvemos la lógica AND de las validaciones.
  return lengthValid && formatValid;
};

const validateForm = () => {
  // obtener elementos del DOM usando el nombre del formulario.
  let myForm = document.forms["myForm"];
  let department = myForm["select-region"].value;
  let comuna = myForm["select-comuna"].value;
  let sector = myForm["sector"].value;
  let nombre = myForm["nombre"].value;
  let email  = myForm["email"].value;
  let phone  = myForm["phone"].value;
  let pet  = myForm["select-mascota"].value;
  let time  = myForm["select-edad"].value;


  // variables auxiliares de validación y función.
  let invalidInputs = [];
  let isValid = true;
  const setInvalidInput = (inputName) => {
    invalidInputs.push(inputName);
    isValid &&= false;
  };

  // lógica de validación
  if (!validateSelect(department)) {
    setInvalidInput("Region");
  }
  if (!validateSelect(comuna)) {
    setInvalidInput("Comuna");
  }
  if (!validateSector(sector)) {
    setInvalidInput("Sector");
  }
   if (!validateName(nombre)) {
    setInvalidInput("Nombre");
  }

  if (!validateEmail(email)) {
    setInvalidInput("Email");
  }
  if (!validatePhone(phone)) {
    setInvalidInput("Número de Celular");
  }
  if (!validateSelect(pet)) {
    setInvalidInput("Tipo");
  }
  if (!validateSelect(time)) {
    setInvalidInput("Unidad medidad edad");
  }




  // finalmente mostrar la validación
  let validationBox = document.getElementById("val-box");
  let validationMessageElem = document.getElementById("val-msg");
  let validationListElem = document.getElementById("val-list");
  let formContainer = document.querySelector(".main-container");

  if (!isValid) {
    validationListElem.textContent = "";
    // agregar elementos inválidos al elemento val-list.
    for (input of invalidInputs) {
      let listElement = document.createElement("li");
      listElement.innerText = input;
      validationListElem.append(listElement);
    }
    // establecer val-msg
    validationMessageElem.innerText = "Los siguientes campos son inválidos:";

    // aplicar estilos de error
    validationBox.style.backgroundColor = "#ffdddd";
    validationBox.style.borderLeftColor = "#f44336";

    // hacer visible el mensaje de validación
    validationBox.hidden = false;
  } else {
    // Ocultar el formulario
    myForm.style.display = "none";

    // establecer mensaje de éxito
    validationMessageElem.innerText = "¿Está seguro que desea agregar este aviso de adopción?";
    validationListElem.textContent = "";

    // aplicar estilos de éxito
    validationBox.style.backgroundColor = "#ddffdd";
    validationBox.style.borderLeftColor = "#4CAF50";

    // Agregar botones para enviar el formulario o volver
    let submitButton = document.createElement("button");
    submitButton.innerText = "Sí, estoy seguro";
    submitButton.style.marginRight = "10px";
    submitButton.addEventListener("click", () => {
      // myForm.submit();
      // no tenemos un backend al cual enviarle los datos
      let homeButton = document.getElementById("home-btn");
      validationMessageElem.innerText = "Hemos recibido la información de adopción, muchas gracias y suerte";
      validationListElem.textContent = "";
      homeButton.hidden=false;
      
    });

    let backButton = document.createElement("button");
    backButton.innerText = "No, no estoy seguro, quiero volver al formular";
    backButton.addEventListener("click", () => {
      // Mostrar el formulario nuevamente
      myForm.style.display = "block";
      validationBox.hidden = true;
    });

    validationListElem.appendChild(submitButton);
    validationListElem.appendChild(backButton);

    // hacer visible el mensaje de validación
    validationBox.hidden = false;
  }
};


let submitBtn = document.getElementById("submit-btn");
submitBtn.addEventListener("click", validateForm);
