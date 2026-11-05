# 🚀 Guía de Inicio Rápido - Nexus-Fin

## ⏱️ Tiempo estimado: 5 minutos

---

## Opción 1: Script Automático (Windows)

### Paso 1: Ejecutar el script de inicio

Doble clic en:

```
start.bat
```

Este script automáticamente:
- ✅ Crea el entorno virtual si no existe
- ✅ Instala todas las dependencias
- ✅ Copia el archivo `.env.example` a `.env`
- ✅ Inicia la aplicación Streamlit

### Paso 2: Configurar API Key (Opcional)

Si quieres usar el LLM real (recomendado):

1. Obtén tu API Key: https://openrouter.ai/keys
2. Abre el archivo `.env` con un editor de texto
3. Reemplaza `tu_clave_aqui` con tu clave real
4. Guarda el archivo
5. Reinicia la aplicación

---

## Opción 2: Manual (Windows/Linux/Mac)

### Paso 1: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 2: Configurar API Key (Opcional)

```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

Edita `.env` y añade tu clave de OpenRouter.

### Paso 3: Ejecutar la aplicación

```bash
streamlit run app.py
```

---

## 🎮 Primer Uso

1. **Barra lateral izquierda**: Selecciona un escenario
   - 📈 Entorno Estable (para probar el motor predictivo)
   - ⚡ Shock de Liquidez (para probar el motor adaptativo)

2. **Configuración de API**: 
   - Si tienes API Key, introdúcela aquí
   - Si no, déjala como está (usará lógica heurística)

3. **Clic en "🚀 Ejecutar Análisis"**

4. **Observa**:
   - El LLM decidirá la ruta (A o B)
   - Verás el gráfico interactivo con la trayectoria
   - Lee el razonamiento completo del agente

---

## 🧪 Prueba Rápida sin API Key

La aplicación funciona perfectamente sin API Key usando lógica heurística:

1. Ejecuta `streamlit run app.py`
2. Selecciona "📈 Entorno Estable"
3. Clic en "🚀 Ejecutar Análisis"
4. Verás la Ruta A (Motor Predictivo) activada automáticamente

---

## ❓ Problemas Comunes

### "python no se reconoce como comando"

Instala Python 3.11+ desde: https://www.python.org/downloads/

Durante la instalación, marca la opción "Add Python to PATH".

### "streamlit no se reconoce como comando"

```bash
pip install streamlit
```

### El navegador no se abre

Abre manualmente: http://localhost:8501

---

## 🎉 ¡Listo!

Ahora deberías ver la interfaz de Nexus-Fin en tu navegador.

**Siguiente paso**: Lee el `README.md` completo para entender la arquitectura del sistema.
