package com.hjBrain.demo.model.dao;

import com.hjBrain.demo.controller.InputForm;
import com.hjBrain.demo.model.dto.ApartmentInfo;

import com.hjBrain.demo.model.dto.GuName;
import com.hjBrain.demo.model.dto.SidoName;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
@Mapper
public interface DataMapper {
    List<ApartmentInfo> getAllDataList();
    List<GuName> getGuName();
    List<SidoName> getSidoName();
    List<ApartmentInfo> bestRecommendedData(InputForm form);
    ApartmentInfo getInfoByDanjicode(String danjicode);
}
