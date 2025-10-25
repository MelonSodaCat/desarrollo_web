const tableBody = document.getElementById("aviso_completo");
const modal = document.getElementById("row-modal");
const modalDetails = document.getElementById("modal-details");
const closeBtn = document.getElementById("close-modal");



const imageModal = document.getElementById("image-modal");
const largeImage = document.getElementById("large-image");
const closeImageBtn = document.getElementById("close-image-modal");


async function fetchComentarios(avisoId) {
    try {

    const response = await fetch("http://127.0.0.1:5000/get-comments?avisoId="  + avisoId);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    data = await response.json();

    return data;
   
  } catch (error) {
    console.error("There has been a problem with your fetch operation:", error);
    throw error;
  }
} 

for (let i = 0; i < tableBody.rows.length; i++) {
    const row = tableBody.rows[i];

    row.addEventListener("click", async () => {
        const cells = row.cells;

        if (cells.length === 0) return;
        //datos del modal
        modalDetails.innerHTML = `
            <p><strong>Fecha publicación:</strong> ${cells[0].innerText}</p>
            <p><strong>Fecha entrega:</strong> ${cells[1].innerText}</p>
            <p><strong>Comuna:</strong> ${cells[2].innerText}</p>
            <p><strong>Sector:</strong> ${cells[3].innerText}</p>
            <p><strong>Cantidad Tipo Edad:</strong> ${cells[4].innerText}</p>
            <p><strong>Nombre Contacto:</strong> ${cells[5].innerText}</p>
            <p><strong>Email:</strong> ${row.dataset.email}</p>
            <p><strong>Celular:</strong> ${row.dataset.celular}</p>
            <p><strong>Descripción:</strong> ${row.dataset.descripcion}</p>
            <img id="modal-img" src="${cells[6].querySelector("img").src}" 
                 alt="${cells[6].querySelector("img").alt}" style="cursor:pointer;">
        `;

        const redesTd = cells[7]; //escondido
        const redesRaw = redesTd ? redesTd.innerText : "";
        const redesArray = redesRaw.split("|").filter(s => s); 

        redesArray.forEach(item => {
          
          const [red_social, usuario] = item.split(":");
          if (red_social && usuario){
          modalDetails.innerHTML += `<p><strong>${red_social}:</strong> ${usuario}</p>`;
          }
          });
        
        try {
            const avisoId = row.dataset.id;
            const comments = await fetchComentarios(avisoId);
            modalDetails.innerHTML+=`<p id="title" class="comment-title"><strong>Comentarios</strong></p>`
            

            if (comments.length > 0) {
                comments.forEach(c => {
                    modalDetails.innerHTML += `<p><strong>${c.nombre}</strong> <em>(${c.fecha})</em>: ${c.comentario}</p>`;
                });
            } else {
                modalDetails.innerHTML = "<p>No hay comentarios para este aviso.</p>"; 

            }
            } catch(error) {
                modalDetails.innerHTML = "<p>Error al cargar los comentarios.</p>";
            }


     

        modal.style.display = "flex";

        const modalImg = document.getElementById("modal-img");
        modalImg.addEventListener("click", () => {
            largeImage.src = modalImg.src;
            largeImage.alt = modalImg.alt;
            imageModal.style.display = "flex";
        });
    });
}


closeBtn.addEventListener("click", () => {
    modal.style.display = "none";
});


closeImageBtn.addEventListener("click", () => {
    imageModal.style.display = "none";
    
});

modal.onclick = (event) => {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}