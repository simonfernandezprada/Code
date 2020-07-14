CREATE TABLE AFILIADO
  (
    cod_persona      NUMBER (3) NOT NULL ,
    cod_afiliado     NUMBER (10) NOT NULL ,
    estado_membresia CHAR (1) NOT NULL
  ) ;
ALTER TABLE AFILIADO ADD CONSTRAINT AFILIADO_PK PRIMARY KEY ( cod_persona ) ;
ALTER TABLE AFILIADO ADD CONSTRAINT AFILIADO_PKv1 UNIQUE ( cod_afiliado ) ;


CREATE TABLE BENEFICIO
  (
    cod_beneficio_1   NUMBER (10) NOT NULL ,
    cod_tpo_beneficio NUMBER (3) NOT NULL ,
    nombre_beneficio  VARCHAR2 (200) NOT NULL ,
    stock_max_de_uso  NUMBER (10) ,
    cobertura         VARCHAR2 (20) NOT NULL
  ) ;
ALTER TABLE BENEFICIO ADD CONSTRAINT BENEFICIOS_PK PRIMARY KEY ( cod_beneficio_1 ) ;


CREATE TABLE BENEFICIO_AFILIADO
  (
    cod_af_be       NUMBER (10) NOT NULL ,
    cod_afiliado    NUMBER (10) NOT NULL ,
    cod_beneficio_1 NUMBER (10) NOT NULL ,
    cantidad_uso    NUMBER (10) NOT NULL
  ) ;
ALTER TABLE BENEFICIO_AFILIADO ADD CONSTRAINT BENEFICIO_AFILIADO_PK PRIMARY KEY ( cod_af_be, cod_afiliado, cod_beneficio_1 ) ;


CREATE TABLE CARGA
  (
    cod_p_c          NUMBER (12) NOT NULL ,
    primer_nombre    VARCHAR2 (20) NOT NULL ,
    segundo_nombre   VARCHAR2 (20) ,
    primer_apellido  VARCHAR2 (20) NOT NULL ,
    segundo_apellido VARCHAR2 (20) ,
    fec_nac          DATE NOT NULL ,
    cod_parentesco   NUMBER (2) NOT NULL ,
    cod_genero       NUMBER (2) NOT NULL
  ) ;
ALTER TABLE CARGA ADD CONSTRAINT CARGA_PK PRIMARY KEY ( cod_p_c ) ;


CREATE TABLE CHEQUE
  (
    num_cheque NUMBER (30) NOT NULL ,
    nom_banco  VARCHAR2 (200) NOT NULL ,
    cod_banco  NUMBER (4) NOT NULL
  ) ;
ALTER TABLE CHEQUE ADD CONSTRAINT CHEQUE_PK PRIMARY KEY ( num_cheque ) ;


CREATE TABLE CIUDAD
  (
    cod_ciudad NUMBER (5) NOT NULL ,
    ciudad     VARCHAR2 (80) NOT NULL ,
    cod_region NUMBER (5) NOT NULL
  ) ;
ALTER TABLE CIUDAD ADD CONSTRAINT CIUDAD_PK PRIMARY KEY ( cod_ciudad ) ;


CREATE TABLE COMUNA
  (
    cod_comuna NUMBER (5) NOT NULL ,
    comuna     VARCHAR2 (80) NOT NULL ,
    cod_ciudad NUMBER (5) NOT NULL
  ) ;
ALTER TABLE COMUNA ADD CONSTRAINT COMUNA_PK PRIMARY KEY ( cod_comuna ) ;


CREATE TABLE CONVENIO_AFILIADO
  (
    cod_af_conv  NUMBER (10) NOT NULL ,
    cod_afiliado NUMBER (10) NOT NULL ,
    cod_convenio NUMBER (10) NOT NULL
  ) ;
ALTER TABLE CONVENIO_AFILIADO ADD CONSTRAINT BENEFICIO_AFILIADO_PKv2 PRIMARY KEY ( cod_af_conv, cod_afiliado, cod_convenio ) ;


