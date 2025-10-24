# 🚀 Guía de Despliegue - Laboratorio AWS AI/ML

## Para Participantes: Cómo Acceder al Laboratorio

> **📋 Prerrequisito**: Usuario IAM en una cuenta de AWS con permisos para servicios de AI/ML y SageMaker.

### Amazon SageMaker (Acceso Inmediato)

#### Paso 1: Crear Notebook Instance

1. Ir a https://console.aws.amazon.com/sagemaker/
2. Hacer login con tu usuario IAM
3. En el menú izquierdo: **"Notebook instances"**
4. Hacer clic en **"Create notebook instance"**
5. Configurar:
   - **Notebook instance name**: `laboratorio-ai-ml`
   - **Notebook instance type**: `ml.t3.medium` (incluido en free tier)
   - **IAM role**: Usar rol existente o crear uno con permisos básicos
6. Hacer clic en **"Create notebook instance"**
7. **Esperar 2-3 minutos** hasta que el estado sea **"InService"**

#### Paso 2: Acceder a Jupyter

1. Una vez **"InService"**, hacer clic en **"Open Jupyter"**
2. Se abrirá Jupyter Notebook en una nueva pestaña

#### Paso 3: Obtener los Notebooks

En Jupyter, hacer clic en **"New"** → **"Terminal"** y ejecutar:

```bash
git clone https://github.com/dominickcg/igp-cloud-essentials-labs.git
cd igp-cloud-essentials-labs/lab-05-aws-ai-ml-services
pip install -r requirements.txt
```

#### Paso 4: Comenzar el Laboratorio

1. En Jupyter, navegar a la carpeta `igp-cloud-essentials-labs/lab-05-aws-ai-ml-services/notebooks/`
2. Abrir `00-laboratorio-maestro.ipynb`
3. **No necesitas configurar credenciales** - SageMaker usa tu usuario IAM automáticamente
4. Seguir las instrucciones del navegador
5. Completar módulos 1-6 en orden

---

## ⏱️ Cronograma Sugerido

### Sesión de 90 Minutos

```
00:00-10:00  Setup: Crear notebook instances
10:00-25:00  Módulo 1: Rekognition
25:00-40:00  Módulo 2: Comprehend
40:00-55:00  Módulo 3: Textract
55:00-70:00  Módulo 4: Polly
70:00-85:00  Módulo 5: Bedrock
85:00-90:00  Módulo 6: Q Developer + Validación
```

---

## 🎯 Objetivos de Aprendizaje

Al completar este laboratorio en Amazon SageMaker, los participantes podrán:

✅ **Usar SageMaker** como entorno de desarrollo para AI/ML  
✅ **Analizar imágenes** usando Amazon Rekognition para detectar objetos y características  
✅ **Procesar texto** con Amazon Comprehend para extraer entidades y sentimientos  
✅ **Extraer texto de documentos** usando Amazon Textract para digitalizar contenido  
✅ **Generar audio** con Amazon Polly para crear contenido hablado  
✅ **Crear contenido** usando Amazon Bedrock para IA generativa  
✅ **Asistir programación** con Amazon Q Developer para generar código

---

## 🆘 Soporte Durante el Laboratorio

### Problemas Comunes

- **"No puedo crear notebook instance"**: Verificar permisos de SageMaker
- **"Access Denied"**: Verificar permisos de AI/ML en tu usuario IAM
- **"Notebook no inicia"**: Esperar hasta que esté "InService"
- **"Git clone falla"**: Usar terminal de Jupyter, no el notebook
- **"Los servicios fallan"**: Verificar región (usar us-east-1)

---

### Limpieza (IMPORTANTE)

1. **Detener notebook instance**: SageMaker Console → Stop
2. **Eliminar notebook instance**: Para evitar costos futuros
3. Verificar que no queden recursos activos

---