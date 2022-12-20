## Manual de Despliegue

### Requisitos para el despliegue

Esta sección es para que los desarrolladores puedan entender cómo se debe desplegar el proyecto. Para ello, se debe tener en cuenta los siguientes aspectos:

- Sistema operativo basado en GNU/Linux. Se recomienda Ubuntu Server 18.04 LTS.

- La instalación de los programas __git__, __at__, __python3__ y __python3-pip__.
- La instalación de las librerías de __python__:
  - python-dotenv
  - tweepy
  - requests
  
### Pasos para el despliegue

 - Asegurarnos de tener instalados los programas y librerías indicadas. Para asegurarnos de que los programas están instalados, ejecutamos los siguientes comandos:
   - ``` git --version ``` o bien ```  apt show git ```
   - ``` at --version ``` o bien ``` apt show at ```
   - ``` python3 --version ``` o bien ``` apt show python3 ```
   - ``` pip3 --version ``` o bien ``` apt show python3-pip ```
  
 - Si no lo estuvieran, se instalan con los siguientes comandos:
   - ``` sudo apt install git ```
   - ``` sudo apt install at ```
   - ``` sudo apt install python3 ```
  
 - Para asegurarnos de que las librerías necesarias están instaladas, ejecutamos los siguientes comandos:
   - ```python3 -c "import dotenv" ``` o bien ``` pip3 show python-dotenv ```
   - ``` python3 -c "import tweepy" ``` o bien ``` pip3 show tweepy ```
   - ``` python3 -c "import requests" ``` o bien ``` pip3 show requests ```

 - Si no lo estuvieran, se instalan con los siguientes comandos:
   - ``` pip3 install python-dotenv ```
   - ``` pip3 install tweepy ```
   - ``` pip3 install requests ```
   - ``` pip3 install python-dotenv ```

Se ha facilitado el archivo **deploy.sh** que se encarga de instalar los programas y librerías necesarias para el despliegue. Para ello, ejecutamos el siguiente comando:

``` sudo sh deploy.sh ```

 - Una vez instalados los programas y librerías necesarias, se procede a clonar el repositorio del proyecto. Para ello, ejecutamos el siguiente comando:

```git clone https://github.com/iesgrancapitan-proyectos/202223daw-diciembre-REDES_SOCIALES--Carloschaves12-Cebry```

 - Una vez clonado el repositorio, cambiamos los ficheros de configuración:
   - renombraremos el archivo **.env.example** a **.env** y lo editaremos con los datos de nuestra cuenta de Twitter.
   - **config/credentials.json**.
   - **config/jobs.json**.
    El formato de los archivos y su uso se aborda en el [Manual de Usuario](Manual_Usuario)

El último paso es ejecutar desde el directorio **src** el programa **control/startPosting.py**. Para ello, ejecutamos el siguiente comando:

``` python3 control/startPosting.py ```

El este script se ejecutará cada 24 horas hasta que se cancele su ejecución. Para ello, ejecutamos el siguiente comando:

``` python3 control/stopPosting.py ```