package examen.prueba.examen.services;

import java.io.IOException;

import java.nio.file.Path;
import java.nio.file.Paths;

import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Map;


import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;
import org.springframework.util.ResourceUtils;

import org.springframework.data.domain.Page;

import examen.prueba.examen.models.Aviso;
import examen.prueba.examen.models.AvisoRepository;
import examen.prueba.examen.models.Foto;
import examen.prueba.examen.models.Log;
import examen.prueba.examen.models.FotoRepository;
import examen.prueba.examen.models.LogRepository;


@Service
public class AppService {

    private final FotoRepository fotoRepo;
    private final LogRepository logRepo;
    private final AvisoRepository avisoRepo;
    private final String pathStatic;

    public AppService(FotoRepository fotoRepo, LogRepository logRepo, AvisoRepository avisoRepo)  throws IOException {
        this.fotoRepo = fotoRepo;
        this.logRepo = logRepo;
        this.avisoRepo = avisoRepo;

        Path staticDir = Paths.get(ResourceUtils.getFile("classpath:static").getAbsolutePath());
        this.pathStatic = staticDir.toString();
        System.out.println("Static path resolved to: " + this.pathStatic);
    }

  

    public Page<Map<String, Object>> getAvisosData(int page, int size) {
    Page<Aviso> avisosPage = avisoRepo.findAllByOrderByFechaIngresoDesc(PageRequest.of(page, size));

    return avisosPage.map(aviso -> {
        Map<String,Object> m = new HashMap<>();
        m.put("id", aviso.getId());
        m.put("fecha_publicacion", aviso.getFechaIngreso());
        m.put("comuna", aviso.getComuna() != null ? aviso.getComuna().getNombre() : null);
        m.put("sector", aviso.getSector());
        m.put("cantidad", aviso.getCantidad());
        m.put("tipo", aviso.getTipo());
        m.put("edad", aviso.getEdad());
        m.put("unidad_medida", aviso.getUnidadMedida());
        if (aviso.getFotos() != null && !aviso.getFotos().isEmpty()) {
            Foto f = aviso.getFotos().iterator().next();
            m.put("foto_path", f.getRutaArchivo());
            m.put("foto_nombre", f.getNombreArchivo());
        }
        return m;
    });

}

 public Page<Map<String, Object>> getFotoData(int page, int size) {
        var fotosPage = fotoRepo.findAllPhotosWithAvisoInfoOrderByAvisoFechaDesc(PageRequest.of(page, size));

        return fotosPage.map(foto -> {
            Map<String, Object> m = new HashMap<>();
            m.put("foto_id", foto.getFotoId().toString());
            m.put("ruta_archivo", foto.getRutaArchivo());
            m.put("nombre_archivo", foto.getNombreArchivo());
            m.put("aviso_email", foto.getEmail());
            m.put("aviso_comuna", foto.getComunaNombre());
            m.put("fecha_ingreso", foto.getFechaIngreso());
            return m;
        });
    }

    public Page<Map<String, Object>> getLogsData(int page, int size) {
        var logsPage = logRepo.findAllByOrderByFechaDesc(PageRequest.of(page, size));

        return logsPage.map(log -> {
            Map<String, Object> m = new HashMap<>();
            m.put("log_id", log.getId().toString());
            m.put("mensaje", log.getMensaje());
            m.put("fecha", log.getFecha());
            return m;
        });
    }




    public void deleteFoto(Integer fotoId, String motivo) {
        //validate motivo
        if (motivo == null || motivo.trim().length() < 5 || motivo.trim().length() > 200) {
        throw new IllegalArgumentException("El motivo debe tener entre 5 y 200 caracteres.");
    }

        Foto f = fotoRepo.findById(fotoId)
        .orElseThrow(() -> new RuntimeException("Foto no encontrada: " + fotoId));
        f.setEliminada(true);
        fotoRepo.save(f);
        if(Log.validateLog(motivo)){
        Log log = new Log(LocalDateTime.now(), "eliminado foto " + fotoId + " por usuario admin, motivo: " + motivo);
        logRepo.save(log);
        } else {
            throw new IllegalArgumentException("Motivo validation failed.");
        }
        
    }


    
    
}
