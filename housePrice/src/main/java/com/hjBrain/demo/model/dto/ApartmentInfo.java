package com.hjBrain.demo.model.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class ApartmentInfo {
    private String danjigubn;
    private String sedesu;
    private String nambang;
    private String sigog;
    private String siheg;
    private String gukag;
    private String eill;
    private String guard;
    private String danjicode;
    private String clean;
    private String food;
    private String water;
    private String ellbe;
    private String gisa;
    private String giha;
    private String cctv;
    private String gucha;
    private String amenites;
    private String doro;
    private String donli;
    private String danjiname;
    private int amenitiesCnt;

    public String getDanjigubn() {
        return danjigubn;
    }

    public String getSedesu() {
        return sedesu;
    }

    public String getNambang() {
        return nambang;
    }

    public String getSigog() {
        return sigog;
    }

    public String getSiheg() {
        return siheg;
    }

    public String getGukag() {
        return gukag;
    }

    public String getEill() {
        return eill;
    }

    public String getGuard() {
        return guard;
    }

    public String getDanjicode() {
        return danjicode;
    }

    public String getClean() {
        return clean;
    }

    public String getFood() {
        return food;
    }

    public String getWater() {
        return water;
    }

    public String getEllbe() {
        return ellbe;
    }

    public String getGisa() {
        return gisa;
    }

    public String getGiha() {
        return giha;
    }

    public String getCctv() {
        return cctv;
    }

    public String getGucha() { return gucha; }

    public String getAmenites() {
        return amenites;
    }

    public String getDoro() {
        return doro;
    }

    public String getDonli() {
        return donli;
    }

    public String getDanjiname() {
        return danjiname;
    }

    public int getAmenitiesCnt() {
        return amenitiesCnt;
    }

    @Override
    public String toString() {
        return "ApartmentInfo{" +
                "danjigubn='" + danjigubn + '\'' +
                ", sedesu='" + sedesu + '\'' +
                ", nambang='" + nambang + '\'' +
                ", sigog='" + sigog + '\'' +
                ", siheg='" + siheg + '\'' +
                ", gukag='" + gukag + '\'' +
                ", eill='" + eill + '\'' +
                ", guard='" + guard + '\'' +
                ", danjicode='" + danjicode + '\'' +
                ", clean='" + clean + '\'' +
                ", food='" + food + '\'' +
                ", water='" + water + '\'' +
                ", ellbe='" + ellbe + '\'' +
                ", gisa='" + gisa + '\'' +
                ", giha='" + giha + '\'' +
                ", cctv='" + cctv + '\'' +
                ", gucha='" + gucha +'\'' +
                ", amenites='" + amenites + '\'' +
                ", doro='" + doro + '\'' +
                ", donli='" + donli + '\'' +
                ", danjiname='" + danjiname + '\'' +
                ", amenitiesCnt=" + amenitiesCnt +
                '}';
    }
}

