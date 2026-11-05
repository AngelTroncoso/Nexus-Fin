# Changelog

Todos los cambios notables del proyecto Nexus-Fin serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

---

## [1.0.0] - 2026-11-05

### 🎉 Versión Inicial

#### Añadido
- **Router Engine**: Sistema de decisión autónoma con LLM vía OpenRouter API
- **Motor Predictivo (Ruta A)**: Proyecciones econométricas basadas en series temporales
- **Motor Adaptativo (Ruta B)**: Políticas de control dinámico y rebalanceo
- **Interfaz Streamlit**: Dashboard interactivo con diseño minimalista en modo oscuro
- **Visualización Plotly**: Gráficos interactivos con zoom, pan y hover dinámico
- **Modo Fallback**: Lógica heurística cuando no hay API key configurada
- **Escenarios predefinidos**: Entorno Estable y Shock de Liquidez Crítico
- **Panel de razonamiento**: Muestra el JSON completo de la decisión del LLM
- **Sistema de métricas**: Volatilidad, rebalanceos, proyecciones y más
- **Recomendaciones estratégicas**: Basadas en el motor ejecutado

#### Características
- ✅ Decisión autónoma del LLM sin intervención humana
- ✅ Razonamiento transparente en formato JSON
- ✅ Bandas de confianza (95%) en modo predictivo
- ✅ Detección y visualización de shocks en modo adaptativo
- ✅ Configuración flexible de horizonte temporal y balance inicial
- ✅ Soporte para múltiples modelos LLM vía OpenRouter

#### Documentación
- `README.md`: Documentación completa del proyecto
- `QUICKSTART.md`: Guía de inicio rápido (5 minutos)
- `ARCHITECTURE.md`: Arquitectura técnica detallada
- `EXAMPLES.md`: Casos de uso y ejemplos prácticos
- `CHANGELOG.md`: Este archivo

#### Scripts y Utilidades
- `start.bat`: Script de inicio automático para Windows
- `test_system.py`: Suite de tests del sistema
- `.env.example`: Plantilla de configuración
- `.gitignore`: Configuración de Git

#### Estructura de Código
```
estaticodinamico/
├── app.py                    # Interfaz Streamlit
├── router_engine.py          # Motor de enrutamiento LLM
├── engines/
│   ├── predictive_engine.py  # Motor A
│   └── adaptive_engine.py    # Motor B
├── requirements.txt          # Dependencias
└── [documentación]
```

#### Dependencias
- Python 3.11+
- Streamlit 1.28+
- Plotly 5.17+
- Pandas 2.1+
- NumPy 1.24+
- Requests 2.31+
- Python-dotenv 1.0+
- OpenAI 1.0+ (cliente compatible con OpenRouter)

#### Stack Tecnológico
- **Backend**: Python 3.11
- **Frontend**: Streamlit
- **Visualización**: Plotly
- **API LLM**: OpenRouter (multi-modelo)
- **Procesamiento**: Pandas, NumPy

---

## [Próximas Versiones] - Roadmap

### [1.1.0] - Planificado
- [ ] Exportación de resultados a Excel/PDF
- [ ] Historial de decisiones en sesión
- [ ] Comparación lado a lado de rutas A y B
- [ ] Métricas adicionales de riesgo (VaR, CVaR)

### [1.2.0] - Planificado
- [ ] Integración con APIs financieras reales (Yahoo Finance, Alpha Vantage)
- [ ] Backtesting con datos históricos
- [ ] Sistema de alertas por email/Slack
- [ ] Persistencia de sesiones en base de datos

### [2.0.0] - Futuro
- [ ] API REST para integración externa
- [ ] Sistema multi-agente con votación entre LLMs
- [ ] Reinforcement Learning para mejora de decisiones
- [ ] Despliegue en producción con autenticación

---

## Notas de Versión

### Compatibilidad
- Compatible con Python 3.11 y superior
- Funciona en Windows, Linux y macOS
- Requiere navegador moderno para Streamlit

### Limitaciones Conocidas
- Datos sintéticos (no conectado a mercados reales en v1.0)
- Modelos econométricos simplificados (no ARIMA real)
- Sin persistencia entre sesiones

### Contribuciones
Las contribuciones son bienvenidas. Por favor, sigue el estándar de commits convencionales:
- `feat:` Nueva funcionalidad
- `fix:` Corrección de bugs
- `docs:` Cambios en documentación
- `refactor:` Refactorización de código
- `test:` Añadir o modificar tests

---

**Última actualización:** 2026-11-05  
**Mantenedor:** Nexus-Fin Development Team
