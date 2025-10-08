const tableBody = document.getElementById("aviso_completo");
const modal = document.getElementById("row-modal");
const modalDetails = document.getElementById("modal-details");
const closeBtn = document.getElementById("close-modal");

const imageModal = document.getElementById("image-modal");
const largeImage = document.getElementById("large-image");
const closeImageBtn = document.getElementById("close-image-modal");

  for (let i = 0; i < tableBody.rows.length; i++) {
    const row = tableBody.rows[i];

    row.addEventListener("click", () => {
      const cells = row.cells; // HTMLCollection of td elements

      if (cells.length === 0) return;

      // Build HTML for modal
      modalDetails.innerHTML = `
        <p><strong>Fecha publicación:</strong> ${cells[0].innerText}</p>
        <p><strong>Fecha entrega:</strong> ${cells[1].innerText}</p>
        <p><strong>Comuna:</strong> ${cells[2].innerText}</p>
        <p><strong>Sector:</strong> ${cells[3].innerText}</p>
        <p><strong>Cantidad Tipo Edad:</strong> ${cells[4].innerText}</p>
        <p><strong>Nombre Contacto:</strong> ${cells[5].innerText}</p>
        <img id="modal-img" src="${cells[6].querySelector("img").src}" 
             alt="${cells[6].querySelector("img").alt}" style="cursor:pointer;">
      `;

      modal.style.display = "flex";
      const modalImg = document.getElementById("modal-img");
      modalImg.addEventListener("click", () => {
        largeImage.src = modalImg.src;
        largeImage.alt = modalImg.alt;
        imageModal.style.display = "flex";
       });

      
    });
  }

// Close row modal
closeBtn.addEventListener("click", () => {
    modal.style.display = "none";
});
//Close image modal
closeImageBtn.addEventListener("click", () => {
  imageModal.style.display = "none";
});



