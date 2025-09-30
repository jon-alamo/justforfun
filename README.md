# Tests


## Build con Docker
Genera una imagen basada en python:13.3-slim con los tests y el parser pero SIN los archivos para testear. Hay que hacer el build cada vez que se haga un cambio en el código.

```
docker compose build
```


## Ejecuta tests
Monta la imagen y ejecuta los test para los archivos que haya en el directorio `data/` de la raíz del repo. Para cada archivo que encuentre en el directorio `data/` añade los tests de las dos clases `TestCase` que hay en el archivo `tests/test_raw_file.py` dinámicamente, por lo que no hace falta hacer build al añadir o modificar los archivos de datos.

```
docker compose up
```

