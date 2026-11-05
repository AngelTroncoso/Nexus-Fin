# 📊 Resumen Ejecutivo - Nexus-Fin

## Sistema de Decisiones Autónomas para Gestión de Tesorería

---

## 🎯 Visión General

**Nexus-Fin** es un prototipo funcional de sistema multiagente que utiliza **Inteligencia Artificial (LLM)** para decidir autónomamente entre dos estrategias financieras paralelas en la gestión de flujo de caja:

- **Ruta A - Motor Predictivo**: Proyecciones econométricas (entornos estables)
- **Ruta B - Motor Adaptativo**: Control dinámico (crisis y volatilidad)

El sistema analiza el contexto financiero en tiempo real, consulta a un LLM vía **OpenRouter API**, ejecuta el motor seleccionado y visualiza los resultados de forma interactiva.

---

## ⚡ Características Clave

| Característica | Descripción |
|----------------|-------------|
| 🤖 **Decisión Autónoma** | El LLM elige la estrategia sin intervención humana |
| 🔍 **Razonamiento Transparente** | JSON explícito con justificación de cada decisión |
| 📈 **Visualización Interactiva** | Gráficos dinámicos con Plotly (zoom, pan, hover) |
| 🔄 **Modo Fallback** | Funciona sin API key usando lógica heurística |
| 🎛️ **Escenarios Múltiples** | Estable vs. Shock de liquidez crítico |
| 📊 **Métricas en Tiempo Real** | Volatilidad, rebalanceos, proyecciones, bandas |

---

## 🏗️ Arquitectura Simplificada

```
┌─────────────────────────────────────────┐
│       Interfaz Streamlit (UI)           │
│  • Configuración de escenarios          │
│  • Visualización de resultados          │
└────────────────┬────────────────────────┘
                 │
                 ▼
        ┌────────────────────┐
        │   Router Engine    │
        │   (OpenRouter API) │
        │   Decide: A o B    │
        └────────┬───────────┘
                 │
         ┌───────┴───────┐
         ▼               ▼
    ┌────────┐      ┌────────┐
    │ Motor A│      │ Motor B│
    │Predict.│      │Adaptivo│
    └────────┘      └────────┘
         │               │
         └───────┬───────┘
                 ▼
        ┌────────────────┐
        │   Resultados   │
        │  + Métricas    │
        └────────────────┘
```

---

## 🚀 Inicio Rápido (3 pasos)

### Paso 1: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 2: Configurar API Key (opcional)

```bash
copy .env.example .env
# Editar .env con tu clave de OpenRouter
```

**Obtener clave gratuita:** https://openrouter.ai/keys

### Paso 3: Ejecutar aplicación

```bash
streamlit run app.py
```

O en Windows, doble clic en: **`start.bat`**

---

## 📊 Ejemplo de Uso

### Escenario: Entorno Estable

**Configuración:**
- Balance inicial: $2,500,000
- Horizonte: 90 días
- Volatilidad: 5%
- Sin shocks detectados

**Decisión del LLM:**
```json
{
  "route": "A",
  "confidence": 0.89,
  "reasoning": "Entorno estable con baja volatilidad permite proyecciones econométricas confiables.",
  "key_factors": ["volatilidad_baja", "serie_temporal_estable"]
}
```

**Resultado:**
- ✅ Motor Predictivo activado
- 📈 Proyección suave con bandas de confianza estrechas
- 💰 Flujo promedio proyectado: $2,650,000
- 📊 Volatilidad: 4.2%

---

### Escenario: Shock de Liquidez

**Configuración:**
- Balance inicial: $850,000
- Horizonte: 30 días
- Volatilidad: 28%
- Shock detectado

**Decisión del LLM:**
```json
{
  "route": "B",
  "confidence": 0.94,
  "reasoning": "Shock crítico requiere control adaptativo para proteger capital.",
  "key_factors": ["shock_liquidez", "volatilidad_extrema"]
}
```

**Resultado:**
- ✅ Motor Adaptativo activado
- ⚡ 5 eventos de shock manejados
- 🔄 8 acciones de rebalanceo ejecutadas
- 💰 Flujo promedio: $720,000 (con rebalanceos)
- 📊 Eficiencia de recuperación: 78%

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología | Versión |
|------------|------------|---------|
| **Lenguaje** | Python | 3.11+ |
| **UI** | Streamlit | 1.28+ |
| **Visualización** | Plotly | 5.17+ |
| **LLM API** | OpenRouter | Latest |
| **Procesamiento** | Pandas, NumPy | 2.1+, 1.24+ |

---

## 📁 Estructura del Proyecto

