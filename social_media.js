const social_media = ["X", "Instagram", "Telegram", "Whatsapp", "Tiktok"]
const pets = ["Gato", "Perro"]
const time = ["Meses", "Años"]

const poblarRegiones = () => {
  let regionSelect = document.getElementById("select-region");
  region_comuna.regiones.forEach(region => {
      let option = document.createElement("option");
      option.value = region.numero;
      option.textContent = region.nombre;
      regionSelect.appendChild(option);
    });
};

const updateComunas = () => {
  let regionSelect = document.getElementById("select-region");
  let comunaSelect = document.getElementById("select-comuna");
  let selectedRegion = regionSelect.value;

  
  comunaSelect.innerHTML = '<option value="">Seleccione una comuna</option>';
  
  if (!selectedRegion) return; // si no eligieron nada, se queda vacío

  const region = region_comuna.regiones.find(r => r.numero == selectedRegion);
  if (region) {
      region.comunas.forEach(comuna => {
        let option = document.createElement("option");
        option.value = comuna.id;
        option.textContent = comuna.nombre;
        comunaSelect.appendChild(option);
      });
    }
};

document.getElementById("select-region").addEventListener("change", updateComunas);


window.onload = () => {
  poblarRegiones();
  updateComunas();

};