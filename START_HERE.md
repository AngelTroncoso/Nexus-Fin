# 🚀 ¡Bienvenido a Nexus-Fin!

## Motor de Decisiones Autónomas para Gestión de Tesorería

---

## 👋 Empieza Aquí

Este es tu punto de entrada al proyecto **Nexus-Fin**, un sistema multiagente que usa **IA (LLM)** para tomar decisiones financieras autónomas en tiempo real.

---

## ⚡ Inicio Súper Rápido (2 minutos)

### Opción 1: Script Automático (Windows)

**Doble clic en:**

```
start.bat
```

✨ ¡Eso es todo! El script instalará todo y abrirá la aplicación.

---

### Opción 2: Manual (Cualquier sistema)

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecutar aplicación
streamlit run app.py
```

**La aplicación se abrirá en:** http://localhost:8501

---

## 📖 ¿Primera Vez? Lee Esto

### 1️⃣ ¿Qué es Nexus-Fin? (2 minutos)

Nexus-Fin es un **sistema de decisión autónoma** que:

- 🧠 Analiza el entorno financiero (volatilidad, liquidez, shocks)
- 🤖 Consulta a un LLM (vía OpenRouter API)
- 🎯 Decide entre dos estrategias:
  - **Ruta A**: Proyecciones predictivas (entornos estables)
  - **Ruta B**: Control adaptativo (crisis y volatilidad)
- 📊 Visualiza los resultados en gráficos interactivos
- 💬 Explica su razonamiento en formato JSON

### 2️⃣ ¿Qué Puedo Hacer? (3 minutos)

**En la interfaz Streamlit podrás:**

✅ Seleccionar entre escenarios: Estable vs. Shock de Liquidez  
✅ Ver cómo el LLM decide la estrategia óptima  
✅ Explorar proyecciones de flujo de caja interactivas  
✅ Leer el razonamiento completo del agente de IA  
✅ Analizar métricas como volatilidad, rebalanceos, etc.  

### 3️⃣ ¿Necesito una API Key? (1 minuto)

**Respuesta corta:** No es obligatorio.

- ✅ **Con API Key** (OpenRouter): El LLM real decide la estrategia
- ✅ **Sin API Key**: El sistema usa lógica heurística (fallback)

**Obtener API Key gratis:** https://openrouter.ai/keys

**Configurar:**
1. Copia `.env.example` a `.env`
2. Añade tu clave en `OPENROUTER_API_KEY`

---

## 📚 Documentación Disponible

Tenemos **documentación exhaustiva** para todos los perfiles:

| Documento | Para Quién | Tiempo |
|-----------|------------|--------|
| **[RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md)** | Todos | 5 min |
| **[QUICKSTART.md](QUICKSTART.md)** | Usuarios | 5 min |
| **[README.md](README.md)** | Todos | 15 min |
| **[EXAMPLES.md](EXAMPLES.md)** | Analistas | 20 min |
| **[ARCHITECTURE.md](ARCHITECTURE.md)** | Desarrolladores | 30 min |
| **[INDEX.md](INDEX.md)** | Navegación | 5 min |

---

## 🎯 Tu Primera Ejecución (5 minutos)

### Paso 1: Ejecutar la App

```bash
streamlit run app.py
```

O doble clic en `start.bat` (Windows)

### Paso 2: En la Barra Lateral

1. **Escenario**: Selecciona "📈 Entorno Estable"
2. **API Key**: Déjala como está (funciona sin ella)
3. **Horizonte**: Deja 90 días
4. **Balance**: Deja $2,000,000

### Paso 3: Ejecutar Análisis

Clic en: **🚀 Ejecutar Análisis**

### Paso 4: Observar

🎊 **¡Felicidades!** Acabas de ver:

- ✅ La decisión del sistema (probablemente Ruta A)
- ✅ Un gráfico interactivo de proyección
- ✅ El razonamiento del agente
- ✅ Métricas financieras

### Paso 5: Probar el Otro Escenario

1. Cambia a: "⚡ Shock de Liquidez Crítico"
2. Clic en: **🚀 Ejecutar Análisis**
3. Observa cómo el sistema decide **Ruta B** (adaptativo)
4. Ve los eventos de shock en el gráfico

---

## 🧪 Verificar que Todo Funciona

Ejecuta los tests del sistema:

```bash
python test_system.py
```

Deberías ver:

```
✅ Test de Creación de Escenarios: PASADO
✅ Test de Router Fallback: PASADO
✅ Test de Motor Predictivo: PASADO
✅ Test de Motor Adaptativo: PASADO
✅ Test de Integración: PASADO