CREATE TABLE CONVENIO_ASEGURADORA
  (
    cod_convenio     NUMBER (10) NOT NULL ,
    prima            NUMBER (10) NOT NULL ,
    prcj_dscto       NUMBER (3) NOT NULL ,
    cod_tpo_convenio NUMBER (10) NOT NULL
  ) ;
ALTER TABLE CONVENIO_ASEGURADORA ADD CONSTRAINT CONVENIO_ASEGURADORA_PK PRIMARY KEY ( cod_convenio ) ;


CREATE TABLE CREDITO
  ( cod_credito NUMBER (15) NOT NULL
  ) ;
ALTER TABLE CREDITO ADD CONSTRAINT CREDITO_PK PRIMARY KEY ( cod_credito ) ;


CREATE TABLE DIRECCION
  (
    cod_direccion NUMBER (5) NOT NULL ,
    direccion     VARCHAR2 (200) NOT NULL ,
    cod_comuna    NUMBER (5) NOT NULL
  ) ;
ALTER TABLE DIRECCION ADD CONSTRAINT DIRECCION_PK PRIMARY KEY ( cod_direccion ) ;


CREATE TABLE DIRECCION_PERSONA
  (
    cod_dir_persona NUMBER (5) NOT NULL ,
    cod_direccion   NUMBER (5) NOT NULL ,
    cod_persona     NUMBER (3) NOT NULL
  ) ;
ALTER TABLE DIRECCION_PERSONA ADD CONSTRAINT DIRECCION_PERSONA_PK PRIMARY KEY ( cod_dir_persona, cod_direccion, cod_persona ) ;


CREATE TABLE DISCAPACIDAD
  (
    cod_discapacidad NUMBER (4) NOT NULL ,
    cod_tipo         NUMBER (10) NOT NULL ,
    cod_persona      NUMBER (3) NOT NULL
  ) ;
ALTER TABLE DISCAPACIDAD ADD CONSTRAINT DISCAPACIDAD_PK PRIMARY KEY ( cod_discapacidad ) ;


CREATE TABLE DNI_PERSONA
  (
    cod_dni_postulante NUMBER (8) NOT NULL ,
    numero_documento   VARCHAR2 (20) NOT NULL ,
    cod_pais           NUMBER (3) NOT NULL
  ) ;
ALTER TABLE DNI_PERSONA ADD CONSTRAINT DNI_POSTULANTE_PK PRIMARY KEY ( cod_dni_postulante ) ;


CREATE TABLE EFECTIVO
  ( cod_efectivo NUMBER (15) NOT NULL
  ) ;
ALTER TABLE EFECTIVO ADD CONSTRAINT EFECTIVO_PK PRIMARY KEY ( cod_efectivo ) ;


CREATE TABLE GENERO
  (
    cod_genero  NUMBER (2) NOT NULL ,
    descripcion VARCHAR2 (80) NOT NULL
  ) ;
ALTER TABLE GENERO ADD CONSTRAINT GENERO_PK PRIMARY KEY ( cod_genero ) ;


CREATE TABLE HIJO
  (
    cod_p_c  NUMBER (12) NOT NULL ,
    cod_hijo NUMBER (5) NOT NULL
  ) ;
ALTER TABLE HIJO ADD CONSTRAINT HIJO_PKv2 PRIMARY KEY ( cod_p_c ) ;
ALTER TABLE HIJO ADD CONSTRAINT HIJO_PK UNIQUE ( cod_hijo ) ;


CREATE TABLE HISTORIAL_PAGO
  (
    cod_historial_pago NUMBER (9) NOT NULL ,
    cod_afiliado       NUMBER (10) NOT NULL ,
    mes                VARCHAR2 (80) NOT NULL ,
    año                NUMBER (4) NOT NULL
  ) ;
ALTER TABLE HISTORIAL_PAGO ADD CONSTRAINT HISTORIAL_PAGOS_PK PRIMARY KEY ( cod_historial_pago ) ;


