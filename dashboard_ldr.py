import streamlit as st
import serial
import time
from collections import deque
import matplotlib.pyplot as plt

st.title("Monitor de Luz en Tiempo Real")
st.markdown("Sensor LDR conectado a Arduino")

PUERTO = 'COM7'
BAUDIOS = 9600
MAX_DATOS = 50

if 'datos' not in st.session_state:
    st.session_state.datos = deque([0] * MAX_DATOS, maxlen=MAX_DATOS)

try:
    ser = serial.Serial(PUERTO, BAUDIOS, timeout=1)
    time.sleep(2)

    linea = ser.readline().decode('utf-8').strip()
    luz = float(linea)
    st.session_state.datos.append(luz)
    ser.close()

    # Mostrar valor actual
    st.metric(label="Nivel de luz", value=f"{luz:.1f}%")

    # Graficar
    fig, ax = plt.subplots()
    ax.plot(list(st.session_state.datos), color='orange')
    ax.set_ylim(0, 100)
    ax.set_ylabel("Luz (%)")
    ax.set_xlabel("Muestras")
    ax.set_title("Nivel de luz - LDR")
    ax.grid(True)
    st.pyplot(fig)
    plt.close(fig)

except Exception as e:
    st.error(f"Error: {e}")

# Actualizar cada segundo
time.sleep(1)
st.rerun()