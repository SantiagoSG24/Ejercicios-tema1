import sys

def descomponer_ip(ip):
    octetos = ip.split('.')
    for i, octeto in enumerate(octetos, start=1):
        print(f"Octeto {i}: {octeto}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python Ejercicio5.py <dirección IP>")
    else:
        direccion_ip = sys.argv[1]
        descomponer_ip(direccion_ip)