import os
import multiprocessing

def child_process():
    print(f"Child process PID : {multiprocessing.current_process().pid}")
    os.system("java -jar Lavalink.jar")
