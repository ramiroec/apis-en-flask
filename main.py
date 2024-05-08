import psycopg2
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Configuración de la conexión a la base de datos
db_connection = psycopg2.connect(
    "postgresql://bzvpsdcz:0RmfG9N5OyThBp8SC1oxQEnGin-bNjx5@isabelle.db.elephantsql.com/bzvpsdcz"
)

# Función para ejecutar consultas SQL y obtener los resultados
def execute_query(query):
    with db_connection.cursor() as cursor:
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results

# API para listar productos
@app.route('/api/productos')
def listar_productos():
    query = "SELECT * FROM productos;"
    results = execute_query(query)
    return jsonify(results)

# API para listar empleados
@app.route('/api/empleados')
def listar_empleados():
    query = "SELECT * FROM empleados;"
    results = execute_query(query)
    return jsonify(results)

# API para listar clientes
@app.route('/api/clientes')
def listar_clientes():
    query = "SELECT * FROM clientes;"
    results = execute_query(query)
    return jsonify(results)
  
# Ruta por defecto con tres enlaces

@app.route('/')
def index():
    return '''
  <h1>APIs Disponibles:</h1>
  <ul>
    <li><a href="/api/clientes">Clientes</a></li>
    <li><a href="/api/empleados">Empleados</a></li>
    <li><a href="/api/productos">Productos</a></li>
  </ul>
    '''

@app.route('/empleados')
def mostrar_empleados():
    query = "SELECT * FROM empleados;"
    results = execute_query(query)
    return render_template('empleados.html', empleados=results)

app.run(host='0.0.0.0', port=81)
