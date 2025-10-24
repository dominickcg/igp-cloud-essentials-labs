"""
Datos de muestra embebidos para el laboratorio AWS AI/ML
Datos simples que se pueden usar directamente en los notebooks
"""

# URLs de imágenes públicas para Rekognition
SAMPLE_IMAGES = {
    "geological": [
        "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",  # Montaña
        "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800",  # Rocas
        "https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?w=800"   # Tierra desde espacio
    ]
}

# Textos de muestra para Comprehend
SAMPLE_TEXTS = {
    "scientific_report": """
    El Instituto Geofísico del Perú reporta actividad sísmica significativa en la región sur. 
    Los análisis preliminares indican un evento de magnitud 6.2 con epicentro a 45 km de profundidad. 
    Las estaciones de monitoreo registraron ondas P y S características de sismos tectónicos. 
    Se recomienda mantener protocolos de seguridad en las zonas urbanas cercanas.
    """,
    
    "emergency_alert": """
    ALERTA SÍSMICA: Se ha detectado un sismo de magnitud 5.8 en la costa peruana. 
    Tiempo estimado de llegada a Lima: 2 minutos. Busque refugio inmediatamente. 
    Aléjese de ventanas y objetos que puedan caer. Mantenga la calma.
    """,
    
    "research_abstract": """
    This study analyzes volcanic activity patterns in the Andes mountain range using 
    satellite imagery and seismic data. Results show increased thermal anomalies 
    correlating with micro-seismic events. The findings suggest enhanced monitoring 
    protocols for early volcanic eruption detection.
    """
}

# Textos para síntesis de voz con Polly
POLLY_TEXTS = {
    "spanish_alert": "Atención: Se ha registrado actividad sísmica en la región. Mantenga la calma y siga los protocolos de seguridad establecidos.",
    
    "english_description": "The Andes mountain range is one of the most seismically active regions in the world, with frequent earthquakes and volcanic activity.",
    
    "educational_content": "La geología estudia la composición, estructura y procesos de la Tierra. Los terremotos ocurren cuando las placas tectónicas se mueven y liberan energía acumulada."
}

# Prompts para Bedrock
BEDROCK_PROMPTS = {
    "report_generation": """
    Genera un breve reporte científico sobre actividad sísmica basado en estos datos:
    - Magnitud: 6.2
    - Profundidad: 45 km
    - Ubicación: Costa sur del Perú
    - Fecha: Hoy
    
    El reporte debe ser técnico pero comprensible.
    """,
    
    "data_analysis": """
    Analiza estos datos sísmicos y proporciona conclusiones:
    - 15 sismos registrados en la última semana
    - Magnitudes entre 3.1 y 4.8
    - Profundidades variables: 10-60 km
    - Patrón de distribución: Concentrado en zona costera
    
    ¿Qué patrones observas y qué recomendaciones darías?
    """,
    
    "educational_explanation": """
    Explica de manera simple y educativa qué causa los terremotos en Perú, 
    considerando la ubicación geográfica y las placas tectónicas. 
    Debe ser comprensible para estudiantes de secundaria.
    """
}

# Código de ejemplo para Q Developer
Q_DEVELOPER_TASKS = {
    "data_analysis": "Crear una función en Python que analice datos sísmicos y calcule la magnitud promedio, desviación estándar y frecuencia de eventos por día",
    
    "visualization": "Generar un gráfico de barras que muestre la distribución de magnitudes sísmicas por rangos (3.0-3.9, 4.0-4.9, 5.0-5.9, etc.)",
    
    "alert_system": "Desarrollar una función que determine el nivel de alerta (Verde, Amarillo, Rojo) basado en la magnitud del sismo y la profundidad"
}

# Datos tabulares simples para Textract (simulados)
TEXTRACT_SAMPLE = {
    "table_data": [
        ["Fecha", "Magnitud", "Profundidad", "Ubicación"],
        ["2024-11-15", "6.2", "45 km", "Costa Sur"],
        ["2024-11-14", "4.1", "25 km", "Lima"],
        ["2024-11-13", "3.8", "15 km", "Arequipa"],
        ["2024-11-12", "5.0", "35 km", "Ica"]
    ]
}

def get_sample_image_url(category="geological", index=0):
    """Obtiene URL de imagen de muestra"""
    return SAMPLE_IMAGES.get(category, [])[index] if index < len(SAMPLE_IMAGES.get(category, [])) else None

def get_sample_text(category):
    """Obtiene texto de muestra por categoría"""
    return SAMPLE_TEXTS.get(category, "")

def get_polly_text(category):
    """Obtiene texto para Polly por categoría"""
    return POLLY_TEXTS.get(category, "")

def get_bedrock_prompt(category):
    """Obtiene prompt para Bedrock por categoría"""
    return BEDROCK_PROMPTS.get(category, "")

def get_q_developer_task(category):
    """Obtiene tarea para Q Developer por categoría"""
    return Q_DEVELOPER_TASKS.get(category, "")