```
estaticodinamico/
├── 📄 app.py                          # Interfaz principal
├── 🧠 router_engine.py                # Motor de decisión LLM
├── 📁 engines/
│   ├── predictive_engine.py           # Motor A (Econométrico)
│   └── adaptive_engine.py             # Motor B (Adaptativo)
├── 📋 requirements.txt                # Dependencias
├── 🔧 .env.example                    # Plantilla de config
├── 📖 README.md                       # Documentación completa
├── ⚡ QUICKSTART.md                   # Inicio rápido
├── 🏗️ ARCHITECTURE.md                 # Arquitectura técnica
├── 📚 EXAMPLES.md                     # Ejemplos de uso
├── 🧪 test_system.py                  # Suite de tests
└── 🚀 start.bat                       # Script de inicio (Windows)
```

---

## 🎓 Casos de Uso

### 1. Planificación Financiera
Proyectar flujo de caja trimestral en condiciones normales de mercado.

### 2. Gestión de Crisis
Respuesta táctica ante shocks de liquidez o volatilidad extrema.

### 3. Análisis de Sensibilidad
Comparar estrategias en múltiples escenarios (pesimista, base, optimista).

### 4. Backtesting
Simular decisiones del sistema con datos históricos reales.

### 5. Educación Financiera
Demostrar diferencias entre modelos predictivos y adaptativos.

---

## 💡 Ventajas Competitivas

| Ventaja | Descripción |
|---------|-------------|
| 🎯 **Autonomía** | Decisiones sin intervención humana 24/7 |
| 🔬 **Transparencia** | Razonamiento explícito en cada decisión |
| ⚡ **Velocidad** | Análisis en <10 segundos por escenario |
| 🔄 **Flexibilidad** | Soporta 100+ modelos LLM vía OpenRouter |
| 💰 **Económico** | Costos de API ~$0.001 por decisión |
| 🛡️ **Resiliencia** | Modo fallback cuando API no está disponible |

---

## 📈 Métricas del Sistema

### Motor Predictivo (Ruta A)
- Flujo promedio proyectado
- Desviación estándar
- Bandas de confianza (95%)
- Volatilidad index
- Proyección min/max

### Motor Adaptativo (Ruta B)
- Número de rebalanceos
- Eventos de shock manejados
- Impacto total de shocks
- Eficiencia de recuperación
- Flujo min/max

---

## 🧪 Testing

El proyecto incluye una suite completa de tests:

```bash
python test_system.py
```

**Tests incluidos:**
1. ✅ Creación de escenarios
2. ✅ Router en modo fallback
3. ✅ Motor predictivo
4. ✅ Motor adaptativo
5. ✅ Integración completa

---

## 🔮 Roadmap

### Versión 1.1 (Próximo)
- [ ] Exportación a Excel/PDF
- [ ] Historial de decisiones
- [ ] Comparación A vs B lado a lado

### Versión 1.2 (Futuro cercano)
- [ ] Integración con APIs financieras reales
- [ ] Backtesting automático
- [ ] Sistema de alertas

### Versión 2.0 (Largo plazo)
- [ ] API REST
- [ ] Multi-agente con votación
- [ ] Machine Learning para mejora continua

---

## 🤝 Soporte y Contribuciones

### Documentación Completa
- **README.md**: Guía completa del proyecto
- **QUICKSTART.md**: Inicio en 5 minutos
- **ARCHITECTURE.md**: Detalles técnicos profundos
- **EXAMPLES.md**: 8+ casos de uso reales

### Obtener Ayuda
1. Revisar la documentación
2. Ejecutar `python test_system.py` para diagnosticar
3. Verificar configuración de `.env`

### Contribuir
Las contribuciones son bienvenidas. El proyecto usa:
- Licencia MIT
- Commits convencionales
- Tests obligatorios para nuevas features

---

## 📞 Contacto Técnico

**Proyecto:** Nexus-Fin - Motor de Decisiones Paralelas  
**Versión:** 1.0.0  
**Fecha:** Noviembre 2026  
**Licencia:** MIT  
**Stack:** Python | Streamlit | OpenRouter API | Plotly  

---

## 🎉 Empezar Ahora

```bash
# Clonar/descargar el proyecto
cd estaticodinamico

# Opción 1: Script automático (Windows)
start.bat

# Opción 2: Manual
pip install -r requirements.txt
streamlit run app.py
```

**La aplicación se abrirá automáticamente en tu navegador en:** http://localhost:8501

---

**¿Preguntas?** Lee la documentación completa en `README.md`

**¿Problemas?** Ejecuta `python test_system.py` para diagnosticar

**¿Listo?** Ejecuta `streamlit run app.py` y empieza a analizar 🚀
