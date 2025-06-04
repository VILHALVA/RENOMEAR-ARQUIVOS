import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import re
from mutagen.easyid3 import EasyID3

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class RenomearArquivos:
    def __init__(self, root):
        self.root = root
        self.root.title("RENOMEADOR DE ARQUIVOS")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")  
        self.root.resizable(True, True)

        self.var_modo = ctk.StringVar(value="GERAL")

        ctk.CTkLabel(root, text="SELECIONE O DIRETÓRIO:").pack(pady=10)
        self.entry_pasta = ctk.CTkEntry(root, width=600)
        self.entry_pasta.pack()

        self.btn_pasta = ctk.CTkButton(root, text="SELECIONAR", command=self.selecionar_pasta)
        self.btn_pasta.pack(pady=10)

        self.frame_radios = ctk.CTkFrame(root)
        self.frame_radios.pack(pady=10)

        radios = [("GERAL", "GERAL"), ("0", "0"), ("UPPER", "UPPER"), ("LOWER", "LOWER"), ("MISTO", "MISTO")]
        for texto, valor in radios:
            ctk.CTkRadioButton(self.frame_radios, text=texto, variable=self.var_modo, value=valor,
                               command=self.atualizar_visibilidade_nome_universal).pack(side=ctk.LEFT, padx=10)

        self.frame_nome = ctk.CTkFrame(root)
        ctk.CTkLabel(self.frame_nome, text="NOME UNIVERSAL:").pack()
        self.entry_nome = ctk.CTkEntry(self.frame_nome, width=300)
        self.entry_nome.pack()

        if self.var_modo.get() == "GERAL":
            self.frame_nome.pack(pady=10)

        self.btn_renomear = ctk.CTkButton(root, text="RENOMEAR", command=self.executar_renomeacao)
        self.btn_renomear.pack(pady=20)

        self.footer = ctk.CTkLabel(root, text="APP CRIADO PELO VILHALVA\nGITHUB: @VILHALVA", fg_color="gray", height=40)
        self.footer.pack(side=ctk.BOTTOM, fill=ctk.X)

    def selecionar_pasta(self):
        pasta = filedialog.askdirectory(title="SELECIONE O DIRETÓRIO!")
        if pasta:
            self.entry_pasta.delete(0, ctk.END)
            self.entry_pasta.insert(0, pasta)

    def obter_faixa(self, mp3_path):
        try:
            audio = EasyID3(mp3_path)
            track = audio.get("tracknumber", [None])[0]
            if track:
                return int(track.split("/")[0])
        except Exception:
            pass
        return 9999

    def executar_renomeacao(self):
        modo = self.var_modo.get()
        pasta = self.entry_pasta.get().strip()

        if not pasta or not os.path.isdir(pasta):
            messagebox.showerror("Erro", "Por favor, selecione um diretório válido.")
            return

        arquivos = os.listdir(pasta)

        if modo == "GERAL":
            nome = self.entry_nome.get().strip()
            arquivos.sort(key=lambda f: self.obter_faixa(os.path.join(pasta, f)) if f.lower().endswith('.mp3') else 9999)

            padrao = re.match(r"^(.*?)(\d+)$", nome)

            if padrao:
                prefixo = padrao.group(1).strip()
                numero_inicial = int(padrao.group(2))
                casas_decimais = len(padrao.group(2))

                for i, arquivo in enumerate(arquivos):
                    ext = os.path.splitext(arquivo)[1]
                    numero_atual = str(numero_inicial + i).zfill(casas_decimais)
                    novo_nome = f"{prefixo} {numero_atual}{ext}" if prefixo else f"{numero_atual}{ext}"
                    os.rename(os.path.join(pasta, arquivo), os.path.join(pasta, novo_nome))
            else:
                for count, arquivo in enumerate(arquivos, start=1):
                    ext = os.path.splitext(arquivo)[1]
                    novo_nome = f"{nome} {count:02d}{ext}" if nome else f"{count:02d}{ext}"
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

    def atualizar_visibilidade_nome_universal(self):
        if self.var_modo.get() == "GERAL":
            self.frame_nome.pack_forget()
            self.frame_nome.pack(pady=10, before=self.btn_renomear)
        else:
            self.frame_nome.pack_forget()

if __name__ == "__main__":
    root = ctk.CTk()
    app = RenomearArquivos(root)
    root.mainloop()