CREATE TABLE NACIONALIDAD
  (
    cod_pais    NUMBER (3) NOT NULL ,
    nombre_pais VARCHAR2 (100) NOT NULL
  ) ;
ALTER TABLE NACIONALIDAD ADD CONSTRAINT NACIONALIDAD_PK PRIMARY KEY ( cod_pais ) ;


CREATE TABLE PAGO
  (
    cod_pago           NUMBER (20) NOT NULL ,
    monto_pagado       NUMBER (15) NOT NULL ,
    cod_historial_pago NUMBER (9) NOT NULL ,
    num_cheque         NUMBER (30) ,
    cod_efectivo       NUMBER (15) ,
    cod_credito        NUMBER (15) ,
    cod_transferencia  NUMBER (15)
  ) ;
ALTER TABLE PAGO ADD CONSTRAINT Arc_3 CHECK ( ( (num_cheque IS NOT NULL) AND (cod_efectivo IS NULL) AND (cod_credito IS NULL) AND (cod_transferencia IS NULL) ) OR ( (cod_efectivo IS NOT NULL) AND (num_cheque IS NULL) AND (cod_credito IS NULL) AND (cod_transferencia IS NULL) ) OR ( (cod_credito IS NOT NULL) AND (num_cheque IS NULL) AND (cod_efectivo IS NULL) AND (cod_transferencia IS NULL) ) OR ( (cod_transferencia IS NOT NULL) AND (num_cheque IS NULL) AND (cod_efectivo IS NULL) AND (cod_credito IS NULL) ) ) ;
ALTER TABLE PAGO ADD CONSTRAINT PAGO_PK PRIMARY KEY ( cod_pago ) ;


CREATE TABLE PAREJA
  (
    cod_p_c     NUMBER (12) NOT NULL ,
    cod_pareja  NUMBER (10) NOT NULL ,
    tipo_pareja NUMBER (5) NOT NULL
  ) ;
ALTER TABLE PAREJA ADD CONSTRAINT PAREJA_PK PRIMARY KEY ( cod_p_c ) ;
ALTER TABLE PAREJA ADD CONSTRAINT PAREJA_PKv1 UNIQUE ( cod_pareja , tipo_pareja ) ;


CREATE TABLE PARENTESCO
  (
    cod_parentesco NUMBER (2) NOT NULL ,
    descripcion    VARCHAR2 (200) NOT NULL
  ) ;
ALTER TABLE PARENTESCO ADD CONSTRAINT PARENTESCO_PK PRIMARY KEY ( cod_parentesco ) ;


CREATE TABLE PERSONA
  (
    cod_persona        NUMBER (3) NOT NULL ,
    primer_nombre      VARCHAR2 (20) NOT NULL ,
    segundo_nombre     VARCHAR2 (20) ,
    primer_apellido    VARCHAR2 (20) NOT NULL ,
    segundo_apellido   VARCHAR2 (20) ,
    fec_nac            DATE NOT NULL ,
    correo_electronico VARCHAR2 (20) NOT NULL ,
    numero_socio       NUMBER (12) ,
    cod_dni_postulante NUMBER (8) NOT NULL ,
    cod_genero         NUMBER (2) NOT NULL
  ) ;
ALTER TABLE PERSONA ADD CONSTRAINT PERSONA_PK PRIMARY KEY ( cod_persona ) ;


CREATE TABLE PERSONA_CARGA
  (
    codigo_carga   NUMBER (10) NOT NULL ,
    HIIJO_cod_hijo NUMBER (5) NOT NULL ,
    cod_pareja     NUMBER (10) NOT NULL ,
    cod_persona    NUMBER (3) NOT NULL ,
    tipo_pareja    NUMBER (5) NOT NULL ,
    cod_hijo       NUMBER NOT NULL
  ) ;
ALTER TABLE PERSONA_CARGA ADD CONSTRAINT AFILIADO_CARGA_PK PRIMARY KEY ( cod_hijo, codigo_carga, cod_pareja, tipo_pareja, cod_persona ) ;


