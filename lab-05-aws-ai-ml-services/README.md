# Laboratorio 05: Servicios de IA/ML en AWS

## 🎯 Objetivo

Aprender a usar servicios de IA/ML de AWS en 90 minutos a través de ejercicios prácticos con casos científicos.

## 🚀 Inicio Rápido para Participantes

> **📋 Prerrequisito**: Usuario IAM en una cuenta de AWS con permisos de SageMaker y AI/ML

### ⚡ Empezar AHORA en Amazon SageMaker (Ver `INICIO-RAPIDO.md`)

1. **Ir a SageMaker Console**: https://console.aws.amazon.com/sagemaker/
2. **Crear notebook instance**: `ml.t3.medium` (gratuito)
3. **Clonar repositorio**: `git clone https://github.com/dominickcg/igp-cloud-essentials-labs.git` en terminal de Jupyter
4. **Abrir**: `notebooks/00-laboratorio-maestro.ipynb`

**✅ Sin configuración de credenciales** - SageMaker usa tu usuario IAM automáticamente

## 📖 Documentación Completa

### 📋 Guías para Participantes
- **[🚀 docs/deployment-guide.md](docs/deployment-guide.md)** - Guía completa de despliegue
- **[🆘 docs/troubleshooting.md](docs/troubleshooting.md)** - Solución de problemas

### 📚 Notebooks del Laboratorio
- **[🔍 notebooks/01-rekognition.ipynb](notebooks/01-rekognition.ipynb)** - Análisis de imágenes
- **[📝 notebooks/02-comprehend.ipynb](notebooks/02-comprehend.ipynb)** - Análisis de texto
- **[📄 notebooks/03-textract.ipynb](notebooks/03-textract.ipynb)** - OCR documentos
- **[🔊 notebooks/04-polly.ipynb](notebooks/04-polly.ipynb)** - Síntesis de voz
- **[🤖 notebooks/05-bedrock.ipynb](notebooks/05-bedrock.ipynb)** - IA Generativa
- **[💻 notebooks/06-q-developer.ipynb](notebooks/06-q-developer.ipynb)** - Asistente de código


## 📚 Módulos del Laboratorio

| Módulo | Servicio AWS       | Tiempo | Notebook               |
| ------ | ------------------ | ------ | ---------------------- |
| 1      | Amazon Rekognition | 15 min | `01-rekognition.ipynb` |
| 2      | Amazon Comprehend  | 15 min | `02-comprehend.ipynb`  |
| 3      | Amazon Textract    | 10 min | `03-textract.ipynb`    |
| 4      | Amazon Polly       | 10 min | `04-polly.ipynb`       |
| 5      | Amazon Bedrock     | 15 min | `05-bedrock.ipynb`     |
| 6      | Amazon Q Developer | 5 min  | `06-q-developer.ipynb` |

**Total: 90 minutos**

## 📋 Requisitos Previos

### Para Participantes

- ✅ **Usuario IAM** en una cuenta de AWS con permisos de SageMaker y AI/ML
- ✅ **Acceso a AWS Console** funcionando
- ✅ Navegador web moderno

**💡 Ventaja**: Sin configuración de credenciales. SageMaker usa automáticamente los permisos de tu usuario IAM.

## 🔧 Configuración (Solo para Instructores)

```bash
# 1. Crear notebook instance en SageMaker Console
# 2. En Jupyter terminal:
git clone https://github.com/dominickcg/igp-cloud-essentials-labs.git
cd igp-cloud-essentials-labs/lab-05-aws-ai-ml-services

# 3. Probar notebooks
# Abrir notebooks/00-laboratorio-maestro.ipynb
```

## 📁 Estructura del Proyecto

```
lab-05-aws-ai-ml-services/
├── README.md                           # Esta guía
├── setup_simple.py                     # Setup opcional para instructores
├── requirements.txt                    # Dependencias mínimas
├── lab_config.json                     # Configuración generada (auto)
│
├── notebooks/                          # 📚 Notebooks principales (70 min)
│   ├── README.md                       # Guía de notebooks
│   ├── 01-rekognition.ipynb           # Análisis de imágenes (15 min)
│   ├── 02-comprehend.ipynb            # Análisis de texto (15 min)
│   ├── 03-textract.ipynb             # OCR documentos (10 min)
│   ├── 04-polly.ipynb                # Síntesis de voz (10 min)
│   ├── 05-bedrock.ipynb              # IA Generativa (15 min)
│   └── 06-q-developer.ipynb          # Asistencia código (5 min)
│
├── data/                              # 📊 Datos embebidos
│   ├── sample_data.py                 # URLs y textos de muestra
│   └── texts/                         # Textos científicos locales
│       ├── emergency-alerts/          # Alertas sísmicas
│       ├── scientific-descriptions/   # Descripciones técnicas
│       └── educational-content/       # Contenido educativo
│

│
├── scripts/                           # 🛠️ Scripts de utilidad
│   └── validate_credentials.py       # Validador de permisos IAM
│
└── docs/                             # 📖 Documentación
    ├── deployment-guide.md           # Guía completa de despliegue
    └── troubleshooting.md            # Solución de problemas
```

### 📋 Descripción de Archivos Clave

**Para Participantes:**
- **[⚡ INICIO-RAPIDO.md](INICIO-RAPIDO.md)** - Empezar inmediatamente
- **[notebooks/](notebooks/)** - Notebooks principales del laboratorio
- **[data/sample_data.py](data/sample_data.py)** - Datos embebidos (no requiere descarga)

## 🆘 Soporte y Recursos

- **[🆘 Troubleshooting](docs/troubleshooting.md)**: Soluciones a problemas comunes

### 🌐 Enlaces Externos
- **AWS Console SageMaker**: https://console.aws.amazon.com/sagemaker/
- **Repositorio GitHub**: https://github.com/dominickcg/igp-cloud-essentials-labs
- **Documentación AWS AI/ML**: https://docs.aws.amazon.com/machine-learning/

---

**Duración total**: 90 minutos | **Nivel**: AWS Cloud Practitioner | **Modalidad**: Hands-on