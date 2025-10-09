# Lab 1: Servidor Web en EC2

## Objetivos de Aprendizaje
Al finalizar este lab, serás capaz de:
- Lanzar y configurar instancias EC2 desde cero
- Automatizar despliegues con User Data scripts
- Configurar Security Groups y entender reglas de firewall
- Conectarte vía SSH y administrar servidores
- Entender metadata de instancias EC2

## Duración estimada
60 minutos

## Requisitos
- Cuenta de AWS con permisos para EC2
- Navegador web
- Cliente SSH (PuTTY en Windows, terminal en Mac/Linux)

## Progreso del Lab

Aprenderás las funcionalidades clave de EC2 en 4 fases:
1. **Fase 1 (15 min):** Lanzar instancia EC2 con User Data
2. **Fase 2 (15 min):** Conexión SSH, exploración del servidor e Instance Metadata
3. **Fase 3 (15 min):** Volúmenes EBS, snapshots y estados de instancia
4. **Fase 4 (15 min):** Security Groups, CloudWatch y monitoreo

---

## FASE 1: Despliegue Inicial (15 minutos)

### 1.1 Crear tu primera instancia EC2

1. Ve a la consola de AWS → **EC2 → Lanzar instancia**

2. **Configuración básica:**
   - **Nombre:** `webserver-lab1-<tu-nombre>`
   - **AMI:** Amazon Linux 2023
   - **Tipo de instancia:** t2.micro
   - **Par de claves:** 
     - Clic en "Crear un nuevo par de claves"
     - Nombre: `key-lab1-<tu-nombre>`
     - Tipo: RSA
     - Formato: `.pem` (Mac/Linux) o `.ppk` (Windows/PuTTY)
     - **Crear par de claves**
>    **⚠️ Importante:** Descarga y guarda este archivo, lo necesitarás después.

3. **Configuraciones de red:**
   - Clic en "Editar"
   - **Crear grupo de seguriddad:**
     - Nombre: `webserver-lab1-sg`
     - Descripción: `Security group para lab 1 - Web Server`
   - **Reglas de entrada:**
     - Regla 1:
       - Tipo: SSH (22)
       - Tipo de origen: Mi IP (tu IP actual)
     - Regla 2:
       - Tipo: HTTP (80)
       - Tipo de origen: Cualquier lugar (0.0.0.0/0)

4. **Configurar almacenamiento:**
   - Dejar por defecto: 8 GB, gp3

5. Despliega **Detalles avanzados:**
   - Desplázate hasta el final
   - En **Datos de usuario (User Data)**, pega el contenido de [`user-data.sh`](user-data.sh)

6. **Revisar y lanzar:**
   - Revisa el resumen en el panel derecho
   - Clic en **"Lanzar instancia"**

### 1.2 Verificar el despliegue

1. Ve a **EC2 → Instancias**
2. Selecciona tu instancia y espera a que:
   - **Estado de la instancia:** `En ejecución` (verde)

3. En la pestaña **Monitoreo** , **copia la IP pública** de tu instancia

4. Abre un navegador y ve a: `http://<TU-IP-PUBLICA>`
   Deberías ver una página web con:
     - Título de bienvenida
     - IP pública y privada, y el ID de la instancia EC2
     - AZ y región de AWS
     - Timestamp de despliegue

---

## FASE 2: Conexión SSH y Personalización (15 minutos)

### 2.1 Conectarte vía SSH

**En Mac/Linux:**
```bash
# Dar permisos al archivo de clave
chmod 400 lab1-keypair-<tu-nombre>.pem

# Conectar
ssh -i lab1-keypair-<tu-nombre>.pem ec2-user@<TU-IP-PUBLICA>
```

**En Windows (con PuTTY):**
1. En PuTTY:
   - Host: `ec2-user@<TU-IP-PUBLICA>`
   - Connection → SSH → Auth → Credentials: selecciona tu `.ppk`
   - Clic en "Open"

### 2.2 Explorar el servidor

Una vez conectado, ejecuta estos comandos para familiarizarte:

```bash
# Ver información del sistema operativo
cat /etc/os-release

# Ver uso de CPU y memoria
top

# Ver uso de disco
df -h

# Ver información de red
ip add
netstat -tuln

# Ver si Apache está corriendo
sudo systemctl status httpd

# Ver logs de httpd
sudo journalctl -u httpd -n 50

# Ver los archivos del sitio web
ls -l /var/www/html/

# Ver el contenido de la página principal
cat /var/www/html/index.html
```

### 2.3 Explorar Instance Metadata Service (IMDS)