CREATE TABLE POSTULANTE
  (
    cod_persona       NUMBER (3) NOT NULL ,
    cod_postulante    NUMBER (10) NOT NULL ,
    pretension_sueldo VARCHAR2 (8) NOT NULL ,
    cv BLOB NOT NULL
  ) ;
ALTER TABLE POSTULANTE ADD CONSTRAINT POSTULANTE_PK PRIMARY KEY ( cod_persona ) ;
ALTER TABLE POSTULANTE ADD CONSTRAINT POSTULANTE_PKv1 UNIQUE ( cod_postulante ) ;


CREATE TABLE REGION
  (
    cod_region NUMBER (5) NOT NULL ,
    region     VARCHAR2 (20) NOT NULL
  ) ;
ALTER TABLE REGION ADD CONSTRAINT REGION_PK PRIMARY KEY ( cod_region ) ;


CREATE TABLE SOLICITUD
  (
    cod_solicitud  NUMBER (8) NOT NULL ,
    fecha_ingreso  TIMESTAMP NOT NULL ,
    cod_postulante NUMBER (10) NOT NULL
  ) ;
ALTER TABLE SOLICITUD ADD CONSTRAINT SOLICITUD_PK PRIMARY KEY ( cod_solicitud ) ;


CREATE TABLE TELEFONO
  (
    cod_telefono     NUMBER (20) NOT NULL ,
    cod_tpo_telefono NUMBER (10) NOT NULL ,
    telefono         VARCHAR2 (10) NOT NULL
  ) ;
ALTER TABLE TELEFONO ADD CONSTRAINT TELEFONO_PK PRIMARY KEY ( cod_telefono ) ;


CREATE TABLE TELEFONO_PERSONA
  (
    cod_tele_pers NUMBER (12) NOT NULL ,
    cod_telefono  NUMBER (20) NOT NULL ,
    cod_persona   NUMBER (3) NOT NULL
  ) ;
COMMENT ON COLUMN TELEFONO_PERSONA.cod_persona
IS
  'Codigo de una persona sea postulante o afiliado' ;
ALTER TABLE TELEFONO_PERSONA ADD CONSTRAINT Telefono_Persona_PK PRIMARY KEY ( cod_tele_pers, cod_telefono, cod_persona ) ;


CREATE TABLE TIPO_CONVENIO
  (
    cod_tpo_convenio NUMBER (10) NOT NULL ,
    descripcion      VARCHAR2 (40) NOT NULL
  ) ;
ALTER TABLE TIPO_CONVENIO ADD CONSTRAINT TPO_CONVENIO_PK PRIMARY KEY ( cod_tpo_convenio ) ;


CREATE TABLE TIPO_DISCAPACIDAD
  (
    cod_tipo    NUMBER (10) NOT NULL ,
    nombre_tipo VARCHAR2 (80) NOT NULL
  ) ;
ALTER TABLE TIPO_DISCAPACIDAD ADD CONSTRAINT TIPO_DISCAPACIDAD_PK PRIMARY KEY ( cod_tipo ) ;


CREATE TABLE TIPO_PAREJA
  (
    cod_tipo_pareja NUMBER (5) NOT NULL ,
    nombre_tipo     VARCHAR2 (20) NOT NULL
  ) ;
ALTER TABLE TIPO_PAREJA ADD CONSTRAINT TIPO_PAREJA_PK PRIMARY KEY ( cod_tipo_pareja ) ;


CREATE TABLE TIPO_TELEFONO
  (
    cod_tpo_telefono     NUMBER (2) NOT NULL ,
    descripcion_telefono VARCHAR2 (30) NOT NULL
  ) ;
ALTER TABLE TIPO_TELEFONO ADD CONSTRAINT TIPO_TELEFONO_PK PRIMARY KEY ( cod_tpo_telefono ) ;


CREATE TABLE TPO_BENEFICIO
  (
    cod_tpo_beneficio NUMBER (3) NOT NULL ,
    descripcion       VARCHAR2 (20) NOT NULL
  ) ;
