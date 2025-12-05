package examen.prueba.examen.models;

import java.time.LocalDateTime;
import java.util.Set;

import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToMany;
import jakarta.persistence.SequenceGenerator;
import jakarta.persistence.Table;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

@Entity
@Table(name = "aviso_adopcion", schema = "tarea2")
public class Aviso {
    @Id
    @SequenceGenerator(
        name = "aviso_sequence",
        sequenceName = "aviso_sequence",
        allocationSize = 1
    )
    @GeneratedValue(
        strategy = GenerationType.SEQUENCE,
        generator = "aviso_sequence"
    )
    private Integer id;

    @NotNull
    private LocalDateTime fechaIngreso;

    @Size(max = 100)
    private String sector;

    @NotNull
    @Size(max = 200)
    private String nombre;

    @NotNull
    @Size(max = 100)
    private String email;

    @Size(max = 15)
    private String celular;

    @NotNull
    @Enumerated(EnumType.STRING)
    private Tipo tipo;

    @NotNull
    private Integer cantidad;

    @NotNull
    private Integer edad;

    
    @NotNull
    @Enumerated(EnumType.STRING)
    private UnidadMedida unidadMedida;

    @NotNull
    private LocalDateTime fechaEntrega;

    @Size(max = 500)
    private String descripcion;

    @ManyToOne
    @NotNull
    private Comuna comuna; 

    @OneToMany(mappedBy = "aviso")
    private Set<Foto> fotos;

    public Aviso() {
    }

    public Aviso(LocalDateTime fechaIngreso, 
                    Comuna comuna,
                    String sector,
                    String nombre,
                    String email,
                    String celular,
                    Tipo tipo,
                    Integer cantidad,
                    Integer edad,
                    UnidadMedida unidadMedida,
                    LocalDateTime fechaEntrega,
                    String descripcion
                ) {

        this.fechaIngreso = fechaIngreso;
        this.comuna = comuna;
        this.sector = sector;
        this.nombre = nombre;
        this.email = email;
        this.celular = celular;
        this.tipo = tipo;
        this.cantidad = cantidad;
        this.edad = edad;
        this.fechaEntrega = fechaEntrega;
        this.unidadMedida = unidadMedida;
        this.descripcion = descripcion;
    }

    public Integer getId() {
        return id;
    }

    public String getEmail() {
        return email;
    }

    public Comuna getComuna() {
        return comuna;
    }

    public LocalDateTime getFechaIngreso() {
        return fechaIngreso;
    }

    public String getSector() {
        return sector;
    }
    public String getNombre() {
        return nombre;
    }
    public String getCelular() {
        return celular;
    }
    public Tipo getTipo() {
        return tipo;
    }
    public Integer getCantidad() {
        return cantidad;
    }
    public Integer getEdad() {
        return edad;
    }
    public UnidadMedida getUnidadMedida() {
        return unidadMedida;
    }
    public LocalDateTime getFechaEntrega() {
        return fechaEntrega;
    }
    public String getDescripcion() {
        return descripcion;
    }

    public Set<Foto> getFotos() {
    return fotos;
}



}