"""
Motor Adaptativo - Control Dinámico y Rebalanceo
Simula políticas reactivas ante shocks y alta volatilidad
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple


class AdaptiveEngine:
    """
    Motor de control adaptativo con rebalanceo dinámico
    Diseñado para entornos volátiles y shocks de liquidez
    """
    
    def __init__(self, initial_balance: float = 2_000_000):
        self.initial_balance = initial_balance
        self.control_params = {
            "safety_buffer": 0.20,  # 20% de buffer de seguridad
            "rebalance_threshold": 0.10,  # Rebalancear si desviación > 10%
            "shock_damping": 0.65,  # Factor de amortiguamiento ante shocks
            "recovery_rate": 0.03  # Tasa de recuperación post-shock
        }
        self.shock_events = []
    
    def generate_adaptive_path(
        self, 
        days: int = 90, 
        scenario_data: Dict = None
    ) -> Tuple[pd.DataFrame, Dict]:
        """
        Genera trayectoria adaptativa con rebalanceo dinámico
        
        Args:
            days: Horizonte de simulación en días
            scenario_data: Datos del escenario actual
            
        Returns:
            Tuple de (DataFrame con trayectoria adaptativa, métricas)
        """
        
        # Ajustar parámetros según escenario
        if scenario_data:
            self._configure_for_scenario(scenario_data)
        
        dates = pd.date_range(start='2024-01-01', periods=days, freq='D')
        
        # Inicializar arrays
        cashflow = np.zeros(days)
        cashflow[0] = self.initial_balance
        
        safety_buffer = np.zeros(days)
        rebalance_actions = np.zeros(days)
        shock_intensity = np.zeros(days)
        
        # Simular shocks aleatorios
        shock_days = self._generate_shock_schedule(days, scenario_data)
        
        # Simulación dinámica día a día
        for t in range(1, days):
            # Detectar shock
            is_shock_day = t in shock_days
            
            if is_shock_day:
                shock_magnitude = self._generate_shock_magnitude(scenario_data)
                shock_intensity[t] = shock_magnitude
                self.shock_events.append({'day': t, 'magnitude': shock_magnitude})
            else:
                shock_magnitude = 0
            
            # Aplicar shock amortiguado
            shock_impact = shock_magnitude * (1 - self.control_params["shock_damping"])
            
            # Calcular flujo base con recuperación
            base_flow = cashflow[t-1] * (1 + self.control_params["recovery_rate"] / 30)
            
            # Aplicar shock
            cashflow[t] = base_flow - shock_impact
            
            # Calcular buffer de seguridad dinámico
            volatility_estimate = np.std(cashflow[max(0, t-10):t+1])
            safety_buffer[t] = cashflow[t] * self.control_params["safety_buffer"] + volatility_estimate * 2
            
            # Decisión de rebalanceo
            deviation = abs(cashflow[t] - self.initial_balance) / self.initial_balance
            
            if deviation > self.control_params["rebalance_threshold"]:
                rebalance_amount = (self.initial_balance - cashflow[t]) * 0.5
                cashflow[t] += rebalance_amount
                rebalance_actions[t] = rebalance_amount
        
        # Construir DataFrame
        df = pd.DataFrame({
            'date': dates,
            'cashflow': cashflow,
            'safety_buffer': safety_buffer,
            'rebalance_actions': rebalance_actions,
            'shock_intensity': shock_intensity,
            'adaptive_target': self.initial_balance + safety_buffer,
            'forecast_type': 'adaptive'
        })
        
        # Calcular métricas
        metrics = self._calculate_metrics(df)
        
        return df, metrics
    
    def _configure_for_scenario(self, scenario_data: Dict):
        """Configura parámetros adaptativos según escenario"""
        
        volatility = scenario_data.get('volatility', 0.15)
        shock_detected = scenario_data.get('shock_detected', False)
        
        # Aumentar buffer en entornos volátiles
        self.control_params["safety_buffer"] = min(0.15 + volatility, 0.35)
        
        # Ajustar sensibilidad de rebalanceo
        if shock_detected:
            self.control_params["rebalance_threshold"] = 0.05  # Más reactivo
            self.control_params["shock_damping"] = 0.50  # Menor amortiguamiento inicial
        else:
            self.control_params["rebalance_threshold"] = 0.10
            self.control_params["shock_damping"] = 0.65
    
    def _generate_shock_schedule(self, days: int, scenario_data: Dict = None) -> List[int]:
        """Genera calendario de eventos de shock"""
        
        if scenario_data and scenario_data.get('shock_detected'):
            # Escenario de crisis: shocks frecuentes
            num_shocks = max(3, days // 15)
            shock_days = np.random.choice(
                range(5, days), 
                size=num_shocks, 
                replace=False
            )
        else:
            # Escenario normal: shocks ocasionales
            num_shocks = max(1, days // 45)
            shock_days = np.random.choice(
                range(10, days), 
                size=num_shocks, 
                replace=False
            )
        
        return sorted(shock_days.tolist())
    
    def _generate_shock_magnitude(self, scenario_data: Dict = None) -> float:
        """Genera magnitud de un shock de liquidez"""
        
        if scenario_data and scenario_data.get('shock_detected'):
            # Shocks severos en crisis
            base_magnitude = self.initial_balance * 0.25
            variance = base_magnitude * 0.5
        else:
            # Shocks moderados en escenario normal
            base_magnitude = self.initial_balance * 0.08
            variance = base_magnitude * 0.3
        
        return abs(np.random.normal(base_magnitude, variance))
    
    def _calculate_metrics(self, df: pd.DataFrame) -> Dict:
        """Calcula métricas de la trayectoria adaptativa"""
        
        cashflow = df['cashflow'].values
        rebalances = df['rebalance_actions'].values
        shocks = df['shock_intensity'].values
        
        num_rebalances = np.sum(rebalances != 0)
        num_shocks = np.sum(shocks > 0)
        total_shock_impact = np.sum(shocks)
        
        return {
            "mean_cashflow": float(np.mean(cashflow)),
            "std_deviation": float(np.std(cashflow)),
            "min_cashflow": float(np.min(cashflow)),
            "max_cashflow": float(np.max(cashflow)),
            "num_rebalances": int(num_rebalances),
            "num_shock_events": int(num_shocks),
            "total_shock_impact": float(total_shock_impact),
            "avg_shock_magnitude": float(total_shock_impact / num_shocks if num_shocks > 0 else 0),
            "recovery_efficiency": float((cashflow[-1] - cashflow.min()) / (cashflow.max() - cashflow.min()) if cashflow.max() != cashflow.min() else 1.0),
            "volatility_index": float(np.std(cashflow) / np.mean(cashflow)),
            "model_type": "Dynamic Control Policy"
        }
    
    def get_recommendations(self, metrics: Dict) -> List[str]:
        """Genera recomendaciones basadas en la simulación adaptativa"""
        
        recommendations = [
            "⚡ Modo adaptativo activado - Control dinámico habilitado",
            f"⚡ Acciones de rebalanceo ejecutadas: {metrics['num_rebalances']}",
            f"⚡ Eventos de shock manejados: {metrics['num_shock_events']}"
        ]
        
        if metrics['recovery_efficiency'] > 0.7:
            recommendations.append("✓ Alta eficiencia de recuperación post-shock")
        else:
            recommendations.append("⚠ Revisar capacidad de recuperación ante shocks")
        
        if metrics['min_cashflow'] > self.initial_balance * 0.6:
            recommendations.append("✓ Buffer de seguridad mantenido durante toda la simulación")
        else:
            recommendations.append("⚠ Se detectaron caídas significativas - Considerar aumentar buffer")
        
        if metrics['num_rebalances'] > 15:
            recommendations.append("💰 Alto costo operativo por rebalanceos frecuentes")
        
        return recommendations
