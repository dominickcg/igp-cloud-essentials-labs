# ⚡ INICIO RÁPIDO - Laboratorio AWS AI/ML

## 🎯 ¿Qué vas a hacer?
Aprender 6 servicios de IA de AWS en 90 minutos usando casos científicos reales.

## 📋 ¿Qué necesitas?
- ✅ **Usuario IAM** en una cuenta de AWS (ya lo tienes)
- ✅ Navegador web

---

## 🚀 Empezar AHORA en SageMaker (3 pasos)

### 1️⃣ Acceder a Amazon SageMaker
- Ir a: https://console.aws.amazon.com/sagemaker/
- Hacer login con tu usuario IAM
- Ir a **"Notebook instances"** → **"Create notebook instance"**
- Nombre: `laboratorio-ai-ml`
- Instance type: `ml.t3.medium` (gratuito)
- **Create notebook instance**

### 2️⃣ Obtener los Notebooks
Una vez que el notebook esté **"InService"**:
- Hacer clic en **"Open Jupyter"**
- En Jupyter, abrir terminal y ejecutar:
```bash
git clone https://github.com/dominickcg/igp-cloud-essentials-labs.git
cd igp-cloud-essentials-labs/lab-05-aws-ai-ml-services
pip install -r requirements.txt
```

### 3️⃣ Comenzar el Laboratorio
- Abrir `notebooks/00-laboratorio-maestro.ipynb`
- **No necesitas configurar credenciales** (SageMaker usa tu usuario IAM automáticamente)
- Seguir las instrucciones del navegador
- Completar módulos 1-6 en orden

---

## 📚 Los 6 Módulos (15 min cada uno)

| # | Servicio | ¿Qué hace? | Notebook |
|---|----------|------------|----------|
| 1 | **Rekognition** | Analiza imágenes científicas | `01-rekognition.ipynb` |
| 2 | **Comprehend** | Extrae información de textos | `02-comprehend.ipynb` |
| 3 | **Textract** | Digitaliza documentos escaneados | `03-textract.ipynb` |
| 4 | **Polly** | Convierte texto a voz | `04-polly.ipynb` |
| 5 | **Bedrock** | Genera contenido con IA | `05-bedrock.ipynb` |
| 6 | **Q Developer** | Asiste programación con IA | `06-q-developer.ipynb` |

---

## 🔑 Credenciales AWS

**✅ ¡No necesitas configurar nada!** 

SageMaker usa automáticamente los permisos de tu usuario IAM. Los notebooks se conectan directamente a los servicios AWS.

---

## 🆘 ¿Problemas?

| Problema | Solución |
|----------|----------|
| "No puedo crear notebook instance" | Verificar permisos de SageMaker en tu usuario IAM |
| "Access Denied en servicios" | Verificar permisos de AI/ML en tu usuario IAM |
| "Notebook no inicia" | Esperar 2-3 minutos, debe cambiar a "InService" |
| "Git clone falla" | Usar la terminal de Jupyter, no el notebook |

**📖 Guía completa**: Ver `docs/deployment-guide.md`

---

## ✅ Al Terminar

1. **Validar progreso**: Ejecutar `validation-checkpoint.ipynb`
2. **Generar certificado**: Usar el botón en el notebook de validación
3. **Limpiar recursos**: **IMPORTANTE** - Detener o eliminar notebook instance
4. **¡Celebrar!** Has aprendido 6 servicios de IA de AWS

---

## 📞 Contacto

- **Durante el taller**: Preguntar al instructor
- **Después del taller**: soporte@laboratorio-aws.com
- **Issues técnicos**: GitHub Issues del repositorio

---

**⏱️ Tiempo total: 90 minutos | 🎓 Nivel: Principiante | 🚀 ¡Empezar ya!**