package examen.prueba.examen.models;

import java.time.LocalDateTime;

public class PhotoAvisoDto {

    private Integer fotoId;
    private String rutaArchivo;
    private String nombreArchivo;
    private String email;
    private String comunaNombre;
    private LocalDateTime fechaIngreso;

    public PhotoAvisoDto(Integer fotoId, String rutaArchivo, String nombreArchivo,
                         String email, String comunaNombre,
                         LocalDateTime fechaIngreso) {
        this.fotoId = fotoId;
        this.rutaArchivo = rutaArchivo;
        this.nombreArchivo = nombreArchivo;
        this.email = email;
        this.comunaNombre = comunaNombre;
        this.fechaIngreso = fechaIngreso;
    }

    public Integer getFotoId() { return fotoId; }
    public String getRutaArchivo() { return rutaArchivo; }
    public String getNombreArchivo() { return nombreArchivo; }
    public String getEmail() { return email; }
    public String getComunaNombre() { return comunaNombre; }
    public LocalDateTime getFechaIngreso() { return fechaIngreso; }
    
}
