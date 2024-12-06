import sys
from app_notificacion.views import consumir_mensajes

if __name__ == '__main__':
    try:
        consumir_mensajes()
    except KeyboardInterrupt:
        print("\nConsumo de mensajes detenido manualmente.")
        sys.exit(0)
    except Exception as e:
        print(f"Error crítico al consumir mensajes: {e}")
        sys.exit(1)
