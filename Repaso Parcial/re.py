"""
===============================================================================
    PLANTILLAS MAESTRAS - EXPRESIONES REGULARES (re)
===============================================================================
"""
import re

# =============================================================================
# 1. VALIDAR PLACA DE VEHÍCULO (Colombia: AAA123 o AAA-123)
# =============================================================================
def validar_placa(placa):
    # ^[A-Z]{3} -> Exactamente 3 letras mayúsculas al inicio
    # -?        -> El guion es opcional
    # \d{3}$    -> Exactamente 3 dígitos al final
    patron = r"^[A-Z]{3}-?\d{3}$"
    return bool(re.match(patron, placa))


# =============================================================================
# 2. VALIDAR CORREO ELECTRÓNICO (usuario@dominio.extension)
# =============================================================================
def validar_correo(correo):
    # [\w.-]+   -> Caracteres de usuario (letras, números, puntos, guiones)
    # @         -> Arroba obligatoria
    # [a-zA-Z0-9.-]+ -> Nombre del dominio
    # \.[a-zA-Z]{2,} -> Punto seguido de extensión (mínimo 2 letras, ej: .com, .co)
    patron = r"^[\w.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(patron, correo))


# =============================================================================
# 3. VALIDAR CONTRASEÑA SEGURA (Mínimo 8 caracteres, mayúscula, minúscula, número y especial)
# =============================================================================
def validar_contrasena(contrasena):
    # La forma más limpia y robusta sin enredarse con lookaheads complejos
    if len(contrasena) < 8:
        return False
    
    tiene_mayuscula = bool(re.search(r"[A-Z]", contrasena))
    tiene_minuscula = bool(re.search(r"[a-z]", contrasena))
    tiene_numero    = bool(re.search(r"\d", contrasena))
    tiene_especial  = bool(re.search(r"[@#$%&!*-_]", contrasena))
    
    return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial


# =============================================================================
# 4. EXTRAER DATOS DE UN TEXTO (URLs o Números)
# =============================================================================
def extraer_urls(texto):
    # Busca enlaces que empiecen con http://, https:// o www.
    patron = r"(https?://\S+|www\.\S+)"
    return re.findall(patron, texto)

def extraer_numeros(texto):
    # Busca números enteros o decimales (ej: 19.99, 50, 1000.5)
    patron = r"\d+(?:\.\d+)?"
    return re.findall(patron, texto)
#DICCIONARIO
^: Inicio de la cadena.

$: Fin de la cadena.

\d: Un dígito (del 0 al 9).

\w: Un carácter de palabra (letras, números y guion bajo _).

[A-Z]: Una letra mayúscula.

[a-z]: Una letra minúscula.

{3}: Ocurre exactamente 3 veces.

{2,}: Ocurre 2 o más veces.

?: Opcional (0 o 1 vez).

+: 1 o más veces.

re.match(): Compara desde el inicio del texto (para validar todo el formato).

re.search(): Busca si existe el patrón en cualquier parte del texto.

re.findall(): Retorna una lista con todas las coincidencias encontradas.