ALTER TABLE TPO_BENEFICIO ADD CONSTRAINT TPO_BENEFICIO_PK PRIMARY KEY ( cod_tpo_beneficio ) ;


CREATE TABLE TRANSFERENCIA
  ( cod_transferencia NUMBER (15) NOT NULL
  ) ;
ALTER TABLE TRANSFERENCIA ADD CONSTRAINT TRANSFERENCIA_PK PRIMARY KEY ( cod_transferencia ) ;


CREATE TABLE VEHICULO
  (
    cod_vehiculo    NUMBER (10) NOT NULL ,
    cod_afiliado    NUMBER (10) ,
    marca_vehiculo  VARCHAR2 (50) NOT NULL ,
    modelo_vehiculo VARCHAR2 (50) NOT NULL ,
    patente         VARCHAR2 (7) NOT NULL ,
    color           VARCHAR2 (20) NOT NULL ,
    num_chasis      VARCHAR2 (17) NOT NULL ,
    num_motor       VARCHAR2 (12) NOT NULL
  ) ;
ALTER TABLE VEHICULO ADD CONSTRAINT VEHICULO_PK PRIMARY KEY ( cod_vehiculo ) ;


ALTER TABLE AFILIADO ADD CONSTRAINT AFILIADO_PERSONA_FK FOREIGN KEY ( cod_persona ) REFERENCES PERSONA ( cod_persona ) ;

ALTER TABLE DISCAPACIDAD ADD CONSTRAINT DISCAPACIDAD_PERSONA_FK FOREIGN KEY ( cod_persona ) REFERENCES PERSONA ( cod_persona ) ;

ALTER TABLE HIJO ADD CONSTRAINT HIJO_CARGA_FK FOREIGN KEY ( cod_p_c ) REFERENCES CARGA ( cod_p_c ) ;

ALTER TABLE PAREJA ADD CONSTRAINT PAREJA_CARGA_FK FOREIGN KEY ( cod_p_c ) REFERENCES CARGA ( cod_p_c ) ;

ALTER TABLE POSTULANTE ADD CONSTRAINT POSTULANTE_PERSONA_FK FOREIGN KEY ( cod_persona ) REFERENCES PERSONA ( cod_persona ) ;

ALTER TABLE PERSONA_CARGA ADD CONSTRAINT Relation_11 FOREIGN KEY ( cod_pareja, tipo_pareja ) REFERENCES PAREJA ( cod_pareja, tipo_pareja ) ;

ALTER TABLE DISCAPACIDAD ADD CONSTRAINT Relation_12 FOREIGN KEY ( cod_tipo ) REFERENCES TIPO_DISCAPACIDAD ( cod_tipo ) ;

ALTER TABLE PERSONA ADD CONSTRAINT Relation_13 FOREIGN KEY ( cod_dni_postulante ) REFERENCES DNI_PERSONA ( cod_dni_postulante ) ;

ALTER TABLE PAREJA ADD CONSTRAINT Relation_15 FOREIGN KEY ( tipo_pareja ) REFERENCES TIPO_PAREJA ( cod_tipo_pareja ) ;

ALTER TABLE PERSONA_CARGA ADD CONSTRAINT Relation_16 FOREIGN KEY ( cod_persona ) REFERENCES PERSONA ( cod_persona ) ;

ALTER TABLE CARGA ADD CONSTRAINT Relation_18 FOREIGN KEY ( cod_parentesco ) REFERENCES PARENTESCO ( cod_parentesco ) ;

ALTER TABLE BENEFICIO ADD CONSTRAINT Relation_19 FOREIGN KEY ( cod_tpo_beneficio ) REFERENCES TPO_BENEFICIO ( cod_tpo_beneficio ) ;

ALTER TABLE BENEFICIO_AFILIADO ADD CONSTRAINT Relation_20 FOREIGN KEY ( cod_afiliado ) REFERENCES AFILIADO ( cod_afiliado ) ;

