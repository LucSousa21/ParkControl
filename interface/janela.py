import customtkinter as ctk
from tkinter import messagebox
from logica.controle_vagas import registrar_veiculo, liberarvaga
from logica.calculo_valor import calcular_valor

class JanelaEstacionamento(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ParkControl")
        self.geometry("900x800")

        # Entrada de veículo
        self.label_tipo = ctk.CTkLabel(self, text="Tipo do veículo:")
        self.label_tipo.pack(pady=10)

        self.tipo_var = ctk.StringVar(value="carro")
        self.radio_carro = ctk.CTkRadioButton(self, text="Carro", variable=self.tipo_var, value="carro")
        self.radio_moto = ctk.CTkRadioButton(self, text="Moto", variable=self.tipo_var, value="moto")
        self.radio_carro.pack()
        self.radio_moto.pack()

        self.label_modelo = ctk.CTkLabel(self, text="Digite o Modelo:")
        self.label_modelo.pack(pady=(10, 0)) # 10 de espaço
        self.entry_modelo = ctk.CTkEntry(self, placeholder_text="Ex: Fiat Uno", width=200)
        self.entry_modelo.pack(pady=5)

        self.label_placa = ctk.CTkLabel(self, text="Digite a Placa:")
        self.label_placa.pack(pady=(10, 0)) # 10 de espaço em cima, 0 embaixo

# O campo de entrada propriamente dito
        self.entry_placa = ctk.CTkEntry(self, placeholder_text="Ex: ABC-1234", width=200)
        self.entry_placa.pack(pady=5)

        self.btn_entrada = ctk.CTkButton(self, text="Registrar Entrada", command=self.entrada_veiculo)
        self.btn_entrada.pack(pady=10)

        # Saída de veículo
        #self.label_id = ctk.CTkLabel(self, text="ID do veículo:")
        #self.label_id.pack(pady=10)

        #self.entry_id = ctk.CTkEntry(self)
        #self.entry_id.pack()

        self.btn_saida = ctk.CTkButton(self, text="Registrar Saída", command=self.saida_veiculo)
        self.btn_saida.pack(pady=10)

    def entrada_veiculo(self):
        tipo = self.tipo_var.get()
        modelo = self.entry_modelo.get()
        placa = self.entry_placa.get()
        veiculo = registrar_veiculo(tipo, modelo, placa)
        messagebox.showinfo("Entrada", f"Veículo registrado!\nPlaca: {placa}")

    def saida_veiculo(self):
        
        placa = self.entry_placa.get()
        tipo = self.tipo_var.get()
        try:
            valor = calcular_valor(placa)
            liberarvaga(tipo,placa)
            messagebox.showinfo("Saída", f"Veículo saiu!\nValor a pagar: R${valor}")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))



