# 📚 Ejemplos de Uso - Nexus-Fin

## Casos de Uso Reales

---

## Ejemplo 1: Planificación de Tesorería Trimestral

### Contexto
Una empresa fintech necesita proyectar su flujo de caja para el próximo trimestre (90 días) en un entorno macroeconómico estable.

### Configuración en Nexus-Fin

**Sidebar:**
- Escenario: 📈 Entorno Estable
- Horizonte: 90 días
- Balance Inicial: $2,500,000
- API Key: [Configurada]

**Ejecutar Análisis**

### Resultado Esperado

**Decisión del LLM:**
```json
{
  "route": "A",
  "confidence": 0.89,
  "reasoning": "El entorno estable con volatilidad del 5% y tendencia ascendente permite utilizar proyecciones econométricas confiables. La serie temporal muestra patrones predecibles ideales para el Motor Predictivo.",
  "key_factors": [
    "volatility_baja_5_percent",
    "serie_temporal_estable",
    "ausencia_de_shocks",
    "horizonte_medio_plazo"
  ],
  "risk_assessment": "Riesgo bajo. Recomendable optimizar costos de carry con buffer mínimo.",
  "recommended_horizon": "medio_plazo"
}
```

**Gráfico Generado:**
- Línea principal: Proyección suave con tendencia ligeramente ascendente
- Bandas de confianza: Estrechas (±$150k)
- Sin eventos de shock marcados

**Métricas:**
- Flujo Promedio: $2,650,000
- Volatilidad: 4.2%
- Proyección Mínima: $2,480,000
- Proyección Máxima: $2,820,000

**Recomendaciones:**
- ✓ Entorno estable detectado - Proyección confiable
- ✓ Volatilidad baja - Ideal para optimización de carry
- ✓ Sin riesgo de déficit en el horizonte proyectado

### Acción Empresarial
El CFO aprueba una estrategia de inversión de excedentes en instrumentos de mediano plazo, confiando en la proyección del Motor Predictivo.

---

## Ejemplo 2: Gestión de Crisis de Liquidez

### Contexto
Durante una crisis bancaria regional, la empresa enfrenta retiros masivos de clientes y necesita gestionar el riesgo de liquidez en los próximos 30 días.

### Configuración en Nexus-Fin

**Sidebar:**
- Escenario: ⚡ Shock de Liquidez Crítico
- Horizonte: 30 días
- Balance Inicial: $850,000
- API Key: [Configurada]

**Ejecutar Análisis**

### Resultado Esperado

**Decisión del LLM:**
```json
{
  "route": "B",
  "confidence": 0.94,
  "reasoning": "Shock de liquidez crítico con volatilidad del 28% y caída abrupta del cashflow. Las proyecciones econométricas no son confiables en este contexto. Se requiere control adaptativo con rebalanceo dinámico para proteger capital.",
  "key_factors": [
    "shock_liquidez_detectado",
    "volatilidad_extrema_28_percent",
    "tendencia_descendente_abrupta",
    "ratio_estabilidad_critico_43_percent"
  ],
  "risk_assessment": "Riesgo ALTO. Priorizar preservación de capital sobre rendimiento. Activar buffers de emergencia.",
  "recommended_horizon": "corto_plazo"
}
```

**Gráfico Generado:**
- Línea principal: Trayectoria con caídas bruscas y recuperaciones
- Eventos de shock: Barras rojas en días 3, 9, 15, 22, 28
- Acciones de rebalanceo: Marcadas como puntos verdes
- Buffer de seguridad: Línea punteada mostrando el target dinámico

**Métricas:**
- Flujo Promedio: $720,000 (con rebalanceos)
- Volatilidad: 22.7%
- Flujo Mínimo: $560,000 (día 15)
- Eventos de Shock: 5
- Rebalanceos: 8 acciones correctivas
- Eficiencia de Recuperación: 78%

**Recomendaciones:**
- ⚡ Modo adaptativo activado - Control dinámico habilitado
- ⚡ Acciones de rebalanceo ejecutadas: 8
- ⚡ Eventos de shock manejados: 5
- ⚠ Revisar capacidad de recuperación ante shocks
- ✓ Buffer de seguridad mantenido durante toda la simulación

