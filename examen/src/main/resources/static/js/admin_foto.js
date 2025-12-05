document.querySelectorAll('.delete-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.getElementById('fotoIdInput').value = btn.dataset.id;
        document.getElementById('deleteModal').style.display = 'block';
    });
    });
    document.getElementById('cancelDelete').addEventListener('click', () => {
    document.getElementById('deleteModal').style.display = 'none';
    });

document.getElementById("deleteForm").addEventListener("submit", function (e) {
    const motivo = document.getElementById("motivoInput").value.trim();
    const errorDiv = document.getElementById("motivoError");

    if (motivo.length < 5 || motivo.length > 200) {
        e.preventDefault(); // Detiene el envío del formulario
        errorDiv.textContent = "El motivo debe tener entre 5 y 200 caracteres.";
        errorDiv.style.display = "block";
    } else {
        errorDiv.style.display = "none"; // Oculta mensaje si está correcto
    }
});
