#!/bin/bash

# Actualizar paquetes
yum update -y

# Instalar, iniciar y habilitar Apache (httpd)
yum install -y httpd
systemctl start httpd
systemctl enable httpd

# Obtener token para IMDSv2 (Instance Metadata Service v2)
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")

# Obtener información de la instancia usando el token
PRIVATE_IP=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta-data/local-ipv4)
PUBLIC_IP=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta-data/public-ipv4)
INSTANCE_ID=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta-data/instance-id)
AVAILABILITY_ZONE=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta-data/placement/availability-zone)
REGION=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta-data/placement/region)

# Crear archivo CSS
cat << 'EOF' > /var/www/html/styles.css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
}

.container {
    max-width: 600px;
    background: white;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    animation: fadeIn 0.5s ease-in;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

h1 {
    color: #667eea;
    margin-bottom: 10px;
    font-size: 2em;
    text-align: center;
}

.subtitle {
    text-align: center;
    color: #666;
    margin-bottom: 30px;
    font-size: 1.1em;
}

.info-box {
    background: #f8f9fa;
    padding: 15px;
    border-radius: 10px;
    margin: 15px 0;
    border-left: 4px solid #667eea;
}

.info-box strong {
    color: #764ba2;
    display: inline-block;
    min-width: 120px;
}

.success-badge {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    margin: 20px 0;
    font-weight: bold;
}

.timestamp {
    text-align: center;
    color: #999;
    font-size: 0.9em;
    margin-top: 20px;
    padding-top: 20px;
    border-top: 1px solid #eee;
}

.lab-info {
    margin-top: 10px;
}

.phase-indicator {
    background: #e8f4fd;
    color: #0066cc;
    padding: 10px;
    border-radius: 8px;
    text-align: center;
    margin-bottom: 20px;
    font-weight: bold;
}
EOF

# Crear página web inicial
cat << 'EOF' > /var/www/html/index.html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Servidor Web EC2 - Lab 1</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <div class="phase-indicator">
            FASE 1: Despliegue Inicial Completado
        </div>
        
        <h1>¡Servidor Web Activo!</h1>
        <p class="subtitle">Tu instancia EC2 está funcionando correctamente</p>
        
        <div class="success-badge">
            Apache instalado y configurado automáticamente
        </div>
        
        <div class="info-box">
            <p><strong>IP Pública:</strong> PUBLIC_IP_PLACEHOLDER</p>
        </div>
        
        <div class="info-box">
            <p><strong>IP Privada:</strong> PRIVATE_IP_PLACEHOLDER</p>
        </div>
        
        <div class="info-box">
            <p><strong>Instance ID:</strong> INSTANCE_ID_PLACEHOLDER</p>
        </div>
        
        <div class="info-box">
            <p><strong>AZ:</strong> AZ_PLACEHOLDER</p>
        </div>
        
        <div class="info-box">
            <p><strong>Región:</strong> REGION_PLACEHOLDER</p>
        </div>
        
        <div class="timestamp">
            <p>Desplegado el: TIMESTAMP_PLACEHOLDER</p>
            <p class="lab-info"><em>Lab 1 - AWS Cloud Essentials</em></p>
        </div>
    </div>
</body>
</html>
EOF

# Reemplazar placeholders con valores reales
OFFSET=$(TZ='America/Lima' date '+%z' | sed 's/^-0//' | sed 's/00$//')
TIMESTAMP=$(TZ='America/Lima' date "+%d/%m/%Y %H:%M:%S GMT-${OFFSET}")

sed -i "s/PUBLIC_IP_PLACEHOLDER/$PUBLIC_IP/g" /var/www/html/index.html
sed -i "s/PRIVATE_IP_PLACEHOLDER/$PRIVATE_IP/g" /var/www/html/index.html
sed -i "s/INSTANCE_ID_PLACEHOLDER/$INSTANCE_ID/g" /var/www/html/index.html
sed -i "s/AZ_PLACEHOLDER/$AVAILABILITY_ZONE/g" /var/www/html/index.html
sed -i "s/REGION_PLACEHOLDER/$REGION/g" /var/www/html/index.html
sed -i "s|TIMESTAMP_PLACEHOLDER|$TIMESTAMP|g" /var/www/html/index.html

# Configurar permisos
chown -R apache:apache /var/www/html/
chmod -R 755 /var/www/html/

# Reiniciar Apache para asegurar que todo esté cargado
systemctl restart httpd