sSELECT PRIMER_NOMBRE,SEGUNDO_NOMBRE,PRIMER_APELLIDO,SEGUNDO_APELLIDO,CASE ESTADO_MEMBRESIA 
  WHEN '0' THEN 'DESHABILITADO'
END AS ESTADO
FROM AFILIADO, PERSONA
WHERE PERSONA.COD_PERSONA = AFILIADO.COD_PERSONA AND AFILIADO.ESTADO_MEMBRESIA = 0;
