""" Script que borra todos los archivos que coinciden con el patron indicado"""
import os
import glob

#Variables de definiciones
folderFiles = 'Downloads'
queryFiles = '\RptCupon*.pdf'

#Obtengo la ruta de la carpeta Downloads
path_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), folderFiles)
#Armo la ruta con el comodín de busqueda de archivos
path_files = path_desktop + queryFiles
py_files = glob.glob(path_files)

for py_file in py_files:
    try:
        os.remove(py_file)
    except OSError as e:
        print(f"Error:{ e.strerror}")