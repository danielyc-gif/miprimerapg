from flask import Flask, request, redirect, render_template, session, flash
import hashlib
import json
import os

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_muy_segura_aqui'  # Cambia esto por una clave segura

# Archivos para almacenar datos
USERS_FILE = 'users.json'
TAREAS_FILE = 'tareas.json'

def cargar_usuarios():
    """Carga los usuarios desde el archivo JSON"""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def guardar_usuarios(usuarios):
    """Guarda los usuarios en el archivo JSON"""
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=2)

def cargar_tareas():
    """Carga las tareas del usuario actual"""
    if 'user_id' not in session:
        return []
    
    if os.path.exists(TAREAS_FILE):
        with open(TAREAS_FILE, 'r', encoding='utf-8') as f:
            todas_tareas = json.load(f)
            return todas_tareas.get(session['user_id'], [])
    return []

def guardar_tareas(tareas):
    """Guarda las tareas del usuario actual"""
    if 'user_id' not in session:
        return
    
    if os.path.exists(TAREAS_FILE):
        with open(TAREAS_FILE, 'r', encoding='utf-8') as f:
            todas_tareas = json.load(f)
    else:
        todas_tareas = {}
    
    todas_tareas[session['user_id']] = tareas
    
    with open(TAREAS_FILE, 'w', encoding='utf-8') as f:
        json.dump(todas_tareas, f, ensure_ascii=False, indent=2)

def hash_password(password):
    """Crea un hash de la contraseña"""
    return hashlib.sha256(password.encode()).hexdigest()

def agregar_tarea(texto):
    """Agrega una nueva tarea para el usuario actual"""
    tareas = cargar_tareas()
    siguiente_id = max([t['id'] for t in tareas], default=0) + 1
    
    tareas.append({
        'id': siguiente_id,
        'texto': texto,
        'hecho': False
    })
    guardar_tareas(tareas)

def completar_tarea(id):
    """Marca una tarea como completada"""
    tareas = cargar_tareas()
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['hecho'] = True
            break
    guardar_tareas(tareas)

def eliminar_tarea(id):
    """Elimina una tarea del usuario actual"""
    tareas = cargar_tareas()
    tareas = [tarea for tarea in tareas if tarea['id'] != id]
    guardar_tareas(tareas)

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect('/login')
    
    # Ordenar tareas: incompletas primero, luego completadas
    tareas = cargar_tareas()
    tareas_ordenadas = sorted(tareas, key=lambda t: t['hecho'])
    return render_template('index.html', tareas=tareas_ordenadas)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        usuarios = cargar_usuarios()
        
        if username in usuarios and usuarios[username]['password'] == hash_password(password):
            session['user_id'] = username
            flash('¡Bienvenido!', 'success')
            return redirect('/')
        else:
            flash('Usuario o contraseña incorrectos', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if not username or not password:
            flash('Todos los campos son obligatorios', 'error')
            return render_template('register.html')
        
        if password != confirm_password:
            flash('Las contraseñas no coinciden', 'error')
            return render_template('register.html')
        
        if len(password) < 6:
            flash('La contraseña debe tener al menos 6 caracteres', 'error')
            return render_template('register.html')
        
        usuarios = cargar_usuarios()
        
        if username in usuarios:
            flash('El usuario ya existe', 'error')
            return render_template('register.html')
        
        usuarios[username] = {
            'password': hash_password(password),
            'created_at': '2024-01-01'  # Fecha de creación
        }
        
        guardar_usuarios(usuarios)
        flash('¡Usuario creado exitosamente!', 'success')
        return redirect('/login')
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('¡Hasta luego!', 'info')
    return redirect('/login')

@app.route('/agregar', methods=['POST'])
def agregar():
    if 'user_id' not in session:
        return redirect('/login')
    
    texto_tarea = request.form.get('texto_tarea')
    if texto_tarea:
        agregar_tarea(texto_tarea)
        flash('Tarea agregada exitosamente!', 'success')
    
    return redirect('/')

@app.route('/completar/<int:id>')
def completar(id):
    if 'user_id' not in session:
        return redirect('/login')
    
    completar_tarea(id)
    return redirect('/')

@app.route('/eliminar/<int:id>')
def eliminar(id):
    if 'user_id' not in session:
        return redirect('/login')
    
    eliminar_tarea(id)
    flash('Tarea eliminada exitosamente!', 'success')
    return redirect('/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)