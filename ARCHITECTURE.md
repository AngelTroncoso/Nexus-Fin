# 🏗️ Arquitectura del Sistema Nexus-Fin

## Visión General

Nexus-Fin implementa un **patrón de arquitectura de decisión multiagente** donde un agente orquestador (Router) consulta a un LLM para seleccionar dinámicamente entre dos motores especializados.

```
┌─────────────────────────────────────────────────────────┐
│                    USUARIO / UI                         │
│                  (Streamlit Interface)                  │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
         ┌─────────────────────────┐
         │   ROUTER ENGINE (LLM)   │
         │  • Analiza contexto     │
         │  • Consulta OpenRouter  │
         │  • Decide ruta A o B    │
         └─────────┬───────┬───────┘
                   │       │
         ┌─────────┘       └─────────┐
         ▼                           ▼
┌────────────────────┐     ┌────────────────────┐
│  MOTOR PREDICTIVO  │     │  MOTOR ADAPTATIVO  │
│      (Ruta A)      │     │      (Ruta B)      │
│                    │     │                    │
│ • Series Temp.     │     │ • Control Dinámico │
│ • Proyecciones     │     │ • Rebalanceo       │
│ • Bandas Confianza │     │ • Shock Handling   │
└────────────────────┘     └────────────────────┘
```

---

## 📦 Componentes Principales

### 1. **app.py** - Capa de Presentación

**Responsabilidades:**
- Interfaz de usuario con Streamlit
- Orquestación del flujo de ejecución
- Visualización de resultados con Plotly
- Gestión de estado de sesión

**Funciones clave:**
- `render_sidebar()`: Configuración y parámetros
- `create_visualization()`: Gráficos interactivos
- `render_metrics_panel()`: Panel de métricas
- `render_reasoning_section()`: Transparencia del LLM

**Flujo de ejecución:**
```python
1. Usuario configura escenario → 
2. Clic en "Ejecutar" → 
3. crear scenario_data → 
4. Router analiza → 
5. Ejecutar engine seleccionado → 
6. Renderizar resultados
```

---

### 2. **router_engine.py** - Motor de Decisión (Cerebro)

**Responsabilidades:**
- Construcción del prompt contextual
- Llamada a OpenRouter API
- Parseo y validación de respuestas
- Lógica de fallback

**Clase principal: `RouterEngine`**

```python
class RouterEngine:
    def analyze_scenario(self, scenario_data: Dict) -> Tuple[str, Dict]:
        """
        Entrada: Métricas del entorno financiero
        Salida: ("A" o "B", {decision_json})
        """
        prompt = self._build_decision_prompt(scenario_data)
        response = self._call_openrouter(prompt)
        decision = self._parse_llm_response(response)
        return decision["route"], decision
```

**Prompt Engineering:**

El prompt incluye:
1. **Contexto del escenario**: Volatilidad, liquidez, shocks, tendencias
2. **Descripción de rutas**: Estrategias A y B con ventajas/riesgos
3. **Formato de respuesta**: JSON estructurado estricto
4. **Temperatura baja (0.3)**: Para decisiones consistentes

**Manejo de errores:**
- JSON mal formado → Fallback
- API no disponible → Fallback
- Sin API key → Fallback automático

**Lógica de fallback (heurística):**
```python
if shock_detected or volatility > 15% or stability < 0.6:
    return "B"  # Adaptativo
else:
    return "A"  # Predictivo
```

---

### 3. **engines/predictive_engine.py** - Motor A (Econométrico)

**Paradigma:** Series Temporales Estables

**Modelo simulado:**
```
Cashflow(t) = Balance_inicial × (1 + Tendencia + Estacionalidad + AR(1) + Ruido)
```

**Componentes:**

1. **Tendencia lineal**: Crecimiento/decrecimiento suave
2. **Estacionalidad**: Ciclos semanales y mensuales
3. **Proceso AR(1)**: Autocorrelación temporal
4. **Ruido blanco**: Variabilidad estocástica controlada

**Salidas:**
- Serie de proyección central
- Bandas de confianza (95%)
- Métricas: volatilidad, min/max proyectado

**Parámetros ajustables:**
```python
{
    "trend": 0.002,              # 0.2% diario
    "seasonality_amplitude": 50_000,
    "noise_level": 0.015,        # 1.5% de volatilidad
    "ar_coef": 0.85             # Coef. autorregresivo
}
```

**Casos de uso ideal:**
- Planificación de mediano plazo
- Entornos macroeconómicos estables
- Optimización de costos de carry

---

### 4. **engines/adaptive_engine.py** - Motor B (Control Dinámico)

**Paradigma:** Políticas Reactivas y Rebalanceo

**Arquitectura:**
```
Estado(t) → Detectar anomalía → Calcular buffer → Decidir rebalanceo → Estado(t+1)
```

**Políticas implementadas:**

1. **Buffer de seguridad dinámico:**
   ```python
   buffer(t) = cashflow(t) × safety_ratio + 2 × std_reciente
   ```

2. **Detección de shocks:**
   - Eventos estocásticos con calendario aleatorio
   - Magnitud ajustada según severidad del escenario

3. **Amortiguamiento de shocks:**
   ```python
   impacto_real = shock × (1 - damping_factor)
   ```

4. **Rebalanceo automático:**
   ```python
   if desviación > threshold:
       rebalanceo = (target - actual) × 0.5
   ```

**Salidas:**
- Trayectoria adaptativa
- Eventos de shock marcados
- Acciones de rebalanceo
- Métricas de resiliencia

