package examen.prueba.examen.models;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;



@Entity
@Table(name = "foto", schema = "tarea2")
public class Foto {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @NotNull
    @Size(max = 300)
    private String rutaArchivo;

    @NotNull
    @Size(max = 300)
    private String nombreArchivo;

    @NotNull
    private boolean eliminada = false;

    @NotNull
    @ManyToOne
    private Aviso aviso;

    public Integer getId() {
        return id;
    }
    public String getRutaArchivo() {
        return rutaArchivo;
    }

    public String getNombreArchivo() {
        return nombreArchivo;
    }

    public Boolean getEliminada() {
        return eliminada;
    }

    public void setEliminada(boolean eliminada) {
        this.eliminada = eliminada;
    }

    public Aviso getAviso() {
        return aviso;
    }
}
