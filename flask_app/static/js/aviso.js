const social_media = ["X", "Instagram", "Telegram", "Whatsapp", "Tiktok", "otra"]

const poblarSocialMedia = () => {
  let mediaSelect = document.getElementById("select-medio");
  for (const social of social_media) {
      let option = document.createElement("option");
      option.value = social;
      option.text = social;
      mediaSelect.appendChild(option);
  }
};

function addSocialUrlID() {
  const medioSelect = document.getElementById("select-medio");
  const idurlInput = document.getElementById("id_url_container");


  idurlInput.innerHTML = "";

  const selectedValues = Array.from(medioSelect.selectedOptions).map(opt => opt.value);

  selectedValues.forEach(value => {
    const label = document.createElement("label");
    label.innerText = `URL/ID para ${value}:`;
    label.setAttribute("for", `input-${value}`);

    const input = document.createElement("input");
    input.type = "text";
    input.id = `input-${value}`;
    input.name = `input-${value}`;
    input.minLength = 4;
    input.maxLength = 50;
    input.style.display = "block";
    input.style.marginBottom = "10px";

    idurlInput.appendChild(label);
    idurlInput.appendChild(input);
  });
}



const updateComunas = () => { 
  const regionSelect = document.getElementById('select-region');
  const comunaSelect = document.getElementById('select-comuna');


  if (!updateComunas.allComunas) {
    updateComunas.allComunas = Array.from(comunaSelect.options);
  }

  const allComunas = updateComunas.allComunas;
  const selectedRegion = regionSelect.value;

  comunaSelect.innerHTML = '<option value="">Seleccione una Comuna</option>';

 
  allComunas.forEach(opt => {
    if (opt.dataset.region === selectedRegion) {
      comunaSelect.appendChild(opt.cloneNode(true));
    }
  });
};

function formatDateTimeLocal(date) {
    const pad = (n) => String(n).padStart(2, '0');

    const year = date.getFullYear();
    const month = pad(date.getMonth() + 1); // months are 0-indexed
    const day = pad(date.getDate());
    const hours = pad(date.getHours());
    const minutes = pad(date.getMinutes());

    return `${year}-${month}-${day}T${hours}:${minutes}`;
  }

  /**
   * Prefill the datetime-local input with current time + 3 hours
   */
function llenarFechaEntrega() {
    const startInput = document.getElementById("fecha-entrega");
    if (!startInput) return;

    const now = new Date();
    now.setHours(now.getHours() + 3); // add 3 hours
    

    startInput.value = formatDateTimeLocal(now);
  }

document.getElementById("select-region").addEventListener("change", updateComunas);
document.getElementById("select-medio").addEventListener("change", addSocialUrlID);

window.onload = () => {
  poblarSocialMedia();
  updateComunas();
  llenarFechaEntrega();

};