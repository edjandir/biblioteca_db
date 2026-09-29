import subprocess
import sys

def limpa_tela():
    if sys.platform == "win32":
        subprocess.run(['cmd', '/c', 'cls'])
    else:
        subprocess.run(['clear'])