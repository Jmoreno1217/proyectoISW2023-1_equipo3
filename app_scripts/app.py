from flask import Flask, render_template, request, redirect, url_for, session
import datetime
import os
from conector import ejecutarBusqueda, insertarBorrarActualizar

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mariascookies123132'

@app.context_processor
def handle_context():
    return dict(os=os)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/iniciar_sesion")
def login():
    return render_template("login.html")

@app.route("/registrarse")
def registrarse():
    return render_template("registro.html")

@app.route("/validarl")
def validarl():
    usuario=request.args.get('user')
    contrasenia=request.args.get('pass')
    print(usuario)
    print(contrasenia)
    busqueda=ejecutarBusqueda(f'SELECT cuenta.cliente_id, cuenta.cuenta_usuario, cuenta.cuenta_contrasenia, CONCAT(cliente.cliente_nombre, \' \', cliente.cliente_apellidop) cliente_nombre, cuenta.cuenta_administrador FROM cuenta INNER JOIN cliente ON cuenta.cliente_id=cliente.cliente_id WHERE cuenta.cuenta_usuario=\'{usuario}\' AND cuenta.cuenta_contrasenia=\'{contrasenia}\';')
    """for fila in busqueda:
            for columna, valor in fila.items():
                print(f'{columna}:{valor}')"""
    if busqueda:
        for fila in busqueda:
            ##print(fila['cliente_nombre'])
            session['id']=fila['cliente_id']
            session['nombre']=fila['cliente_nombre']
            session['cuenta_administrador']=fila['cuenta_administrador']
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login', contraseniaincorrrecta=1))

@app.route("/validarr")
def validarr():
    id=generar_id_usuario()
    nombre=request.args.get('nombre')
    apellidop=request.args.get('apellidop')
    apellidom=request.args.get('apellidom')
    telefono=request.args.get('telefono')
    correo=request.args.get('correo')
    usuario=request.args.get('user')
    contrasenia=request.args.get('pass')
    tipo=0
    insertarBorrarActualizar(f'INSERT INTO cliente VALUES ({id},\'{nombre}\',\'{apellidop}\',\'{apellidom}\',\'{telefono}\',\'{correo}\');')
    insertarBorrarActualizar(f'INSERT INTO cuenta VALUES ({id},\'{usuario}\',\'{contrasenia}\',{tipo});')
    return redirect(url_for('login'))

@app.route("/cerrar_sesion")
def logout():
    if 'id' in session:
        session.pop('nombre',None)
        session.pop('id',None)
        session.pop('cuenta_administrador',None)
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

def generar_id_usuario():
        x=datetime.datetime.now()
        idbase = x.strftime("%y")+x.strftime("%m") + x.strftime("%d")+""
        idbase2 = x.strftime("%y")+x.strftime("%m") + x.strftime("%d")+"000"
        busqueda=ejecutarBusqueda(f'SELECT cliente_id FROM cuenta WHERE cliente_id LIKE \'{idbase}%\';')
        n=0
        if busqueda:
            for usuario in busqueda:
                temp = busqueda[usuario]['cuenta_id'][0:len(id)-3]
                temp2=idbase2[0:len(idbase2)-3]
                if temp == temp2:
                    n+=1
            n+=1
            n = str(n)
            id= idbase2[0:len(idbase2)-len(n)]+n
        else:
            id = x.strftime("%y")+x.strftime("%m") + x.strftime("%d")+"001"
        return(id)

if __name__ == "__main__":
    print(generar_id_usuario())
    app.run(debug=True, host='0.0.0.0')