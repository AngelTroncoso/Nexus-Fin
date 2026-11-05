# 📑 Índice de Documentación - Nexus-Fin

## Guía Rápida de Navegación

---

## 🚀 Comenzar

Si es tu primera vez con Nexus-Fin, sigue este orden:

1. **[RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md)** ⏱️ 5 min
   - Visión general del sistema
   - Características clave
   - Arquitectura simplificada

2. **[QUICKSTART.md](QUICKSTART.md)** ⏱️ 5 min
   - Instalación rápida
   - Primer uso
   - Solución de problemas básicos

3. **Ejecutar la aplicación**
   ```bash
   streamlit run app.py
   ```

---

## 📚 Documentación Completa

### Nivel 1: Usuario Final

| Documento | Propósito | Tiempo Lectura |
|-----------|-----------|----------------|
| **[README.md](README.md)** | Documentación completa del proyecto | 15 min |
| **[EXAMPLES.md](EXAMPLES.md)** | 8+ casos de uso prácticos | 20 min |
| **[QUICKSTART.md](QUICKSTART.md)** | Guía de inicio rápido | 5 min |
| **[RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md)** | Visión ejecutiva | 5 min |

### Nivel 2: Desarrollador

| Documento | Propósito | Tiempo Lectura |
|-----------|-----------|----------------|
| **[ARCHITECTURE.md](ARCHITECTURE.md)** | Arquitectura técnica profunda | 30 min |
| **[CHANGELOG.md](CHANGELOG.md)** | Historial de versiones | 5 min |
| **[LICENSE](LICENSE)** | Licencia MIT | 2 min |

### Nivel 3: Código Fuente

| Archivo | Descripción | Líneas |
|---------|-------------|--------|
| **[app.py](app.py)** | Interfaz principal Streamlit | ~400 |
| **[router_engine.py](router_engine.py)** | Motor de decisión con LLM | ~250 |
| **[engines/predictive_engine.py](engines/predictive_engine.py)** | Motor A (Econométrico) | ~180 |
| **[engines/adaptive_engine.py](engines/adaptive_engine.py)** | Motor B (Adaptativo) | ~250 |
| **[test_system.py](test_system.py)** | Suite de tests | ~300 |

---

## 🎯 Navegación por Objetivo

### "Quiero entender qué hace el sistema"
→ Lee **[RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md)**

### "Quiero ejecutarlo rápidamente"
→ Sigue **[QUICKSTART.md](QUICKSTART.md)**

### "Quiero ver ejemplos de uso"
→ Explora **[EXAMPLES.md](EXAMPLES.md)**

### "Necesito toda la información"
→ Lee **[README.md](README.md)**

### "Quiero entender la arquitectura"
→ Estudia **[ARCHITECTURE.md](ARCHITECTURE.md)**

### "Quiero modificar el código"
→ Lee **[ARCHITECTURE.md](ARCHITECTURE.md)** + código fuente

### "Quiero integrar con mi sistema"
→ Lee **[EXAMPLES.md](EXAMPLES.md)** (Ejemplo 5: Uso Programático)

---

## 📂 Estructura del Proyecto

```
estaticodinamico/
│
├─ 📄 DOCUMENTACIÓN
│  ├── INDEX.md                      ← Estás aquí
│  ├── RESUMEN_EJECUTIVO.md          (Visión general)
│  ├── QUICKSTART.md                 (Inicio rápido)
│  ├── README.md                     (Guía completa)
│  ├── ARCHITECTURE.md               (Arquitectura técnica)
│  ├── EXAMPLES.md                   (Casos de uso)
│  ├── CHANGELOG.md                  (Historial de versiones)
│  └── LICENSE                       (Licencia MIT)
│
├─ 🧠 CÓDIGO PRINCIPAL
│  ├── app.py                        (Interfaz Streamlit)
│  ├── router_engine.py              (Motor de decisión LLM)
│  └── engines/
│      ├── __init__.py
│      ├── predictive_engine.py      (Motor A)
│      └── adaptive_engine.py        (Motor B)
│
├─ 🔧 CONFIGURACIÓN
│  ├── requirements.txt              (Dependencias Python)
│  ├── .env.example                  (Plantilla de configuración)
│  └── .gitignore                    (Git ignore)
│
└─ 🧪 UTILIDADES
   ├── test_system.py                (Suite de tests)
   └── start.bat                     (Script de inicio Windows)
```

---

## 🔍 Búsqueda por Tema

### Configuración e Instalación
- [QUICKSTART.md](QUICKSTART.md) - Instalación y primer uso
- [README.md](README.md) - Sección "Instalación Rápida"
- `.env.example` - Plantilla de configuración

### Uso de la Aplicación
- [README.md](README.md) - Sección "Uso de la Aplicación"
- [EXAMPLES.md](EXAMPLES.md) - Casos de uso reales
- [app.py](app.py) - Código de la interfaz

### Arquitectura y Diseño
- [ARCHITECTURE.md](ARCHITECTURE.md) - Arquitectura completa
- [RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md) - Diagrama simplificado
- [router_engine.py](router_engine.py) - Implementación del router

### Motores de Decisión
- [ARCHITECTURE.md](ARCHITECTURE.md) - Secciones 3 y 4
- [engines/predictive_engine.py](engines/predictive_engine.py) - Motor A
- [engines/adaptive_engine.py](engines/adaptive_engine.py) - Motor B

