# Troubleshooting - Laboratorio AWS AI/ML en Amazon SageMaker

## 🔧 Problemas Comunes y Soluciones

### 1. Problemas de SageMaker Notebook Instance

#### ❌ Error: "No puedo crear notebook instance"
**Causa**: Permisos insuficientes de SageMaker

**Solución**:
1. Verificar que tu usuario IAM tiene permisos de SageMaker
2. Contactar al administrador para agregar política:
```json
{
  "Effect": "Allow",
  "Action": [
    "sagemaker:CreateNotebookInstance",
    "sagemaker:DescribeNotebookInstance",
    "sagemaker:StartNotebookInstance",
    "sagemaker:StopNotebookInstance"
  ],
  "Resource": "*"
}
```

#### ❌ Error: "Notebook instance no inicia"
**Causa**: Proceso de inicialización normal

**Solución**:
1. **Esperar 2-3 minutos** - es normal
2. Verificar que el estado cambie a **"InService"**
3. Si toma más de 5 minutos, contactar al instructor

#### ❌ Error: "No puedo abrir Jupyter"
**Causa**: Notebook instance no está listo

**Solución**:
1. Verificar que el estado sea **"InService"**
2. Hacer clic en **"Open Jupyter"** (no "Open JupyterLab")
3. Permitir pop-ups en el navegador

---

### 2. Problemas de Credenciales y Permisos

#### ❌ Error: "AccessDenied" en servicios AI/ML
**Causa**: Tu usuario IAM no tiene permisos para servicios específicos

**Solución**:
1. **Contactar al administrador** de tu cuenta AWS
2. **Solicitar permisos** para estos servicios:
   - Amazon Rekognition: `rekognition:*`
   - Amazon Comprehend: `comprehend:*`
   - Amazon Textract: `textract:*`
   - Amazon Polly: `polly:*`
   - Amazon Bedrock: `bedrock:*`

#### ✅ **Ventaja de SageMaker**: No necesitas configurar credenciales
SageMaker usa automáticamente los permisos de tu usuario IAM. No hay que configurar Access Keys.

---

### 3. Problemas de Notebooks y Git

#### ❌ Error: "git clone falla"
**Causa**: Ejecutando en notebook en lugar de terminal

**Solución**:
1. En Jupyter, hacer clic en **"New"** → **"Terminal"**
2. En la terminal ejecutar:
```bash
git clone https://github.com/dominickcg/igp-cloud-essentials-labs.git
cd igp-cloud-essentials-labs/lab-05-aws-ai-ml-services
```

#### ❌ Error: "pip install falla"
**Causa**: Problemas de conectividad o dependencias

**Solución**:
```bash
# En terminal de Jupyter:
pip install --upgrade pip
pip install boto3 ipywidgets matplotlib pandas
```

#### ❌ Error: "No encuentro los notebooks"
**Causa**: No navegaste a la carpeta correcta

**Solución**:
1. En Jupyter, hacer clic en la carpeta `igp-cloud-essentials-labs`, luego `lab-05-aws-ai-ml-services`
2. Luego hacer clic en la carpeta `notebooks`
3. Abrir `00-laboratorio-maestro.ipynb`

---

### 4. Problemas de Servicios AWS

#### ❌ Error: "Service not available in region"
**Causa**: Servicio no disponible en tu región

**Solución**:
1. Cambiar región a **us-east-1** (Virginia del Norte)
2. En AWS Console, seleccionar región en la esquina superior derecha

#### ❌ Error: "Rate limit exceeded"
**Causa**: Demasiadas solicitudes muy rápido

**Solución**:
1. Esperar 1-2 minutos
2. Ejecutar las celdas más lentamente
3. No ejecutar todas las celdas al mismo tiempo

---

### 5. Problemas de Costos

#### ⚠️ "¿Cuánto cuesta el laboratorio?"
**Respuesta**: 
- **Notebook instance ml.t3.medium**: ~$0.05/hora (incluido en free tier)
- **Servicios AI/ML**: Muy bajo costo para el laboratorio (~$1-2 total)
- **IMPORTANTE**: Detener/eliminar notebook instance al terminar

#### 🔧 **Limpieza obligatoria**:
1. SageMaker Console → Notebook instances
2. Seleccionar tu instance → **"Stop"**
3. Después → **"Delete"** para evitar costos futuros

---

## 🆘 Contacto de Emergencia

### Durante el Laboratorio
- **Instructor**: Levantar la mano o preguntar en chat
- **Compañeros**: Trabajar en equipo es bienvenido

### Después del Laboratorio
- **Issues técnicos**: GitHub Issues del repositorio
- **Soporte**: soporte@laboratorio-aws.com

---

## 📋 Checklist de Troubleshooting

Antes de pedir ayuda, verificar:

- [ ] ¿Tu notebook instance está "InService"?
- [ ] ¿Puedes abrir Jupyter correctamente?
- [ ] ¿Clonaste el repositorio en terminal (no en notebook)?
- [ ] ¿Estás en la región us-east-1?
- [ ] ¿Tu usuario IAM tiene permisos de SageMaker y AI/ML?

---

**💡 Recuerda**: Amazon SageMaker simplifica todo. No necesitas configurar credenciales, solo usar tus permisos IAM existentes.