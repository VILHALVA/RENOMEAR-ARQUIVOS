import tkinter as tk
from tkinter import filedialog, messagebox
import os
from mutagen.easyid3 import EasyID3

def selecionar_pasta():
    pasta = filedialog.askdirectory(title="SELECIONE O DIRETÓRIO!")
    if pasta:
        entry_pasta.delete(0, tk.END)
        entry_pasta.insert(0, pasta)

def obter_faixa(mp3_path):
    try:
        audio = EasyID3(mp3_path)
        track = audio.get("tracknumber", [None])[0]
        if track:
            return int(track.split("/")[0])
    except Exception:
        pass
    return 9999

def executar_renomeacao():
    modo = var_modo.get()
    pasta = entry_pasta.get().strip()

    if not pasta or not os.path.isdir(pasta):
        messagebox.showerror("Erro", "Por favor, selecione um diretório válido.")
        return

    if modo == "GERAL":
        nome = entry_nome.get().strip()
        if not nome:
            messagebox.showwarning("Atenção", "Informe um nome universal.")
            return
        arquivos = os.listdir(pasta)
        arquivos.sort(key=lambda f: obter_faixa(os.path.join(pasta, f)) if f.lower().endswith('.mp3') else 9999)
        for count, arquivo in enumerate(arquivos, start=1):
            ext = os.path.splitext(arquivo)[1]
            novo_nome = f"{nome} {count:02d}{ext}"
            os.rename(os.path.join(pasta, arquivo), os.path.join(pasta, novo_nome))
        messagebox.showinfo("Sucesso", "Arquivos renomeados com sucesso!")

    elif modo == "0":
        for arquivo in os.listdir(pasta):
            caminho_antigo = os.path.join(pasta, arquivo)
            if os.path.isfile(caminho_antigo):
                novo_nome = '0' + arquivo
                caminho_novo = os.path.join(pasta, novo_nome)
                if caminho_antigo != caminho_novo:
                    os.rename(caminho_antigo, caminho_novo)
        messagebox.showinfo("Sucesso", "Arquivos renomeados com '0' no início!")

    elif modo == "UPPER":
        for arquivo in os.listdir(pasta):
            caminho = os.path.join(pasta, arquivo)
            if os.path.isfile(caminho):
                nome, ext = os.path.splitext(arquivo)
                novo_nome = f"{nome.upper()}{ext}"
                os.rename(caminho, os.path.join(pasta, novo_nome))
        messagebox.showinfo("Sucesso", "Arquivos renomeados para MAIÚSCULO!")

    elif modo == "LOWER":
        for arquivo in os.listdir(pasta):
            caminho = os.path.join(pasta, arquivo)
            if os.path.isfile(caminho):
                nome, ext = os.path.splitext(arquivo)
                novo_nome = f"{nome.lower()}{ext}"
                os.rename(caminho, os.path.join(pasta, novo_nome))
        messagebox.showinfo("Sucesso", "Arquivos renomeados para minúsculo!")

def atualizar_visibilidade_nome_universal():
    if var_modo.get() == "GERAL":
        frame_nome.pack(pady=10)
        btn_renomear.pack(pady=20)
    else:
        frame_nome.pack_forget()
        btn_renomear.pack(pady=20)

root = tk.Tk()
root.title("RENOMEADOR DE ARQUIVOS")
root.state("zoomed")

footer = tk.Label(root, text="APP CRIADO PELO VILHALVA\nGITHUB: @VILHALVA", bg="gray", fg="white", height=2)
footer.pack(side=tk.BOTTOM, fill=tk.X)

tk.Label(root, text="SELECIONE O DIRETÓRIO:").pack()
entry_pasta = tk.Entry(root, width=80)
entry_pasta.pack()

btn_pasta = tk.Button(root, text="SELECIONAR", command=selecionar_pasta, bg="blue", fg="white")
btn_pasta.pack(pady=5)

var_modo = tk.StringVar(value="GERAL")

frame_radios = tk.Frame(root)
frame_radios.pack(pady=5)

radios = [("GERAL", "GERAL"), ("0", "0"), ("UPPER", "UPPER"), ("LOWER", "LOWER")]
for texto, valor in radios:
    tk.Radiobutton(frame_radios, text=texto, variable=var_modo, value=valor, command=atualizar_visibilidade_nome_universal).pack(side=tk.LEFT, padx=10)

frame_nome = tk.Frame(root)
tk.Label(frame_nome, text="NOME UNIVERSAL:").pack()
entry_nome = tk.Entry(frame_nome, width=40)
entry_nome.pack()

if var_modo.get() == "GERAL":
    frame_nome.pack(pady=10)

btn_renomear = tk.Button(root, text="RENOMEAR", command=executar_renomeacao, bg="green", fg="white", height=2, width=20)
btn_renomear.pack(pady=20)

root.mainloop()
