# Proyecto Final Grupo 4

## Descripción
Drowsiness Processor es una aplicación diseñada para detectar signos de somnolencia en tiempo real mediante el análisis de imágenes faciales y movimientos de las manos. Utiliza procesamiento de imágenes con modelos de aprendizaje automático para evaluar parpadeos, inclinación de la cabeza y bostezos, ayudando a prevenir accidentes debido a fatiga.

Este proyecto se basa en la ingeniería inversa del repositorio [driver_fatigue_detection](https://github.com/AprendeIngenia/driver_fatigue_detection) desarrollado por **AprendeIngenia**, al cual damos los créditos correspondientes. Se han agregado nuevas funcionalidades y optimizaciones.

## Características Principales
- **Procesamiento en tiempo real:** Utiliza Mediapipe para detectar puntos clave faciales y de las manos.
- **API robusta con FastAPI:** Permite una arquitectura modular y extensible.
- **YOLOv8:** Para la detección avanzada de objetos.
- **Nuevo Sistema de Alertas Sonoras:** Implementado con `pygame`.
- **Análisis Automático de Código:** Usamos **DeepSource** y **SonarQube** para mejorar la calidad del código y aplicar correcciones automáticas.
---

## Instalación
### Requisitos
Antes de instalar, asegúrate de tener los siguientes requisitos:
- **Sistema operativo compatible:** Windows, Linux o macOS
- **Python 3.10 o superior**
- **CUDA 11.7** (opcional para aceleración en GPU)
- **Paquetes adicionales:** NumPy, OpenCV, Flet, pygame, threading, etc. Consulte `requirements.txt` para ver la lista completa de dependencias.

### Clonar el Repositorio
```bash
git clone https://github.com/Grupo4-Construccion/ProyectoFinal-Grupo4.git
cd ProyectoFinal-Grupo4
```

### Crear y Activar Entorno Virtual
```bash
python -m venv venv
```

Activar en **Windows**:
```bash
./venv/Scripts/activate
```

Activar en **Linux**:
```bash
source venv/bin/activate
```

### Instalar Dependencias
```bash
pip install -r requirements.txt
```

---

## Uso
### 1. Iniciar el Servidor API
El sistema utiliza **FastAPI** para proporcionar una interfaz de comunicación entre la detección en tiempo real y la aplicación.

Para iniciar el servidor, ejecuta:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```
Esto iniciará el servidor en `http://localhost:8000`, donde se podrá consumir la API.

### 2. Ejecutar el Proyecto
Para iniciar la detección de somnolencia en tiempo real, en una nueva terminal ejecuta (vuelve a activar el entorno):
```bash
python main.py
```

### 3. Análisis en Tiempo Real
- La aplicación procesará la entrada de la cámara.
- Se visualizarán los resultados en tiempo real con indicadores de fatiga.
- Se generarán reportes de alerta en formato CSV.
- Se activará **una alerta sonora** en caso de somnolencia detectada.

### 4. Generación de Reportes
Los reportes se guardarán en la carpeta `reports/`.

---

## Análisis de Calidad de Código con DeepSource y SonarQube
Para garantizar un código limpio y seguro, utilizamos:
- **DeepSource:** Análisis automatizado con autofix en GitHub.
- **SonarQube:** Evaluación detallada de calidad y seguridad del código.

---

## Pruebas Automáticas con GitHub Actions
El proyecto cuenta con un conjunto de **pruebas unitarias** escritas en `unittest` para validar las funcionalidades clave, asegurando que los cambios en el código no introduzcan errores inesperados.

### Configuración de GitHub Actions
Hemos configurado un workflow en `.github/workflows/python-app.yml` que ejecuta automáticamente las pruebas en cada `push` y `pull request` al repositorio.

### Configuración de Pytest
Se ha configurado `pytest` para el manejo de pruebas asíncronas mediante el archivo `pytest.ini`, que contiene la siguiente configuración:
```ini
[pytest]
asyncio_mode = auto
```
Esto permite ejecutar pruebas que involucran operaciones asíncronas de manera eficiente, asegurando la correcta validación del código sin bloqueos innecesarios.

### Ejecución de Pruebas
Las pruebas incluyen:
- **Generación de reportes de somnolencia** (`DrowsinessReports`)
- **Procesamiento de características de somnolencia** (`FeaturesDrowsinessProcessing`)
- **Detección de frotamiento de ojos** (`EyeRubDetection`)
- **Contador y reportes de frotamiento de ojos** (`EyeRubCounter`, `EyeRubReportGenerator`)

Ejemplo de ejecución manual de pruebas:
```bash
python -m unittest discover tests/
```
También se pueden ejecutar las pruebas con `pytest` de la siguiente manera:
```bash
pytest tests/
```
---

## Créditos y Autores
- **Basado en:** [driver_fatigue_detection](https://github.com/AprendeIngenia/driver_fatigue_detection) de AprendeIngenia.
- **Modificado y mejorado por:**
    - **Sebastian Aisalla**
    - **Tatiana Gualpa**
    - **Marcelo Maisincho**
    - **Stalin Yungan**

---

## Licencia
Este proyecto está bajo la **Licencia MIT**. Puedes usarlo y modificarlo libremente.


