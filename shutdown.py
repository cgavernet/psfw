import os

def shutdown():
    """Shutdown PC fro windows 7"""
    os.system("shutdown /s /t 1")

def main():
    shutdown()

main()