"""
Router Engine - Decisión Autónoma de Ruta (Predictivo vs Adaptativo)
Utiliza OpenRouter API con LLM para determinar la estrategia óptima
"""

import os
import json
import requests
from typing import Dict, Tuple, Optional
from dotenv import load_dotenv

load_dotenv()


class RouterEngine:
    """Motor de enrutamiento inteligente usando LLM via OpenRouter"""
    
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        self.model = model or os.getenv("OPENROUTER_MODEL", "nvidia/nemotron-3-nano-30b-a3b:free")
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        
    def analyze_scenario(self, scenario_data: Dict) -> Tuple[str, Dict]:
        """
        Analiza el escenario financiero y decide la ruta óptima
        
        Args:
            scenario_data: Diccionario con métricas del entorno financiero
            
        Returns:
            Tuple de (ruta_elegida, razonamiento_completo)
        """
        
        # Preparar el contexto para el LLM
        prompt = self._build_decision_prompt(scenario_data)
        
        # Si no hay API key, usar lógica determinista
        if not self.api_key or self.api_key == "tu_clave_aqui":
            return self._fallback_logic(scenario_data)
        
        try:
            # Llamada a OpenRouter API
            response = self._call_openrouter(prompt)
            
            # Parsear la respuesta
            decision = self._parse_llm_response(response)
            
            return decision["route"], decision
            
        except Exception as e:
            print(f"Error en llamada a LLM: {str(e)}")
            return self._fallback_logic(scenario_data)
    
    def _build_decision_prompt(self, scenario_data: Dict) -> str:
        """Construye el prompt para el LLM"""
        
        prompt = f"""Eres un Arquitecto de Decisiones Financieras especializado en gestión de tesorería.

CONTEXTO DEL ESCENARIO ACTUAL:
- Tipo de Entorno: {scenario_data['scenario_type']}
- Volatilidad del Mercado: {scenario_data['volatility']:.2%}
- Liquidez Disponible: ${scenario_data['liquidity']:,.2f}
- Tendencia de Flujo de Caja: {scenario_data['cashflow_trend']}
- Shock de Mercado Detectado: {'SÍ' if scenario_data['shock_detected'] else 'NO'}
- Horizonte Temporal: {scenario_data['time_horizon']} días

MÉTRICAS TÉCNICAS:
- Ratio de Estabilidad: {scenario_data['stability_ratio']:.2f}
- Coeficiente de Variación: {scenario_data['variation_coef']:.2f}
- Desviación Estándar: {scenario_data['std_dev']:.2f}

RUTAS DISPONIBLES:

**Ruta A - Motor Predictivo (Econométrico)**
- Ideal para: Entornos estables con series temporales predecibles
- Estrategia: Proyecciones basadas en modelos ARIMA, suavización exponencial
- Ventajas: Precisión en horizontes medios, optimización de costos de carry
- Riesgos: Falla ante shocks no anticipados

**Ruta B - Motor Adaptativo (Control Dinámico)**
- Ideal para: Alta volatilidad, shocks de liquidez, incertidumbre extrema
- Estrategia: Políticas de rebalanceo reactivo, buffers de seguridad dinámicos
- Ventajas: Resiliencia ante eventos extremos, protección de capital
- Riesgos: Mayor costo operativo, menor eficiencia en entornos estables

TU TAREA:
Analiza el escenario y decide de manera autónoma cuál ruta es óptima.

Responde ÚNICAMENTE en formato JSON válido con esta estructura exacta:
{{
  "route": "A" o "B",
  "confidence": 0.0 a 1.0,
  "reasoning": "Explicación detallada de tu decisión en 2-3 oraciones",
  "key_factors": ["factor1", "factor2", "factor3"],
  "risk_assessment": "Breve evaluación de riesgos",
  "recommended_horizon": "corto_plazo" o "medio_plazo" o "largo_plazo"
}}

NO incluyas texto adicional fuera del JSON."""

        return prompt
    
    def _call_openrouter(self, prompt: str) -> Dict:
        """Realiza la llamada HTTP a OpenRouter API"""
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://nexus-fin-demo.local",
            "X-Title": "Nexus-Fin Treasury Engine"
        }
        
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": "Eres un experto en análisis financiero y toma de decisiones cuantitativas. Respondes siempre en JSON válido."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.3,  # Baja temperatura para decisiones consistentes
            "max_tokens": 500
        }
        
        response = requests.post(
            self.base_url,
            headers=headers,
            json=payload,
            timeout=30
        )
        
        response.raise_for_status()
        return response.json()
    
    def _parse_llm_response(self, api_response: Dict) -> Dict:
        """Extrae y valida la decisión del LLM"""
        
        try:
            content = api_response["choices"][0]["message"]["content"]
            
            # Limpiar posibles markdown code blocks
            content = content.strip()
            if content.startswith("```json"):
                content = content[7:]
            if content.startswith("```"):
                content = content[3:]
            if content.endswith("```"):
                content = content[:-3]
            content = content.strip()
            
            decision = json.loads(content)
            
            # Validar estructura
            required_keys = ["route", "confidence", "reasoning"]
            if not all(key in decision for key in required_keys):
                raise ValueError("Respuesta del LLM incompleta")
            
            # Normalizar ruta
            decision["route"] = decision["route"].upper()
            if decision["route"] not in ["A", "B"]:
                raise ValueError(f"Ruta inválida: {decision['route']}")
            
            return decision
            
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            # Fallback si el LLM responde mal
            print(f"Error parseando respuesta LLM: {e}")
            print(f"Contenido recibido: {content if 'content' in locals() else 'N/A'}")
            raise
    
    def _fallback_logic(self, scenario_data: Dict) -> Tuple[str, Dict]:
        """Lógica determinista cuando no hay API key o falla el LLM"""
        
        # Reglas heurísticas simples
        shock = scenario_data['shock_detected']
        volatility = scenario_data['volatility']
        stability = scenario_data['stability_ratio']
        
        if shock or volatility > 0.15 or stability < 0.6:
            route = "B"
            reasoning = "Modo adaptativo activado: alta volatilidad o shock detectado"
            confidence = 0.75
        else:
            route = "A"
            reasoning = "Modo predictivo activado: entorno estable con baja volatilidad"
            confidence = 0.85
        
        return route, {
            "route": route,
            "confidence": confidence,
            "reasoning": reasoning,
            "key_factors": ["fallback_heuristic"],
            "risk_assessment": "Decisión automática sin LLM",
            "recommended_horizon": "medio_plazo",
            "mode": "fallback"
        }


def create_scenario_data(scenario_type: str, custom_params: Optional[Dict] = None) -> Dict:
    """
    Genera datos de escenario para análisis
    
    Args:
        scenario_type: 'stable' o 'shock'
        custom_params: Parámetros personalizados opcionales
    """
    
    if scenario_type == "stable":
        base_data = {
            "scenario_type": "Entorno Estable",
            "volatility": 0.05,
            "liquidity": 2_500_000,
            "cashflow_trend": "Ascendente Moderada",
            "shock_detected": False,
            "time_horizon": 90,
            "stability_ratio": 0.92,
            "variation_coef": 0.08,
            "std_dev": 45_000
        }
    else:  # shock
        base_data = {
            "scenario_type": "Shock de Liquidez Crítico",
            "volatility": 0.28,
            "liquidity": 850_000,
            "cashflow_trend": "Descendente Abrupta",
            "shock_detected": True,
            "time_horizon": 30,
            "stability_ratio": 0.43,
            "variation_coef": 0.35,
            "std_dev": 180_000
        }
    
    if custom_params:
        base_data.update(custom_params)
    
    return base_data
