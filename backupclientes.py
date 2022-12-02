import os 


dir = "\\\\10.50.50.1\\backup_cli"
lista_arquivos = os.listdir(dir)
lista_datas=[]

for arquivo in lista_arquivos:
    data = os.path.getctime(f"{dir}/{arquivo}")
    lista_datas.append((arquivo,data))
    
lista_datas.sort(reverse=True)
ultimo_arquivo = lista_datas[0]
print(ultimo_arquivo[0])
