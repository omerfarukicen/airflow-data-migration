DO $$
    BEGIN
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_durum') THEN CREATE TYPE enum_musteri_durum AS ENUM ('PASIF','AKTIF','ADAY'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_medeni_hali') THEN CREATE TYPE enum_musteri_medeni_hali AS ENUM ('BEKAR','EVLI','BOSANMIS','DUL','EVLILIGIN_FESHI','EVLILIGIN_IPTALI','BILINMEYEN'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_yurtici_faaliyet_var_mi') THEN CREATE TYPE enum_musteri_yurtici_faaliyet_var_mi AS ENUM ('HAYIR','EVET'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_tramerden_dogrulandimi') THEN CREATE TYPE enum_musteri_tramerden_dogrulandimi AS ENUM ('DOGRULAMASI_YAPILDI','SORGULAMASI_YAPILAMADI','DOGRULAMASI_YAPILAMADI','SORGULAMASI_YAPILDI','SORGULAMASI_YAPILMAYACAK'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_yuksek_risk_grubunda_mi') THEN CREATE TYPE enum_musteri_yuksek_risk_grubunda_mi AS ENUM ('HAYIR','EVET'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_modul_tipi') THEN CREATE TYPE enum_musteri_modul_tipi AS ENUM ('GENEL','SATIS_KAYNAGI','URUN','URETIM','TAHSILAT','HASAR','MUHASEBE','MUSTERI','REASURANS','ONMUHASEBE','SATINALMA','RUCU','HUKUK','ACENTE_CARI','SAGLIK','MUHABERAT'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_ilbis_mus_tipi') THEN CREATE TYPE enum_musteri_ilbis_mus_tipi AS ENUM ('YEREL_YONETIM','IL_OZEL_IDARELERI','BANKA_PERSONELI','DIGER','MUTEAHHIT_SIRKET'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_isletme_tipi') THEN CREATE TYPE enum_musteri_isletme_tipi AS ENUM ('MAHALLI_SIRKETLER','YABANCI_SIRKETLER','ULUSLARARASI_ISLETMELER'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_sirket_turu') THEN CREATE TYPE enum_musteri_sirket_turu AS ENUM ('GERCEK','ADI','KOLLEKTIF','ADI_KOMANDIT','ESH_KOMANDIT','LIMITED','ANONIM','KOOPERATIF','DIGER','T_A_O','VAKIF'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_egitim_durumu') THEN CREATE TYPE enum_musteri_egitim_durumu AS ENUM ('ILKOGRETIM','LISE','ONLISANS','LISANS','LISANSUSTU','OKUR_YAZAR_DEGIL','OKUL_ONCESI'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_referans_tipi') THEN CREATE TYPE enum_musteri_referans_tipi AS ENUM ('MUSTERI','SATIS_KAYNAGI','SIRKET_PERSONELI','DIGER'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_etk_email2_izni') THEN CREATE TYPE enum_musteri_etk_email2_izni AS ENUM ('HAYIR','EVET'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_sgk_kullaniyor_mu') THEN CREATE TYPE enum_musteri_sgk_kullaniyor_mu AS ENUM ('HAYIR','EVET'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_mukellef_turu') THEN CREATE TYPE enum_musteri_mukellef_turu AS ENUM ('GERCEK','TUZEL','DIGER'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_sosyal_guvenlik_tipi') THEN CREATE TYPE enum_musteri_sosyal_guvenlik_tipi AS ENUM ('SSK','BAGKUR','EMEKLI_SANDIGI','ORDU_YARDIMLASMA','YUPASS'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_adresden_dogrulandimi') THEN CREATE TYPE enum_musteri_adresden_dogrulandimi AS ENUM ('SORGULANMADI','SORGULANDI','SORGULANACAK_ADRES','SORGULANAMADI'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_etk_email1_izni') THEN CREATE TYPE enum_musteri_etk_email1_izni AS ENUM ('HAYIR','EVET'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_mevzuat_uyum_onayli_mi') THEN CREATE TYPE enum_musteri_mevzuat_uyum_onayli_mi AS ENUM ('HAYIR','EVET'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_iban_dogrulanimis_mi') THEN CREATE TYPE enum_musteri_iban_dogrulanimis_mi AS ENUM ('HAYIR','EVET'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_uyruk') THEN CREATE TYPE enum_musteri_uyruk AS ENUM ('TC','KKTC','DIGER','MAVIKART'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_cinsiyet') THEN CREATE TYPE enum_musteri_cinsiyet AS ENUM ('ERKEK','KADIN'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_ozel_musteri_mi') THEN CREATE TYPE enum_musteri_ozel_musteri_mi AS ENUM ('HAYIR','EVET'); END IF;
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'enum_musteri_alt_sirket_turu') THEN CREATE TYPE enum_musteri_alt_sirket_turu AS ENUM ('DERNEK','SENDIKA_VE_KONFEDERASYONLAR','SIYASI_PARTILER','YURTDISINDA_YERLESIK_TUZEL_KISILER','APARTMAN_ISHANI_SITE_YONETIMI','KAMU_KURUMLARI','DIGER'); END IF;
    END $$;
