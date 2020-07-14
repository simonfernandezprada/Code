import re
s = "Se	requiere	implementar	en	un	consultorio	médico	un	sistema	que	permita	administrar	los	datos	de	pacientes.	El	aplicativo	debe	tener	un	menú	con	3 opciones:"

re.sub('\s{2,}', ' ', s)
print(s)
