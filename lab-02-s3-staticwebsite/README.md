# Lab 2: Sitio Web con S3 y CloudFront

## Objetivos
- Subir una página web estática a un bucket S3
- Configurar el bucket para hosting web
- Acelerar el sitio globalmente con CloudFront

## Duración estimada
30-40 minutos

## Requisitos
- Cuenta de AWS con permisos para S3 y CloudFront
- Navegador para acceder al sitio web

## Parte 1: Alojar en S3

### 1. Crear el bucket S3
1. Ir a **S3 → Crear bucket**.
2. Asignar un nombre único a nivel global: `bucket-lab2-web-<tu-nombre>`.
3. Desactivar **Bloquear todo el acceso público** para el lab.
4. Crear el bucket.

> **⚠️ Advertencia:** Desactivar el bloqueo de acceso público permite que el contenido del bucket sea accesible desde Internet. Solo hazlo para buckets destinados a hosting web público y nunca para datos privados.

### 2. Subir los archivos de la página
1. Descargar el contenido de la carpeta [`website`](website).
2. Haz clic en **Cargar** en tu bucket S3.
3. Selecciona todos los archivos y carpetas (`assets`, `scripts`, `styles`, `index.html`, etc.).
4. Mantén las configuraciones por defecto y haz clic en **Cargar**.

### 3. Configurar hosting web estático
1. Ve a **Propiedades → Alojamiento de sitios web estáticos → Editar**.
2. Selecciona **Habilitar**.
3. Documento de índice: `index.html`.
4. Documento de error: `404.html`.
5. Guarda los cambios.

### 4. Configurar política de acceso público
1. Ve a **Permisos → Política de bucket → Editar**.
2. Copia el contenido de [`bucket-policy.json`](bucket-policy.json) y reemplaza `mi-bucket` con el nombre de tu bucket.
3. Pega la política en el editor y guarda los cambios.

> **¿Por qué es necesaria?** Esta política permite que cualquier persona acceda (GET) a los archivos de tu sitio web. Sin ella, los visitantes recibirían errores de acceso denegado.

> **⚠️ Importante:** Solo usa esta configuración para contenido público. Nunca apliques políticas públicas a buckets con información sensible.

### 5. Verificar el sitio web
1. Vuelve a **Propiedades → Alojamiento de sitios web estáticos**.
2. Abre la URL del bucket en el navegador.
3. Verifica que todas las páginas (`index.html`, `about.html`, `contacto.html`) funcionen y que el contenido y los estilos carguen correctamente.

## Parte 2: Acelerar con CloudFront

### 6. Crear distribución de CloudFront
1. Ve a **CloudFront → Create distribution**.
2. **Get started:**
   - Distribution name: `distribution-lab2-<tu-nombre>`
   - Distribution type: **Single website or app**
3. **Specify origin:**
   - Origin type: **Amazon S3**
   - S3 Origin: Selecciona tu bucket
   - **Use website endpoint**
   - **Settings → Cache settings → Customize cache settings**
   - Viewer protocol policy: **Redirect HTTP to HTTPS**
   - Allowed HTTP methods: **GET, HEAD**
   - Cache policy: **CachingOptimized**

4. **Enable security:**
   - Web Application Firewall (WAF): **Enable security protections**

5. Finalmente, **Create distribution**

### 7. Probar la distribución CloudFront
1. **Espera a que el estado sea "Deployed"** (5-10 minutos).
2. Copia la **URL de dominio de CloudFront** (ejemplo: `d1234567890.cloudfront.net`).
3. Abre la URL en el navegador.
4. Verifica que tienes **HTTPS automático** (🔒 en la barra de direcciones).

## Parte 3: Probar protecciones del WAF
   
### 8. Verificar WAF en funcionamiento
1. Ve a **WAF & Shield → Web ACLs**.
2. Selecciona tu ACL web creada.
3. Ve a **Métricas y muestras** para ver el dashboard.

## Limpieza de recursos

Para evitar costos innecesarios, elimina los recursos en este orden:

### 1. Eliminar distribución CloudFront
1. Ve a **CloudFront → Distribuciones**.
2. Selecciona tu distribución.
3. **Deshabilitar** → Espera a que el estado cambie a "Disabled" (5-15 min).
4. **Eliminar** → Confirma la eliminación.

### 2. Eliminar WAF Web ACL
1. Ve a **WAF & Shield → Web ACLs**.
2. Selecciona tu ACL web.
3. **Eliminar** → Confirma escribiendo "delete".

### 3. Vaciar y eliminar bucket S3
1. **Vaciar el bucket S3:**
   - Ve a **S3 → Buckets**
   - Selecciona tu bucket
   - **Vaciar** → Confirma escribiendo "eliminar permanentemente"

2. **Eliminar el bucket:**
   - Selecciona el bucket vacío
   - **Eliminar** → Confirma escribiendo el nombre del bucket