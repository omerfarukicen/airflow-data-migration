create table if not exists airflow_gnl_enum_deger
(
    id                    bigint            not null,
    durum                 integer default 1 not null,
    guncelleme_tarihi     date,
    guncelleyen_kullanici varchar(255),
    olusturan_kullanici   varchar(255),
    olusturulma_tarihi    date,
    version               bigint  default 0,
    tablo                 varchar(255),
    kolon                 varchar(255),
    deger                 varchar(255),
    aciklama              varchar(255),
    enum_class_name       varchar(255)
);