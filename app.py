from flask import render_template, redirect, request, session, jsonify
from icfes_api import app

# Rutas de páginas (Front)
@app.route('/')
@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard_page():
    # Verificar si el usuario está logueado y es profesor
    if 'user_type' not in session or session['user_type'] != 'profesor':
        return redirect('/login')
    return render_template('dashboard_profesor.html')

@app.route('/dashboard-estudiante')
def dashboard_estudiante_page():
    # Verificar si el usuario está logueado y es estudiante
    if 'user_type' not in session or session['user_type'] != 'estudiante':
        return redirect('/login')
    return render_template('dashboard_estudiante.html')

@app.route('/simulator')
def simulator_page():
    # Verificar si el usuario está logueado como estudiante
    if 'user_type' not in session or session['user_type'] != 'estudiante':
        return redirect('/login')
    return render_template('icfes_exam_simulator.html')

@app.route('/generator')
def generator_page():
    # Ambos tipos de usuario pueden acceder al generador de preguntas
    if 'user_type' not in session:
        return redirect('/login')
    return render_template('icfes_generator_mcq.html')

@app.route('/pdf-evaluation')
def pdf_evaluation_page():
    # Verificar si el usuario está logueado como profesor
    if 'user_type' not in session or session['user_type'] != 'profesor':
        return redirect('/login')
    return render_template('icfes_pdf_evaluation.html')

@app.route('/order-exercise')
def order_exercise_page():
    # Verificar si el usuario está logueado como estudiante
    if 'user_type' not in session or session['user_type'] != 'estudiante':
        return redirect('/login')
    return render_template('icfes_order_exercise.html')

@app.route('/progress')
def progress_page():
    # Verificar si el usuario está logueado como estudiante
    if 'user_type' not in session or session['user_type'] != 'estudiante':
        return redirect('/login')
    return render_template('progress.html')

@app.route('/chat')
def chat_page():
    # Ambos tipos de usuario pueden acceder al chat
    if 'user_type' not in session:
        return redirect('/login')
    return render_template('chat.html')

@app.route('/library')
def library_page():
    # Verificar si el usuario está logueado como profesor
    if 'user_type' not in session or session['user_type'] != 'profesor':
        return redirect('/login')
    return render_template('library.html')

@app.route('/reorder')
def reorder_page():
    # Verificar si el usuario está logueado como estudiante
    if 'user_type' not in session or session['user_type'] != 'estudiante':
        return redirect('/login')
    return render_template('icfes_order_exercise.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    cedula = data.get('cedula')
    user_type = data.get('user_type')

    if not cedula or not user_type:
        return jsonify({'success': False, 'message': 'Datos incompletos'}), 400

    # Para demo, aceptamos cualquier cédula válida
    # En producción, aquí validarías contra una base de datos
    if len(cedula) >= 6:
        session['user_type'] = user_type
        session['cedula'] = cedula
        return jsonify({'success': True, 'redirect': '/dashboard' if user_type == 'profesor' else '/dashboard-estudiante'})
    else:
        return jsonify({'success': False, 'message': 'Cédula inválida'}), 400

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    import os
    host = '0.0.0.0' if os.getenv('FLASK_ENV') == 'production' else '127.0.0.1'
    debug_mode = os.getenv('FLASK_ENV') != 'production'
    app.run(debug=debug_mode, host=host, port=5000)
else:
    # Para producción con gunicorn
    application = app
