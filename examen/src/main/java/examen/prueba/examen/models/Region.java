package examen.prueba.examen.models;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;
import java.util.Set;

@Entity
@Table(name = "region", schema = "tarea2")
public class Region {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @NotNull
    @Size(max = 200)
    private String nombre;

    @OneToMany(mappedBy = "region")
    private Set<Comuna> comunas;

    public Integer getId() {
        return id;
    }
    public String getNombre() {
        return nombre;
    }

    public Set<Comuna> getComunas() {
        return comunas;
    }
}
