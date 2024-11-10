# Usando `kcat` para demostrar el funcionamiento de Kafka

## Setup

Aparte de instalar `kcat`, yo me prepararía un terminal dividido en 3 paneles: 2 para consumidores y 1 para productor.

## Ejecutar productor

```
kcat -b localhost:9092 -P -t topic-name
```

Tras eso, se escribe el mensaje y se pulsa `Control+D`.

A partir de ahí, cada pulsación de intro se enviará como un evento nuevo al topic.

En algún momento puede interesarte para hacer alguna prueba usar 

```
kcat -b localhost:9092 -P -t topic-name -p 0
```

Eso fuerza a enviar todos los eventos a la partición 0.

## Ejecutar consumidores sin consumer group

```
kcat -b localhost:9092 -C -t topic-name
```

Si lanzas eso en las 2 terminales, verás que los mensajes que envíes desde el productor llegan a la vez* a los dos
consumidores.

Se puede usar la opción `-f "[%p]%o - %s\n"` para imprimir la partición y el offset de cada evento.

## Ejecutar consumidores con consumer group

1. Se prepara el setup pero se lanza únicamente un consumidor en uno de los terminales
    ```
    kcat -b localhost:9092 -G group1 topic-name
    ```
    Con ésto, en los mensajes de "depuración" que comienzan con `%`, se verá que se produce un rebalanceo del consumer group
    y que a éste cliente se le asignarán todas las particiones disponibles.

1. Se envían algunos mensajes desde el productor, suficientes para que le lleguen mensajes por las diferentes particiones.
1. Tras eso, se lanza un segundo consumidor en el mismo grupo
    ```
    kcat -b localhost:9092 -G group1 topic-name
    ```
    Con ésto, los mensajes de depuración mostrarán que se ha hecho un rebalanceo y que ahora se han asignado particiones a ambos programas.
1. Se vuelven a enviar mensajes, observándose que en ningún caso se envía el mismo mensaje a los dos clientes.


