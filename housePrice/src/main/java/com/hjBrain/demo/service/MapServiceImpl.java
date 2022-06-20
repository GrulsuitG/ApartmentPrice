package com.hjBrain.demo.service;

import com.hjBrain.demo.controller.InputForm;
import com.hjBrain.demo.model.dao.DataMapper;
import com.hjBrain.demo.model.dto.ApartmentInfo;

import com.hjBrain.demo.model.dto.GuName;
import com.hjBrain.demo.model.dto.SidoName;
import lombok.RequiredArgsConstructor;

import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class MapServiceImpl implements MapService{
    private final DataMapper dataMapper;

    @Override
    public List<ApartmentInfo> getAllDataList() {
//        List<ApartmentInfo> data = dataMapper.getAllDataList();

        return dataMapper.getAllDataList();
    }

    @Override
    public List<GuName> getGuNameList() {
        return dataMapper.getGuName();
    }

    @Override
    public List<SidoName> getSidoNameList() {
        return dataMapper.getSidoName();
    }

    @Override
    public List<ApartmentInfo> bestRecommendedData(InputForm form) {
        return dataMapper.bestRecommendedData(form);
    }

    @Override
    public ApartmentInfo getInfoByDanjicode(String danjicode) {
        return dataMapper.getInfoByDanjicode(danjicode);
    }
}
