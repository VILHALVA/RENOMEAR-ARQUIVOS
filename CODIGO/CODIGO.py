import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import re
import ctypes
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
        self.var_ordem = ctk.StringVar(value="NOME")
        self.var_crescente = ctk.BooleanVar(value=True)
        self.var_zeros = ctk.IntVar(value=1)

        self.backup_nomes = []  

        self.label_dir = ctk.CTkLabel(root, text="RENOMEADOR DE ARQUIVOS", font=("Arial", 32, "bold"))
        self.label_dir.pack(pady=10)
        
        self.entry_pasta = ctk.CTkEntry(root, width=600, placeholder_text="SELECIONE O DIRETÓRIO")
        self.entry_pasta.pack(pady=10)
        self.btn_pasta = ctk.CTkButton(root, text="SELECIONAR", command=self.selecionar_pasta)
        self.btn_pasta.pack(pady=10)

        self.frame_radios = ctk.CTkFrame(root)
        self.frame_radios.pack(pady=10)
        modos = [("GERAL", "GERAL"), ("0", "0"), ("UPPER", "UPPER"), ("LOWER", "LOWER"), ("MISTO", "MISTO")]
        for texto, valor in modos:
            ctk.CTkRadioButton(self.frame_radios, text=texto, variable=self.var_modo, value=valor,
                               command=self.atualizar_visibilidade_componentes).pack(side=ctk.LEFT, padx=10)

        self.frame_ordem = ctk.CTkFrame(root)
        ordens = [("NOME", "NOME"), ("TÍTULO", "TITULO"), ("NÚMERO", "NUMERO"),
                  ("CRIAÇÃO", "CRIACAO"), ("MODIFICAÇÃO", "MODIFICACAO")]
        for texto, valor in ordens:
            ctk.CTkRadioButton(self.frame_ordem, text=texto, variable=self.var_ordem, value=valor).pack(side=ctk.LEFT, padx=10)

        self.frame_switch = ctk.CTkFrame(root)
        self.switch_ordem = ctk.CTkSwitch(
            self.frame_switch,
            text="CRESCENTE",
            variable=self.var_crescente,
            command=self.atualizar_switch_estilo,
            onvalue=True,
            offvalue=False,
            switch_width=40,
            switch_height=20,
            progress_color="blue"
        )
        self.switch_ordem.pack()

        self.frame_nome = ctk.CTkFrame(root)
        ctk.CTkLabel(self.frame_nome, text="NOME UNIVERSAL:").pack()
        self.entry_nome = ctk.CTkEntry(self.frame_nome, width=300)
        self.entry_nome.pack()

        self.var_zeros = ctk.IntVar(value=3)  
        self.frame_zeros = ctk.CTkFrame(root)
        self.label_zeros = ctk.CTkLabel(self.frame_zeros, text=f"QUANTIDADE: {self.var_zeros}")
        
        self.label_zeros.pack(pady=5)
        self.slider_zeros = ctk.CTkSlider(
            self.frame_zeros,
            from_=1,
            to=9,
            number_of_steps=8,
            variable=self.var_zeros,
            command=self.atualizar_label_zeros
        )
        self.slider_zeros.pack(padx=20)

        self.btn_renomear = ctk.CTkButton(root, text="RENOMEAR", command=self.executar_renomeacao)
        self.btn_renomear.pack(pady=10)

        self.btn_resetar = ctk.CTkButton(root, text="RESETAR", command=self.resetar_nomes)
        self.btn_resetar.pack(pady=0)

        self.footer = ctk.CTkLabel(root, text="APP CRIADO PELO VILHALVA\nGITHUB: @VILHALVA", fg_color="gray", height=40)
        self.footer.pack(side=ctk.BOTTOM, fill=ctk.X)

        self.atualizar_switch_estilo()
        self.atualizar_visibilidade_componentes()

    def atualizar_switch_estilo(self):
        if self.var_crescente.get():
            self.switch_ordem.configure(text="CRESCENTE", progress_color="blue")
        else:
            self.switch_ordem.configure(text="DESCRESCENTE", progress_color="gray")

    def atualizar_label_zeros(self, valor):
        self.label_zeros.configure(text=f"QUANTIDADE: {int(float(valor))}")

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

    def obter_titulo(self, caminho):
        try:
            audio = EasyID3(caminho)
            titulo = audio.get("title", [None])[0]
            return titulo or ""
        except Exception:
            return ""

    def ordenar_arquivos(self, arquivos, pasta):
        criterio = self.var_ordem.get()
        reverso = not self.var_crescente.get()

        if criterio == "NOME":
            arquivos.sort(reverse=reverso)
        elif criterio == "CRIACAO":
            arquivos.sort(key=lambda f: os.path.getctime(os.path.join(pasta, f)), reverse=reverso)
        elif criterio == "MODIFICACAO":
            arquivos.sort(key=lambda f: os.path.getmtime(os.path.join(pasta, f)), reverse=reverso)
        elif criterio == "NUMERO":
            arquivos.sort(key=lambda f: self.obter_faixa(os.path.join(pasta, f)), reverse=reverso)
        elif criterio == "TITULO":
            arquivos.sort(key=lambda f: self.obter_titulo(os.path.join(pasta, f)).lower(), reverse=reverso)

        return arquivos

    def executar_renomeacao(self):
        self.backup_nomes.clear()
        modo = self.var_modo.get()
        pasta = self.entry_pasta.get().strip()

        if not pasta or not os.path.isdir(pasta):
            messagebox.showerror("Erro", "Por favor, selecione um diretório válido.")
            return

        arquivos = [f for f in os.listdir(pasta) if not is_oculto_ou_sistema(os.path.join(pasta, f))]

        if modo == "GERAL":
            nome = self.entry_nome.get().strip()
            padrao = re.match(r"^(.*?)(\d+)$", nome)
            arquivos = self.ordenar_arquivos(arquivos, pasta)

            if padrao:
                prefixo = padrao.group(1).strip()
                numero_inicial = int(padrao.group(2))
                casas_decimais = len(padrao.group(2))

                for i, arquivo in enumerate(arquivos):
                    ext = os.path.splitext(arquivo)[1]
                    numero_atual = str(numero_inicial + i).zfill(casas_decimais)
                    novo_nome = f"{prefixo} {numero_atual}{ext}" if prefixo else f"{numero_atual}{ext}"
                    self.backup_nomes.append((novo_nome, arquivo))
                    os.rename(os.path.join(pasta, arquivo), os.path.join(pasta, novo_nome))
            else:
                for count, arquivo in enumerate(arquivos, start=1):
                    ext = os.path.splitext(arquivo)[1]
                    novo_nome = f"{nome} {count:02d}{ext}" if nome else f"{count:02d}{ext}"
                    self.backup_nomes.append((novo_nome, arquivo))
                    os.rename(os.path.join(pasta, arquivo), os.path.join(pasta, novo_nome))

            messagebox.showinfo("Sucesso", "Arquivos renomeados com sucesso!")

        elif modo == "0":
            qtd_zeros = self.var_zeros.get()
            renomeado = False

            for i, arquivo in enumerate(arquivos, start=1):
                caminho_antigo = os.path.join(pasta, arquivo)
                if os.path.isfile(caminho_antigo):
                    nome, ext = os.path.splitext(arquivo)
                    novo_nome = None

                    if nome.isdigit():
                        if len(nome) >= qtd_zeros:
                            continue  
                        novo_nome = f"{nome.zfill(qtd_zeros)}{ext}"

                    elif " " in nome:
                        prefixo, sufixo = nome.rsplit(" ", 1)
                        if sufixo.isdigit():
                            if len(sufixo) >= qtd_zeros:
                                continue
                            sufixo = sufixo.zfill(qtd_zeros)
                            novo_nome = f"{prefixo} {sufixo}{ext}"

                    if novo_nome and novo_nome != arquivo:
                        self.backup_nomes.append((novo_nome, arquivo))
                        os.rename(caminho_antigo, os.path.join(pasta, novo_nome))
                        renomeado = True

            if renomeado:
                messagebox.showinfo("Sucesso", "Números atualizados com zeros à esquerda!")
            else:
                messagebox.showwarning("Aviso", f"Nenhum arquivo foi renomeado. Todos já possuem {qtd_zeros} dígitos ou mais.")

        elif modo == "UPPER":
            for arquivo in arquivos:
                caminho = os.path.join(pasta, arquivo)
                if os.path.isfile(caminho):
                    nome, ext = os.path.splitext(arquivo)
                    novo_nome = f"{nome.upper()}{ext}"
                    self.backup_nomes.append((novo_nome, arquivo))
                    os.rename(caminho, os.path.join(pasta, novo_nome))
            messagebox.showinfo("Sucesso", "Arquivos renomeados para MAIÚSCULO!")

        elif modo == "LOWER":
            for arquivo in arquivos:
                caminho = os.path.join(pasta, arquivo)
                if os.path.isfile(caminho):
                    nome, ext = os.path.splitext(arquivo)
                    novo_nome = f"{nome.lower()}{ext}"
                    self.backup_nomes.append((novo_nome, arquivo))
                    os.rename(caminho, os.path.join(pasta, novo_nome))
            messagebox.showinfo("Sucesso", "Arquivos renomeados para minúsculo!")

        elif modo == "MISTO":
            for arquivo in arquivos:
                caminho = os.path.join(pasta, arquivo)
                if os.path.isfile(caminho):
                    nome, ext = os.path.splitext(arquivo)
                    novo_nome = f"{nome.capitalize()}{ext}"
                    self.backup_nomes.append((novo_nome, arquivo))
                    os.rename(caminho, os.path.join(pasta, novo_nome))
            messagebox.showinfo("Sucesso", "Arquivos com apenas a primeira letra maiúscula!")

    def resetar_nomes(self):
        pasta = self.entry_pasta.get().strip()
        if not self.backup_nomes:
            messagebox.showwarning("Aviso", "Nenhuma renomeação recente encontrada para resetar.")
            return

        erros = []
        for novo, antigo in self.backup_nomes:
            caminho_novo = os.path.join(pasta, novo)
            caminho_antigo = os.path.join(pasta, antigo)
            if os.path.exists(caminho_novo):
                try:
                    os.rename(caminho_novo, caminho_antigo)
                except Exception as e:
                    erros.append(f"{novo} -> {antigo}: {e}")
        self.backup_nomes.clear()

        if erros:
            messagebox.showerror("Erros", "\n".join(erros))
        else:
            messagebox.showinfo("Sucesso", "Arquivos restaurados com sucesso!")

    def atualizar_visibilidade_componentes(self):
        modo = self.var_modo.get()
        self.frame_nome.pack_forget()
        self.frame_ordem.pack_forget()
        self.frame_switch.pack_forget()
        self.frame_zeros.pack_forget()

        if modo == "GERAL":
            self.frame_ordem.pack(pady=5, before=self.btn_renomear)
            self.frame_switch.pack(pady=5, before=self.btn_renomear)
            self.frame_nome.pack(pady=10, before=self.btn_renomear)
        elif modo == "0":
            self.frame_zeros.pack(pady=10, before=self.btn_renomear)
            self.atualizar_label_zeros(self.var_zeros.get())

def is_oculto_ou_sistema(path):
    if os.name == "nt":
        try:
            atributos = ctypes.windll.kernel32.GetFileAttributesW(str(path))
            if atributos == -1:
                return False
            FILE_ATTRIBUTE_HIDDEN = 0x2
            FILE_ATTRIBUTE_SYSTEM = 0x4
            return bool(atributos & (FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_SYSTEM))
        except Exception:
            return False
    else:
        return os.path.basename(path).startswith(".")

if __name__ == "__main__":
    root = ctk.CTk()
    app = RenomearArquivos(root)
    root.mainloop()
