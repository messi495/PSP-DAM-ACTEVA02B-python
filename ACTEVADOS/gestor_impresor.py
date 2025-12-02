import multiprocessing
import time
import random


# ============================================================
# Clase/Proceso: Usuario
# ============================================================
# Cada usuario simula un trabajador que quiere imprimir varios
# documentos. Usa el semáforo para acceder a la impresora.
def usuario(nombre, semaforo, cola_trabajos):
    """
    nombre: identificador del usuario (ej. 'Usuario 1')
    semaforo: control de acceso a la impresora
    cola_trabajos: lista compartida donde se añaden trabajos
    """
    # Cada usuario generará entre 2 y 4 trabajos
    num_trabajos = random.randint(2, 4)

    for i in range(1, num_trabajos + 1):
        # Simula el tiempo en que prepara el trabajo
        time.sleep(random.uniform(0.5, 2))

        # Solicita acceso a la impresora
        print(f"{nombre} quiere imprimir el trabajo {i}...")

        # Intentar acceder a la impresora
        semaforo.acquire()
        try:
            print(f"{nombre} está imprimiendo el trabajo {i} 🖨️")
            # Simula el tiempo de impresión (1–3 seg)
            time.sleep(random.uniform(1, 3))
            print(f"{nombre} terminó de imprimir el trabajo {i} ✅")

            # Registrar el trabajo completado
            cola_trabajos.append((nombre, i))
        finally:
            # Libera la impresora
            semaforo.release()


# ============================================================
# Clase/Proceso: Gestor de impresión
# ============================================================
# Este proceso principal crea el semáforo, lanza a los usuarios
# y espera a que todos terminen.
def gestor_impresion():
    # Crear semáforo binario (solo 1 proceso puede imprimir)
    semaforo = multiprocessing.Semaphore(1)

    # Lista compartida entre procesos para registrar trabajos
    cola_trabajos = multiprocessing.Manager().list()

    # Crear los procesos de usuarios
    usuarios = []
    for n in range(1, 4):  # Mínimo 3 usuarios
        nombre = f"Usuario {n}"
        p = multiprocessing.Process(target=usuario, args=(nombre, semaforo, cola_trabajos))
        usuarios.append(p)

    # Iniciar los procesos
    for p in usuarios:
        p.start()

    # Esperar a que todos terminen
    for p in usuarios:
        p.join()

    # Mostrar resultados finales
    print("\nResumen de trabajos impresos:")
    for nombre, num in cola_trabajos:
        print(f" - {nombre}: trabajo {num}")

    print("\n✅ Todos los trabajos han sido impresos.")


# ============================================================
# Proceso principal
# ============================================================
if __name__ == "__main__":
    gestor_impresion()
