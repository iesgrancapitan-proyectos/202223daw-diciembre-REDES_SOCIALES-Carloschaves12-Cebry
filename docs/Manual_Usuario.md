## Manual de Usuario

Sección dedicada al desarrollo de la documentación de ayuda necesaria para el uso de la aplicación/servicio al usuario

### Índice de contenidos

1. Obtención de credenciales
   1. Pocket
   2. Twitter
   3. Telegram
2. Configuración de credenciales
3. Programación de tareas con horarios
4. Publicación de enlaces

## 1. Obtención de credenciales

### 1. Pocket
Lo primero es crear una cuenta de Pocket en la que guardar las noticias que se publicarán.

Ahora crearemos una aplicación en Pocket, para ello iremos a https://getpocket.com/developer/ y clicaremos en crear una nueva app, le pondremos el nombre y descripción que queramos y le daremos todos los permisos y en plataformas solo Desktop(other). Con esto obtendremos la consumer key.

Una vez tengamos la consumer key de Pocket en nuestra aplicación iremos a ```../src/``` y modificaremos en ``` .env ``` el valor de POCKET_CONSUMER_KEY y también el de REDIRECT_URI por cualquier URL.

Ejecutaremos el script **config/scriptPocketAuthorize.py** para obtener las credenciales de la API de Pocket desde el directorio **src**. Para ello, ejecutamos el siguiente comando:

``` python3 ../config/scriptPocketAuthorize.py ```

Esto generará un enlace que nos llevará a la página de Pocket para autorizar el uso de la API. Una vez autorizado, pulsaremos enter para que nos muestre las credenciales de la API (__correo__ y __access_token__) para ese usuario de Pocket.

### 2. Twitter

Asumiendo que tenemos una cuenta en Twitter que usaremos para tuitear los enlaces, entramos a https://developer.twitter.com/en y nos logeamos con la cuenta desde la que vamos a tuitear.

Nos llevará a un formulario muy simple, el que completaremos, aceptaremos los términos y usos de condición y por último, nos enviarán un correo para confirmar el e-mail.

Nos llevarán a una página con una serie de pasos. Entre los cuales nos harán preguntas sobre nuestro nivel de programación y el uso que vamos a hacer de la API, en este paso es importante señalar en las especificaciones la opción de tuitear, dar retweet, like, seguir, o mandar mensajes directos, esto se encuentra en el segundo paso.

Una vez terminamos esto, nos pregutarán por el nombre de nuestra app. Además, nos devolverán la __API Key__, __API Key Secret__ y __Bearer Token__ que debemos guardar para que más tarde, una vez hecho, volvamos al dashboard para ir a nuestra app. Estará en **Projects & Apps** en el panel de la izquierda, allí seleccionaremos la pestaña de **Keys and Tokens**  para poder generar las __Access Token and Secret__ que deberemos guardar.
### 3. Telegram
Lo primero que haremos será crear nuestro bot para publicar en los diferentes grupos. Para ello hay que buscar en el buscador de Telegram __BotFather__ y abriremos el chat con él. En el chat pondremos el comando ``` /start ``` para que nos pueda devolver un mensaje con todos los comandos disponibles, nosotros usaremos el comando para crear el bot ``` /newbot ```. El siguiente mensaje que enviaremos será el nombre del bot y el último será el nombre de ususario del bot.

Despues de esto el bot nos mandará un ultimo mensaje en el que estará el APIToken, entraremos a ```../src/``` y editaremos ``` .env ``` y lo pegaremos en TELEGRAM_BOT_TOKEN.

Una vez tengamos nuestro bot, crearemos el grupo de Telegram al que se enviarán las noticias. Para este paso es obligatorio usar telegram web, ya que desde el móvil no se puede. Entramos al grupo y en la URL del navegador veremos algo similar a ``` https://web.telegram.org/k/#-YYYYYYYYYY ```, de ahí seleccinaremos desde el - hasta el final y le añadiremos un 100 entre el menos y los números, se quedaría tal que así: -100YYYYYYYYYY (siendo Y números). Con esto tendríamos el id del grupo de Telegram.

## 2. Configuración de credenciales

Para configurar tanto las credenciales como el horario de publicación, es necesario conocer JSON [Anexo Referencia JSON](Anexo_Referencia_JSON).

Primero debemos ir a ```../config/ ``` y editar ___credentials_.json__, durante todo el documento las cadenas <asdf> serán las que puedan ser sustituidas. En primer lugar, encontraremos la configuración de Pocket donde pocket_id será cada uno de las cuentas de Pocket, cada una con su e-mail y access_token correspondientes, ahí pondremos el e-mail y access_token que nos devuelve el script. Por último, en tags hay que añadir la o las tags que queremos que nuestra aplicación tenga en cuenta a la hora de obtener las noticias.

La configuaración de Twitter es parecida a la de Pocket, ya que también tenemos un twitter_id que será el usuario de la cuenta. En user_name escribiremos el nombre de la cuenta, este es el @ de tu cuenta, pero sin la @. Después pondremos todas las claves guardadas anteriormente: consumer key, consumer secret, bearer token, access token y access token secret (cada una en su lugar correspondiente). Por último last_time_read que será la fecha desde que leeremos los tweets, debe llevar este formato AAAA-MM-DDTHH:MM:SSZ.

Finalmente, solo queda configurar Telegram al igual que las anteriores. Lo primero, el telegram_id hay que cambiarlo por el nombre de telegram y lo último que habría que hacer es cambiar el valor de chat_id por el id del chat de telegram que antes habíamos obtenido.

## 3. Programación de tareas con horarios
Para controlar el horario de las publicaciones entramos en ``` ../config/ ``` y editamos el archivo jobs.json,
lo único que editaremos en este archivo son los valores del campo time y account.

Cada campo se puede repitir las veces que se necesite.

## 4. Publicación de enlaces

Cada usuario autorizado puede guardar enlaces en su cuenta de Pocket, para ello, se puede usar la pagina web de Pocket o una extensión para el navegador (en firefox viene instalada de serie).

Una vez la tengamos, guardamos las noticas con alguna etiqueta de las guardadas en **config/credentials.json**.

- Mediante la extensión una vez estemos en la página web de la noticia hacemos click sobre la extensión y se nos abrirá un cuadro de diálogo para poner las etiquetas.