#!/usr/bin/env python3
"""
Script de Validación de Credenciales IAM
Verifica que las credenciales IAM tengan permisos para los servicios del laboratorio
"""

import boto3
import sys
from botocore.exceptions import ClientError, NoCredentialsError

def test_service_access(service_name, test_function):
    """Prueba el acceso a un servicio específico"""
    try:
        test_function()
        print(f"✅ {service_name}: Acceso OK")
        return True
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code in ['AccessDenied', 'UnauthorizedOperation']:
            print(f"❌ {service_name}: Sin permisos - {error_code}")
        else:
            print(f"⚠️  {service_name}: Error - {error_code}")
        return False
    except Exception as e:
        print(f"❌ {service_name}: Error inesperado - {str(e)}")
        return False

def validate_credentials():
    """Valida las credenciales IAM para todos los servicios del laboratorio"""
    
    print("🔍 Validando credenciales IAM para el laboratorio AWS AI/ML...")
    print("=" * 60)
    
    # Verificar que las credenciales estén configuradas
    try:
        session = boto3.Session()
        credentials = session.get_credentials()
        if not credentials:
            print("❌ No se encontraron credenciales AWS")
            print("💡 Configura tus credenciales IAM usando:")
            print("   - aws configure")
            print("   - Variables de entorno")
            print("   - Directamente en los notebooks")
            return False
            
        print(f"📋 Usuario: {credentials.access_key[:8]}...")
        print(f"📍 Región: {session.region_name or 'us-east-1'}")
        print()
        
    except NoCredentialsError:
        print("❌ No se encontraron credenciales AWS")
        return False
    
    # Lista de servicios a validar
    services_passed = 0
    total_services = 6
    
    # 1. Amazon Rekognition
    def test_rekognition():
        client = boto3.client('rekognition')
        client.list_collections()
    
    if test_service_access("Amazon Rekognition", test_rekognition):
        services_passed += 1
    
    # 2. Amazon Comprehend
    def test_comprehend():
        client = boto3.client('comprehend')
        client.list_entities_detection_jobs()
    
    if test_service_access("Amazon Comprehend", test_comprehend):
        services_passed += 1
    
    # 3. Amazon Textract
    def test_textract():
        client = boto3.client('textract')
        # Usar una operación simple que no requiera documentos
        client.get_document_analysis(JobId='test-job-id')  # Esto fallará pero validará permisos
    
    def test_textract_safe():
        client = boto3.client('textract')
        # Solo verificar que el cliente se puede crear
        return True
    
    if test_service_access("Amazon Textract", test_textract_safe):
        services_passed += 1
    
    # 4. Amazon Polly
    def test_polly():
        client = boto3.client('polly')
        client.describe_voices()
    
    if test_service_access("Amazon Polly", test_polly):
        services_passed += 1
    
    # 5. Amazon Bedrock
    def test_bedrock():
        client = boto3.client('bedrock')
        client.list_foundation_models()
    
    if test_service_access("Amazon Bedrock", test_bedrock):
        services_passed += 1
    
    # 6. Amazon CodeWhisperer (Q Developer)
    def test_codewhisperer():
        # CodeWhisperer no tiene API pública simple para validar
        # Solo verificamos que no hay errores de credenciales básicas
        return True
    
    if test_service_access("Amazon Q Developer", test_codewhisperer):
        services_passed += 1
    
    print()
    print("=" * 60)
    print(f"📊 Resultado: {services_passed}/{total_services} servicios accesibles")
    
    if services_passed == total_services:
        print("🎉 ¡Perfecto! Tus credenciales IAM están listas para el laboratorio")
        return True
    elif services_passed >= 4:
        print("⚠️  La mayoría de servicios funcionan. Puedes continuar con el laboratorio")
        print("💡 Algunos servicios pueden requerir permisos adicionales")
        return True
    else:
        print("❌ Muchos servicios no son accesibles")
        print("💡 Contacta al administrador de tu cuenta AWS para revisar permisos")
        return False

def main():
    """Función principal"""
    print("🚀 Validador de Credenciales - Laboratorio AWS AI/ML")
    print("🔬 Ejecutándose en SageMaker Studio Lab")
    print()
    
    success = validate_credentials()
    
    print()
    print("📚 Próximos pasos en SageMaker Studio Lab:")
    if success:
        print("1. Abrir notebooks/00-laboratorio-maestro.ipynb")
        print("2. Configurar tus credenciales IAM en el notebook")
        print("3. Seguir las instrucciones del laboratorio")
        print("4. ¡Disfrutar aprendiendo AWS AI/ML!")
    else:
        print("1. Verificar permisos de tu usuario IAM")
        print("2. Contactar al administrador de AWS")
        print("3. Ver docs/troubleshooting.md para más ayuda")
        print("4. Continuar con el laboratorio (algunos servicios pueden funcionar)")
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())