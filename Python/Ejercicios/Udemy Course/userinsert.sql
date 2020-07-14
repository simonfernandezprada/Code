-- Documentos:      Oracle Database 11g
insert into DNI_PERSONA values (auto_increment_dir_pers.nextval, '19746549-2',39);
insert into DNI_PERSONA values (auto_increment_dir_pers.nextval, '18066166-2',39);

-- TIPO TELEFONO:      Oracle Database 11g

insert into TIPO_TELEFONO values (auto_increment_tpo_telefono.nextval, '+56');

-- TELEFONO: Oracle Database
insert into TELEFONO (COD_TELEFONO,TELEFONO,COD_TPO_TELEFONO) values (auto_increment_telefono.nextval, '992495684', 1);

-- PERSONA:      Oracle Database 11g
insert into PERSONA values (auto_increment_persona.nextval, 'Eduardo',null,'Onetto','Correa','01/01/97', 'ed.onetto@gmail.com',123,1,2);
insert into PERSONA values (auto_increment_persona.nextval, 'Josselin',null,'Gallardo','Correa','19/09/92', 'jo.galla@gmail.com',124,2,1);

--AFILIADO:      Oracle Database 11g
INSERT INTO AFILIADO VALUES (1, auto_increment_afiliado.nextval, 1);
INSERT INTO AFILIADO VALUES (2, auto_increment_afiliado.nextval, 0);
