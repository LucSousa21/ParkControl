import customtkinter as ctk
from banco.consultar_banco import exibirVagas
from tkinter import messagebox


class JanelaAdm(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ParkControl - Administração")
        self.geometry("800x500")

        # Login
        self.label_login = ctk.CTkLabel(
            self,
            text="Bem-vindo! Faça login para acessar a administração."
        )
        self.label_login.pack(pady=20)

        self.entry_username = ctk.CTkEntry(self, placeholder_text="Username", width=200)
        self.entry_username.pack(pady=5)

        self.entry_password = ctk.CTkEntry(self, placeholder_text="Password", width=200, show="*")
        self.entry_password.pack(pady=5)

        self.btn_login = ctk.CTkButton(self, text="Login", command=self.validar_login)
        self.btn_login.pack(pady=20)

    # LOGIN
    def validar_login(self):
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()

        if username == "admin" and password == "admin123":
            messagebox.showinfo("Sucesso", "Bem-vindo, Administrador!")

            self.abrir_painel()


        else:
            messagebox.showerror("Erro", "Login inválido!")

    # PAINEL PRINCIPAL
    def abrir_painel(self):
        self.painel = ctk.CTkFrame(self)
        self.painel.pack(fill="both", expand=True, padx=10, pady=10)

        btn_carros = ctk.CTkButton(self.painel, text="Ver Carros", command=self.consultar_carros)
        btn_carros.pack(pady=10)

        btn_motos = ctk.CTkButton(self.painel, text="Ver Motos", command=self.consultar_motos)
        btn_motos.pack(pady=10)

    # TABELA 
    def mostrar_tabela(self, titulo, dados):
        janela = ctk.CTkToplevel(self)
        janela.title(titulo)
        janela.geometry("900x400")

        frame = ctk.CTkScrollableFrame(janela)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Cabeçalho
        colunas = ["ID", "Ocupada", "Vaga", "Veículo", "Placa", "Entrada"]

        for i, col in enumerate(colunas):
            label = ctk.CTkLabel(frame, text=col, font=("Arial", 12, "bold"))
            label.grid(row=0, column=i, padx=10, pady=5)

        # Linhas
        for row_index, linha in enumerate(dados, start=1):
            for col_index, valor in enumerate(linha):
                ctk.CTkLabel(frame, text=str(valor)).grid(
                    row=row_index,
                    column=col_index,
                    padx=10,
                    pady=5
                )
        

    # CARROS
    def consultar_carros(self):
        carros, motos = exibirVagas()
        self.mostrar_tabela("Vagas de Carros", carros)

    # MOTOS
    def consultar_motos(self):
        carros, motos = exibirVagas()
        self.mostrar_tabela("Vagas de Motos", motos)