### Acción Empresarial
El equipo de tesorería implementa:
1. Líneas de crédito contingentes activadas
2. Límites de retiro temporales
3. Monitoreo en tiempo real del ratio de liquidez
4. Rebalanceos preventivos cada 3 días

---

## Ejemplo 3: Comparación de Estrategias

### Contexto
Un analista quiere comparar qué hubiera pasado si se usara la estrategia "incorrecta" en cada escenario.

### Experimento A: Motor Predictivo en Crisis

**Configuración:**
- Escenario: ⚡ Shock
- Forzar Ruta A (simulación manual)

**Resultado:**
- Proyección inicial: $850k → $920k (optimista)
- **Realidad:** Múltiples shocks no contemplados
- **Impacto:** Déficit de liquidez en día 12
- **Conclusión:** Motor predictivo falla ante eventos impredecibles

### Experimento B: Motor Adaptativo en Estabilidad

**Configuración:**
- Escenario: 📈 Estable
- Forzar Ruta B (simulación manual)

**Resultado:**
- Trayectoria: Múltiples rebalanceos innecesarios
- **Costo operativo:** 15 acciones de rebalanceo (vs. 2 necesarias)
- **Eficiencia:** -3.2% de rendimiento perdido por sobre-precaución
- **Conclusión:** Motor adaptativo es conservador pero costoso en estabilidad

### Lección
La decisión autónoma del LLM optimiza el trade-off entre:
- **Riesgo** (protección vs. exposición)
- **Costo** (eficiencia vs. precaución)
- **Horizonte** (corto vs. mediano plazo)

---

## Ejemplo 4: Serie Temporal de Decisiones

### Contexto
Simulación de 6 meses con cambio de régimen de mercado en el tiempo.

### Configuración Dinámica

| Mes | Escenario | Ruta Decidida | Justificación |
|-----|-----------|---------------|---------------|
| Ene | Estable | A (Predictivo) | Inicio de año, mercado tranquilo |
| Feb | Estable | A (Predictivo) | Continúa estabilidad |
| Mar | **Shock** | **B (Adaptativo)** | Crisis bancaria regional detectada |
| Abr | Shock | B (Adaptativo) | Persistencia de volatilidad |
| May | **Estable** | **A (Predictivo)** | Recuperación confirmada |
| Jun | Estable | A (Predictivo) | Normalización completa |

**Insights:**
- El LLM detecta cambios de régimen en tiempo real
- Transiciones automáticas entre estrategias
- Posibilidad de crear un "historial de decisiones" acumulativo

---

## Ejemplo 5: Uso Programático (Sin UI)

### Script Python Standalone

```python
from router_engine import RouterEngine, create_scenario_data
from engines.predictive_engine import PredictiveEngine
from engines.adaptive_engine import AdaptiveEngine

# 1. Crear escenario
scenario = create_scenario_data("stable")

# 2. Router decide
router = RouterEngine(api_key="tu_key", model="nvidia/nemotron-3-nano-30b-a3b:free")
route, decision = router.analyze_scenario(scenario)

print(f"Decisión: Ruta {route}")
print(f"Confianza: {decision['confidence']:.1%}")

# 3. Ejecutar engine
if route == "A":
    engine = PredictiveEngine(initial_balance=2_000_000)
    df, metrics = engine.generate_forecast(days=90, scenario_data=scenario)
else:
    engine = AdaptiveEngine(initial_balance=2_000_000)
    df, metrics = engine.generate_adaptive_path(days=90, scenario_data=scenario)

# 4. Exportar resultados
df.to_csv("resultados.csv", index=False)
print(f"Flujo promedio: ${metrics['mean_cashflow']:,.0f}")
```

**Ejecutar:**
```bash
python mi_script.py
```

**Salida:**
```
Decisión: Ruta A
Confianza: 87.0%
Flujo promedio: $2,650,000
```

---

## Ejemplo 6: Integración con Sistema de Alertas

### Caso de Uso
Automatizar la ejecución diaria y enviar alertas si se detecta un cambio de ruta.

### Script de Monitoreo

