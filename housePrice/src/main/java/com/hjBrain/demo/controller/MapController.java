package com.hjBrain.demo.controller;

import com.hjBrain.demo.model.dto.ApartmentInfo;
import com.hjBrain.demo.service.MapService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.List;

@RequiredArgsConstructor
@Controller
public class MapController {
    private final MapService mapService;

    @GetMapping("/getAllData")
    public List<ApartmentInfo> GetAllData() {
        return mapService.getAllDataList();
    }


    @RequestMapping("/")
    public String RepresentGu(Model model) {
        model.addAttribute("guList", mapService.getGuNameList());
        return "home";
    }

    @PostMapping("/")
    public String InputData(Model model, InputForm form) {
        model.addAttribute("guList", mapService.getGuNameList());
        model.addAttribute("recommendData", mapService.bestRecommendedData(form));
//        model.addAttribute("recommendData", mapService.getAllDataList());

//        for (ApartmentInfo datum : data) {
//            System.out.println("datum = " + datum);
//        }
//        model.addAttribute("guList", mapService.getGuNameList());

        return "home";
    }

    @RequestMapping("result")
    public String Result(Model model, String danjicode) {
        ApartmentInfo apartmentInfo = mapService.getInfoByDanjicode(danjicode);
        model.addAttribute("apart", apartmentInfo);
        return "result";
    }
}