**¿Qué es IMDS?**
Es un servicio interno de AWS, accesible a través de la dirección 169.254.169.254, que permite a las instancias obtener información sobre sí mismas (metadatos), sin necesidad de realizar llamadas externas a la API de AWS ni usar credenciales explícitas.

**¿Para qué sirve en la práctica?**
- Scripts de inicialización (User Data) que necesitan obtener detalles como región, AZ o ID de la instancia
- Aplicaciones que necesitan conocer su propia IP para configurarse
- Obtener credenciales temporales de IAM roles asociados a la instancia
- Configuración dinámica basada en tags o atributos personalizados de la instancia

**Seguridad:**
- **IMDSv1 (antiguo):** No requiere autenticación. Vulnerable a ataques SSRF.
- **IMDSv2 (recomendado):** Requiere token de sesión. Protege contra SSRF.
- **Mejor práctica:** Siempre usa IMDSv2. Deshabilita IMDSv1 en la configuración de la instancia.

```bash
# Obtener token para IMDSv2
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")

# Verificar que el token se obtuvo
echo $TOKEN

# Ver todas las categorías disponibles
curl -w '\n' -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/

# Consultas específicas útiles
curl -w '\n' -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/ami-id
curl -w '\n' -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/instance-type
curl -w '\n' -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-ipv4
curl -w '\n' -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/local-ipv4
curl -w '\n' -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/security-groups
```

## FASE 3: Gestión de Instancias y Volúmenes (15 minutos)

### 3.1 Explorar volúmenes EBS

Para encontrar el volumen de tu instancia:

1. Ve a **EC2 → Instancias**
2. Selecciona tu instancia
3. Pestaña **Almacenamiento**
4. Haz clic en el ID de volumen (enlace azul)
5. Esto te llevará directamente al volumen

Una vez en el volumen, observa sus propiedades:
- ID del volumen
- Tamaño: 8 GiB
- Tipo: gp3
- Estado del volumen: En uso
- IOPS y Rendimiento
- Zona de disponibilidad (debe coincidir con tu instancia)

Desde SSH, verifica el almacenamiento:

```bash
# Ver volúmenes montados
lsblk

# Ver uso de disco
df -h

# Ver información del sistema de archivos
sudo file -s /dev/xvda1

# Crear un archivo de prueba
echo "Datos persistentes en EBS" | sudo tee /var/www/html/test.txt
```

### 3.2 Crear un snapshot (respaldo)

Desde la consola de AWS:

1. Selecciona tu volumen
2. **Acciones → Crear instantánea**
3. Completa los datos:
   - Descripción: `Backup del volumen del lab 1 - <Tu-Nombre>`
4. Clic en **Crear instantánea**

**Verificar la instantánea:**

1. Ve a **EC2 → Elastic Block Store → Instantáneas**
2. Busca tu instantánea por la descripción y selecciónala
3. Observa:
   - Estado: Inicialmente "Pendiente", luego "Completado" (puede tardar 1-2 minutos)
   - Tamaño completo de la instantánea: 1.68 GiB
   - Tamaño del volumen: 8 GiB
   - Volumen de origen: El ID de tu volumen
   - Iniciada: Timestamp de cuándo se creó

### 3.3 Experimentar con estados de instancia

Desde la consola de AWS:

1. Selecciona tu instancia
2. **Estado de la instancia → Detener instancia → Detener**
3. Espera a que el estado cambie de "Deteniéndose" a "Detenida"
4. Observa que:
   - La IP pública desaparece
   - El volumen EBS permanece
   - No se generan costos de cómputo

5. **Estado de la instancia → Iniciar instancia**
6. Espera a que el estado cambie de "Pendiente" a "En ejecución"
6. Observa que:
   - Se asigna una nueva IP pública (diferente a la anterior)
   - Los datos en EBS persisten
   - El archivo test.txt sigue ahí

7. Accede a la página web con la nueva IP pública

**Observación:** La página web mostrará la IP pública ANTIGUA, no la nueva. ¿Por qué?
- El User Data solo se ejecuta en el primer arranque
- El HTML fue generado con la IP antigua y no se actualiza automáticamente
- Los datos en el HTML son estáticos

Para verificar la IP real:

```bash
# Reconecta por SSH con la nueva IP

# Verifica que los datos persisten
cat /var/www/html/test.txt

# Consulta la IP pública actual desde metadata
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-ipv4
```

**Pregunta:** ¿Cómo resolverías el cambio de la IP pública en producción?

---

## FASE 4: Security Groups y Monitoreo (15 minutos)

### 4.1 Experimentar con Security Groups

