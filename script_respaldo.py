"""
Crear backup
Autor : Jesus Parra
Versión 1.0
Fecha 2016-12-18
Versión de Python 3.4.2

"""

# Librerias 
import sys, subprocess, datetime, os

# Definiciones de fecha hoy y ayer
hoy = datetime.date.today()
dia_hoy = str(hoy).replace("-","")
ayer = hoy + datetime.timedelta(days = -1)
dia_ayer = str(ayer).replace("-","")

# Los respaldos se hacen de Lunes a Viernes para este escenario.
esLunes = hoy.strftime("%A") == "Monday"
if esLunes is True:
   ayer = hoy + datetime.timedelta(days = -3)
   dia_ayer = str(ayer).replace("-","")

# Definicion de rutas
ruta_respaldos = "D:\\Respaldos_Servidor\\saint\\"
ruta_historicos = "D:\\Respaldos_Servidor\\saint\\historicos\\"
ruta_script = "C:\\ntbackup\\"

# Definicion de la sentencia para respaldar
script_ntbackup = " \"@" + ruta_script + sys.argv[1] + "\""
parametros = " /n \"Respaldo diario\" /d \"Respaldo diario %date% %time%\" /v:yes /r:no /rs:no /hc:off /m normal /j \"Respaldo de la aplicacin Saint\" /l:s /f "
nombre_backup = ("\"" + ruta_respaldos + "FULL" + sys.argv[2] + "_" + dia_hoy + ".bkf\"")
sentenciaBackup = "C:\\Windows\\system32\\NTBACKUP.EXE backup" + script_ntbackup + parametros + nombre_backup


# Definicion de la sentencia para comprimir con password
password = "J-08517146-0"
sentenciaZip = "7z a -tzip " + ruta_historicos + sys.argv[2] + "_" + dia_ayer + ".zip " + ruta_respaldos + "FULL"  + sys.argv[2] +  "_" + dia_ayer + ".* -p" + password 

# Definicion del comando Borrar
sentenciaBorrar = "DEL /q " + ruta_respaldos + "FULL"  + sys.argv[2] +  "_" + dia_ayer + ".*"

# Definiendo el archivo log
nombreLog = ruta_respaldos + "FULL"  + sys.argv[2] + "_" + dia_hoy + ".txt"
log = open(nombreLog, "a")

existeRespaldo = os.path.isfile(ruta_respaldos + "FULL"  + sys.argv[2] + "_" + dia_ayer + ".bkf")    
   
if (existeRespaldo is True):
    log.write(str(hoy) + " Comprimiendo " + "FULL" + sys.argv[2] + "_" + dia_ayer + ".bkf \n")
    resultado = subprocess.call (sentenciaZip, shell=True)
else:
    log.write(str(hoy) + " No existe el backup FULL"  + sys.argv[2] + "_" + dia_ayer + ".bkf para comprimir \n")
    resultado = 0
    
if (resultado is 0):
    log.write(str(hoy) + " Creando el backup FULL"  + sys.argv[2] + "_" + dia_hoy + ".bkf \n")
    resultado = subprocess.call (sentenciaBackup, shell=True)

if (existeRespaldo is False):
    log.write(str(hoy) + " El backup FULL"  + sys.argv[2] + "_" + dia_ayer + ".bkf no existe para borrar \n")
elif (resultado is 0 and existeRespaldo is True):
    resultado = subprocess.call (sentenciaBorrar, shell=True)
    log.write(str(hoy) + " El backup FULL"  + sys.argv[2] + "_" + dia_ayer + ".bkf fue borrado \n")
log.write("\n")
log.write("Para mas detalles, busque en este directorio : \n")
log.write("\n")
log.write("C:\\Documents and Settings\\Administrator\\Local Settings\\Application Data\\Microsoft\\Windows NT\\NTBackup\\data\\ \n")
log.close()
    
    



