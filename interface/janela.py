import customtkinter as ctk
from tkinter import messagebox
from logica.controle_vagas import registrar_entrada, registrar_saida

class JanelaEstacionamento(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ParkControl")
        self.geometry("400x300")

        # Entrada de veículo
        self.label_tipo = ctk.CTkLabel(self, text="Tipo do veículo:")
        self.label_tipo.pack(pady=10)

        self.tipo_var = ctk.StringVar(value="carro")
        self.radio_carro = ctk.CTkRadioButton(self, text="Carro", variable=self.tipo_var, value="carro")
        self.radio_moto = ctk.CTkRadioButton(self, text="Moto", variable=self.tipo_var, value="moto")
        self.radio_carro.pack()
        self.radio_moto.pack()

        self.btn_entrada = ctk.CTkButton(self, text="Registrar Entrada", command=self.entrada_veiculo)
        self.btn_entrada.pack(pady=10)

        # Saída de veículo
        self.label_id = ctk.CTkLabel(self, text="ID do veículo:")
        self.label_id.pack(pady=10)

        self.entry_id = ctk.CTkEntry(self)
        self.entry_id.pack()

        self.btn_saida = ctk.CTkButton(self, text="Registrar Saída", command=self.saida_veiculo)
        self.btn_saida.pack(pady=10)

    def entrada_veiculo(self):
        tipo = self.tipo_var.get()
        veiculo = registrar_entrada(tipo)
        messagebox.showinfo("Entrada", f"Veículo registrado!\nID: {veiculo.vaga_id}")

    def saida_veiculo(self):
        veiculo_id = self.entry_id.get()
        try:
            valor = registrar_saida(veiculo_id)
            messagebox.showinfo("Saída", f"Veículo saiu!\nValor a pagar: R${valor}")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
