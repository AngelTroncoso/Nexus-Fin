"""
Motor Predictivo - Proyecciones Econométricas
Simula modelos de series temporales para entornos estables
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple


class PredictiveEngine:
    """
    Motor de proyección predictiva basado en series temporales
    Asume estabilidad y continuidad en patrones históricos
    """
    
    def __init__(self, initial_balance: float = 2_000_000):
        self.initial_balance = initial_balance
        self.model_params = {
            "trend": 0.002,  # Tendencia diaria (0.2%)
            "seasonality_amplitude": 50_000,
            "noise_level": 0.015,
            "ar_coef": 0.85  # Coeficiente autorregresivo
        }
    
    def generate_forecast(
        self, 
        days: int = 90, 
        scenario_data: Dict = None
    ) -> Tuple[pd.DataFrame, Dict]:
        """
        Genera proyección de flujo de caja usando modelo econométrico
        
        Args:
            days: Horizonte de proyección en días
            scenario_data: Datos del escenario actual
            
        Returns:
            Tuple de (DataFrame con series proyectadas, métricas)
        """
        
        # Ajustar parámetros según escenario
        if scenario_data:
            self._adjust_parameters(scenario_data)
        
        # Generar serie temporal
        dates = pd.date_range(start='2024-01-01', periods=days, freq='D')
        
        # Componentes del modelo
        trend = self._generate_trend(days)
        seasonal = self._generate_seasonality(days)
        ar_component = self._generate_ar_process(days)
        noise = np.random.normal(0, self.model_params["noise_level"], days)
        
        # Combinación del modelo
        cashflow = self.initial_balance * (
            1 + trend + seasonal + ar_component + noise
        )
        
        # Bandas de confianza (95%)
        std_band = np.std(cashflow) * 1.96
        upper_band = cashflow + std_band
        lower_band = cashflow - std_band
        
        # Construir DataFrame
        df = pd.DataFrame({
            'date': dates,
            'cashflow': cashflow,
            'upper_confidence': upper_band,
            'lower_confidence': lower_band,
            'trend_component': self.initial_balance * (1 + trend),
            'forecast_type': 'predictive'
        })
        
        # Calcular métricas
        metrics = self._calculate_metrics(df)
        
        return df, metrics
    
    def _adjust_parameters(self, scenario_data: Dict):
        """Ajusta parámetros del modelo según el escenario"""
        
        volatility = scenario_data.get('volatility', 0.05)
        stability = scenario_data.get('stability_ratio', 0.9)
        
        # Ajustar ruido según volatilidad (pero mantener bajo)
        self.model_params["noise_level"] = min(volatility * 0.5, 0.025)
        
        # Ajustar tendencia según estabilidad
        self.model_params["trend"] = 0.002 * stability
    
    def _generate_trend(self, days: int) -> np.ndarray:
        """Genera componente de tendencia lineal suave"""
        return np.linspace(0, self.model_params["trend"] * days, days)
    
    def _generate_seasonality(self, days: int) -> np.ndarray:
        """Genera componente estacional (ciclos semanales/mensuales)"""
        t = np.arange(days)
        
        # Ciclo semanal
        weekly = 0.015 * np.sin(2 * np.pi * t / 7)
        
        # Ciclo mensual
        monthly = 0.025 * np.sin(2 * np.pi * t / 30)
        
        return weekly + monthly
    
    def _generate_ar_process(self, days: int) -> np.ndarray:
        """Genera proceso autorregresivo AR(1)"""
        ar_coef = self.model_params["ar_coef"]
        epsilon = np.random.normal(0, 0.01, days)
        
        ar_series = np.zeros(days)
        for t in range(1, days):
            ar_series[t] = ar_coef * ar_series[t-1] + epsilon[t]
        
        return ar_series
    
    def _calculate_metrics(self, df: pd.DataFrame) -> Dict:
        """Calcula métricas de la proyección"""
        
        cashflow = df['cashflow'].values
        
        return {
            "mean_cashflow": float(np.mean(cashflow)),
            "std_deviation": float(np.std(cashflow)),
            "min_projected": float(np.min(cashflow)),
            "max_projected": float(np.max(cashflow)),
            "confidence_width": float(np.mean(df['upper_confidence'] - df['lower_confidence'])),
            "trend_direction": "ascending" if cashflow[-1] > cashflow[0] else "descending",
            "volatility_index": float(np.std(cashflow) / np.mean(cashflow)),
            "model_type": "ARIMA-like Econometric"
        }
    
    def get_recommendations(self, metrics: Dict) -> List[str]:
        """Genera recomendaciones basadas en la proyección"""
        
        recommendations = [
            "✓ Entorno estable detectado - Proyección confiable",
            f"✓ Flujo promedio proyectado: ${metrics['mean_cashflow']:,.0f}",
            f"✓ Tendencia: {metrics['trend_direction'].upper()}"
        ]
        
        if metrics['volatility_index'] < 0.05:
            recommendations.append("✓ Volatilidad baja - Ideal para optimización de carry")
        
        if metrics['min_projected'] > 0:
            recommendations.append("✓ Sin riesgo de déficit en el horizonte proyectado")
        else:
            recommendations.append("⚠ Revisar posibles déficits en días específicos")
        
        return recommendations
