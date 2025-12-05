package examen.prueba.examen.models;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;


@Repository
public interface FotoRepository extends JpaRepository<Foto, Integer> {

    @Query("""
        SELECT new examen.prueba.examen.models.PhotoAvisoDto(
            f.id,
            f.rutaArchivo,
            f.nombreArchivo,
            a.email,
            c.nombre,
            a.fechaIngreso
        )
        FROM Foto f
        JOIN f.aviso a
        JOIN a.comuna c
        WHERE f.eliminada = false
        ORDER BY a.fechaIngreso DESC
    """)
    Page<PhotoAvisoDto> findAllPhotosWithAvisoInfoOrderByAvisoFechaDesc(Pageable pageable);
}
