# **Prueba Técnica con Django y PostgreSQL**

## **Descripción**
Este proyecto implementa una solución para procesar y transferir datos desde un archivo CSV, transformarlos y almacenarlos en una base de datos PostgreSQL. También incluye una API para calcular el número faltante en un conjunto.

---

### **Stack :computer:**

El proyecto esta construido sobre el siguiente stack tecnológico:

- **Python**: >=3.9
- **PostgreSQL**: >=12
- **Git**
- **virtualenv**

---

## **Instrucciones para clonar y configurar el proyecto**

### **1. Clonar el repositorio**
Primero, clona el repositorio desde GitHub:
```bash
git clone https://github.com/Edga-r17/technical-test.git
cd technical-test
```

### **2. Crear y activar un entorno virtual**
Usaremos `virtualenv` para crear un entorno virtual aislado para las dependencias del proyecto:
Crear el ambiente virtual usando [pyenv](https://github.com/pyenv/pyenv#installation)
Activar el ambiente virtual
```bash
pyenv activate <nombre_del_ambiente_creado>
```

### **3. Instalar las dependencias**
Instala las dependencias requeridas desde el archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## **Configuración del proyecto**

### **4. Configurar la base de datos PostgreSQL**
1. Crea una base de datos en PostgreSQL para este proyecto:
   ```sql
   CREATE DATABASE prueba_tecnica;
   ```
   
### **5. Configurar las variables de entorno**
Este proyecto utiliza variables de entorno para la configuración de la base de datos. Crea un archivo `.env` en el directorio raíz del proyecto con el siguiente contenido:
```env
export DB_PORT=5432
export DB_HOST='localhost'
export DB_PASSWORD='postgres'
export DB_USER='postgres'
export DB_NAME='technical_test'
```

Activa las variables de entorno al iniciar el proyecto:
```bash
source .env
```


### **6. Aplicar migraciones**
Ejecuta las migraciones para crear las tablas necesarias en la base de datos:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## **Ejecutar el proyecto**

### **7. Cargar datos iniciales**
Cargaremos los datos desde el archivo CSV en la tabla `RawTransaction`:
```bash
python manage.py shell
>>> exec(open('transactions/load_data.py').read())
```

### **8. Transformar los datos**
Transformaremos y dispersaremos los datos en las tablas `Company` y `Charge`:
```bash
python manage.py shell
>>> exec(open('transactions/transform_data.py').read())
```

### **8. Ejecutar el servidor**
Inicia el servidor de desarrollo de Django:
```bash
python manage.py runserver
```

Accede a la aplicación en tu navegador: [http://localhost:8000](http://localhost:8000)

---

## **Pruebas**

### **9. Probar la API**
La API incluye un endpoint para calcular un número faltante en un conjunto de los primeros 100 números naturales.

#### **Endpoint**
- Método: `POST`
- URL: `api/transactions/find-missing-number/`
- Ejemplo de cuerpo de solicitud:
  ```json
  {
      "number": 45
  }
  ```
- Ejemplo de respuesta:
  ```json
  {
      "missing_number": 45
  }
  ```

Prueba el endpoint con `curl`:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"number": 45}' http://localhost:8000/api/transactions/find-missing-number/
```

---