🎉 ¡TODOS LOS TESTS PASARON!
```

---

## 🎓 Aprender Más

### Usuarios No Técnicos

1. Lee [RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md)
2. Ejecuta la app y experimenta
3. Lee [EXAMPLES.md](EXAMPLES.md) - Ejemplos 1 y 2

### Analistas / Product Managers

1. Lee [README.md](README.md) completo
2. Experimenta con ambos escenarios
3. Explora [EXAMPLES.md](EXAMPLES.md) - Todos los casos

### Desarrolladores

1. Lee [ARCHITECTURE.md](ARCHITECTURE.md)
2. Estudia el código fuente (`app.py`, `router_engine.py`, `engines/`)
3. Ejecuta `python test_system.py`
4. Modifica y experimenta

---

## 🆘 Problemas Comunes

### "No arranca"

```bash
pip install -r requirements.txt
python test_system.py
```

### "Error de API"

Es normal si no configuraste `.env`. El sistema funciona en modo fallback.

### "No veo el gráfico"

Refresca el navegador (F5) y vuelve a ejecutar el análisis.

---

## 🎯 Próximos Pasos Recomendados

1. ✅ Ejecuta `streamlit run app.py`
2. ✅ Prueba ambos escenarios (Estable y Shock)
3. ✅ Lee [RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md)
4. ✅ Explora [EXAMPLES.md](EXAMPLES.md)
5. ✅ (Opcional) Configura tu API Key de OpenRouter

---

## 📊 Estructura del Proyecto

```
📁 estaticodinamico/
├── 📄 START_HERE.md           ← Estás aquí
├── 📄 INDEX.md                (Índice de documentación)
├── 📄 RESUMEN_EJECUTIVO.md    (Visión general)
├── 📄 QUICKSTART.md           (Inicio rápido)
├── 📄 README.md               (Guía completa)
├── 🧠 app.py                  (Interfaz Streamlit)
├── 🧠 router_engine.py        (Motor de decisión)
└── 📁 engines/                (Motores A y B)
```

**Documentación completa:** 8 archivos Markdown  
**Código fuente:** 6 archivos Python  
**Total líneas:** ~5,000 (código + docs)

---

## 🌟 Características Destacadas

✨ **Decisión Autónoma**: El LLM elige sin intervención  
✨ **Razonamiento Transparente**: JSON con explicación completa  
✨ **Visualización Interactiva**: Gráficos profesionales con Plotly  
✨ **Modo Fallback**: Funciona sin API key  
✨ **Documentación Exhaustiva**: 8 guías para todos los perfiles  
✨ **Tests Completos**: Suite de 5 tests automatizados  

---

## 💡 ¿Qué Hace Especial a Nexus-Fin?

### 1. Decisión Autónoma Real

No es una simulación fija. El LLM **realmente decide** basándose en el contexto.

### 2. Transparencia Total

Ves **exactamente** por qué el sistema decidió cada ruta.

### 3. Dos Paradigmas Distintos

- **Motor A**: Proyecciones matemáticas (series temporales)
- **Motor B**: Control dinámico (reacciones a shocks)

### 4. Producción-Ready Architecture

- Modular
- Testeable
- Extensible
- Documentado

---

## 🎉 ¡Listo!

Ahora tienes todo lo que necesitas para empezar.

### 🚀 Comando Mágico

```bash
streamlit run app.py
```

**O en Windows:** Doble clic en `start.bat`

---

## 📞 Más Información

- **Navegación de docs**: [INDEX.md](INDEX.md)
- **Guía completa**: [README.md](README.md)
- **Casos de uso**: [EXAMPLES.md](EXAMPLES.md)
- **Arquitectura**: [ARCHITECTURE.md](ARCHITECTURE.md)

---

## 🤝 Comunidad

**Proyecto:** Nexus-Fin v1.0.0  
**Licencia:** MIT  
**Stack:** Python | Streamlit | OpenRouter | Plotly  

---

**¿Preguntas?** → Lee [README.md](README.md)  
**¿Problemas?** → Ejecuta `python test_system.py`  
**¿Listo?** → Ejecuta `streamlit run app.py` 🚀

---

## 🎊 ¡Disfruta Explorando Nexus-Fin!

Desarrollado con ❤️ como demostración de arquitectura de software aplicada al sector financiero.
