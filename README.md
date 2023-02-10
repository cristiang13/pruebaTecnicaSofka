# pruebaTecnicaSofka
prueba tecnica 

* para ejecutar el proyecto se crea un entorno virtual pthon 
- python -m venv nave_espaciales-env

* despues activar el entorno virtual 

* luego en la raiz del proyecto se instala los paquetes, dirigirse donde esta el archivo requeriments.txt
-pip install requeriments.txt

* crear la base de datos mysql,para este proyecto se uso mariadb que viene en xammp 
el nombre de la base de datos es naves_espaciales

* luego realizar la migracion
python manage.py makemigrations
python manage.py migrate

* por ultimo se ejecuta el proyecto
python manage.py runserver


Tablas de la base de datos naves_espaciones  
![image](https://user-images.githubusercontent.com/13666681/218152933-2e199840-ab7a-4f2b-b45e-0dc0877cb3d2.png)

