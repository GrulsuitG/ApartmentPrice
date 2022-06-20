package com.hjBrain.demo.controller;

public class InputForm {
    private String gu;
    private int market;
    private int amenities;
    private int hospital;

    public InputForm(String gu, int market, int amenities, int hospital) {
        this.gu = gu;
        this.market = market;
        this.amenities = amenities;
        this.hospital = hospital;
    }

    public String getGu() {
        return gu;
    }

    public void setGu(String gu) {
        this.gu = gu;
    }

    public int getMarket() {
        return market;
    }

    public void setMarket(int market) {
        this.market = market;
    }

    public int getAmenities() {
        return amenities;
    }

    public void setAmenities(int amenities) {
        this.amenities = amenities;
    }

    public int getHospital() {
        return hospital;
    }

    public void setHospital(int hospital) {
        this.hospital = hospital;
    }

    @Override
    public String toString() {
        return "InputForm{" +
                "gu='" + gu + '\'' +
                ", market=" + market +
                ", amenities=" + amenities +
                ", hospital=" + hospital +
                '}';
    }
}
