import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
from mutagen.easyid3 import EasyID3

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def selecionar_pasta():
    pasta = filedialog.askdirectory(title="SELECIONE O DIRETÓRIO!")
    if pasta:
        entry_pasta.delete(0, ctk.END)
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

    arquivos = os.listdir(pasta)

    if modo == "GERAL":
        nome = entry_nome.get().strip()
        if not nome:
            messagebox.showwarning("Atenção", "Informe um nome universal.")
            return
        arquivos.sort(key=lambda f: obter_faixa(os.path.join(pasta, f)) if f.lower().endswith('.mp3') else 9999)
        for count, arquivo in enumerate(arquivos, start=1):
            ext = os.path.splitext(arquivo)[1]
            novo_nome = f"{nome} {count:02d}{ext}"
            os.rename(os.path.join(pasta, arquivo), os.path.join(pasta, novo_nome))
        messagebox.showinfo("Sucesso", "Arquivos renomeados com sucesso!")

    elif modo == "0":
        for arquivo in arquivos:
            caminho_antigo = os.path.join(pasta, arquivo)
            if os.path.isfile(caminho_antigo):
                nome, ext = os.path.splitext(arquivo)
                if " " in nome:
                    prefixo, sufixo = nome.rsplit(" ", 1)
                    if sufixo.isdigit():
                        sufixo = sufixo.zfill(3)
                        novo_nome = f"{prefixo} {sufixo}{ext}"
                        caminho_novo = os.path.join(pasta, novo_nome)
                        os.rename(caminho_antigo, caminho_novo)
        messagebox.showinfo("Sucesso", "Números atualizados com zero à esquerda!")

    elif modo == "UPPER":
        for arquivo in arquivos:
            caminho = os.path.join(pasta, arquivo)
            if os.path.isfile(caminho):
                nome, ext = os.path.splitext(arquivo)
                novo_nome = f"{nome.upper()}{ext}"
                os.rename(caminho, os.path.join(pasta, novo_nome))
        messagebox.showinfo("Sucesso", "Arquivos renomeados para MAIÚSCULO!")

    elif modo == "LOWER":
        for arquivo in arquivos:
            caminho = os.path.join(pasta, arquivo)
            if os.path.isfile(caminho):
                nome, ext = os.path.splitext(arquivo)
                novo_nome = f"{nome.lower()}{ext}"
                os.rename(caminho, os.path.join(pasta, novo_nome))
        messagebox.showinfo("Sucesso", "Arquivos renomeados para minúsculo!")

    elif modo == "MISTO":
        for arquivo in arquivos:
            caminho = os.path.join(pasta, arquivo)
            if os.path.isfile(caminho):
                nome, ext = os.path.splitext(arquivo)
                novo_nome = f"{nome.capitalize()}{ext}"
                os.rename(caminho, os.path.join(pasta, novo_nome))
        messagebox.showinfo("Sucesso", "Arquivos com apenas a primeira letra maiúscula!")

def atualizar_visibilidade_nome_universal():
    if var_modo.get() == "GERAL":
        frame_nome.pack(pady=10)
        btn_renomear.pack(pady=20)
    else:
        frame_nome.pack_forget()
        btn_renomear.pack(pady=20)

root = ctk.CTk()
root.title("RENOMEADOR DE ARQUIVOS")
root.geometry("900x600")

footer = ctk.CTkLabel(root, text="APP CRIADO PELO VILHALVA\nGITHUB: @VILHALVA", fg_color="gray", height=40)
footer.pack(side=ctk.BOTTOM, fill=ctk.X)

ctk.CTkLabel(root, text="SELECIONE O DIRETÓRIO:").pack(pady=10)
entry_pasta = ctk.CTkEntry(root, width=600)
entry_pasta.pack()

btn_pasta = ctk.CTkButton(root, text="SELECIONAR", command=selecionar_pasta)
btn_pasta.pack(pady=10)

var_modo = ctk.StringVar(value="GERAL")

frame_radios = ctk.CTkFrame(root)
frame_radios.pack(pady=10)

radios = [("GERAL", "GERAL"), ("0", "0"), ("UPPER", "UPPER"), ("LOWER", "LOWER"), ("MISTO", "MISTO")]
for texto, valor in radios:
    ctk.CTkRadioButton(frame_radios, text=texto, variable=var_modo, value=valor, command=atualizar_visibilidade_nome_universal).pack(side=ctk.LEFT, padx=10)

frame_nome = ctk.CTkFrame(root)
ctk.CTkLabel(frame_nome, text="NOME UNIVERSAL:").pack()
entry_nome = ctk.CTkEntry(frame_nome, width=300)
entry_nome.pack()

if var_modo.get() == "GERAL":
    frame_nome.pack(pady=10)

btn_renomear = ctk.CTkButton(root, text="RENOMEAR", command=executar_renomeacao, height=30, width=100)
btn_renomear.pack(pady=20)

root.mainloop()
