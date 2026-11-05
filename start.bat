@echo off
echo ========================================
echo   Nexus-Fin: Motor de Decisiones
echo   Iniciando aplicacion Streamlit...
echo ========================================
echo.

REM Verificar si existe el entorno virtual
if not exist "venv\" (
    echo [!] No se encontro entorno virtual.
    echo [*] Creando entorno virtual...
    python -m venv venv
    echo [OK] Entorno virtual creado.
    echo.
)

REM Activar entorno virtual
call venv\Scripts\activate.bat

REM Verificar si estan instaladas las dependencias
pip show streamlit >nul 2>&1
if errorlevel 1 (
    echo [!] Dependencias no encontradas.
    echo [*] Instalando dependencias...
    pip install -r requirements.txt
    echo [OK] Dependencias instaladas.
    echo.
)

REM Verificar si existe .env
if not exist ".env" (
    echo [!] Archivo .env no encontrado.
    echo [*] Copiando .env.example a .env...
    copy .env.example .env
    echo [!] IMPORTANTE: Configura tu OPENROUTER_API_KEY en el archivo .env
    echo.
    pause
)

REM Iniciar Streamlit
echo [*] Iniciando Nexus-Fin...
echo [*] La aplicacion se abrira en tu navegador.
echo [*] Presiona Ctrl+C para detener el servidor.
echo.

streamlit run app.py

pause
