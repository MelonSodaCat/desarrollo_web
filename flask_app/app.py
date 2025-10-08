from flask import Flask, request, render_template, redirect, url_for, session
from utils.validations import validate_login_user, validate_register_user, validate_confession
from database import db
from werkzeug.utils import secure_filename
import hashlib
#import filetype
import os

UPLOAD_FOLDER = 'static/imgs'


app = Flask(__name__)



# --- Routes ---
@app.route("/add_aviso", methods=["GET"])
def add_aviso():

    regiones = db.get_regiones()
    comunas = db.get_comunas()
    return render_template("add_aviso.html", regiones=regiones, comunas=comunas)

@app.route("/ver_listado", methods=["GET"])
def ver_listado():
    return render_template("ver_listado.html")

@app.route("/estadisticas", methods=["GET"])
def estadisticas():
    return render_template("estadisticas.html")

@app.route("/aviso_conf", methods=["POST"])
def aviso_conf():
    if validate_confession():
        pass


@app.route("/", methods=["GET"])
def index():
    PAGE_SIZE = 5
    data = []
    for aviso in db.get_avisos(page_size=PAGE_SIZE):
        

        comuna = db.get_comuna_by_id(aviso.comuna_id)
        foto = db.get_foto_by_actv_id(aviso.id)
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

    
    
    return render_template("bienvenida.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
