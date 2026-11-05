# 🚀 Guía de Despliegue en Streamlit Cloud

## Despliegue Rápido (5 minutos)

---

## Opción 1: Streamlit Cloud (Recomendado)

### Paso 1: Preparar el Repositorio

✅ **Ya está hecho** - El repositorio está en GitHub:
```
https://github.com/AngelTroncoso/Nexus-Fin
```

### Paso 2: Acceder a Streamlit Cloud

1. Ve a: https://share.streamlit.io
2. Inicia sesión con tu cuenta de GitHub
3. Haz clic en "New app"

### Paso 3: Configurar la App

**Configuración básica:**
- **Repository**: `AngelTroncoso/Nexus-Fin`
- **Branch**: `main`
- **Main file path**: `app.py`
- **App URL** (personalizable): `nexus-fin-yourname`

### Paso 4: Variables de Entorno (Opcional)

Si quieres usar el LLM real:

1. En "Advanced settings"
2. Sección "Secrets"
3. Añade:

```toml
OPENROUTER_API_KEY = "tu_clave_real_aqui"
OPENROUTER_MODEL = "nvidia/nemotron-3-nano-30b-a3b:free"
```

**Obtener API Key:** https://openrouter.ai/keys

### Paso 5: Deploy

1. Clic en "Deploy!"
2. Espera 2-3 minutos
3. ✅ ¡Listo! Tu app estará en: `https://nexus-fin-yourname.streamlit.app`

---

## Opción 2: Despliegue Local

### Con Docker

```bash
# 1. Crear Dockerfile (ya incluido en el repo)
docker build -t nexus-fin .

# 2. Ejecutar contenedor
docker run -p 8501:8501 nexus-fin
```

### Sin Docker

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecutar
streamlit run app.py
```

---

## Opción 3: Otros Servicios

### Heroku

```bash
# Requiere Procfile y setup.sh
echo "web: streamlit run app.py" > Procfile
git add Procfile
git commit -m "Add Procfile for Heroku"
heroku create nexus-fin-app
git push heroku main
```

### Railway.app

1. Conecta tu repositorio de GitHub
2. Railway detecta automáticamente Streamlit
3. Deploy con un clic

### Render.com

1. New Web Service → GitHub repo
2. Build Command: `pip install -r requirements.txt`
3. Start Command: `streamlit run app.py --server.port $PORT`

---

## Configuración de Secrets en Streamlit Cloud

### Archivo `.streamlit/secrets.toml` (Local)

Para desarrollo local, crea:

```toml
# .streamlit/secrets.toml
OPENROUTER_API_KEY = "tu_clave_local"
OPENROUTER_MODEL = "nvidia/nemotron-3-nano-30b-a3b:free"
```

### En Streamlit Cloud (Producción)

1. Ve a tu app en https://share.streamlit.io
2. Settings → Secrets
3. Pega el contenido del `secrets.toml`

**Importante:** Nunca commitees `secrets.toml` a Git (ya está en `.gitignore`)

---

## Actualizar código en `app.py` para usar secrets

El código ya está preparado para usar secrets de Streamlit:

```python
import streamlit as st

# Intenta usar secrets de Streamlit Cloud primero
try:
    api_key = st.secrets.get("OPENROUTER_API_KEY", "tu_clave_aqui")
except:
    api_key = "tu_clave_aqui"
```

---

## Verificar Despliegue

Una vez desplegado, verifica:

1. ✅ La página carga correctamente
2. ✅ Los gráficos se renderizan
3. ✅ Los escenarios funcionan
4. ✅ El sistema decide entre Ruta A y B

---

## Troubleshooting

### Error: "ModuleNotFoundError"

**Solución:** Verifica que `requirements.txt` esté en el root del repo.

### Error: "API Key inválida"

**Solución:** 
1. Configura secrets en Streamlit Cloud
2. O déjalo sin configurar (funciona en modo fallback)

### La app no inicia

**Solución:** Revisa los logs en Streamlit Cloud (botón "Manage app" → "Logs")

### Gráficos no se ven

**Solución:** Refresca el navegador (Ctrl+F5)

---

## Límites de Streamlit Cloud (Plan Gratuito)

- ✅ Apps ilimitadas
- ✅ 1 GB de RAM por app
- ✅ 1 CPU compartido
- ⚠️ La app se duerme después de inactividad (se despierta en ~30 seg)

**Perfecto para:** Demos, prototipos, portfolios

---

## Compartir tu App

Una vez desplegada:

```
🌐 URL Pública: https://nexus-fin-yourname.streamlit.app
```

Puedes compartir este link directamente. No requiere autenticación.

---

## Monitoreo

Streamlit Cloud provee:

- 📊 **Analytics**: Visualizaciones de uso
- 📝 **Logs**: Debugging en tiempo real
- 🔄 **Auto-redeploy**: Se actualiza automáticamente al hacer push a GitHub

---

## Buenas Prácticas

1. ✅ Usa secrets para API keys
2. ✅ No commitees archivos `.env`
3. ✅ Configura `.gitignore` correctamente (ya está)
4. ✅ Prueba localmente antes de desplegar
5. ✅ Documenta las variables de entorno necesarias

---

## Costo

### Streamlit Cloud
- **Gratis**: Ilimitado para apps públicas
- **Team**: $250/mes (apps privadas)

### OpenRouter API
- **Gemini Flash 1.5**: ~$0.001 por decisión
- **Costo estimado**: <$1/mes para uso demo

---

## Próximos Pasos

1. ✅ Despliega en Streamlit Cloud
2. ✅ Configura tu API Key (opcional)
3. ✅ Comparte el link
4. ✅ Añade el badge a tu README:

```markdown
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://nexus-fin-yourname.streamlit.app)
```

---

## URLs Útiles

- **Streamlit Cloud**: https://share.streamlit.io
- **Docs de Deploy**: https://docs.streamlit.io/streamlit-community-cloud
- **OpenRouter**: https://openrouter.ai
- **Repositorio**: https://github.com/AngelTroncoso/Nexus-Fin

---

**¿Problemas?** Revisa los logs en Streamlit Cloud o ejecuta `python test_system.py` localmente.

**¡Listo para desplegar!** 🚀
