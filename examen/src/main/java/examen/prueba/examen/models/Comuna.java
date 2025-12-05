package examen.prueba.examen.models;

import java.util.Set;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

@Entity
@Table(name = "comuna", schema = "tarea2")
public class Comuna {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @NotNull
    @Size(max = 200)
    private String nombre;

    @ManyToOne
    private Region region; 

    @OneToMany(mappedBy = "comuna")
    private Set<Aviso> avisos;

     public Integer getId() {
        return id;
    }
    public String getNombre() {
        return nombre;
    }
    public Region getRegion() {
        return region;
    }
    
}
