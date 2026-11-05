"""
Script de Prueba del Sistema Nexus-Fin
Ejecuta tests sin necesidad de la interfaz Streamlit
"""

import sys
from router_engine import RouterEngine, create_scenario_data
from engines.predictive_engine import PredictiveEngine
from engines.adaptive_engine import AdaptiveEngine


def print_separator(title=""):
    print("\n" + "="*70)
    if title:
        print(f"  {title}")
        print("="*70)


def test_router_fallback():
    """Test del router en modo fallback (sin API key)"""
    
    print_separator("TEST 1: Router en Modo Fallback")
    
    # Escenario estable
    print("\n[Escenario 1] Entorno Estable")
    scenario_stable = create_scenario_data("stable")
    router = RouterEngine(api_key=None)
    route, decision = router.analyze_scenario(scenario_stable)
    
    print(f"✓ Ruta seleccionada: {route}")
    print(f"✓ Confianza: {decision['confidence']:.1%}")
    print(f"✓ Razonamiento: {decision['reasoning']}")
    print(f"✓ Modo: {decision.get('mode', 'llm')}")
    
    assert route in ["A", "B"], "Ruta debe ser A o B"
    
    # Escenario de shock
    print("\n[Escenario 2] Shock de Liquidez")
    scenario_shock = create_scenario_data("shock")
    route, decision = router.analyze_scenario(scenario_shock)
    
    print(f"✓ Ruta seleccionada: {route}")
    print(f"✓ Confianza: {decision['confidence']:.1%}")
    print(f"✓ Razonamiento: {decision['reasoning']}")
    
    assert route in ["A", "B"], "Ruta debe ser A o B"
    
    print("\n✅ Test de Router Fallback: PASADO")


def test_predictive_engine():
    """Test del motor predictivo"""
    
    print_separator("TEST 2: Motor Predictivo")
    
    engine = PredictiveEngine(initial_balance=2_000_000)
    scenario = create_scenario_data("stable")
    
    print("\n[Generando proyección econométrica...]")
    df, metrics = engine.generate_forecast(days=90, scenario_data=scenario)
    
    print(f"\n✓ Días proyectados: {len(df)}")
    print(f"✓ Flujo promedio: ${metrics['mean_cashflow']:,.0f}")
    print(f"✓ Desviación estándar: ${metrics['std_deviation']:,.0f}")
    print(f"✓ Volatilidad: {metrics['volatility_index']:.2%}")
    print(f"✓ Proyección mínima: ${metrics['min_projected']:,.0f}")
    print(f"✓ Proyección máxima: ${metrics['max_projected']:,.0f}")
    print(f"✓ Tipo de modelo: {metrics['model_type']}")
    
    assert len(df) == 90, "Debe proyectar 90 días"
    assert metrics['mean_cashflow'] > 0, "Flujo promedio debe ser positivo"
    
    print("\n[Recomendaciones generadas:]")
    recommendations = engine.get_recommendations(metrics)
    for rec in recommendations:
        print(f"  {rec}")
    
    print("\n✅ Test de Motor Predictivo: PASADO")


def test_adaptive_engine():
    """Test del motor adaptativo"""
    
    print_separator("TEST 3: Motor Adaptativo")
    
    engine = AdaptiveEngine(initial_balance=2_000_000)
    scenario = create_scenario_data("shock")
    
    print("\n[Generando trayectoria adaptativa...]")
    df, metrics = engine.generate_adaptive_path(days=90, scenario_data=scenario)
    
    print(f"\n✓ Días simulados: {len(df)}")
    print(f"✓ Flujo promedio: ${metrics['mean_cashflow']:,.0f}")
    print(f"✓ Desviación estándar: ${metrics['std_deviation']:,.0f}")
    print(f"✓ Volatilidad: {metrics['volatility_index']:.2%}")
    print(f"✓ Flujo mínimo: ${metrics['min_cashflow']:,.0f}")
    print(f"✓ Flujo máximo: ${metrics['max_cashflow']:,.0f}")
    print(f"✓ Número de rebalanceos: {metrics['num_rebalances']}")
    print(f"✓ Eventos de shock: {metrics['num_shock_events']}")
    print(f"✓ Impacto total de shocks: ${metrics['total_shock_impact']:,.0f}")
    print(f"✓ Eficiencia de recuperación: {metrics['recovery_efficiency']:.1%}")
    print(f"✓ Tipo de modelo: {metrics['model_type']}")
    
    assert len(df) == 90, "Debe simular 90 días"
    assert metrics['num_rebalances'] >= 0, "Rebalanceos debe ser >= 0"
    assert metrics['num_shock_events'] > 0, "Debe haber al menos un shock"
    
    print("\n[Recomendaciones generadas:]")
    recommendations = engine.get_recommendations(metrics)
    for rec in recommendations:
        print(f"  {rec}")
    
    print("\n✅ Test de Motor Adaptativo: PASADO")