```python
import smtplib
from datetime import datetime
from router_engine import RouterEngine, create_scenario_data

def fetch_market_data():
    # Aquí conectarías con APIs reales (Yahoo Finance, Bloomberg, etc.)
    # Por ahora, simulamos
    return create_scenario_data("stable")

def send_alert(route, decision):
    subject = f"🚨 Nexus-Fin: Cambio de Estrategia → Ruta {route}"
    body = f"""
    Nueva decisión del sistema:
    - Ruta: {route}
    - Confianza: {decision['confidence']:.1%}
    - Razonamiento: {decision['reasoning']}
    
    Revisar dashboard: http://nexus-fin.local
    """
    # Enviar email (configurar SMTP)
    print(f"[ALERTA] {subject}")

def main():
    print(f"[{datetime.now()}] Ejecutando análisis diario...")
    
    scenario = fetch_market_data()
    router = RouterEngine(api_key="tu_key")
    route, decision = router.analyze_scenario(scenario)
    
    # Comparar con decisión anterior (guardada en DB/archivo)
    previous_route = load_previous_route()
    
    if route != previous_route:
        send_alert(route, decision)
        print("⚠️  Cambio de estrategia detectado!")
    else:
        print("✓ Estrategia mantiene.")
    
    save_current_route(route)

if __name__ == "__main__":
    main()
```

**Cron Job (Linux/Mac):**
```bash
# Ejecutar cada día a las 8:00 AM
0 8 * * * cd /ruta/nexus-fin && python monitor.py
```

**Tarea Programada (Windows):**
```powershell
# Crear tarea en Task Scheduler
schtasks /create /tn "NexusFin-Monitor" /tr "python C:\nexus-fin\monitor.py" /sc daily /st 08:00
```

---

## Ejemplo 7: Dashboard Multi-Escenario

### Configuración Avanzada

Ejecutar 3 escenarios en paralelo en la misma sesión:

1. **Pesimista**: Volatilidad 30%, Shock activado
2. **Base**: Volatilidad 10%, Sin shock
3. **Optimista**: Volatilidad 3%, Tendencia ascendente fuerte

**Resultado:**
- 3 gráficos lado a lado
- Comparación de métricas
- Análisis de sensibilidad

**Implementación en Streamlit:**
```python
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Escenario Pesimista")
    # Ejecutar con parámetros pesimistas
    
with col2:
    st.subheader("Escenario Base")
    # Ejecutar con parámetros base
    
with col3:
    st.subheader("Escenario Optimista")
    # Ejecutar con parámetros optimistas
```

---

## Ejemplo 8: Backtesting con Datos Históricos

### Caso: Crisis 2008

**Datos de entrada (simulados):**
```python
crisis_2008 = {
    "scenario_type": "Crisis Financiera Global",
    "volatility": 0.45,  # 45% volatilidad
    "liquidity": 600_000,
    "shock_detected": True,
    "cashflow_trend": "Colapso",
    "time_horizon": 180,
    "stability_ratio": 0.22,
    "variation_coef": 0.58,
    "std_dev": 320_000
}
```

**Decisión del LLM:**
- Ruta: **B (Adaptativo)** con 98% de confianza
- Key Factor: "volatilidad_extrema_crisis_sistemica"

**Comparación:**
- **Con Motor Adaptativo:** Supervivencia con pérdida del 15%
- **Con Motor Predictivo:** Quiebra simulada en día 32

---

## Recursos Adicionales

### Datasets de Prueba
- `examples/datos_estables.csv`: 1 año de datos sintéticos estables
- `examples/datos_crisis.csv`: Simulación de crisis de liquidez
- `examples/datos_mixtos.csv`: Cambios de régimen

### Notebooks Jupyter
- `notebooks/analisis_exploratorio.ipynb`: EDA del sistema
- `notebooks/comparacion_motores.ipynb`: Benchmarking A vs B
- `notebooks/tuning_parametros.ipynb`: Optimización de hiperparámetros

### Scripts Útiles
- `scripts/export_to_excel.py`: Exportar resultados a Excel
- `scripts/generate_report_pdf.py`: Generar reportes ejecutivos
- `scripts/batch_analysis.py`: Análisis masivo de escenarios

---

**¿Más ejemplos?** Consulta la documentación completa en `ARCHITECTURE.md`
