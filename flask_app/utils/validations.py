import re
import filetype
from datetime import datetime, timedelta

from database import db

#opcionales
def validate_sector(value):
    if (not value):
        return True
    else:
        return len(value) <= 100

def validate_phone(value):
    if (not value):
        return True
    else: 
        return bool(re.fullmatch(r"^\+569\.\d{8}$", value))
    
def validate_desc(value):
    if (not value):
        return True
    else:
        return len(value) <= 500
    
def validate_social_media(value):
    if value:
        allowed=["whatsapp", "telegram", "X", "instagram", "tiktok", "otra"]
        return value in allowed 
    return True
def validate_social_media_id(value):
    if len(value) < 4 or len(value) > 50:
        return False
    
#obligatorio

def validate_comuna(id):
    return db.get_comuna_by_id(id) is not None

def validate_name(value):
    if not value:
        return False
    return len(value) >=3 and len(value) <=200
  
def validate_region(id):
    return db.get_region_by_id(id) is not None

def validate_tipo(value):
    allowed=["gato", "perro"]
    return value in allowed

def validate_edad_medida(value):
    allowed=["m", "a"]
    return value in allowed

def validate_number(value):
    return 1 <= int(value)

def validate_email(value):
    if not value:
        return False
    return "@" in value and len(value) < 100


def validateDate(value):
    if not value:
        return False
    pattern = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}"
    if not re.fullmatch(pattern, value):
        return False
    try:
        input_date = datetime.strptime(value, "%Y-%m-%dT%H:%M")
    except ValueError:
        return False

    return True
def validateTimeDelta(value):
    try:
        date = datetime.strptime(value, "%Y-%m-%dT%H:%M")
    except ValueError:
        return False
    curr_date = datetime.now() + timedelta(hours=3)
    return date >= curr_date





def validate_files(files):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png"}

    # check if a file was submitted
    if files is None:
        return False

    # check if the browser submitted an empty file
    if files.filename == "":
        return False
    
    # check file extension
    ftype_guess = filetype.guess(files)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True


def validate_form(region_id, comuna_id, sector, nombre, mail, phone,
                  tipo, cantidad, edad, unidad_medida, fecha_entrega, desc, files):
    invalid_inputs = []
    is_valid = True

    def set_invalid_input(input_name):
        nonlocal is_valid
        invalid_inputs.append(input_name)
        is_valid = False

    # Validation logic
    if not validate_region(region_id):
        print(f"Invalid Región: {region_id}")
        set_invalid_input("Región")

    if not validate_comuna(comuna_id):
        print(f"Invalid Comuna: {comuna_id}")
        set_invalid_input("Comuna")

    if not validate_sector(sector):
        print(f"Invalid Sector: {sector}")
        set_invalid_input("Sector")

    if not validate_name(nombre):
        print(f"Invalid Nombre: {nombre}")
        set_invalid_input("Nombre")

    if not validate_email(mail):
        print(f"Invalid Email: {mail}")
        set_invalid_input("Email")

    if not validate_phone(phone):
        print(f"Invalid Número de Celular: {phone}")
        set_invalid_input("Número de Celular")

    if not validate_tipo(tipo):
        print(f"Invalid Tipo: {tipo}")
        set_invalid_input("Tipo")

    if not validate_edad_medida(unidad_medida):
        print(f"Invalid Unidad de medida edad: {unidad_medida}")
        set_invalid_input("Unidad de medida edad")

    if not validate_number(cantidad):
        print(f"Invalid Cantidad: {cantidad}")
        set_invalid_input("Cantidad")

    if not validate_number(edad):
        print(f"Invalid Edad: {edad}")
        set_invalid_input("Edad")

    if not validate_files(files):
        print(f"Invalid Fotos: {files}")
        set_invalid_input("Fotos")

    if not (validateDate(fecha_entrega) and validateTimeDelta(fecha_entrega)):
        print(f"Invalid Fecha Disponible para entrega: {fecha_entrega}")
        set_invalid_input("Fecha Disponible para entrega")

    if not validate_desc(desc):
        print(f"Invalid Descripción: {desc}")
        set_invalid_input("Descripción")

    return is_valid, invalid_inputs




