# Glosario del dominio
Este documento recoge términos comunes del dominio de TruckerMaster para establecer un lenguaje compartido entre los compañeros del proyecto. 
Las definiciones servirán para analizar los problemas descritos en las historias de usuario y modelar el dominio mediante DDD.

## Términos del dominio
| Término | Definición | 
|:----------|:------:|
| Camionero | Persona que realiza los viajes gestionados por la cooperativa.| 
| Oficina | Parte de la cooperativa encargada de gestionar los viajes y asignarlos a los camioneros. | 
| Destinatario | Empresa o entidad que recibe los productos que osn transportados. | 
| Viaje | Servicio que debe hacer un camionero desde un origen a un destino para transportar una determinada mercancía. | 
| Asignación de viaje | Relación por la que un viaje queda ya asociado al camionero que realizará ese viaje. | 
| Criterio de asignación | Reglas por las cuáles se va a decidir qué camionero recibe cada viaje. | 
| Destino | Lugar al que se debe transportar la mercancía. | 
| Distancia del viaje  | Distancia asociada al recorrido que debe realizar el camionero. | 
| Rentabilidad del viaje | Beneficio económico que da cada viaje, su cálculo se debe hacer con respecto a los beneficios del proyecto. | 
| Tarifa de transporte | Importe que se cobra por hacer un servicio de transporte. |
| Tipo de mercancía | Clasificación de los productos transportados que puede determinar requisitos especiales en el viaje.|
| Urgencia de entrega | Grado de prioridad de una entrega. |
| Experiencia del camionero | Experiencia de un camionero para realizar determinados viajes o transportar ciertas mercancías. |   
| Historial de viajes | Registro de los viajes realizados por un camionero. |
| Ganancias del camionero | Información económica asociada a los viajes de cada camionero. |
| Disponibilidad del camionero | Situación en la que un camionero puede incorporarse al proceso de asignación de nuevos viajes. |
| Modelo del dominio | Representación de los conceptos, relaciones y reglas del problema. |
| Entidad | Objeto del dominio cuya identidad permite distinguirlo de otros objetos del mismo tipo. |
| Objeto de valor | Objeto definido por sus atributos y valores, sin identidad propia dentro del modelo. |