def test_integration():
    """Test de integración completa"""
    
    print_separator("TEST 4: Integración Completa")
    
    # Crear escenario
    scenario = create_scenario_data("stable")
    
    # Router decide
    print("\n[1] Router analizando escenario...")
    router = RouterEngine(api_key=None)
    route, decision = router.analyze_scenario(scenario)
    print(f"✓ Decisión: Ruta {route}")
    
    # Ejecutar engine correspondiente
    print(f"\n[2] Ejecutando Motor {'Predictivo' if route == 'A' else 'Adaptativo'}...")
    
    if route == "A":
        engine = PredictiveEngine(initial_balance=2_000_000)
        df, metrics = engine.generate_forecast(days=90, scenario_data=scenario)
    else:
        engine = AdaptiveEngine(initial_balance=2_000_000)
        df, metrics = engine.generate_adaptive_path(days=90, scenario_data=scenario)
    
    print(f"✓ Datos generados: {len(df)} registros")
    print(f"✓ Métricas calculadas: {len(metrics)} indicadores")
    
    # Validar salidas
    print("\n[3] Validando salidas...")
    assert 'date' in df.columns, "DataFrame debe tener columna 'date'"
    assert 'cashflow' in df.columns, "DataFrame debe tener columna 'cashflow'"
    assert 'mean_cashflow' in metrics, "Metrics debe tener 'mean_cashflow'"
    assert 'volatility_index' in metrics, "Metrics debe tener 'volatility_index'"
    
    print("✓ Estructura de datos válida")
    
    print("\n✅ Test de Integración: PASADO")


def test_scenario_creation():
    """Test de creación de escenarios"""
    
    print_separator("TEST 5: Creación de Escenarios")
    
    print("\n[Escenario Estable]")
    stable = create_scenario_data("stable")
    print(f"  Tipo: {stable['scenario_type']}")
    print(f"  Volatilidad: {stable['volatility']:.2%}")
    print(f"  Liquidez: ${stable['liquidity']:,.0f}")
    print(f"  Shock detectado: {stable['shock_detected']}")
    print(f"  Ratio de estabilidad: {stable['stability_ratio']:.2f}")
    
    assert stable['volatility'] < 0.1, "Escenario estable debe tener baja volatilidad"
    assert not stable['shock_detected'], "Escenario estable no debe tener shock"
    
    print("\n[Escenario de Shock]")
    shock = create_scenario_data("shock")
    print(f"  Tipo: {shock['scenario_type']}")
    print(f"  Volatilidad: {shock['volatility']:.2%}")
    print(f"  Liquidez: ${shock['liquidity']:,.0f}")
    print(f"  Shock detectado: {shock['shock_detected']}")
    print(f"  Ratio de estabilidad: {shock['stability_ratio']:.2f}")
    
    assert shock['volatility'] > 0.2, "Escenario de shock debe tener alta volatilidad"
    assert shock['shock_detected'], "Escenario de shock debe tener shock detectado"
    
    print("\n[Escenario Personalizado]")
    custom = create_scenario_data("stable", {"volatility": 0.12, "liquidity": 1_500_000})
    print(f"  Volatilidad personalizada: {custom['volatility']:.2%}")
    print(f"  Liquidez personalizada: ${custom['liquidity']:,.0f}")
    
    assert custom['volatility'] == 0.12, "Debe aplicar parámetros personalizados"
    assert custom['liquidity'] == 1_500_000, "Debe aplicar parámetros personalizados"
    
    print("\n✅ Test de Creación de Escenarios: PASADO")


def run_all_tests():
    """Ejecuta todos los tests"""
    
    print_separator("NEXUS-FIN: Sistema de Tests")
    print("\nEjecutando batería de tests del sistema...\n")
    
    tests = [
        ("Creación de Escenarios", test_scenario_creation),
        ("Router en Modo Fallback", test_router_fallback),
        ("Motor Predictivo", test_predictive_engine),
        ("Motor Adaptativo", test_adaptive_engine),
        ("Integración Completa", test_integration)
    ]
    
    results = []
    
    for name, test_func in tests:
        try:
            test_func()
            results.append((name, "PASADO"))
        except AssertionError as e:
            results.append((name, f"FALLADO: {str(e)}"))
            print(f"\n❌ Test fallido: {e}")
        except Exception as e:
            results.append((name, f"ERROR: {str(e)}"))
            print(f"\n❌ Error inesperado: {e}")
    
    # Resumen final
    print_separator("RESUMEN DE TESTS")
    
    passed = sum(1 for _, result in results if result == "PASADO")
    total = len(results)
    
    print(f"\nResultados: {passed}/{total} tests pasados\n")
    
    for name, result in results:
        status = "✅" if result == "PASADO" else "❌"
        print(f"{status} {name}: {result}")
    
    print_separator()
    
    if passed == total:
        print("\n🎉 ¡TODOS LOS TESTS PASARON!")
        print("\nEl sistema está listo para ejecutarse con Streamlit:")
        print("  streamlit run app.py\n")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test(s) fallaron.")
        print("Por favor, revisa los errores arriba.\n")
        return 1


if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)
