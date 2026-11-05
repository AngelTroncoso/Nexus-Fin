# 🧠 Nexus-Fin: Motor de Decisiones en Paralelo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Sistema multiagente de toma de decisiones autónomas para gestión de tesorería y flujo de caja**

*Predicción vs. Adaptación | Powered by OpenRouter API + LLM*

---

## 🎯 Descripción

Nexus-Fin es un prototipo funcional que simula un **sistema de decisión autónoma** aplicado al sector financiero. Utiliza un LLM (Large Language Model) vía OpenRouter API para decidir en tiempo real entre dos estrategias paralelas:

- **Ruta A - Motor Predictivo**: Proyecciones econométricas basadas en series temporales (ideal para entornos estables)
- **Ruta B - Motor Adaptativo**: Políticas de control dinámico y rebalanceo (ideal para shocks y alta volatilidad)

El sistema analiza el contexto financiero, consulta al LLM, ejecuta el motor seleccionado y visualiza la trayectoria funcional resultante.

---

## ⚡ Características Principales

✅ **Decisión Autónoma**: El LLM decide la ruta sin intervención humana  
✅ **Razonamiento Transparente**: JSON explícito con la justificación de la decisión  
✅ **Visualización Interactiva**: Gráficos dinámicos con Plotly  
✅ **Modo Fallback**: Funciona sin API key usando lógica heurística  
✅ **Escenarios Múltiples**: Entorno estable vs. Shock de liquidez crítico  
✅ **Métricas en Tiempo Real**: Volatilidad, rebalanceos, proyecciones, bandas de confianza  

---

## 🚀 Instalación Rápida

### Prerrequisitos

- Python 3.11 o superior
- pip (gestor de paquetes de Python)

### Pasos

1. **Clonar o descargar el repositorio**

```bash
cd estaticodinamico
```

2. **Crear entorno virtual (recomendado)**

```bash
python -m venv venv
```

**Activar el entorno:**

- Windows (PowerShell):
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```

- Windows (CMD):
  ```cmd
  venv\Scripts\activate.bat
  ```

- Linux/Mac:
  ```bash
  source venv/bin/activate
  ```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Configurar API Key de OpenRouter (opcional pero recomendado)**

Copia el archivo de ejemplo:

```bash
copy .env.example .env
```

Edita `.env` y añade tu clave de OpenRouter:

```env
OPENROUTER_API_KEY=tu_clave_real_aqui
OPENROUTER_MODEL=nvidia/nemotron-3-nano-30b-a3b:free
```

**¿Dónde obtener la API Key?**  
👉 https://openrouter.ai/keys (registro gratuito)

**Nota:** Si no configuras la API key, el sistema funcionará en **modo fallback** con lógica heurística determinista.

5. **Ejecutar la aplicación**

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

---

## 📁 Estructura del Proyecto

```
estaticodinamico/
├── app.py                          # Interfaz principal Streamlit
├── router_engine.py                # Motor de enrutamiento con LLM
├── engines/
│   ├── __init__.py
│   ├── predictive_engine.py        # Motor predictivo (econométrico)
│   └── adaptive_engine.py          # Motor adaptativo (control dinámico)
├── requirements.txt                # Dependencias del proyecto
├── .env.example                    # Plantilla de configuración
├── .env                            # Tu configuración (NO subir a Git)
└── README.md                       # Este archivo
```

---

## 🎮 Uso de la Aplicación

### Barra Lateral (Configuración)

1. **Escenario Financiero**:
   - 📈 Entorno Estable
   - ⚡ Shock de Liquidez Crítico

2. **OpenRouter API**:
   - Introduce tu API Key
   - Selecciona el modelo LLM (recomendado: `nvidia/nemotron-3-nano-30b-a3b:free` - GRATUITO)

3. **Parámetros**:
   - Horizonte temporal (30-180 días)
   - Balance inicial ($100k - $10M)

4. **Ejecutar Análisis** 🚀

### Panel Principal

- **Métricas Clave**: Flujo promedio, volatilidad, proyecciones
- **Gráfico Interactivo**: Trayectoria de flujo de caja con Plotly
  - Líneas de confianza (Ruta A)
  - Eventos de shock y rebalanceos (Ruta B)
- **Razonamiento del Agente**: JSON completo con la decisión del LLM
- **Recomendaciones Estratégicas**: Basadas en el motor ejecutado

---

## 🧠 Lógica del Router Engine

El `RouterEngine` implementa el núcleo de decisión:

```python
# Flujo simplificado
scenario_data = create_scenario_data("stable" o "shock")
router = RouterEngine(api_key="tu_key", model="nvidia/nemotron-3-nano-30b-a3b:free")
route, decision = router.analyze_scenario(scenario_data)

