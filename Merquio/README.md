# 🚀 Proyecto de Inteligencia Artificial: Segmentación y Análisis de Clientes de Cadena de Suministro

## 📌 Descripción del Proyecto
Este proyecto implementa un **sistema de análisis y segmentación de clientes** para una cadena de suministro utilizando técnicas de **Machine Learning** y **Análisis de Datos**. El objetivo principal es identificar patrones de comportamiento, detectar anomalías en las transacciones y agrupar a los clientes en segmentos estratégicos para optimizar la gestión del negocio.

## 🎯 Objetivos del Proyecto
- **Agrupar y analizar** datos de clientes para identificar tendencias.
- **Detectar anomalías** en las transacciones y comportamientos de clientes.
- **Segmentar clientes** utilizando algoritmos de clustering con datos mixtos (numéricos y categóricos).
- **Optimizar el uso de memoria** en el procesamiento de grandes volúmenes de datos.
- **Visualizar resultados** para facilitar la toma de decisiones.

## 📊 Dataset Utilizado
- **Nombre del archivo:** `DataCoSupplyChainDataset.csv`
- **Origen:** Google Drive
- **Columnas principales utilizadas:**
  - Información del cliente: `Customer Id`, `Customer Segment`, `Customer Country`, etc.
  - Transacciones: `Sales per customer`, `Benefit per order`, `Order Item Discount Rate`, etc.
  - Logística: `Delivery Status`, `Late_delivery_risk`, `Shipping Mode`, etc.
  - Productos: `Category Name`, `Product Name`, `Product Price`, etc.

## 🛠️ Tecnologías y Librerías Utilizadas
- **Python 3.x**
- **Pandas & NumPy** – Manipulación y optimización de datos
- **Scikit-learn** – Modelos de Machine Learning (Isolation Forest, Random Forest)
- **K-Prototypes** – Clustering con datos mixtos
- **Matplotlib & Seaborn** – Visualización de datos
- **Joblib** – Serialización de modelos
- **Google Drive API (gdown)** – Descarga del dataset

## 📈 Flujo del Proyecto

### 1. **Carga y Optimización de Datos**
   - Descarga automática del dataset desde Google Drive.
   - Selección de columnas relevantes para el análisis.
   - Eliminación de datos faltantes y columnas innecesarias.
   - **Optimización de memoria** reduciendo tipos de datos (int8, float32, category).

### 2. **Agrupación de Datos por Cliente**
   - Agregación de métricas clave por cliente:
     - `Benefit per order` (suma)
     - `Sales per customer` (suma)
     - `Order Item Discount Rate` (promedio)
     - `Order Item Quantity` (promedio)
     - Número de pedidos únicos

### 3. **Detección de Anomalías con Isolation Forest**
   - Identificación de clientes con comportamientos atípicos.
   - **Resultados:**
     - 19,196 clientes normales
     - 1,445 clientes anómalos (7.0%)
   - Separación entre clientes regulares (incluyendo VIP) y anómalos.

### 4. **Segmentación de Clientes con K-Prototypes**
   - **Algoritmo elegido:** K-Prototypes (manejo de datos numéricos y categóricos).
   - **Variables utilizadas:**
     - Numéricas: `Benefit per order`, `Sales per customer`, etc.
     - Categóricas: `Customer Segment`, `Order Region`, `Order City`, `Order Country`.
   - **Escalado** de variables numéricas con `StandardScaler`.
   - **3 segmentos identificados:**
     - **VIP (Alto Valor):** 9,951 clientes (50.9%)
     - **Regular (Valor Medio):** 5,367 clientes (27.5%)
     - **Ocasional (Bajo Valor):** 4,214 clientes (21.6%)

### 5. **Análisis de Segmentos**
   - Cálculo de estadísticas por segmento:
     - Beneficio promedio por orden
     - Ventas promedio por cliente
     - Tasa de descuento promedio
     - Cantidad promedio por pedido
     - Número promedio de pedidos

### 6. **Visualización y Exportación**
   - Generación de gráficos comparativos entre segmentos.
   - Exportación del dataset segmentado (`df_segmentado`) para uso futuro.

## 📊 Resultados Clave
1. **Segmentación Exitosa:** Los clientes fueron agrupados en 3 categorías claramente diferenciadas por su valor.
2. **Detección de Anomalías:** Identificación del 7% de clientes con comportamientos atípicos.
3. **Optimización de Memoria:** Reducción del 58.6% en el uso de memoria del dataset.
4. **Insights Accionables:**
   - Los clientes VIP generan en promedio **10 veces más beneficio** que los ocasionales.
   - Los clientes regulares y VIP realizan **más pedidos y con mayor frecuencia**.

## 🚀 Cómo Ejecutar el Proyecto
1. **Clonar o descargar** el notebook.
2. **Instalar dependencias:**
   ```bash
   pip install gdown kmodes scikit-learn pandas numpy matplotlib seaborn joblib