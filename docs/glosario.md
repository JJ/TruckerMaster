# Glosario del dominio
Este documento recoge términos comunes del dominio de TruckerMaster para aclarar términos del dominio en lo que respecta a resolver el problema de los usuarios. 
Las definiciones servirán para analizar los problemas descritos en las historias de usuario y modelar el dominio mediante DDD.

## Términos del dominio
| Término | Definición | 
|:----------|:-------|
| Camionero | Persona que realiza los viajes gestionados por la cooperativa.| 
| Oficina | Parte de la cooperativa encargada de gestionar los viajes y asignarlos a los camioneros. | 
| Destinatario | Empresa o entidad que recibe los productos que son transportados. | 
| Viaje | Servicio que debe hacer un camionero desde un origen a un destino para transportar una determinada mercancía. | 
| Asignación de viaje | Relación por la que un viaje queda ya asociado al camionero que realizará ese viaje. | 
| Criterio de asignación | Reglas por las cuáles se va a decidir qué camionero recibe cada viaje. | 
| Destino | Lugar al que se debe transportar la mercancía. | 
| Distancia del viaje  | Kilómetros del recorrido que debe realizar el camionero. | 
| Rentabilidad del viaje | 	Beneficio económico que da un único viaje. Aún no está especificado cómo se va a calcular (ver #81). | 
| Tarifa de transporte | Importe que paga el destinatario por transportar su mercancía. Es más alta en la mercancía especial (HU_04). |
| Tipo de mercancía | Clasificación de los productos transportados que puede determinar requisitos especiales en el viaje. Como pueden ser: especial (productos frágiles y de entrega urgente, como los insumos médicos de la HU_04) y normal (el resto de mercancías).|
| Urgencia de entrega | Grado de prioridad de una entrega. Puede ser un envío urgente o que no corra prisa. |
| Experiencia del camionero | Años que lleva trabajando como camionero. Es el único criterio que se tiene en cuenta para saber si un camionero puede hacer viajes con mercancía especial. |   
| Historial de viajes | Registro de los viajes realizados por un camionero. |
| Ganancias del camionero | Suma de lo que ha ganado un camionero con todos sus viajes en un mes. Se diferencia de la rentabilidad del viaje en que esta es de un solo viaje, mientras que las ganancias son el total acumulado del camionero. |
| Disponibilidad del camionero | Situación en la que un camionero puede incorporarse al proceso de asignación de nuevos viajes o no. Puede estar disponible en terminal o en casa y no disponible. |
