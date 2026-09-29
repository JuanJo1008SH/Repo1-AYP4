roles = {
    "admin": {
        "leer", "escribir", "eliminar", "crear_usuarios",
        "ver_logs", "configurar", "backup", "restaurar"
    },
    "editor": {"leer", "escribir", "subir_archivos"},
    "viewer": {"leer"},
    "moderador": {"leer", "escribir", "eliminar", "ver_logs"},
    "auditor": {"leer", "ver_logs", "exportar_reportes"},
}
usuarios = {
    "Juan": "admin",
    "María": "editor",
    "Pedro": "viewer",
    "Ana": "moderador",
    "Carlos": "auditor",
}

#CREAR UN METODO QUE RECIBA UN CONJUNTO DE ACCIONES Y UN USUARIO, Y RETORNE TRUE O FALSE
#DEPENDIENDO SI EL USUARIO PUEDE O NO REALIZAR TODo ESE CONJUNTO DE ACCIONES

def validar_acciones(usuario, acciones):
    rol = usuarios.get(usuario)
    if not rol:
        return False
    permisos_del_rol = roles.get(rol, set())
    return acciones <= permisos
print (validar_acciones("Ana",{"leer"}))

#Determinar permisos exclusivos de cada rol

def obtener_permisos_exclusivos(rol):
    permisos_rol = roles.get(rol, set())
    otros_permisos = set()
    for nombre_rol, permisos in roles.items():
        if nombre_rol != rol:
            otros_permisos = otros_permisos | permisos
    exclusivos = permisos_rol - otros_permisos
    if exclusivos:
        print(f"Los permisos exclusivos del rol {rol} son {exclusivos}")
    else:
        print(f"El rol {rol} no tiene permisos exclusivos")        
    return exclusivos
