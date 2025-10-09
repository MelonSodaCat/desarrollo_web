from flask import Flask, request, render_template, redirect, url_for, session, flash, get_flashed_messages
from utils.validations import validate_form
from database import db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os
import uuid

UPLOAD_FOLDER = 'static/imgs'

#---necesaria para los mensajes de flash
app = Flask(__name__)
app.secret_key = "secret_key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000



# --- Routes ---
@app.route("/add_aviso", methods=["GET"])
def add_aviso():

    regiones = db.get_regiones()
    comunas = db.get_comunas()
    return render_template("add_aviso.html", regiones=regiones, comunas=comunas)

@app.route("/ver_listado", methods=["GET"])
def ver_listado():
    PAGE_SIZE=5
    page = request.args.get("page", 1, type=int)

    data = []
    for aviso in db.get_avisos(page):
        
        comuna = db.get_comuna_by_id(aviso.comuna_id)
        foto = db.get_foto_by_aviso_id(aviso.id)
        foto_path = f"imgs/{foto.ruta_archivo}"
        contacto_redes_sociales=db.get_contacto_by_aviso_id(aviso.id)
        redes_sociales = [{"red_social": r.nombre, "id": r.identificador} for r in contacto_redes_sociales]
        #----datos del aviso
        data.append({
            "fecha_publicacion": aviso.fecha_ingreso,
            "fecha_entrega": aviso.fecha_entrega,
            "comuna": comuna.nombre,
            "sector": aviso.sector,
            "cantidad": aviso.cantidad,
            "tipo": aviso.tipo,
            "edad": aviso.edad,
            "unidad_medida": aviso.unidad_medida,
            "nombre": aviso.nombre,
            "foto_name": foto.nombre_archivo,
            "foto_path": foto_path, 
            "email": aviso.email,
            "desc": aviso.descripcion,
            "celular": aviso.celular, 
            "contactar_por": redes_sociales

          
        })
        total_avisos = db.count_avisos()
        #paginación
        total_pages = (total_avisos + PAGE_SIZE - 1) // PAGE_SIZE
    return render_template("ver_listado.html", data=data, page=page, total_pages=total_pages)

@app.route("/estadisticas", methods=["GET"])
def estadisticas():
    return render_template("estadisticas.html")

@app.route("/post_aviso", methods=["POST"])
def post_aviso():
    #here we get the elements of the form
    region_id = request.form.get("select-region")
    comuna_id = request.form.get("select-comuna")
    sector = request.files.get("sector")
    nombre = request.form.get("nombre")
    mail = request.form.get("email")
    phone = request.form.get("phone")
    #red_social = request.form.get("select-medio")
    tipo = request.form.get("select-mascota")
    cantidad = request.form.get("cantidad")
    edad = request.form.get("edad")
    unidad_medida = request.form.get("select-edad")
    fecha_entrega = request.form.get("fecha-entrega")
    desc = request.form.get("comments")
    files = request.files.get("files")
    validate, error_msg=validate_form(region_id, comuna_id, sector, nombre, mail, phone, tipo, cantidad, edad, unidad_medida, fecha_entrega, desc, files)

    if validate:
        # 1. generate random name for img
        _filename = hashlib.sha256(
            secure_filename(files.filename).encode("utf-8")
            ).hexdigest()
        _extension = filetype.guess(files).extension
        img_filename = f"{_filename}_{str(uuid.uuid4())}.{_extension}"

        # 2. save img as a file
        files.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))

        # 3. save in db
        
        id_aviso=db.create_aviso(comuna_id, sector, nombre, mail, phone, tipo, int(cantidad), int(edad), unidad_medida, fecha_entrega, desc)
        db.create_foto(img_filename, img_filename, id_aviso)

        flash("Hemos recibido sus datos de aviso, muchas gracias!", "success")
        return redirect(url_for("index"))
    else:
        error_text = f"Los siguientes campos tienen errores: \n" + ", ".join(error_msg)
        flash(error_text, "error")
        return redirect(url_for("add_aviso"))

@app.route("/", methods=["GET"])
def index():
    msg = request.args.get("msg")
    data = []
    for aviso in db.get_avisos():
        

        comuna = db.get_comuna_by_id(aviso.comuna_id)
        foto = db.get_foto_by_aviso_id(aviso.id)
        foto_path = f"imgs/{foto.ruta_archivo}"


        data.append({
            "fecha_publicacion": aviso.fecha_ingreso,
            "comuna": comuna.nombre,
            "sector": aviso.sector,
            "cantidad": aviso.cantidad,
            "tipo": aviso.tipo,
            "edad": aviso.edad,
            "unidad_medida": aviso.unidad_medida,
            "foto_name": foto.nombre_archivo,
            "foto_path": foto_path
          
        })
    messages = get_flashed_messages(with_categories=True)
    return render_template("bienvenida.html", data=data, messages=messages)


if __name__ == "__main__":
    app.run(debug=True)
