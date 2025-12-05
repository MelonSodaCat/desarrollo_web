package examen.prueba.examen.controllers;


import java.util.Map;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.data.domain.Page;


import examen.prueba.examen.services.AppService;

@Controller
public class AppController {
    private final AppService appService;
    public AppController(AppService appService) {
        this.appService = appService;
    }
    
    @GetMapping("/")
    public String indexRoute(Model model, @RequestParam(value = "page", defaultValue = "0") int page,
                         @RequestParam(value = "size", defaultValue = "3") int size) {

        Page<Map<String, Object>> modelPage = appService.getAvisosData(page, size);
        model.addAttribute("data", modelPage.getContent());
        model.addAttribute("currentPage", page);
        model.addAttribute("totalPages", modelPage.getTotalPages());
        return "bienvenida";
    }

    @GetMapping("/t5-admin-fotos")
    public String adminFotosRoute(Model model,  @RequestParam(value = "page", defaultValue = "0") int page,
                         @RequestParam(value = "size", defaultValue = "3") int size) {

        Page<Map<String, Object>> modelPage = appService.getFotoData(page, size);
        model.addAttribute("data", modelPage.getContent());
        model.addAttribute("currentPage", page);
        model.addAttribute("totalPages", modelPage.getTotalPages());
        return "admin-fotos";
    }

    @PostMapping("/t5-admin-fotos/delete")
    public String deleteFoto(@RequestParam("fotoId") Integer fotoId,
                         @RequestParam("motivo") String motivo) {
        //validate motivo
        appService.deleteFoto(fotoId, motivo);
        return "redirect:/t5-admin-fotos";
    }

    @GetMapping("/mensajes-log")
    public String logsRoute(Model model,  @RequestParam(value = "page", defaultValue = "0") int page,
                         @RequestParam(value = "size", defaultValue = "3") int size) {
        Page<Map<String, Object>> modelPage = appService.getLogsData(page, size);
        model.addAttribute("data", modelPage.getContent());
        model.addAttribute("currentPage", page);
        model.addAttribute("totalPages", modelPage.getTotalPages());
        return "logs";
    }

    @GetMapping("/login")
    public String loginRoute() {
        return "login";
    }



}
