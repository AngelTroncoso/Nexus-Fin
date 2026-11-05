"""
Nexus-Fin: Motor de Decisiones en Paralelo
Aplicación Streamlit para gestión inteligente de tesorería
Autor: Sistema de IA | Stack: Python + Streamlit + OpenRouter API
"""

import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from datetime import datetime
import json

from router_engine import RouterEngine, create_scenario_data
from engines.predictive_engine import PredictiveEngine
from engines.adaptive_engine import AdaptiveEngine

# Configuración de página
st.set_page_config(
    page_title="Nexus-Fin | Motor de Decisiones Paralelas",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para modo oscuro minimalista
st.markdown("""
<style>
    .main {
        background-color: #0E1117;
    }
    .stMetric {
        background-color: #1E2530;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #00D9FF;
    }
    .stMetric label {
        color: #8B949E !important;
        font-size: 0.9rem !important;
    }
    .stMetric .metric-value {
        color: #00D9FF !important;
        font-weight: 700 !important;
    }
    h1 {
        color: #00D9FF;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    h2, h3 {
        color: #C9D1D9;
        font-weight: 600;
    }
    .route-badge-a {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-weight: 700;
        display: inline-block;
        margin: 10px 0;
    }
    .route-badge-b {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-weight: 700;
        display: inline-block;
        margin: 10px 0;
    }
    .reasoning-box {
        background-color: #161B22;
        border: 1px solid #30363D;
        border-radius: 8px;
        padding: 20px;
        margin: 15px 0;
    }
    .code-box {
        background-color: #0D1117;
        border: 1px solid #30363D;
        border-radius: 6px;
        padding: 15px;
        font-family: 'Courier New', monospace;
        font-size: 0.85rem;
        color: #C9D1D9;
        overflow-x: auto;
    }
</style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """Inicializa variables de sesión"""
    if 'router_decision' not in st.session_state:
        st.session_state.router_decision = None
    if 'last_scenario' not in st.session_state:
        st.session_state.last_scenario = None
    if 'execution_history' not in st.session_state:
        st.session_state.execution_history = []


def render_sidebar():
    """Renderiza la barra lateral con configuración"""
    with st.sidebar:
        st.image("https://via.placeholder.com/300x80/0E1117/00D9FF?text=NEXUS-FIN", use_container_width=True)
        
        st.markdown("---")
        
        st.subheader("🔧 Configuración")
        
        # Selector de escenario
        scenario_type = st.selectbox(
            "Escenario Financiero",
            options=["stable", "shock"],
            format_func=lambda x: "📈 Entorno Estable" if x == "stable" else "⚡ Shock de Liquidez Crítico",
            index=0
        )
        
        st.markdown("---")
        
        # Configuración de API
        st.subheader("🔑 OpenRouter API")
        
        api_key = st.text_input(
            "API Key",
            type="password",
            value="tu_clave_aqui",
            help="Obtén tu clave en: https://openrouter.ai/keys"
        )
        
        model = st.selectbox(
            "Modelo LLM",
            options=[
                "google/gemini-flash-1.5",
                "anthropic/claude-3-haiku",
                "openai/gpt-3.5-turbo",
                "meta-llama/llama-3-8b-instruct"
            ],
            index=0
        )
        
        st.markdown("---")
        
        # Parámetros de simulación
        st.subheader("⚙️ Parámetros")
        
        days_horizon = st.slider(
            "Horizonte (días)",
            min_value=30,
            max_value=180,
            value=90,
            step=10
        )
        
        initial_balance = st.number_input(
            "Balance Inicial ($)",
            min_value=100_000,
            max_value=10_000_000,
            value=2_000_000,
            step=100_000,
            format="%d"
        )
        
        st.markdown("---")
        
        # Botón de ejecución
        run_button = st.button("🚀 Ejecutar Análisis", type="primary", use_container_width=True)
        
        st.markdown("---")
        st.caption("💡 El LLM decide autónomamente la ruta óptima")
        st.caption("🧠 Sin API Key activa, se usa lógica heurística")
        
        return {
            'scenario_type': scenario_type,
            'api_key': api_key,
            'model': model,
            'days_horizon': days_horizon,
            'initial_balance': initial_balance,
            'run_button': run_button
        }


def create_visualization(df_data, route_selected, scenario_type):
    """
    Crea la visualización principal con Plotly
    Muestra cómo cambia la trayectoria según la decisión del LLM
    """
    
    fig = make_subplots(
        rows=2, cols=1,
        row_heights=[0.7, 0.3],
        subplot_titles=("Trayectoria de Flujo de Caja", "Indicadores de Control"),
        vertical_spacing=0.12,
        specs=[[{"secondary_y": False}], [{"secondary_y": False}]]
    )
    
    # Gráfico principal de flujo de caja
    fig.add_trace(
        go.Scatter(
            x=df_data['date'],
            y=df_data['cashflow'],
            mode='lines',
            name=f"Ruta {route_selected} Activa",
            line=dict(
                color='#667eea' if route_selected == 'A' else '#f5576c',
                width=3
            ),
            hovertemplate='<b>Fecha</b>: %{x}<br><b>Cashflow</b>: $%{y:,.0f}<extra></extra>'
        ),
        row=1, col=1
    )
    
    # Bandas de confianza (solo en modo predictivo)
    if route_selected == 'A' and 'upper_confidence' in df_data.columns:
        fig.add_trace(
            go.Scatter(
                x=df_data['date'],
                y=df_data['upper_confidence'],
                mode='lines',
                name='Banda Superior (95%)',
                line=dict(color='rgba(102, 126, 234, 0.2)', width=0),
                showlegend=False,
                hoverinfo='skip'
            ),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Scatter(
                x=df_data['date'],
                y=df_data['lower_confidence'],
                mode='lines',
                name='Banda Inferior (95%)',
                fill='tonexty',
                fillcolor='rgba(102, 126, 234, 0.15)',
                line=dict(color='rgba(102, 126, 234, 0.2)', width=0),
                showlegend=True,
                hoverinfo='skip'
            ),
            row=1, col=1
        )
    
    # Buffer de seguridad (solo en modo adaptativo)
    if route_selected == 'B' and 'safety_buffer' in df_data.columns:
        fig.add_trace(
            go.Scatter(
                x=df_data['date'],
                y=df_data['adaptive_target'],
                mode='lines',
                name='Target + Buffer',
                line=dict(color='rgba(245, 87, 108, 0.4)', width=2, dash='dash'),
                hovertemplate='<b>Target con Buffer</b>: $%{y:,.0f}<extra></extra>'
            ),
            row=1, col=1
        )
    
    # Línea de referencia (balance inicial)
    fig.add_hline(
        y=df_data['cashflow'].iloc[0],
        line_dash="dot",
        line_color="gray",
        annotation_text="Balance Inicial",
        annotation_position="right",
        row=1, col=1
    )
    
    # Panel inferior: indicadores específicos según ruta
    if route_selected == 'B' and 'shock_intensity' in df_data.columns:
        # Mostrar eventos de shock
        fig.add_trace(
            go.Bar(
                x=df_data['date'],
                y=df_data['shock_intensity'],
                name='Eventos de Shock',
                marker_color='rgba(255, 99, 71, 0.6)',
                hovertemplate='<b>Shock</b>: $%{y:,.0f}<extra></extra>'
            ),
            row=2, col=1
        )
    
    # Configuración del layout
    fig.update_layout(
        height=700,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor="rgba(0,0,0,0)"
        ),
        hovermode='x unified',
        template='plotly_dark',
        paper_bgcolor='#0E1117',
        plot_bgcolor='#1E2530',
        font=dict(color='#C9D1D9', size=12)
    )
    
    fig.update_xaxes(
        title_text="Fecha",
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(139, 148, 158, 0.1)',
        row=1, col=1
    )
    
    fig.update_yaxes(
        title_text="Flujo de Caja ($)",
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(139, 148, 158, 0.1)',
        tickformat='$,.0f',
        row=1, col=1
    )
    
    fig.update_xaxes(title_text="Fecha", row=2, col=1)
    fig.update_yaxes(title_text="Intensidad ($)", row=2, col=1)
    
    return fig


def render_metrics_panel(metrics, route_selected):
    """Renderiza el panel de métricas clave"""
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="💰 Flujo Promedio",
            value=f"${metrics['mean_cashflow']:,.0f}",
            delta=f"σ: ${metrics['std_deviation']:,.0f}"
        )
    
    with col2:
        st.metric(
            label="📊 Volatilidad",
            value=f"{metrics['volatility_index']:.2%}",
            delta="Bajo" if metrics['volatility_index'] < 0.08 else "Alto",
            delta_color="inverse"
        )
    
    with col3:
        if route_selected == 'A':
            st.metric(
                label="📈 Proyección Mín/Máx",
                value=f"${metrics['min_projected']:,.0f}",
                delta=f"Max: ${metrics['max_projected']:,.0f}"
            )
        else:
            st.metric(
                label="⚡ Eventos de Shock",
                value=metrics['num_shock_events'],
                delta=f"Rebalanceos: {metrics['num_rebalances']}"
            )
    
    with col4:
        st.metric(
            label="🎯 Tipo de Modelo",
            value=metrics['model_type'][:20],
            delta=f"Ruta {route_selected}"
        )


def render_reasoning_section(router_decision):
    """Renderiza la sección de razonamiento del agente"""
    
    st.markdown("---")
    st.subheader("🧠 Razonamiento del Agente de Decisión")
    
    route = router_decision.get('route', 'N/A')
    confidence = router_decision.get('confidence', 0)
    reasoning = router_decision.get('reasoning', 'No disponible')
    key_factors = router_decision.get('key_factors', [])
    risk_assessment = router_decision.get('risk_assessment', 'N/A')
    mode = router_decision.get('mode', 'llm')
    
    # Badge de ruta
    badge_class = "route-badge-a" if route == "A" else "route-badge-b"
    route_name = "MOTOR PREDICTIVO (Econométrico)" if route == "A" else "MOTOR ADAPTATIVO (Control Dinámico)"
    
    st.markdown(f'<div class="{badge_class}">✓ {route_name}</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="reasoning-box">', unsafe_allow_html=True)
        st.markdown(f"**🎯 Decisión:** Ruta {route}")
        st.markdown(f"**📊 Nivel de Confianza:** {confidence:.1%}")
        st.markdown(f"**💭 Razonamiento:**")
        st.markdown(f"> {reasoning}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if key_factors and key_factors[0] != 'fallback_heuristic':
            st.markdown("**🔑 Factores Clave Analizados:**")
            for factor in key_factors:
                st.markdown(f"- {factor}")
    
    with col2:
        st.markdown("**⚠️ Evaluación de Riesgo:**")
        st.info(risk_assessment)
        
        if mode == 'fallback':
            st.warning("⚙️ Modo: Lógica Heurística (Sin API Key)")
        else:
            st.success("🤖 Modo: Decisión Autónoma LLM")
    
    # Expandable con JSON completo
    with st.expander("📄 Ver JSON Completo de la Decisión"):
        st.markdown('<div class="code-box">', unsafe_allow_html=True)
        st.json(router_decision)
        st.markdown('</div>', unsafe_allow_html=True)


def render_recommendations(recommendations):
    """Renderiza recomendaciones del engine seleccionado"""
    
    st.markdown("---")
    st.subheader("💡 Recomendaciones Estratégicas")
    
    for rec in recommendations:
        if rec.startswith("✓"):
            st.success(rec)
        elif rec.startswith("⚠"):
            st.warning(rec)
        elif rec.startswith("⚡"):
            st.info(rec)
        else:
            st.write(rec)


def main():
    """Función principal de la aplicación"""
    
    initialize_session_state()
    
    # Header
    st.markdown("# 🧠 Nexus-Fin: Motor de Decisiones en Paralelo")
    st.markdown("### *Predicción vs. Adaptación | Gestión Inteligente de Tesorería*")
    st.markdown("---")
    
    # Sidebar
    config = render_sidebar()
    
    if config['run_button']:
        with st.spinner("🔄 Analizando escenario y ejecutando motor de decisión..."):
            
            # 1. Crear datos del escenario
            scenario_data = create_scenario_data(
                config['scenario_type'],
                {'time_horizon': config['days_horizon']}
            )
            st.session_state.last_scenario = scenario_data
            
            # 2. Inicializar router con LLM
            router = RouterEngine(
                api_key=config['api_key'],
                model=config['model']
            )
            
            # 3. Obtener decisión autónoma del LLM
            route_selected, router_decision = router.analyze_scenario(scenario_data)
            st.session_state.router_decision = router_decision
            
            # 4. Ejecutar el engine correspondiente
            if route_selected == "A":
                engine = PredictiveEngine(initial_balance=config['initial_balance'])
                df_result, metrics = engine.generate_forecast(
                    days=config['days_horizon'],
                    scenario_data=scenario_data
                )
                recommendations = engine.get_recommendations(metrics)
            else:
                engine = AdaptiveEngine(initial_balance=config['initial_balance'])
                df_result, metrics = engine.generate_adaptive_path(
                    days=config['days_horizon'],
                    scenario_data=scenario_data
                )
                recommendations = engine.get_recommendations(metrics)
            
            # 5. Guardar en historial
            st.session_state.execution_history.append({
                'timestamp': datetime.now(),
                'route': route_selected,
                'scenario': config['scenario_type'],
                'metrics': metrics
            })
            
            # 6. Visualización
            st.success(f"✅ Análisis completado - Ruta {route_selected} activada")
            
            # Panel de métricas
            render_metrics_panel(metrics, route_selected)
            
            # Gráfico principal
            st.markdown("---")
            fig = create_visualization(df_result, route_selected, config['scenario_type'])
            st.plotly_chart(fig, use_container_width=True)
            
            # Razonamiento del agente
            render_reasoning_section(router_decision)
            
            # Recomendaciones
            render_recommendations(recommendations)
            
            # Footer con datos del escenario
            with st.expander("📋 Detalles del Escenario Analizado"):
                st.json(scenario_data)
    
    else:
        # Estado inicial
        st.info("👈 Configura los parámetros en la barra lateral y presiona **Ejecutar Análisis**")
        
        # Explicación del sistema
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🎯 ¿Cómo Funciona?")
            st.markdown("""
            **Nexus-Fin** es un sistema de decisión autónoma que:
            
            1. **Analiza** el estado del entorno financiero (volatilidad, liquidez, shocks)
            2. **Consulta** a un LLM vía OpenRouter API
            3. **Decide** autónomamente entre dos rutas:
               - **Ruta A**: Motor Predictivo (proyecciones econométricas)
               - **Ruta B**: Motor Adaptativo (control dinámico)
            4. **Ejecuta** el motor seleccionado
            5. **Visualiza** la trayectoria funcional resultante
            """)
        
        with col2:
            st.markdown("### ⚡ Capacidades")
            st.markdown("""
            - ✅ **Decisión Autónoma**: El LLM elige la estrategia sin intervención
            - ✅ **Razonamiento Transparente**: Justificación explícita en JSON
            - ✅ **Visualización Interactiva**: Curvas funcionales con Plotly
            - ✅ **Modo Fallback**: Funciona sin API key (lógica heurística)
            - ✅ **Escenarios Múltiples**: Estable vs. Shock de Liquidez
            - ✅ **Métricas en Tiempo Real**: Volatilidad, rebalanceos, proyecciones
            """)
        
        st.markdown("---")
        st.markdown("**💡 Stack Tecnológico:** Python 3.11+ | Streamlit | Plotly | OpenRouter API | NumPy | Pandas")


if __name__ == "__main__":
    main()
