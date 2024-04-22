SELECT 
	mm.OLUSTURULMA_TARIHI olusturma_tarihi,
	mm.GUNCELLEME_TARIHI guncelleme_tarihi,
	mm.ID p_musteri_id,
	enDurum.ACIKLAMA durum,
	mm.AD ad,
	mm.SOYAD soyad,
	enCinsiyet.ACIKLAMA cinsiyet,
	mm.DOGUM_TARIH dogum_tarihi,
	mm.YUKSEK_RISK_GRUBUNDA_MI yuksek_risk_grubunda_mi,
	mm.BANK_HESAP_ADI bank_hesap_adi,
	mm.BANK_HESAP_NO bank_hesap_no,
	mm.YABANCI_AD_UNVAN yabanci_ad_unvan
FROM MUSTERI.MS_MUSTERI mm 
	LEFT JOIN GNL_ENUM_DEGER enCinsiyet ON mm.CINSIYET=enCinsiyet.DEGER 
	LEFT JOIN GNL_ENUM_DEGER enDurum ON mm.DURUM =enDurum.DEGER 
WHERE enCinsiyet.TABLO ='MS_MUSTERI' AND enCinsiyet.KOLON='CINSIYET'
	 AND enDurum.TABLO ='MS_MUSTERI' AND enDurum.KOLON ='DURUM'