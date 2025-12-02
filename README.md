# Actividad PSP-DAM-ACTEVA02B: Simulación de Gestor de Impresión

## Descripción

Esta actividad consiste en desarrollar un programa en Python que simula un **gestor de impresión** con varios usuarios. Cada usuario genera trabajos de impresión que se procesan de manera concurrente utilizando **multiprocesos** y **semaforos** para controlar el acceso a la impresora.

El objetivo principal es garantizar que solo un proceso pueda imprimir al mismo tiempo, evitando conflictos y mostrando un registro de los trabajos completados.

---

## Funcionamiento del Programa

1. **Usuarios (procesos):**
   - Cada usuario representa un trabajador que quiere imprimir varios documentos.
   - Cada usuario genera entre 2 y 4 trabajos aleatorios.
   - Antes de imprimir, solicita acceso a la impresora mediante un **semaforo**.
   - Una vez que termina la impresión, registra el trabajo en la lista compartida.

2. **Gestor de impresión (proceso principal):**
   - Crea un **semaforo binario**, asegurando que solo un usuario imprime a la vez.
   - Lanza los procesos de los usuarios y espera a que todos finalicen.
   - Al finalizar, muestra un **resumen de todos los trabajos impresos**.

---

## Estructura del Código

- **usuario(nombre, semaforo, cola_trabajos):**  
  Función que simula el comportamiento de un usuario. Controla la preparación de trabajos, acceso a la impresora y registro de resultados.

- **gestor_impresion():**  
  Función que inicia los procesos de usuarios, gestiona el semáforo y muestra el resumen final.

- **Proceso principal:**  
  Llama a `gestor_impresion()` si el archivo se ejecuta directamente.

---

## Tecnologías y Herramientas

- Python 3.x
- Módulo `multiprocessing` para crear procesos concurrentes.
- Semáforos (`Semaphore`) para controlar el acceso a recursos compartidos.
- `Manager().list()` para mantener una lista compartida entre procesos.

---

## Ejecución

1. Clonar el repositorio o descargar el archivo `gestor_impresor.py`.
2. Abrir la terminal en la carpeta del proyecto.
3. Ejecutar el programa:

```bash
python gestor_impresor.py