if route == "A":
    # Ejecutar motor predictivo
elif route == "B":
    # Ejecutar motor adaptativo
```

### Prompt Engineering

El sistema construye un prompt contextual con:
- Métricas del entorno (volatilidad, liquidez, tendencias)
- Descripción de ambas rutas
- Solicitud de respuesta en JSON estructurado

### Decisión del LLM

El LLM responde con:

```json
{
  "route": "A",
  "confidence": 0.87,
  "reasoning": "Entorno estable con baja volatilidad...",
  "key_factors": ["volatilidad_baja", "serie_temporal_predecible"],
  "risk_assessment": "Riesgo bajo en horizonte proyectado",
  "recommended_horizon": "medio_plazo"
}
```

---

## 🔬 Motores de Simulación

### Motor A - Predictivo (Econométrico)

**Técnicas simuladas:**
- Series temporales ARIMA-like
- Componentes: tendencia + estacionalidad + proceso AR(1) + ruido
- Bandas de confianza (95%)
- Ideal para: planificación de mediano plazo en contextos estables

**Archivo:** `engines/predictive_engine.py`

### Motor B - Adaptativo (Control Dinámico)

**Técnicas simuladas:**
- Políticas de rebalanceo automático
- Buffers de seguridad dinámicos
- Detección y amortiguamiento de shocks
- Ideal para: gestión de crisis y alta volatilidad

**Archivo:** `engines/adaptive_engine.py`

---

## 🌐 Modelos LLM Disponibles

### Recomendados (rápidos y económicos)

| Modelo | Provider | Velocidad | Costo |
|--------|----------|-----------|-------|
| `nvidia/nemotron-3-nano-30b-a3b:free` | NVIDIA | ⚡⚡⚡ | **GRATIS** |
| `anthropic/claude-3-haiku` | Anthropic | ⚡⚡ | $$ |
| `openai/gpt-3.5-turbo` | OpenAI | ⚡⚡ | $$ |
| `meta-llama/llama-3-8b-instruct` | Meta | ⚡ | $ |

Puedes cambiar el modelo en la barra lateral o en el archivo `.env`.

---

## 🛠️ Solución de Problemas

### Error: "ModuleNotFoundError"

```bash
pip install -r requirements.txt
```

### Error: "API Key inválida"

Verifica que tu clave de OpenRouter esté correcta:
1. Visita https://openrouter.ai/keys
2. Genera una nueva clave si es necesario
3. Actualiza el archivo `.env`

### Error: "Respuesta del LLM mal formada"

El sistema tiene un mecanismo de fallback automático. Si el LLM no responde correctamente, se activará la lógica heurística.

### La aplicación no se abre en el navegador

Abre manualmente: http://localhost:8501

---

## 📊 Ejemplos de Escenarios

### Escenario 1: Entorno Estable

**Entrada:**
- Volatilidad: 5%
- Liquidez: $2.5M
- Tendencia: Ascendente moderada
- Shock: No

**Decisión Esperada:** Ruta A (Motor Predictivo)  
**Visualización:** Curva suave con bandas de confianza estrechas

### Escenario 2: Shock de Liquidez Crítico

**Entrada:**
- Volatilidad: 28%
- Liquidez: $850k
- Tendencia: Descendente abrupta
- Shock: Sí

**Decisión Esperada:** Ruta B (Motor Adaptativo)  
**Visualización:** Curva con rebalanceos frecuentes y eventos de shock marcados

---

## 🤝 Contribuciones

Este es un prototipo funcional. Posibles extensiones:

- [ ] Integración con datos reales de mercado (APIs financieras)
- [ ] Modelos econométricos reales (statsmodels, Prophet)
- [ ] Backtesting con datos históricos
- [ ] Sistema multi-agente con votación
- [ ] Dashboard de monitoreo en tiempo real
- [ ] Exportación de reportes en PDF

---

## 📝 Licencia

Proyecto educativo y de demostración. Uso libre para aprendizaje y prototipado.

---

## 👤 Autor

Desarrollado como sistema de arquitectura de software aplicada al sector financiero.  
Stack: Python | Streamlit | OpenRouter API | Plotly | NumPy | Pandas

---

## 📞 Soporte

Si encuentras problemas o tienes sugerencias:
1. Revisa la sección de **Solución de Problemas**
2. Verifica que todas las dependencias estén instaladas
3. Asegúrate de tener Python 3.11+

---

**🎉 ¡Listo para ejecutar!** Abre tu terminal y ejecuta:

```bash
streamlit run app.py
```
