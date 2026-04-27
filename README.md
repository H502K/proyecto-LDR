# Monitor de Luz en Tiempo Real 🌟
Dashboard de monitoreo de nivel de luz usando Arduino y Python.

## Descripción
Sistema de adquisición y visualización de datos en tiempo real 
mediante un sensor LDR conectado a Arduino, con dashboard 
interactivo desarrollado en Python con Streamlit.

## Tecnologías utilizadas
- Arduino Uno
- Python 3
- Streamlit
- Matplotlib
- PySerial

## Componentes de hardware
- Arduino Uno
- Sensor LDR
- Resistencia 10kΩ

## Funcionamiento
1. El sensor LDR mide el nivel de luz del ambiente
2. Arduino envía los datos por puerto serial a Python
3. Python procesa y visualiza los datos en tiempo real
4. El dashboard muestra la gráfica actualizada en el navegador

## Cómo ejecutar
1. Cargar `codigo_arduino.ino` en el Arduino
2. Instalar dependencias Python:
```bash
pip install streamlit pyserial matplotlib
```
3. Ejecutar el dashboard:
```bash
python -m streamlit run dashboard_ldr.py
```

## Autor
Vanesa Cuasapaz — Ingeniera Electrónica
