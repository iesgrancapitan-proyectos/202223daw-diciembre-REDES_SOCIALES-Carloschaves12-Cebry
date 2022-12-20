[Anterior](6Doc_Implantación) - [Índice](Doc) - [Siguiente](8Doc_Conclusiones)

## 7. Recursos
### 7.1. Herramientas hardware

El hardware usado ha sido los equipos personales, la máquina virtual en la que se han realizado las pruebas y el servidor en el que se ha desplegado la solución:

- Equipo 1: Procesador AMD Ryzen 5 5600H, memoria RAM DDR4-3200 MHz 16 GB, disco duro SSD de 512 GB y sistema operativo Windows 10.

- Equipo 2: cpu: Intel(R) Core(TM) i5-4210U CPU @ 1.70GHz, memoria RAM 8 GB, disco duro SSD de 256 GB y sistema operativo dual __Ubuntu__ 20.04 LTS / Windows 10. (Solo se ha usado __Ubuntu__)

- El equipo desconoce las características del servidor del centro.
### 7.2. Herramientas software

Para la implementación de la solución se han utilizado las siguientes herramientas software:

- Máquina virtual de pruebas 1: Sistema Operativo __Ubuntu__[[22]](9Doc_Referencias_Bibliografia#22) 20.04 LTS, software de virtualización: VirtualBox 6.1.18. Se ha utilizado esta máquina virtual para realizar las pruebas de la solución durante el desarrollo del proyecto, ya que eran necesarios los programas at y crontab. RAM: 2 GB, CPU: 1, disco duro: 10 GB.

- Máquina virtual de pruebas 2: Sistema Operativo __Ubuntu Server__ 20.04 LTS, software de virtualización: VirtualBox 6.1.18. Se ha utilizado esta máquina virtual para realizar una prueba de despliegue y funcionalidad de la solución. RAM: 2 GB, CPU: 1, disco duro: 10 GB.

- Máquina virtual de despliegue: El equipo desconoce las características de la máquina virtual en la que se ha desplegado la solución en el servidor del centro, más allá de que se trata de una máquina virtual de __Ubuntu Server__ y que se ha utilizado el software de virtualización __VMware__. Lo que es seguro es que no necesitará recursos extra de computación o espacio ya que nuestra aplicaión consume unos recursos muy bajos.

- Sistema Operativo __Ubuntu__: Se ha elegido este sistema operativo por resultar muy liviano, fácil de intalar en una máquina virtual, por ser de código abierto y por brindar acceso a los programas necesarios para la implementación de la solución, como son python3, at y crontab.

- Sistema Operativo ___Ubuntu Server__: Se ha elegido este sistema operativo por los mismos motivos que el sistema operativo __Ubuntu__, además de ser un sistema operativo que se puede instalar en una máquina virtual sin interfaz gráfica, lo que permite ahorrar recursos y espacio en disco.

- Sofware de virtualización __VirtualBox__[[23]](9Doc_Referencias_Bibliografia#23) 6.1.18: Se ha elegido este software de virtualización por ser de código abierto, por ser multiplataforma y por la familiaridad de los miembros del equipo con el mismo.

- Programa at: Este programa nos permite programar la ejecución de un programa determinado en un momento determinado. En nuestro caso hemos tenido que instalarlo ya que no viene instalado por defecto en las distribuciones GNU/Linux.

- Programa crontab: Este programa nos permite programar la ejecución de un programa determinado de forma periódica.

- Lenguaje de programación Python3: Se ha elegido este lenguaje de programación por ser de código abierto y por ser un lenguaje de programación con el que los miembros del equipo estaban familiarizados.

- TweePy v4.10.1: (Librería de Python para la gestión de la API de __Twitter__. Esta librería ha sido elegida por recomendación del profesorado puesto que había sido uilizada con anterioridad y podría haber brindado su ayuda en caso de haber sido necesario.

- API de Pocket v3: Esta API es la oficial de la plataforma web __Pocket__. Se accedió a seguir utilizando esta plataforma para la interfaz con el usuario _manager_ por su facilidad de uso, la posibilidad de uso desde cualquier dispositivo y por ser la plataforma familiar de los usuarios, además de tener las funcionalidades justas y necesarias para el proyecto.

- API de __Telegram__ v6.3: Esta API es la oficial de __Telegram__. Se ha elegido esta API por ser la oficial de la red social.

- Entorno de desarrollo Visual Studio Code (VSCode): Se ha elegido este entorno de desarrollo por la familiaridad de los miembros del equipo con el mismo, por ser un entorno de desarrollo multiplataforma por las extensiones que ofrece.

- Live Share (Extension de VSCode): Esta extensión nos permite compartir el entorno de desarrollo con otros usuarios, de forma que todos los usuarios pueden ver y editar el código que se está escribiendo en tiempo real.

- Control de versiones __Git__ [[24]](9Doc_Referencias_Bibliografia#24): Se ha elegido este control de versiones como interfaz para publicar el código y la documentación del proyecto en __GitHub__[[25]](9Doc_Referencias_Bibliografia#25).

- __GitHub__: Se ha utilizado esta plataforma por ser la indicada para la entrega de proyectos del centro y por ser una herramienta que los miembros del equipo ya conocían.

- Discord (Chat de voz): Se ha elegido este chat de voz por ser una herramienta que los miembros del equipo ya conocían y por ser una herramienta que permite compartir la pantalla de un usuario con el resto de usuarios del chat.

- JSON: Se ha elegido este formato de archivo por ser un formato de archivo que permite almacenar datos de forma estructurada y por su facilidad de uso incluso para usuarios sin conocimientos de programación.
### 7.3. Personal

Para la implementación de la solución se ha contado con la colaboración de los siguientes miembros del equipo:

- [Carlos Chaves Hernández](http://www.github.com/carloschaves12)
- [Javier Cebrián Muñoz](http://www.github.com/Cebry)

También se ha contado con la colaboración del profesorado del centro:

- [Rafael del Castillo Gomariz](https://github.com/rdelcastillo) en calidad de propulsor y apoyo técnico del proyecto, habiendo sido de gran utilidad la consulta de sus repositorios de Github.[[25]](9Doc_Referencias_Bibliografia#26)
- Miguel Ángel González Ruz en calidad de tutor.

### 7.4. Presupuesto

En el proyecto se ha optado por el uso de software libre, es por eso que el coste de desarrollo es cero, el único coste que hay es del mantenimiento del servidor donde se hace despliegue, el cual es desconocido para el equipo, pero debe suponer un coste muy bajo debido a las mínimas necesidades del proyecto, tanto a nivel de procesamiento como de almacenamiento.

[Anterior](6Doc_Implantación) - [Índice](Doc) - [Siguiente](8Doc_Conclusiones)