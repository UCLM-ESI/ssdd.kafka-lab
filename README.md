# Repositorio de herramientas de Kafka para la sesión de laboratorio

## Depliegue del servicio

Utilizando el Docker Compose:

```bash
docker compose up -d
```

## Herramientas de CLI

`kcat` es una herramienta de línea de comandos para poder interactuar con un servidor Kafka.

### Listar topics en un broker de Kafka

```bash
kcat -b localhost:9092 -L
Metadata for all topics (from broker -1: localhost:9092/bootstrap):
 1 brokers:
  broker 1001 at kafka:9092 (controller)
 1 topics:
  topic "example" with 2 partitions:
    partition 0, leader 1001, replicas: 1001, isrs: 1001
    partition 1, leader 1001, replicas: 1001, isrs: 1001

```

### Producir un mensaje

```
kcat -b localhost:9092 -P -t example
ESCRIBE TU MENSAJE AQUI
```

Para terminar de escribir el mensaje se pulsa `Control+D`. Para terminar la ejecución sin enviar más mensajes,
otro `Control+D`,

### Consumir mensajes desde el principio

```bash
kcat -b localhost:9092 -C -t example
```

Si se quieren consumir sólo mensajes nuevos se puede jugar con la opción `-o`.

Si se quiere imprimir metadatos además de los mensajes, se puede usar `-f`, por ejemplo:

Imprimir el número de partición y offset de cada mensaje:

```bash
kcat -b localhost:9092 -C -t example -o beginning -f "%p:%o %s\n"
```

Para detener el consumidor se puede pulsar `Control+C` o bien, usar `-e`.
