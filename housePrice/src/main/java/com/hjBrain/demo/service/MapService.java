package com.hjBrain.demo.service;


import com.hjBrain.demo.controller.InputForm;
import com.hjBrain.demo.model.dto.ApartmentInfo;
import com.hjBrain.demo.model.dto.GuName;
import com.hjBrain.demo.model.dto.SidoName;

import java.util.List;

public interface MapService {
    public List<ApartmentInfo> getAllDataList();
    public List<GuName> getGuNameList();
    public List<SidoName> getSidoNameList();

    public List<ApartmentInfo> bestRecommendedData(InputForm form);

    public ApartmentInfo getInfoByDanjicode(String danjicode);
}
