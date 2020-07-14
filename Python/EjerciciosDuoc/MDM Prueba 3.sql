-- crea usuario y le da derechos para ver e ingresar datos.
create user ingresador identified by ingresadOr;
grant connect, resource to ingresador;
