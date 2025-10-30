# 🚀 Guía de Deployment - ICFES App

## ⚠️ ANTES DE SUBIR A PRODUCCIÓN

### 1. Configurar Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto (NO lo subas a Git):

```bash
GOOGLE_API_KEY=tu_api_key_de_google_gemini
FLASK_ENV=production
SECRET_KEY=genera_una_clave_secreta_aleatoria
```

### 2. Verificar que `.gitignore` existe
```bash
# Verifica que estos archivos NO se suban:
- .env
- __pycache__/
- *.pyc
```

### 3. Deployment en Render/Railway/Heroku

#### Variables de Entorno a Configurar:
- `GOOGLE_API_KEY`: Tu API key de Google Gemini
- `FLASK_ENV`: `production`
- `SECRET_KEY`: Clave secreta aleatoria

#### Comando de Inicio:
```bash
gunicorn app:application
```

### 4. Checklist de Seguridad

- [x] Archivo `.env` creado y NO incluido en Git
- [x] Variables de entorno configuradas en plataforma de deployment
- [x] API keys removidas del código fuente
- [x] `.gitignore` configurado correctamente
- [x] `debug=False` en producción (ya configurado con gunicorn)
- [x] Usuarios demo eliminados
- [x] CORS configurado apropiadamente para tu dominio (actualiza origins en icfes_api.py con tu dominio de producción)

### 5. Testing Local

```bash
# Instalar dependencias
pip install -r requirements.txt

# Crear archivo .env con tus credenciales

# Ejecutar en modo desarrollo
python app.py

# Ejecutar en modo producción (local)
gunicorn app:application
```

## 📝 Notas Importantes

- **NUNCA** subas archivos `.env` a Git
- **NUNCA** hardcodees API keys en el código
- Usa variables de entorno en todas las plataformas
- El archivo `.env.example` muestra qué variables necesitas (sin valores reales)
- La autenticación se maneja completamente con Supabase (frontend)

## 🔒 Seguridad Frontend (Supabase)

Las credenciales de Supabase están en `static/js/config.js`:
- En desarrollo: usa valores por defecto
- En producción: configura `window.ENV` en tu servidor

## 📊 Endpoints Disponibles

- POST /generate-question - Generar preguntas ICFES
- POST /get-feedback - Retroalimentación individual
- POST /analyze-document - Análisis PDF/Word completo
- POST /generate-visual - Generar gráficos (bar/pie)
- POST /save-model - Guardar modelo entrenado
- GET /users - Lista de usuarios
- GET /health - Estado del sistema