**Parámetros ajustables:**
```python
{
    "safety_buffer": 0.20,           # 20% de margen
    "rebalance_threshold": 0.10,     # Activar si desv. > 10%
    "shock_damping": 0.65,           # 65% de amortiguamiento
    "recovery_rate": 0.03            # Tasa de recuperación
}
```

**Casos de uso ideal:**
- Crisis de liquidez
- Alta volatilidad de mercado
- Eventos cisne negro
- Stress testing

---

## 🔄 Flujo de Datos Completo

### Fase 1: Preparación
```
Usuario selecciona escenario → 
create_scenario_data() genera métricas → 
{volatility, liquidity, shock_detected, ...}
```

### Fase 2: Decisión
```
scenario_data → 
RouterEngine.analyze_scenario() →
  ├─ Construir prompt
  ├─ Llamar OpenRouter API
  └─ Parsear JSON response
→ ("A" o "B", {reasoning})
```

### Fase 3: Ejecución
```
if route == "A":
    PredictiveEngine.generate_forecast()
    → (DataFrame, metrics)
else:
    AdaptiveEngine.generate_adaptive_path()
    → (DataFrame, metrics)
```

### Fase 4: Visualización
```
DataFrame + route → 
create_visualization() → 
Plotly figure con:
  ├─ Línea principal de cashflow
  ├─ Bandas de confianza (A) o eventos de shock (B)
  └─ Línea de referencia
```

---

## 🔐 Seguridad y Manejo de API Keys

### Almacenamiento
- `.env` para configuración local (NUNCA commitearlo)
- `.env.example` como plantilla pública
- `python-dotenv` para cargar variables

### Validación
```python
if not self.api_key or self.api_key == "tu_clave_aqui":
    # Activar modo fallback
```

### Timeout y reintentos
```python
response = requests.post(
    url, 
    headers=headers, 
    json=payload, 
    timeout=30  # Timeout de 30 segundos
)
```

---

## 📊 Métricas y Observabilidad

### Métricas del Motor Predictivo
- `mean_cashflow`: Flujo promedio proyectado
- `std_deviation`: Desviación estándar
- `confidence_width`: Ancho de bandas de confianza
- `volatility_index`: Coeficiente de variación

### Métricas del Motor Adaptativo
- `num_rebalances`: Cantidad de acciones correctivas
- `num_shock_events`: Eventos de shock manejados
- `recovery_efficiency`: Capacidad de recuperación
- `total_shock_impact`: Impacto acumulado

### Transparencia del LLM
Todo lo que el LLM decide se expone:
```json
{
  "route": "B",
  "confidence": 0.87,
  "reasoning": "...",
  "key_factors": [...],
  "risk_assessment": "..."
}
```

---

## 🧪 Extensibilidad

### Añadir nuevos motores (Ruta C, D, ...)

1. Crear `engines/nuevo_motor.py`:
```python
class NuevoMotor:
    def generar_estrategia(self, days, scenario_data):
        # Tu lógica aquí
        return df, metrics
```

2. Actualizar `router_engine.py`:
   - Añadir descripción de la nueva ruta en el prompt
   - Parsear respuesta extendida ("A", "B", "C")

3. Actualizar `app.py`:
   - Añadir lógica de enrutamiento
   - Adaptar visualización

### Integrar datos reales

Reemplazar `create_scenario_data()` con:
```python
import yfinance as yf

def fetch_real_market_data():
    data = yf.download("^GSPC", period="1y")
    volatility = data['Close'].pct_change().std()
    # ... calcular métricas reales
    return scenario_data
```

### Añadir más modelos LLM

En `.env` y `app.py`:
```python
OPENROUTER_MODEL=anthropic/claude-3-opus
```

OpenRouter soporta 100+ modelos sin cambiar código.

---

## 🎯 Decisiones de Diseño

### ¿Por qué OpenRouter en lugar de API directa?

✅ Acceso a múltiples modelos con una sola API  
✅ Balanceo de carga automático  
✅ Precios competitivos  
✅ No lock-in con un proveedor  

### ¿Por qué Streamlit?

✅ Prototipado rápido  
✅ Interactividad sin JavaScript  
✅ Perfecto para demos financieras  
✅ Despliegue simple (Streamlit Cloud)  

### ¿Por qué Plotly?

✅ Gráficos interactivos profesionales  
✅ Zoom, pan, hover dinámico  
✅ Exportación a imágenes  
✅ Tema oscuro nativo  

---

## 📈 Roadmap de Mejoras

### Corto plazo
- [ ] Exportar resultados a Excel/PDF
- [ ] Historial de decisiones en sesión
- [ ] Comparación lado a lado de rutas

### Mediano plazo
- [ ] Backtesting con datos históricos reales
- [ ] API REST para integración externa
- [ ] Sistema de alertas (email/Slack)

### Largo plazo
- [ ] Multi-agente: votación entre varios LLM
- [ ] Reinforcement Learning para mejorar decisiones
- [ ] Despliegue en producción con autenticación

---

## 📚 Referencias Técnicas

### Econometría
- Modelos ARIMA: Box-Jenkins
- Suavización exponencial: Holt-Winters
- Bandas de confianza: Intervalo de predicción

### Control Dinámico
- Model Predictive Control (MPC)
- Políticas de rebalanceo: Markowitz
- Amortiguamiento de shocks: Filtros de Kalman

### LLM para Finanzas
- Prompt Engineering for Financial Decision Making
- Chain-of-Thought Reasoning en análisis cuantitativo

---

**Última actualización:** 2026-11-05  
**Versión:** 1.0.0
