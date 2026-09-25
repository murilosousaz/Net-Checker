import platform
import subprocess

def testar_ping(host: str) -> bool:
    parametro = "-n" if platform.system().lower() == "windows" else "-c"
    comando = ["ping", parametro, "1", host]

    try:
        resultado = subprocess.run(
            comando,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=3
        )
        return resultado.returncode == 0
    except subprocess.TimeoutExpired:
        return False