### API y OpenRouter
- [README.md](README.md) - Sección "OpenRouter API"
- [router_engine.py](router_engine.py) - Clase `RouterEngine`
- [.env.example](.env.example) - Configuración de API

### Testing y Validación
- [test_system.py](test_system.py) - Suite completa de tests
- [README.md](README.md) - Sección "Solución de Problemas"

### Contribución y Desarrollo
- [CHANGELOG.md](CHANGELOG.md) - Historial de cambios
- [LICENSE](LICENSE) - Licencia del proyecto
- [ARCHITECTURE.md](ARCHITECTURE.md) - Sección "Extensibilidad"

---

## 🎓 Rutas de Aprendizaje

### Ruta 1: Usuario No Técnico (30 min)

1. **[RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md)** (5 min)
   - ¿Qué es Nexus-Fin?
   - ¿Para qué sirve?

2. **Ejecutar el sistema** (10 min)
   - Doble clic en `start.bat`
   - Explorar la interfaz

3. **[EXAMPLES.md](EXAMPLES.md)** - Ejemplos 1 y 2 (15 min)
   - Entorno estable
   - Shock de liquidez

### Ruta 2: Analista/Product Manager (1 hora)

1. **[RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md)** (5 min)
2. **[README.md](README.md)** (15 min)
3. **Ejecutar y experimentar** (20 min)
4. **[EXAMPLES.md](EXAMPLES.md)** - Todos los casos (20 min)

### Ruta 3: Desarrollador Frontend (1.5 horas)

1. **[QUICKSTART.md](QUICKSTART.md)** (5 min)
2. **[README.md](README.md)** (15 min)
3. **[app.py](app.py)** - Código de la UI (30 min)
4. **[ARCHITECTURE.md](ARCHITECTURE.md)** - Componente 1 (20 min)
5. **Modificar la interfaz** (20 min)

### Ruta 4: Desarrollador Backend/ML (2 horas)

1. **[ARCHITECTURE.md](ARCHITECTURE.md)** completo (30 min)
2. **[router_engine.py](router_engine.py)** (20 min)
3. **[engines/predictive_engine.py](engines/predictive_engine.py)** (20 min)
4. **[engines/adaptive_engine.py](engines/adaptive_engine.py)** (20 min)
5. **[test_system.py](test_system.py)** (10 min)
6. **Experimentar con el código** (20 min)

### Ruta 5: Arquitecto de Software (2.5 horas)

1. **[RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md)** (5 min)
2. **[ARCHITECTURE.md](ARCHITECTURE.md)** completo (45 min)
3. **Todo el código fuente** (60 min)
4. **[EXAMPLES.md](EXAMPLES.md)** (20 min)
5. **Evaluar extensibilidad** (20 min)

---

## 📖 Glosario Rápido

| Término | Significado |
|---------|-------------|
| **Router Engine** | Motor de decisión que consulta al LLM |
| **Ruta A** | Motor Predictivo (Econométrico) |
| **Ruta B** | Motor Adaptativo (Control Dinámico) |
| **OpenRouter** | API unificada para múltiples LLMs |
| **Fallback Mode** | Modo heurístico sin LLM |
| **Scenario Data** | Métricas del entorno financiero |
| **LLM** | Large Language Model (Modelo de IA) |

---

## 🔗 Enlaces Externos

- **OpenRouter API**: https://openrouter.ai
- **Streamlit Docs**: https://docs.streamlit.io
- **Plotly Python**: https://plotly.com/python/
- **Python 3.11**: https://www.python.org/downloads/

---

## 🆘 Ayuda Rápida

### "No arranca la aplicación"
```bash
python test_system.py  # Diagnosticar
pip install -r requirements.txt  # Reinstalar dependencias
```

### "Error de API Key"
Edita `.env` y añade tu clave de OpenRouter:
```env
OPENROUTER_API_KEY=tu_clave_real
```

### "No entiendo la arquitectura"
Lee en orden:
1. [RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md) - Diagrama simple
2. [ARCHITECTURE.md](ARCHITECTURE.md) - Detalles técnicos

### "Quiero modificar el código"
1. Lee [ARCHITECTURE.md](ARCHITECTURE.md) - Sección "Extensibilidad"
2. Ejecuta `python test_system.py` después de cada cambio
3. Sigue los commits convencionales

---

## 📊 Estadísticas del Proyecto

- **Total líneas de código**: ~1,500
- **Total líneas de documentación**: ~3,000
- **Archivos Python**: 6
- **Archivos Markdown**: 8
- **Tests implementados**: 5
- **Dependencias externas**: 7

---

## 🎯 Próximos Pasos Recomendados

1. ✅ Lee [RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md)
2. ✅ Sigue [QUICKSTART.md](QUICKSTART.md)
3. ✅ Ejecuta `streamlit run app.py`
4. ✅ Experimenta con ambos escenarios
5. ✅ Lee [EXAMPLES.md](EXAMPLES.md) para casos avanzados

---

**Última actualización:** 2026-11-05  
**Versión:** 1.0.0  
**Mantenedor:** Nexus-Fin Development Team

---

**¿Empezamos?** → [QUICKSTART.md](QUICKSTART.md) 🚀
