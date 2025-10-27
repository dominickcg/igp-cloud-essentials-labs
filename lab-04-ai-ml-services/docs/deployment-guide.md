# 🚀 Guía de Despliegue - Laboratorio AWS AI/ML

## Para Participantes: Cómo Acceder al Laboratorio

> **📋 Prerrequisito**: Usuario IAM en una cuenta de AWS con permisos para servicios de AI/ML y SageMaker.

### Amazon SageMaker (Acceso Inmediato)

#### Paso 1: Crear Notebook Instance

1. Ir a https://console.aws.amazon.com/sagemaker/
2. Hacer login con tu usuario IAM
3. En el menú izquierdo, seleccionar: **"Notebooks"**
4. Hacer clic en **"Crear instancia de cuaderno"**
5. Configurar:
   - **Nombre de instancia de cuaderno**: `lab-ai-ml-tunombre`
   - **Tipo de instancia de cuaderno**: `ml.t3.medium`
   - **Identificador de plataforma**: `Amazon Linux 2023, Jupyter Lab 4`
   - **Rol de IAM**: Usar rol existente o crear uno con permisos básicos
6. Hacer clic en **"Crear instancia de cuaderno"**
7. **Esperar 3-5 minutos** hasta que el estado sea **"InService"**

#### Paso 2: Acceder a Jupyter

1. Una vez **"InService"**, hacer clic en **"Abrir Jupyter"**
2. Se abrirá Jupyter Notebook en una nueva pestaña

#### Paso 3: Obtener los Notebooks

En Jupyter, hacer clic en **"File"** → **"New"** → **"Terminal"** y ejecutar:

```bash
cd /home/ec2-user/SageMaker
git clone https://github.com/dominickcg/igp-cloud-essentials-labs.git
cd igp-cloud-essentials-labs/lab-04-ai-ml-services
pip install -r requirements.txt
```

#### Paso 4: Comenzar el Laboratorio

1. Refrescar Jupyter (F5 o botón Refresh)
2. En Jupyter, navegar a la carpeta `igp-cloud-essentials-labs/lab-04-ai-ml-services/notebooks/`
3. Abrir `01-rekognition.ipynb` para comenzar
4. **No necesitas configurar credenciales** - SageMaker usa tu usuario IAM automáticamente
5. Seguir las instrucciones del navegador
6. Completar módulos 1-5 en orden

---

## ⏱️ Cronograma Sugerido

### Sesión de 90 Minutos

```
00:00-05:00  Setup: Crear notebook instances y configuración
05:00-20:00  Módulo 1: Rekognition - Análisis de imágenes geológicas
20:00-35:00  Módulo 2: Comprehend - Procesamiento de texto científico
35:00-50:00  Módulo 3: Textract - OCR de tablas y formularios
50:00-65:00  Módulo 4: Polly - Síntesis de voz para alertas
65:00-90:00  Módulo 5: Bedrock - IA generativa (texto y código)
```

---

## 🎯 Objetivos de Aprendizaje

Al completar este laboratorio en Amazon SageMaker, los participantes podrán:

✅ **Usar SageMaker** como entorno de desarrollo para AI/ML científico  
✅ **Analizar imágenes satelitales** usando Amazon Rekognition para detectar formaciones geológicas  
✅ **Procesar documentos científicos** con Amazon Comprehend para extraer entidades y sentimientos  
✅ **Digitalizar formularios de campo** usando Amazon Textract para convertir tablas a datos estructurados  
✅ **Generar alertas de audio** con Amazon Polly para sistemas de emergencia  
✅ **Crear contenido científico y código** usando Amazon Bedrock para IA generativa aplicada a geofísica

---

## 🆘 Soporte Durante el Laboratorio

### Problemas Comunes

- **"No puedo crear notebook instance"**: Verificar permisos de SageMaker
- **"Access Denied"**: Verificar permisos de AI/ML en tu usuario IAM
- **"Notebook no inicia"**: Esperar hasta que esté "InService"
- **"Git clone falla"**: Usar terminal de Jupyter, no el notebook
- **"Los servicios fallan"**: Verificar región (usar us-east-1)

---

### Limpieza

1. **Detener notebook instance**: SageMaker Console → Stop
2. **Eliminar notebook instance**: Para evitar costos futuros
3. Verificar que no queden recursos activos

---