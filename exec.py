import os

pid = os.fork() #Creation du fils

if pid == 0:
    cmd = 'python calcul.py'
    a = input("Give the value of a : ");
    b = input("Give the value of b ");
    cmd = cmd + " " + a +" " + b # on ajoute les arguments neccessaire au programme
    os.system(cmd)#on lance le programme

else:
    option = os.WSTOPPED | os.WEXITED  # option
    idtype = os.P_ALL  # n'importe qu'elle pid fils
    id = pid  # le pid fils
    status = os.waitid(idtype, id, option)  # on recupere le status du fils mort
    if status.si_status == 0:  # on verifie le status du fils mort
        print("End.")
    else:
        print("Error, the program could not be launched.")