import abc
from comunicador import Comunicador

class Comunicador_email(Comunicador):
	
	def __init__(self, email):
		self.email = email

	def enviar_mensagem(self, nome, uffmail, senha):
		print("======SIMULAÇÃO DO E-MAIL======\n")
		print("Olá,", nome)
		print("\nO seu UFFMail", uffmail, "foi criado com sucesso.")
		print("Acesse http://mail.id.uff.br e use a senha a seguir para acessá-lo:\n\n", senha)
		print("\nRecomendamos a troca da senha no primeiro acesso.")
		print("\n\nAtenciosamente,\nEquipe STI UFF")
		print("\n\n======FIM DA SIMULAÇÃO======")
		#Envia e-mail
		return