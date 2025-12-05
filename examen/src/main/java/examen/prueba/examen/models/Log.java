package examen.prueba.examen.models;


import java.time.LocalDateTime;



import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

@Entity
@Table(name = "log", schema = "tarea2")
public class Log {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @NotNull
    private LocalDateTime fecha;

    @NotNull
    @Size(max = 300)
    private String mensaje;


    public Integer getId() {
        return id;
    }

    public LocalDateTime getFecha() {
        return fecha;
    }
    
    public String getMensaje() {
        return mensaje;
    }

    public Log() {
    }

    public Log(LocalDateTime fecha, String mensaje) {
        this.fecha = fecha;
        this.mensaje = mensaje;
    }

     public static Boolean validateLog(String mensaje) {
    if (mensaje == null) return false;

    String trimmed = mensaje.trim();

    // requerido: no vacío después de trim y longitud máxima 300 (coincide con @Size)
    if (trimmed.isEmpty() || trimmed.length() > 300) return false;

    // rechaza caracteres de control no deseados (permitimos tab, CR, LF)
    if (trimmed.matches(".*[\\x00-\\x08\\x0B\\x0C\\x0E-\\x1F\\x7F].*")) return false;

    // opcional: prevenir inyección de HTML/script en logs (si quieres bloquear etiquetas HTML)
    if (trimmed.matches(".*<[^>]+>.*")) return false;

    // Si necesitas más reglas (profanidad, URLs, etc.) las agregas aquí.
    return true;
    }


}
