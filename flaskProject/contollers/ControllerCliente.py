from flask import Blueprint, request, render_template, flash, url_for
from random import randint

cliente_blueprint = Blueprint('cliente', __name__, url_prefix='/cliente')

@cliente_blueprint.route('/') #localhost:5000/cliente/
def ver_clientes():
    return "select * from cliente"

#responde a localhost:5000/cliente/id/1
@cliente_blueprint.route('/id/<int:id_cliente>/<string:nombre>') #<tipo:nombre_variable>
def ver_cliente_id(id_cliente, nombre):
    return f"Se hace el query con el id {id_cliente} y el nombre {nombre}"


@cliente_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_cliente():
    if request.method == 'GET':
        return render_template('add_user.html')
    else:
        #Obtengo la información del método post
        name = request.form['name']
        ap_pat = request.form['ap_pat']
        ap_mat = request.form['ap_mat']
        num_cta = request.form['num_cta']
        passwd = request.form['passwd']
        #Creo mi usuario.
        #cliente = cliente(name, ap....)
        #Lo guardo en la DB
        #url_for
        #flash
        v = randint(0, 2)
        if v == 1:
            flash("Hello from flash!")
            return url_for('cliente.agregar_cliente')
        # Y regreso al flujo que me hayan especificado.
        return render_template('user_added.html', name=name, num_cta=num_cta)