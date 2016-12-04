import abc
from comunicador import Comunicador

class Comunicador_sms(Comunicador):
	
	def __init__(self, telefone):
		self.telefone = telefone

	def enviar_mensagem(self, nome, uffmail, senha):
		print("======SIMULAÇÃO DO SMS PARA", self.telefone, "======")
		print("Use a senha", senha, "para acessar o seu UFFMail", uffmail)
		print("======FIM DA SIMULAÇÃO======")
		#Envia para o número
		return