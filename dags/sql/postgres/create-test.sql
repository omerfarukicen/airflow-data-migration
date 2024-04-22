create table if not exists airflow_test
(
    id                      bigint,
    adi                     varchar,
    soyadi                  varchar,
    create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

truncate table airflow_test;

insert into airflow_test (id, adi, soyadi)
values (1, 'Ahmet','Can');

insert into airflow_test (id, adi, soyadi)
values (2, 'Mehmet','Ali');