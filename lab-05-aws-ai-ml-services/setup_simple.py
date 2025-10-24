#!/usr/bin/env python3
"""
Setup simple para el Laboratorio AWS AI/ML
Solo crea un bucket S3 básico para el instructor
"""

import boto3
import json
from datetime import datetime

def setup_lab():
    """Setup mínimo del laboratorio"""
    print("🚀 Setup simple del Laboratorio AWS AI/ML")
    print("=" * 50)
    
    try:
        # Crear cliente S3
        s3 = boto3.client('s3')
        
        # Nombre del bucket con timestamp
        bucket_name = f"aws-ai-ml-lab-{datetime.now().strftime('%Y%m%d-%H%M')}"
        
        # Crear bucket
        print(f"📦 Creando bucket: {bucket_name}")
        s3.create_bucket(Bucket=bucket_name)
        
        # Crear archivo de configuración simple
        config = {
            "bucket_name": bucket_name,
            "region": "us-east-1",
            "created": datetime.now().isoformat()
        }
        
        with open('lab_config.json', 'w') as f:
            json.dump(config, f, indent=2)
        
        print("✅ Setup completado!")
        print(f"📋 Bucket creado: {bucket_name}")
        print("📄 Configuración guardada en: lab_config.json")
        print("\n🎯 Próximos pasos:")
        print("1. Los participantes pueden usar SageMaker Studio Lab directamente")
        print("2. Los notebooks tienen datos embebidos")
        print("3. Solo necesitan credenciales AWS básicas")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Los participantes pueden usar el lab sin este setup")
        print("   Los notebooks funcionan con datos públicos")

if __name__ == "__main__":
    setup_lab()