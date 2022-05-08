# Practica 1 - Descargar la dataset de internet

# En este caso usamos Kaggle y se requiere de una autentificación.
# Primero generamos nuestra API key de Kaggle desde la página web.
# Guardamos la API key en nuestro equipo.
# La movemos a una carpeta llamada ".kaggle" que se ubica en la ruta de nuestro usuario en Windows.
# En caso de que la carpeta ".kaggle" no exista entonces habrá que crearla.
# Una vez colocada la API key dentro de la carpeta entonces ya podemos comenzar.

# Importamos Kaggle
import kaggle
# Importamos la libreria para descomprimir archivos .zip
import zipfile

# Nos autenticamos en Kaggle con nuestra API key previamente guardada en el equipo
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

# Descargamos la dataset que más nos guste
# Lo que va entre las comillas simples primero va el nombre del usuario, después el nombre del dataset
# En "path" el ./ indica el directorio actual donde nos encontremos en la terminal
api.dataset_download_files('brunovr/metacritic-videogames-data', path='./')

# Se descargará la dataset en .zip, toca descomprimirlo
with zipfile.ZipFile('/Users/Armando/Desktop/CodigoPython/Practica_1/metacritic-videogames-data.zip', 'r') as zipref:
    zipref.extractall('target/path')

# Y listo, ya tendriamos nuestro archivo listo para abrirlo y trabajar.

