import os
from testar_ping import testar_ping
from validar_ip import validar_ip

def processar_lista(caminho_arquivo: str) -> None:
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo {caminho_arquivo} não foi encontrado.")
        return

    with open(caminho_arquivo, "r", encoding="utf-8") as file:
        hosts = [linha.strip() for linha in file if linha.strip()]

    print("=" * 55)
    print(f"{'HOST':<20} | {'IP VÁLIDO?':<12} | {'STATUS'}")
    print("=" * 55)

    for host in hosts:
        ip_valido = "Sim" if validar_ip(host) else "Não/Domínio"
        status = "ONLINE" if testar_ping(host) else "OFFLINE"
        print(f"{host:<20} | {ip_valido:<12} | {status}")

    print("=" * 55)