ALTER TABLE BENEFICIO_AFILIADO ADD CONSTRAINT Relation_21 FOREIGN KEY ( cod_beneficio_1 ) REFERENCES BENEFICIO ( cod_beneficio_1 ) ;

ALTER TABLE PERSONA ADD CONSTRAINT Relation_22 FOREIGN KEY ( cod_genero ) REFERENCES GENERO ( cod_genero ) ;

ALTER TABLE CARGA ADD CONSTRAINT Relation_23 FOREIGN KEY ( cod_genero ) REFERENCES GENERO ( cod_genero ) ;

ALTER TABLE CONVENIO_ASEGURADORA ADD CONSTRAINT Relation_24 FOREIGN KEY ( cod_tpo_convenio ) REFERENCES TIPO_CONVENIO ( cod_tpo_convenio ) ;

ALTER TABLE VEHICULO ADD CONSTRAINT Relation_25 FOREIGN KEY ( cod_afiliado ) REFERENCES AFILIADO ( cod_afiliado ) ;

ALTER TABLE CONVENIO_AFILIADO ADD CONSTRAINT Relation_26 FOREIGN KEY ( cod_afiliado ) REFERENCES AFILIADO ( cod_afiliado ) ;

ALTER TABLE CONVENIO_AFILIADO ADD CONSTRAINT Relation_27 FOREIGN KEY ( cod_convenio ) REFERENCES CONVENIO_ASEGURADORA ( cod_convenio ) ;

ALTER TABLE SOLICITUD ADD CONSTRAINT Relation_28 FOREIGN KEY ( cod_postulante ) REFERENCES POSTULANTE ( cod_postulante ) ;

ALTER TABLE TELEFONO_PERSONA ADD CONSTRAINT Relation_30 FOREIGN KEY ( cod_persona ) REFERENCES PERSONA ( cod_persona ) ;

ALTER TABLE TELEFONO_PERSONA ADD CONSTRAINT Relation_31 FOREIGN KEY ( cod_telefono ) REFERENCES TELEFONO ( cod_telefono ) ;

ALTER TABLE DIRECCION_PERSONA ADD CONSTRAINT Relation_32 FOREIGN KEY ( cod_persona ) REFERENCES PERSONA ( cod_persona ) ;

ALTER TABLE DIRECCION_PERSONA ADD CONSTRAINT Relation_33 FOREIGN KEY ( cod_direccion ) REFERENCES DIRECCION ( cod_direccion ) ;

ALTER TABLE HISTORIAL_PAGO ADD CONSTRAINT Relation_34 FOREIGN KEY ( cod_afiliado ) REFERENCES AFILIADO ( cod_afiliado ) ;

ALTER TABLE PAGO ADD CONSTRAINT Relation_35 FOREIGN KEY ( num_cheque ) REFERENCES CHEQUE ( num_cheque ) ;

ALTER TABLE PAGO ADD CONSTRAINT Relation_36 FOREIGN KEY ( cod_efectivo ) REFERENCES EFECTIVO ( cod_efectivo ) ;

ALTER TABLE PAGO ADD CONSTRAINT Relation_37 FOREIGN KEY ( cod_credito ) REFERENCES CREDITO ( cod_credito ) ;

ALTER TABLE PAGO ADD CONSTRAINT Relation_38 FOREIGN KEY ( cod_transferencia ) REFERENCES TRANSFERENCIA ( cod_transferencia ) ;

ALTER TABLE CIUDAD ADD CONSTRAINT Relation_4 FOREIGN KEY ( cod_region ) REFERENCES REGION ( cod_region ) ;

ALTER TABLE PAGO ADD CONSTRAINT Relation_40 FOREIGN KEY ( cod_historial_pago ) REFERENCES HISTORIAL_PAGO ( cod_historial_pago ) ;

ALTER TABLE COMUNA ADD CONSTRAINT Relation_5 FOREIGN KEY ( cod_ciudad ) REFERENCES CIUDAD ( cod_ciudad ) ;

ALTER TABLE DIRECCION ADD CONSTRAINT Relation_6 FOREIGN KEY ( cod_comuna ) REFERENCES COMUNA ( cod_comuna ) ;

