import customtkinter as ctk
from interface.janela_user import JanelaEstacionamento
from interface.janela_adm import JanelaAdm

class JanelaInicial(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ParkControl - Bem-vindo")
        self.geometry("400x300")

        # Bloco de boas-vindas
        self.label_welcome = ctk.CTkLabel(self, text="Bem-vindo ao ParkControl!\nEscolha uma opção para continuar.", font=ctk.CTkFont(size=16))
        self.label_welcome.pack(pady=40)

        # Bloco de botões para escolher entre usuário e administrador
        self.btn_user = ctk.CTkButton(self, text="Entrar como Usuário", command=self.abrir_janela_usuario)
        self.btn_user.pack(pady=10)
        self.btn_admin = ctk.CTkButton(self, text="Entrar como Administrador", command=self.abrir_janela_adm)
        self.btn_admin.pack(pady=10)

    def abrir_janela_usuario(self):
        janela_usuario = JanelaEstacionamento()
        janela_usuario.mainloop()

    def abrir_janela_adm(self):
        janela_adm = JanelaAdm()
        janela_adm.mainloop()