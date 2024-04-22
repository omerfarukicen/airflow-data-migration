create table if not exists airflow_ms_musteri
(
    id                            numeric(19),
    ad_soyad                      varchar(100),
    aile_sira_no                  numeric(19),
    ana_ad                        varchar(50),
    baba_ad                       varchar(50),
    bank_hesap_adi                varchar(100),
    bank_hesap_no                 varchar(30),
    cilt_no                       numeric(19),
    cinsiyet                      numeric(10),
    cocuk_sayisi                  numeric(10),
    dogum_tarih                   date,
    dogum_yer                     varchar(50),
    durum                         numeric(10),
    egitim_durumu                 numeric(10),
    email1                        varchar(255),
    email2                        varchar(255),
    ev_tel_no                     varchar(7),
    ev_tel_alan_kod               varchar(3),
    ev_tel_ulke_kod               varchar(3),
    gsm_tel_no                    varchar(7),
    gsm_tel_alan_kodu             varchar(3),
    gsm_tel_ulke_kodu             varchar(3),
    guncelleme_tarihi             timestamp,
    guncelleyen_kullanici         varchar(255),
    is_fax                        varchar(7),
    is_fax_alan_kodu              varchar(3),
    is_fax_ulke_kodu              varchar(3),
    is_tel_no                     varchar(7),
    is_tel_alan_kodu              varchar(3),
    is_tel_dahili                 varchar(5),
    is_tel_ulke_kodu              varchar(3),
    kimlik_no                     varchar(11),
    medeni_hali                   numeric(10),
    mukellef_turu                 numeric(10),
    olusturan_kullanici           varchar(255),
    olusturulma_tarihi            timestamp,
    pasaport_no                   varchar(20),
    referans_ad                   varchar(255),
    referans_tipi                 numeric(10),
    seri_no                       varchar(10),
    sira_no                       numeric(19),
    sirket_kurulus_tarih          date,
    sirket_turu                   numeric(10),
    sirket_unvan                  varchar(100),
    sosyal_guvenlik_no            numeric(19),
    sosyal_guvenlik_tipi          numeric(10),
    tramerden_dogrulandimi        numeric(10),
    uyruk                         numeric(10),
    vefat_tarih                   date,
    vergi_no                      varchar(10),
    version                       numeric(19),
    web_adresi                    varchar(100),
    ulke_id                       numeric(19),
    nufusa_kayitli_oldugu_ilce_id numeric(19),
    sirket_kurulus_sehir_id       numeric(19),
    musteri_calisan_sayisi_id     numeric(19),
    banka_subesi_id               numeric(19),
    referans_musteri_id           numeric(19),
    sektor_id                     numeric(19),
    meslek_id                     numeric(19),
    musteri_gelir_araligi_id      numeric(19),
    referans_sirket_personel_id   numeric(19),
    musteri_ciro_araligi_id       numeric(19),
    vip_id                        numeric(19),
    referans_satis_kaynagi_id     numeric(19),
    dask_musteri_kod              numeric(19, 2),
    eski_musteri_id               numeric(19),
    banka_musteri_tipi_id         numeric(19),
    tarsim_musteri_kod            numeric(19),
    iban_numarasi                 varchar(26),
    yuksek_risk_grubunda_mi       numeric(1) default 0,
    vergi_dairesi                 varchar(255),
    aciklama                      varchar(255),
    modul_tipi                    numeric(10),
    yurtici_faaliyet_var_mi       numeric(10),
    kod                           varchar(20),
    tarsim_musteri_info           varchar(4000),
    ad                            varchar(100),
    soyad                         varchar(70),
    saglik_musterisi_mi           numeric(1),
    ilbis_mus_tipi                numeric(10),
    ilbis_kod                     varchar(255),
    kimlik_turu                   numeric,
    ehliyet_no                    varchar(25),
    ehliyet_tipi                  varchar(25),
    ehliyet_yili                  varchar(25),
    isletme_tipi                  numeric,
    kimlik_turu_id                numeric(19),
    ehliyet_ulke_id               numeric(19),
    ehliyet_tipi_id               numeric(19),
    ehliyet_tarihi                date,
    aile_iliski_sorgulama_tarihi  date,
    vip_aciklama                  varchar(255),
    saglik_tss_musteri_id         numeric(19),
    saglik_tss_bagli_musteri_id   numeric(19),
    iliskili_banka_musteri_id     numeric(19),
    adresden_dogrulandimi         numeric(10),
    kps_sorgu_tarihi              date,
    ozel_musteri_mi               numeric(1) default 0,
    servis_saglayici_id           numeric(19),
    hesap_aciklama                varchar(255),
    evrak_id                      numeric(19),
    sgk_kullaniyor_mu             numeric(1) default '0'::numeric,
    uyruk_ad                      varchar(50),
    uyruk_kod                     varchar(10),
    kayit_durumu                  varchar(20),
    son_gecerlilik_tarihi         date,
    mevzuat_uyum_onayli_mi        numeric(1),
    alt_sirket_turu               numeric(10),
    alt_sirket_turu_aciklama      varchar(255),
    block_chain_hashcode          varchar(255),
    yabanci_ad_unvan              varchar(250),
    mono_sube_id                  numeric(19),
    eski_kimlik_no                varchar(11),
    vb_musteri_kod                varchar(20),
    zb_musteri_kod                varchar(20),
    hb_musteri_kod                varchar(20),
    vb_tuzel_musteri_kod          varchar(20),
    zb_tuzel_musteri_kod          varchar(20),
    hb_tuzel_musteri_kod          varchar(20),
    eski_must_kod                 varchar(15),
    eski_vergi_no                 varchar(10),
    eski_pasaport_no              varchar(20),
    ikamet_ulke_id                numeric(19),
    vb_musteri_grubu              varchar(100),
    zb_musteri_grubu              varchar(100),
    hb_musteri_grubu              varchar(100),
    vb_musteri_segment            varchar(100),
    zb_musteri_segment            varchar(100),
    hb_musteri_segment            varchar(100),
    email1_dogrulama_tarihi       date,
    meslek_detay                  varchar(100),
    sbm_ikamet_baslangic_tarihi   date,
    sbm_ikamet_bitis_tarihi       date,
    sbm_ikamet_iptal_tarihi       date,
    iban_dogrulanmis_mi           numeric(1),
    iban_dogrulanma_tarihi        date,
    etk_email1_izni               numeric(1),
    etk_email2_izni               numeric(1),
    zd_mono_sube_id               numeric(19),
    zd_musteri_kod                varchar(20),
    zd_tuzel_musteri_kod          varchar(20),
    zd_musteri_segment            varchar(100),
    zd_musteri_grubu              varchar(100),
    etk_email_beyan_tipi1         numeric(19),
    etk_email_beyan_tipi2         numeric(19),
    zb_personel_no                varchar(255),
    vb_personel_no                varchar(255),
    hb_personel_no                varchar(255)
);