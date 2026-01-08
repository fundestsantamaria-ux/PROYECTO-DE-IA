# 🤟 Signify — Traductor de Lengua de Señas (EC/CL/MX)

**Tecnología para incluir, aprender y comunicar.** Signify es una plataforma web que permite **buscar, comparar y aprender** lengua de señas en **tres variantes regionales** (Ecuador, Chile y México) con apoyo de **IA**. Ideal para **instituciones y equipos de innovación** que buscan impacto social medible.

[![Streamlit](https://img.shields.io/badge/Powered%20by-Streamlit-red?style=flat-square&logo=streamlit)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Built%20with-Python-blue?style=flat-square&logo=python)](https://python.org)
[![AI](https://img.shields.io/badge/Enhanced%20by-AI-orange?style=flat-square&logo=openai)](https://openai.com)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Version](https://img.shields.io/badge/versión-2.0.0-informational)

---

## 🎯 Propuesta de Valor (TL;DR)
- **Una sola plataforma** para **consultar** y **comparar** señas latinoamericanas con **búsqueda inteligente** (texto y voz).
- **Aprendizaje guiado** con panel de métricas, historial y análisis comparativo por país.
- **Tecnologías de IA** (Whisper, NLP, fuzzy matching) para **hacer accesible** la información a estudiantes, docentes y público general.

> **Resultados hoy**: **223 señas** documentadas (EC **203**, CL **10**, MX **10**) y **búsqueda por voz** en español con múltiples acentos.

---

## 💡 ¿Por qué Signify?
- **Reduce barreras** de comunicación entre personas oyentes y comunidades Sordas.
- **Estandariza el aprendizaje** al comparar variantes regionales en una vista.
- **Escalable**: arquitectura modular lista para API, nuevos países y móviles.

**Para quién:** escuelas y universidades, instituciones públicas, ONGs, equipos de innovación, medios y empresas con foco en accesibilidad.

---

## ✨ Diferenciadores Clave
- **Multipaís real**: EC, CL y MX en paralelo con **análisis comparativo**.
- **Búsqueda inteligente**: exacta, tolerante a errores (fuzzy) y **por voz** (Whisper).
- **Panel de control** con métricas de uso en tiempo real e historial de consultas.
- **Síntesis de voz** (gTTS) para **instrucciones y lectura accesible**.
- **Rendimiento** optimizado (caché, carga lazy y procesamiento eficiente).

---

## 🧪 Explicación demo de funcionalidades clave
1. **Búsqueda por voz**: decir "hola" → Whisper transcribe → aparece la seña.
2. **Tolerancia a errores**: buscar "ola" → mostrar sugerencia "hola" (fuzzy matching).
3. **Análisis Comparativo**: seleccionar una palabra → abrir vista paralela EC/CL/MX con análisis estadístico descriptivo completo:
   - **Tabla resumen** con datos principales (mediana, percentiles, rango intercuartílico)
   - **Tres gráficos ilustrativos** de distribución y complejidad
   - **Conteo detallado** de señas comunes por idioma
   - **Comparación exhaustiva** de niveles de complejidad entre países
   - **Clasificación sistemática** usando métodos no paramétricos
4. **Síntesis de voz**: activar lectura de instrucciones en español regional.
5. **Métricas**: visitar el panel para evidenciar historial y velocidad de respuesta.

> Consejo: mantén la demo en **un solo flujo** (voz → resultado → análisis comparativo → métricas) para conservar la atención.

---

## 🌍 Cobertura actual
- **Lengua de Señas Ecuatoriana (LSE-EC)**: **203** señas documentadas
- **Lengua de Señas Chilena (LSCh)**: **10** señas documentadas
- **Lengua de Señas Mexicana (LSM)**: **10** señas documentadas
- **Comparación** visual y analítica entre variantes regionales

> Formato de datos: CSV en UTF-8 con campos **Palabra**, **Descripción**, **Categoría**.

---

## 🔎 Funcionalidades
- **Búsqueda Exacta** — coincidencia 1:1 por palabra.
- **Búsqueda Inteligente (fuzzy)** — tolera errores tipográficos (Levenshtein/FuzzyWuzzy).
- **Búsqueda por Voz** — Whisper AI para español con múltiples acentos.
- **Análisis Comparativo** — análisis estadístico descriptivo con visualización paralela entre países (Ecuador, Chile, México):
  - Tabla resumen con medidas de tendencia central y dispersión
  - Gráficos ilustrativos de distribución y complejidad de instrucciones
  - Conteo sistemático de señas comunes por idioma
  - Comparación exhaustiva de niveles de complejidad usando métodos no paramétricos
  - Clasificación sistemática basada en percentiles y rangos intercuartílicos
- **Exploración Aleatoria** — descubre nuevas señas.
- **Panel de Estadísticas** — métricas de uso, historial, tiempos y comparativos.
- **Síntesis de Voz** — gTTS para leer instrucciones.

---

## 📋 Prerrequisitos del Sistema

### **Antes de clonar, asegúrate de tener:**
- **Git** instalado y configurado:
  ```bash
  git --version  # Verificar instalación
  git config --global user.name "Tu Nombre"
  git config --global user.email "tu@email.com"
  ```
- **Python 3.10.X** instalado:
  ```bash
  python --version  # Debe mostrar Python 3.10.X
  ```
- **pip** actualizado:
  ```bash
  python -m pip --version
  ```

### **Configuración de SSH (Recomendado)**
```bash
# Generar clave SSH si no tienes una
ssh-keygen -t ed25519 -C "tu@email.com"

# Agregar clave al agente SSH
ssh-add ~/.ssh/id_ed25519

# Copiar clave pública para GitHub
cat ~/.ssh/id_ed25519.pub
```

---

## ⚙️ Instalación Express 
```bash
# 1) Clona y entra al proyecto
git clone https://github.com/tu-usuario/signify-lengua-senas.git
cd signify-lengua-senas

# 2) Crea y activa entorno virtual (Python 3.10)
python -m venv .venv_310

# Activar entorno virtual:
# Windows (PowerShell)
.venv_310\Scripts\Activate.ps1
# Windows (CMD)
.venv_310\Scripts\activate.bat
# macOS/Linux
source .venv_310/bin/activate

# Verificar activación (debe mostrar (.venv_310) al inicio del prompt)
python --version
which python  # macOS/Linux
where python   # Windows

# 3) Instala dependencias
python -m pip install --upgrade pip
pip install -r requirements.txt

# 4) Ejecuta
streamlit run app.py
# App disponible en: http://localhost:8501
```

### 🚨 **Solución de Problemas Comunes**

#### **Error de permisos en Windows:**
```powershell
# Habilitar ejecución de scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### **Error "python no reconocido":**
```bash
# Usar py en lugar de python (Windows)
py -m venv .venv_310
py -m pip install --upgrade pip
```

#### **Error de módulo venv:**
```bash
# Instalar venv si no está disponible
sudo apt-get install python3-venv  # Ubuntu/Debian
brew install python3               # macOS
```

### Instalación mínima (dependencias esenciales)
```bash
pip install streamlit plotly pandas numpy python-dateutil gtts pygame sounddevice openai-whisper fuzzywuzzy python-Levenshtein
```

### Opciones de ejecución
```bash
# Puerto específico
streamlit run app.py --server.port 8502
# Headless / CORS
streamlit run app.py --server.headless true --server.enableCORS false
# Logs detallados
streamlit run app.py --logger.level=debug
```

---

## 🧭 Guía de uso rápida
**Inicio** → Header profesional, selector de variante (EC/CL/MX), área de búsqueda y resultados.

**Búsqueda Exacta**
```
Entrada: "hola" → Resultado: seña "hola"
```

**Búsqueda Inteligente (fuzzy)**
```
Entrada: "ola" → Sugerencia: "hola" (p.ej., 85% de similitud)
```

**Búsqueda por Voz**
```
Flujo: Hablar → Whisper → Transcripción → Búsqueda
Idiomas: Español con múltiples acentos
```

**Comparación entre variantes**
- Vista paralela EC/CL/MX
- Métricas de similitud y diferencias

**Análisis Comparativo Detallado**
```
Flujo: Seleccionar palabra → Activar análisis → Visualización estadística
Componentes:
├── Tabla resumen (mediana, percentiles Q1/Q3, rango intercuartílico)
├── Gráfico de distribución de complejidad por país
├── Gráfico comparativo de longitud de instrucciones
├── Histograma de frecuencias por categoría
└── Clasificación sistemática (métodos no paramétricos)

Métricas incluidas:
• Complejidad promedio por variante
• Análisis de dispersión estadística
• Conteo de señas comunes/únicas
• Comparación de niveles de dificultad
```

**Síntesis de voz**
- Activación vía checkbox (panel lateral)
- Lectura automática de instrucciones

---

## 📊 Panel y Métricas
- **Total de señas por variante**
- **Búsquedas por sesión** e **historial reciente**
- **Tiempos de respuesta** (búsqueda/voz/análisis)
- **Análisis estadístico** por país y categoría (percentiles, medianas, dispersión)

---

## 🗃️ Datos y archivos
- `señas_ecuatorianas.csv` — EC (**203**)
- `señas_chilenas.csv` — CL (**10**)
- `señas_mexicanas.csv` — MX (**10**)

**Ejemplo**
```csv
Palabra,Descripción,Categoría
"Hola","La mano se levanta a la altura del hombro y se mueve de lado a lado","Saludos"
"Gracias","Las manos se juntan frente al pecho y se inclinan hacia adelante","Cortesía"
"Buenos Días","Se coloca una letra b sobre el corazón y se mueve al frente","Saludos"
```

> Recomendación: mantén los CSV en **UTF-8** para evitar errores de codificación.

---

## � Implementación del Modelo de IA (Webcam)
El sistema incorpora un modelo de reconocimiento de señas en tiempo real basado en **MediaPipe** y **K-Nearest Neighbors (KNN)**. El flujo de trabajo se encuentra en la carpeta `webcam_dataset/` y consta de tres etapas:

### 1. Recolección de Datos (`collect_data.py`)
- **Propósito**: Capturar muestras de señas usando la cámara web.
- **Funcionamiento**: 
  - Utiliza **MediaPipe Hands** para detectar 21 puntos clave (landmarks) por mano.
  - Extrae las coordenadas (x, y, z) generando un vector de características de **126 dimensiones** (2 manos * 21 puntos * 3 coordenadas).
  - Las muestras se guardan como archivos `.npy` (NumPy) en la carpeta `dataset_senas/`.
  - Permite definir el nombre de la seña y captura frames automáticamente cada 200ms.

### 2. Entrenamiento del Modelo (`train.py`)
- **Propósito**: Generar el modelo de clasificación.
- **Algoritmo**: **K-Nearest Neighbors (KNN)** con `n_neighbors=3`.
- **Proceso**:
  - Carga todos los archivos `.npy` del dataset recolectado.
  - Entrena el clasificador con los vectores de características y sus etiquetas correspondientes.
  - Exporta el modelo entrenado como `modelo_senas.pkl`.

### 3. Integración en la Interfaz (`webcam_integration.py` / `app.py`)
- **Carga del Modelo**: La aplicación carga `modelo_senas.pkl` al iniciar la pestaña de webcam.
- **Predicción en Tiempo Real**:
  - Captura video frame a frame.
  - Procesa la imagen con MediaPipe para obtener los landmarks.
  - Convierte los landmarks al vector de 126 dimensiones.
  - Consulta al modelo KNN para obtener la predicción.
  - Aplica un **suavizado temporal** (historial de 7 frames) para estabilizar el resultado y evitar parpadeos.
  - Muestra la traducción superpuesta en la interfaz de Streamlit.

---

## � Arquitectura (alto nivel)
- **Frontend/UI**: Streamlit + CSS personalizado + Plotly
- **Core**: motor de búsqueda (exacta/fuzzy), procesador de señas, comparador
- **IA**: Whisper (voz → texto), NLP, fuzzy matching (Levenshtein)
- **Audio**: gTTS (síntesis), Pygame/SoundDevice/PyAudio
- **Datos**: Pandas/NumPy; estructura modular por país
- **Rendimiento**: caché, carga lazy, threading seguro

### Estructura de proyecto
```
Lengua_Senas/
├── .gitignore                  # Configuración de Git
├── README.md                   # Documentación del proyecto
├── __init__.py                 # Inicialización del paquete
├── app.py                      # Aplicación principal Streamlit
├── requirements.txt            # Dependencias del proyecto
├── run.bat                     # Script de ejecución rápida
├── setup.py                    # Configuración de instalación
├── señas_ecuatorianas.csv     # Base de datos ecuatoriana
├── señas_chilenas.csv         # Base de datos chilena
├── señas_mexicanas.csv        # Base de datos mexicana
├── webcam_integration.py       # Lógica de integración webcam
├── analysis/                   # Módulos de análisis
│   ├── __init__.py            # Inicialización del módulo
│   └── comparative_analysis.py # Análisis comparativo
├── audio/                      # Procesamiento de audio
│   └── speech_engine.py       # Motor de síntesis y reconocimiento de voz
├── core/                       # Lógica central
│   └── sign_processor.py      # Procesador de señas y búsquedas
├── database/                   # Gestión de datos
│   └── signs_database.py      # Base de datos de señas
├── utils/                      # Utilidades del sistema
│   ├── __init__.py            # Inicialización del módulo
│   ├── config_utils.py        # Configuración de la aplicación
│   ├── file_utils.py          # Utilidades de archivos
│   └── validation_utils.py    # Validaciones del sistema
└── webcam_dataset/             # Módulo de reconocimiento visual
    ├── collect_data.py        # Script de recolección de datos
    ├── dataset_senas/         # Dataset de muestras (.npy)
    ├── modelo_senas.pkl       # Modelo entrenado (KNN)
    ├── predict.py             # Script de predicción independiente
    └── train.py               # Script de entrenamiento del modelo
```

---

## 📈 Rendimiento (objetivos y mediciones actuales)
- **Carga inicial**: < 3 s
- **Búsqueda**: < 1 s (200+ entradas)
- **Voz → Texto (Whisper)**: 2–5 s
- **Síntesis de voz**: 1–3 s
- **Análisis comparativo**: < 2 s

> Estas métricas dependen de hardware y conexión. Se miden en entorno local.

---

## 🧩 Solución de problemas (FAQ)
**Dependencias**
```bash
ModuleNotFoundError: No module named 'streamlit'
```
**Solución**
```bash
# Activar entorno virtual y reinstalar
.venv_310\Scripts\activate  # Windows
source .venv_310/bin/activate # macOS/Linux
pip install -r requirements.txt
```

**Audio/Micrófono**
```bash
Error: No se pudo acceder al micrófono
```
**Soluciones**
1) Revisar permisos del SO  2) Verificar conexión  3) Reiniciar app  4) Actualizar drivers

**Puerto ocupado**
```bash
Port 8501 is already in use
```
**Solución**
```bash
streamlit run app.py --server.port 8502
```

**Codificación CSV**
```bash
UnicodeDecodeError: 'utf-8' codec can't decode
```
**Soluciones**
1) Asegurar UTF-8  2) Usar editor compatible  3) Convertir con `iconv`

**Validación del sistema**
```bash
python -c "from utils.validation_utils import run_comprehensive_validation; run_comprehensive_validation()"
python -c "from utils.file_utils import validate_project_structure; validate_project_structure()"
python -c "from audio.voice_recognition import test_microphone; test_microphone()"
```

---

## 🧭 Roadmap
**v2.1 (próximo)**
- [ ] 500+ señas por idioma
- [ ] Reconocimiento visual (cámara web)
- [ ] Modo offline
- [ ] Gamificación (logros y progreso)
- [ ] Comunidad (foro y feedback)

**v2.2 (técnico)**
- [ ] API REST
- [ ] BD externa (PostgreSQL/MongoDB)
- [ ] Caché Redis
- [ ] Microservicios
- [ ] Docker

**v2.3 (UX/UI)**
- [ ] Modo oscuro
- [ ] Personalización por usuario
- [ ] Accesibilidad **WCAG 2.1 AA** (en progreso)
- [ ] PWA (instalable)
- [ ] UI multiidioma (ES/EN/PT)

**v3.0 (expansión)**
- [ ] Nuevos países: AR, CO, PE, VE
- [ ] Lenguas indígenas: Quechua, Guaraní, Mapuche
- [ ] Certificación con instituciones
- [ ] Apps móviles nativas
- [ ] Realidad aumentada para gestos 3D

---

## 🤝 Contribuir
¡Las contribuciones son bienvenidas! Abre un **issue** o envía un **pull request**. Recomendado: pruebas unitarias, validación de datos y convenciones de estilo.

### 💬 Únete a la Comunidad
Participa en nuestro grupo de WhatsApp para discusiones, soporte y colaboración: [**Signify Community**](https://chat.whatsapp.com/KSRZ7K3L3KC4XFHRXq3Oez?mode=ems_copy_t)

---

## 📄 Licencia
Proyecto bajo **Licencia MIT**. Consulta `LICENSE` para más detalle.

```
MIT License

Copyright (c) 2024 Signify Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 👥 Equipo y Contacto
- **Proyecto**: Signify v2.0.0  
- **Repositorio**: *GitHub – Signify*  
- **Documentación**: *Docs Online*  
- **Demo en vivo**: *signify-demo.streamlit.app*

> **Frase guía**: *La tecnología al servicio de la inclusión social.*

<p align="center">
  <strong>🤟 Signify — Conectando mundos a través de la Lengua de Señas</strong><br/>
  <em>Desarrollado con ❤️ para promover la inclusión</em>
</p>