1. Ve a **EC2 → Red y seguridad → Security Groups**
2. Selecciona tu security group `webserver-lab1-<tu-nombre>-sg`
3. Pestaña **Reglas de entrada → Editar reglas de entrada**
4. **Elimina temporalmente** la regla:
   - Tipo: HTTP (80)
   - Tipo de origen: Cualquier lugar (0.0.0.0/0)
5. Guarda los cambios
6. Intenta acceder a tu página web desde el navegador
7. **¿Qué sucede?** La página no carga (timeout o connection refused)
8. **Vuelve a agregar** la regla:
   - Tipo: HTTP (80)
   - Tipo de origen: Cualquier lugar (0.0.0.0/0)
9. Guarda los cambios y verifica que ahora sí puedes acceder

**Pregunta:** ¿Qué pasaría si eliminas la regla SSH (22) mientras estás conectado por SSH? ¿Podrías volver a conectarte después?

### 4.2 Monitoreo con CloudWatch

Desde la consola de AWS:

1. Ve a **EC2 → Instancias**
2. Selecciona tu instancia
3. Pestaña **Monitoreo**
4. Observa las métricas disponibles:
   - Utilización de la CPU (%)
   - Entrada de red (bytes)
   - Salida de red (bytes)

**Nota sobre frecuencia de métricas:**
- **Monitoreo básico (gratis):** Métricas cada 5 minutos
- **Monitoreo detallado (costo):** Métricas cada 1 minuto

### Habilitar monitoreo detallado:

1. Selecciona tu instancia
2. **Acciones →** Pestaña **Monitoreo → Administrar el monitoreo detallado**
3. Marca la casilla **Habilitar**
4. **Confirmar**

**Importante:** Después de habilitar:
- Puede tomar 1-2 minutos ver la primera métrica nueva

### Visualizar las métricas cada 1 minuto:

**Importante:** Los paneles por defecto muestran datos cada 5 minutos aunque tengas monitoreo detallado habilitado.

Para ver las métricas cada 1 minuto:
1. En la pestaña **Monitoreo**, ubícate en cualquier métrica (ej: Utilización de la CPU)
2. Clic en **Ampliar** (icono de expandir)
3. En el gráfico ampliado, busca el selector de período
4. Cambia de **5 minutos** a **1 minuto**
5. Ahora verás los puntos de datos cada 1 minuto

Para verificar que funciona, genera carga y observa:

```bash
# Desde SSH, genera carga de CPU continua
yes > /dev/null &
PID=$!

# Deja correr por 2-3 minutos
# Ve al gráfico ampliado con período de 1 minuto
# Refresca y deberías ver puntos de datos cada 1 minuto

# Detener la carga
kill $PID
```

**Verificación exitosa:** Si en el gráfico (con período de 1 minuto) ves puntos de datos cada 1 minuto, el monitoreo detallado está funcionando correctamente.

### 4.3 Explorar tags

Desde la consola de AWS:

1. Selecciona tu instancia
2. Pestaña **Tags**
3. **Administrar tags → Agregar tag**
   - Clave: `Environment`
   - Valor: `Lab`
4. Agregar otro tag:
   - Clave: `Owner`
   - Valor: `<tu-nombre>`

**Pregunta:** ¿Para qué sirven los tags en producción?
---

## Limpieza de Recursos

**IMPORTANTE:** Para evitar costos, elimina todos los recursos creados:

### Paso 1: Terminar la instancia EC2
1. Ve a **EC2 → Instancias**
2. Selecciona tu instancia `webserver-lab1-<tu-nombre>`
3. **Estado de la instancia → Terminar instancia**
4. Confirma la terminación
5. Espera a que el estado cambie a `Terminated`

### Paso 2: Eliminar Security Group
1. Ve a **EC2 → Security Groups**
2. Selecciona `webserver-lab1-sg`
3. **Acciones → Eliminar security group**
4. Si no puedes eliminarlo, espera unos minutos (la instancia debe estar completamente terminada)

### Paso 3: Eliminar par de claves (opcional)
1. Ve a **EC2 → Pares de claves**
2. Selecciona `lab1-keypair-<tu-nombre>`
3. **Acciones  Eliminar**
4. Tambin elimina el archivo `.pem` o `.ppk` de tu computadora

### Verificacin final
-  Instancia en estado "Terminated"
-  Security Group eliminado
-  Par de claves eliminado
-  No hay volmenes EBS hurfanos (EC2  Volmenes)

---

##  Recursos Adicionales

- [Documentacin oficial de EC2](https://docs.aws.amazon.com/ec2/)
- [User Data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)
- [IMDS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html)
- [Security Groups Best Practices](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)