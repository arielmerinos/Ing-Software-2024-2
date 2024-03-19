from flask import Blueprint, request, render_template, flash, url_for
from random import randint

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/') #localhost:5000/pelicula/
def ver_peliculas():
    return "select * from pelicula"

#responde a localhost:5000/pelicula/id/1
@pelicula_blueprint.route('/id/<int:id_pelicula>/<string:nombre>') #<tipo:nombre_variable>
def ver_pelicula_id(id_pelicula, nombre):
    return f"Se hace el query con el id {id_pelicula} y el nombre {nombre}"


@pelicula_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'GET':
        return render_template('add_user.html')
    else:
        #Obtengo la información del método post.
        name = request.form['name']
        ap_pat = request.form['ap_pat']
        ap_mat = request.form['ap_mat']
        num_cta = request.form['num_cta']
        passwd = request.form['passwd']
        #Creo mi usuario.
        #pelicula = pelicula(name, ap....)
        #Lo guardo en la DB
        #url_for
        #flash
        v = randint(0, 2)
        if v == 1:
            flash("Hello from flash!")
            return url_for('pelicula.agregar_pelicula')
        # Y regreso al flujo que me hayan especificado.
        return render_template('user_added.html', name=name, num_cta=num_cta)