ALTER TABLE TELEFONO ADD CONSTRAINT Relation_7 FOREIGN KEY ( cod_tpo_telefono ) REFERENCES TIPO_TELEFONO ( cod_tpo_telefono ) ;

ALTER TABLE DNI_PERSONA ADD CONSTRAINT Relation_8 FOREIGN KEY ( cod_pais ) REFERENCES NACIONALIDAD ( cod_pais ) ;

CREATE OR REPLACE TRIGGER ARC_FKArc_1_HIJO BEFORE
  INSERT OR
  UPDATE OF cod_p_c ON HIJO FOR EACH ROW DECLARE d NUMBER (12);
  BEGIN
    SELECT A.cod_p_c INTO d FROM CARGA A WHERE A.cod_p_c = :new.cod_p_c;
    IF (d IS NULL OR d <> 1) THEN
      raise_application_error(-20223,'FK HIJO_CARGA_FK in Table HIJO violates Arc constraint on Table CARGA - discriminator column cod_p_c doesn''t have value 1');
    END IF;
  EXCEPTION
  WHEN NO_DATA_FOUND THEN
    NULL;
  WHEN OTHERS THEN
    RAISE;
  END;
  /
CREATE OR REPLACE TRIGGER ARC_FKArc_1_PAREJA BEFORE
  INSERT OR
  UPDATE OF cod_p_c ON PAREJA FOR EACH ROW DECLARE d NUMBER (12);
  BEGIN
    SELECT A.cod_p_c INTO d FROM CARGA A WHERE A.cod_p_c = :new.cod_p_c;
    IF (d IS NULL OR d <> 2) THEN
      raise_application_error(-20223,'FK PAREJA_CARGA_FK in Table PAREJA violates Arc constraint on Table CARGA - discriminator column cod_p_c doesn''t have value 2');
    END IF;
  EXCEPTION
  WHEN NO_DATA_FOUND THEN
    NULL;
  WHEN OTHERS THEN
    RAISE;
  END;
  /

CREATE OR REPLACE TRIGGER ARC_FKArc_2_POSTULANTE BEFORE
  INSERT OR
  UPDATE OF cod_persona ON POSTULANTE FOR EACH ROW DECLARE d NUMBER (3);
  BEGIN
    SELECT A.cod_persona
    INTO d
    FROM PERSONA A
    WHERE A.cod_persona = :new.cod_persona;
    IF (d              IS NULL OR d <> 2) THEN
      raise_application_error(-20223,'FK POSTULANTE_PERSONA_FK in Table POSTULANTE violates Arc constraint on Table PERSONA - discriminator column cod_persona doesn''t have value 2');
    END IF;
  EXCEPTION
  WHEN NO_DATA_FOUND THEN
    NULL;
  WHEN OTHERS THEN
    RAISE;
  END;
  /
CREATE OR REPLACE TRIGGER ARC_FKArc_2_AFILIADO BEFORE
  INSERT OR
  UPDATE OF cod_persona ON AFILIADO FOR EACH ROW DECLARE d NUMBER (3);
  BEGIN
    SELECT A.cod_persona
    INTO d
    FROM PERSONA A
    WHERE A.cod_persona = :new.cod_persona;
    IF (d              IS NULL OR d <> 1) THEN
      raise_application_error(-20223,'FK AFILIADO_PERSONA_FK in Table AFILIADO violates Arc constraint on Table PERSONA - discriminator column cod_persona doesn''t have value 1');
    END IF;
  EXCEPTION
  WHEN NO_DATA_FOUND THEN
    NULL;
  WHEN OTHERS THEN
    RAISE;
  END;
  /


-- Oracle SQL Developer Data Modeler Summary Report:
--
-- CREATE TABLE                            36
-- CREATE INDEX                             0
-- ALTER TABLE                             77
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           4
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
--
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
--
-- REDACTION POLICY                         0
--
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
--
-- ERRORS                                   0
-- WARNINGS                                 0
