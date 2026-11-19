# Investigación sobre las preferencias de los camioneros según sus condiciones económicas y físicas

> Este documento complementa a restricciones.md, que recoge las restricciones laborales (tiempo, capacitación y calendario) del convenio de Granada. Aquí nos centramos en la duración de los viajes y en cuánto cobra el conductor.

## 1. Duración de los viajes

La duración depende de la distancia, del tipo de transporte y de las condiciones de trabajo del conductor. Distinguimos:

| Tipo de viaje | Ámbito | Duración orientativa |
|---|---|---|
| Corto | Misma provincia o localidades cercanas | Unas horas (dentro de una jornada) |
| Nacional | Entre provincias de España | De 1 a 3 días, según la distancia |
| Internacional | Fuera de España | Varios días; un viaje a Reino Unido ronda los 8-10 días ida y vuelta (estimación, ver más abajo) |

### Normas aplicables y de dónde sale cada cifra

Las cifras de conducción y descanso no son todas de la misma norma, por eso a veces no coinciden con [restricciones.md](restricciones.md):

| Concepto | Valor | Norma de origen |
|---|---|---|
| Conducción diaria | 9 h (10 h, dos veces por semana) | Normativa europea (Reglamento (CE) 561/2006) |
| Pausa | 45 min tras 4 h 30 min de conducción | Normativa europea |
| Descanso diario | 11 h | Normativa europea |
| Conducción semanal máxima | 56 h | Normativa europea |
| Descanso entre jornadas | 12 h | Convenio colectivo de Granada |

La norma europea regula el tiempo de conducción y descanso. El convenio de Granada regula la jornada laboral (incluye esperas, carga y descarga) y es más exigente. Para el proyecto aplicamos siempre el límite más restrictivo, es decir, 12 h entre jornadas.

Fuente:
- Comisión Europea: [Driving time and rest periods](https://transport.ec.europa.eu/transport-modes/road/social-provisions/driving-time-and-rest-periods_en)
- [Convenio Colectivo de Transporte de Mercancías por Carretera de Granada](https://ccoo.app/convenio/convenio-colectivo-transporte-de-mercancias-por-carretera-de-granada/)

## 2. Cómo se calcula el dinero que recibe el camionero

El dinero depende de la categoría profesional, el convenio aplicable, los complementos salariales y los desplazamientos. En Granada, el Convenio Colectivo de Transporte de Mercancías por Carretera 2024-2026.

Conceptos que influyen:

- Salario base: según la categoría profesional.
- Dietas: compensan comida y alojamiento en los desplazamientos.
- Complementos salariales: según el vehículo, la distancia o las características del trabajo.
- Antigüedad.

Según las tablas salariales de 2026 del convenio de Granada:

| Categoría | Salario base diario |
|---|---:|
| Conductor mecánico | 40,67 € |
| Conductor | 40,29 € |
| Conductor de mercancías peligrosas | 45,16 € |

Complementos:

- Vehículos de más de 7.500 kg: 249,25 € mensuales.
- Largo recorrido: 117,90 € mensuales.

Estos importes dependen de que se cumplan las condiciones del convenio.

Fuente:
- [Convenio Colectivo de Transporte de Mercancías por Carretera de Granada](https://ccoo.app/convenio/convenio-colectivo-transporte-de-mercancias-por-carretera-de-granada/)
- [Tablas salariales y condiciones del convenio de Granada](https://truckclock.com/es/convenios/granada/)

## 3. Dietas por desplazamiento

| Tipo de desplazamiento | Dieta completa |
|---|---:|
| Nacional | 43,25 € |
| Internacional | 60,00 € |

En los desplazamientos internacionales, el alojamiento corre a cargo de la empresa según el convenio. Dos conductores con el mismo salario base pueden cobrar cantidades distintas según los desplazamientos que hagan.

Fuente:
- [Convenio Colectivo de Transporte de Mercancías por Carretera de Granada](https://ccoo.app/convenio/convenio-colectivo-transporte-de-mercancias-por-carretera-de-granada/)

## 4. Coste de los viajes para la empresa

Conviene distinguir lo que cobra el camionero de lo que le cuesta el viaje a la empresa. El Ministerio de Transportes publica un Observatorio de Costes del Transporte de Mercancías por Carretera, que incluye combustible, personal de conducción, mantenimiento, seguros, neumáticos, amortización, peajes y otros gastos, por tipo de vehículo (incluidas cisternas). Sirve para estimar el coste de un transporte, no lo que cobra el conductor por viaje.

Fuente:
- [Observatorio de Costes del Transporte de Mercancías por Carretera – Ministerio de Transportes](https://publicaciones.transportes.gob.es/observatorio-de-costes-del-transporte-de-mercancias-por-carretera-abril-2026)

## 5. Conclusión y aplicación al proyecto

Las preferencias de los camioneros dependen de factores económicos y físicos. Por ejemplo, un conductor puede preferir viajes cortos para pasar más tiempo en casa, y otro, viajes internacionales por las dietas y complementos.

Parte de la información ya está en el modelo: la distancia (distancia_km), la disponibilidad (Disponibilidad) y la preferencia por viajes cortos o largos (Preferencias.distancia_max_km). Lo que sería nuevo y convendría almacenar es:

- Duración estimada del viaje.
- Si el viaje es nacional o internacional.
- Salario y complementos del conductor.
- Dietas que le corresponden.
- Preferencia por pasar más tiempo en casa (relacionada con el descanso en domicilio de [restricciones.md](restricciones.md)).

Así se pueden tener en cuenta tanto las condiciones económicas como las personales al asignar un viaje.