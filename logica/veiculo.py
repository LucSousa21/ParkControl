from datetime import datetime

class Veiculo:
    def __init__(self, tipo, vaga_id):
        # Valida o tipo do veículo
        if tipo not in ['carro', 'moto']:
            raise ValueError("Tipo de veículo inválido. Use 'carro' ou 'moto'.")

        self.vaga_id = vaga_id            # Ex: "C1", "M5"
        self.tipo = tipo                  # 'carro' ou 'moto'
        self.hora_entrada = datetime.now()
        self.hora_saida = None

    def registrar_saida(self):
        """Registra a hora de saída do veículo"""
        self.hora_saida = datetime.now()
        return self.hora_saida

    def calcular_tempo_permanencia(self):
        """
        Retorna o tempo de permanência.
        Se o veículo ainda não saiu, calcula até o momento atual.
        """
        fim = self.hora_saida or datetime.now()
        return fim - self.hora_entrada

    def __str__(self):
        return f"Veículo {self.tipo.capitalize()} - Vaga: {self.vaga_id}"
