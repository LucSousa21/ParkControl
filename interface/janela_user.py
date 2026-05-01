import customtkinter as ctk
import re
from tkinter import messagebox
from logica.controle_vagas import registrar_veiculo, liberarvaga, obter_placa_tratada
from logica.calculo_valor import calcular_valor

# Janela principal do sistema de estacionamento
class JanelaEstacionamento(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Bloco de configuração da janela
        self.title("ParkControl")
        self.geometry("900x800")

        # Bloco de entrada de dados
        self.label_tipo = ctk.CTkLabel(self, text="Tipo do veículo:")
        self.label_tipo.pack(pady=10)

        # Variável para armazenar o tipo selecionado
        self.tipo_var = ctk.StringVar(value="carro")
        self.radio_carro = ctk.CTkRadioButton(self, text="Carro", variable=self.tipo_var, value="carro")
        self.radio_moto = ctk.CTkRadioButton(self, text="Moto", variable=self.tipo_var, value="moto")
        self.radio_carro.pack()
        self.radio_moto.pack()

        # Bloco de entrada de dados para modelo
        self.label_modelo = ctk.CTkLabel(self, text="Digite o Modelo:")
        self.label_modelo.pack(pady=(10, 0)) # 10 de espaço
        self.entry_modelo = ctk.CTkEntry(self, placeholder_text="Ex: Fiat Uno", width=200)
        self.entry_modelo.pack(pady=5)

        # Bloco de entrada de dados para placa
        self.label_placa = ctk.CTkLabel(self, text="Digite a Placa:")
        self.label_placa.pack(pady=(10, 0)) # 10 de espaço em cima, 0 embaixo
        self.entry_placa = ctk.CTkEntry(self, placeholder_text="Ex: ABC1234", width=200)
        self.entry_placa.pack(pady=5)

        # Bloco de botões para registrar entrada e saída
        self.btn_entrada = ctk.CTkButton(self, text="Registrar Entrada", command=self.entrada_veiculo)
        self.btn_entrada.pack(pady=10)
        self.btn_saida = ctk.CTkButton(self, text="Registrar Saída", command=self.saida_veiculo)
        self.btn_saida.pack(pady=10)


    # Função para registrar a entrada do veículo
    def entrada_veiculo(self):
        tipo = self.tipo_var.get()
        modelo = self.entry_modelo.get()
        placa = self.entry_placa.get()

        # Verificação simples para não enviar campos em branco
        if not modelo or not placa:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
            return

        try:
            # 1. Tenta formatar a placa
            placa_formatada = obter_placa_tratada(placa)
            
            # 2. Tenta salvar no banco de dados
            registrar_veiculo(tipo, modelo, placa_formatada)
            
            messagebox.showinfo("Entrada", f"Veículo {tipo} registrado com sucesso!\nPlaca: {placa_formatada}")

            # Limpa os campos após o registro com sucesso
            self.entry_modelo.delete(0, 'end')
            self.entry_placa.delete(0, 'end')

        except ValueError as e:
            # Captura erro de placa inválida ou tipo inválido
            messagebox.showerror("Erro de Validação", str(e))
        except Exception as e:
            # Captura o erro do banco de dados (placa duplicada) sem fechar o programa
            messagebox.showerror("Erro no Banco", f"Não foi possível registrar: {e}")

    # Função para registrar a saída do veículo e calcular o valor a pagar
    def saida_veiculo(self):
        tipo = self.tipo_var.get()
        placa = self.entry_placa.get()
        
        if not placa:
            messagebox.showerror("Erro", "Por favor, digite a placa para dar saída!")
            return

        try:
            # 1. Tenta formatar a placa
            placa_formatada = obter_placa_tratada(placa)
            
            # 2. Calcula o valor
            valor = calcular_valor(tipo, placa_formatada)
            
            # 3. Libera a vaga no banco
            liberarvaga(tipo, placa_formatada)
            
            messagebox.showinfo("Saída", f"Veículo {tipo} saiu!\nValor a pagar: R${valor:.2f}")

            # Limpa os campos após a saída
            self.entry_modelo.delete(0, 'end')
            self.entry_placa.delete(0, 'end')
            
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
        except Exception as e:
            messagebox.showerror("Erro Inesperado", f"Ocorreu um problema: {e}")
