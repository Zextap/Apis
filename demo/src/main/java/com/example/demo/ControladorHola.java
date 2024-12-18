package com.example.demo;

import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;


@RestController
public class ControladorHola {
    @GetMapping("/hola")
    public Map<String,String> HolaMundo() {
        return Map.of("mensaje","hola mundo");
    }

    @GetMapping(path = "/hola/{nombre}")
    public Map<String,String> getMethodName(@PathVariable("nombre") String nom) {
        return Map.of("mensaje",  "hola "+nom);
    }
    
    
}
