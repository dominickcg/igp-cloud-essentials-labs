# Laboratorio 04: Servicios de IA/ML en AWS

## 🎯 Objetivo

Aprender a usar servicios de IA/ML de AWS en 90 minutos a través de ejercicios prácticos con casos científicos.

## 📖 Documentación Completa

### 📋 Guías para Participantes

- **[🚀 docs/deployment-guide.md](docs/deployment-guide.md)** - Guía completa de despliegue

### 📚 Notebooks del Laboratorio

- **[🔍 notebooks/01-rekognition.ipynb](notebooks/01-rekognition.ipynb)** - Análisis de imágenes satelitales
- **[📝 notebooks/02-comprehend.ipynb](notebooks/02-comprehend.ipynb)** - Análisis de texto científico
- **[📄 notebooks/03-textract.ipynb](notebooks/03-textract.ipynb)** - OCR de documentos y formularios
- **[🔊 notebooks/04-polly.ipynb](notebooks/04-polly.ipynb)** - Síntesis de voz para alertas
- **[🤖 notebooks/05-bedrock.ipynb](notebooks/05-bedrock.ipynb)** - IA Generativa (texto y código)

## 📚 Módulos del Laboratorio

| Módulo | Servicio AWS       | Tiempo | Notebook               | Descripción                           |
| ------ | ------------------ | ------ | ---------------------- | ------------------------------------- |
| 1      | Amazon Rekognition | 15 min | `01-rekognition.ipynb` | Análisis de imágenes geológicas       |
| 2      | Amazon Comprehend  | 15 min | `02-comprehend.ipynb`  | Procesamiento de texto científico     |
| 3      | Amazon Textract    | 15 min | `03-textract.ipynb`    | OCR de tablas y formularios           |
| 4      | Amazon Polly       | 15 min | `04-polly.ipynb`       | Síntesis de voz para alertas          |
| 5      | Amazon Bedrock     | 30 min | `05-bedrock.ipynb`     | IA Generativa para contenido y código |

**Total: 90 minutos**

## 📋 Requisitos Previos

### Para Participantes

- ✅ **Usuario IAM** en una cuenta de AWS con permisos de SageMaker y AI/ML
- ✅ **Acceso a AWS Console** funcionando
- ✅ Navegador web moderno

**Ventaja**: Sin configuración de credenciales. SageMaker usa automáticamente los permisos del rol de IAM asignado a la instancia de notebook.

## 📁 Estructura del Proyecto

```
lab-04-ai-ml-services/
├── README.md                           # Esta guía
├── requirements.txt                    # Dependencias Python
├── .gitignore                          # Archivos ignorados por Git
│
├── notebooks/                          # 📚 Notebooks principales (90 min)
│   ├── README.md                       # Guía de notebooks
│   ├── 01-rekognition.ipynb           # Análisis de imágenes (15 min)
│   ├── 02-comprehend.ipynb            # Análisis de texto (15 min)
│   ├── 03-textract.ipynb             # OCR documentos (15 min)
│   ├── 04-polly.ipynb                # Síntesis de voz (15 min)
│   └── 05-bedrock.ipynb              # IA Generativa - texto y código (30 min)
│
├── scripts/                           # �️ Stcripts de utilidad
│   ├── validate_credentials.py       # Validador de permisos IAM
│   ├── validation_system.py          # Sistema de validación
│   └── setup/                         # Scripts de configuración
│
└── docs/                             # 📖 Documentación
    └── deployment-guide.md           # Guía completa de despliegue
```

### 🌐 Enlaces Externos

- **AWS Console SageMaker**: https://console.aws.amazon.com/sagemaker/
- **Documentación AWS AI/ML**: https://docs.aws.amazon.com/machine-learning/

---

**Duración total**: 90 minutos | **Nivel**: AWS Cloud Practitioner | **Modalidad**: Hands-on
