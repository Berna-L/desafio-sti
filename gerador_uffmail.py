from comunicador import Comunicador
import string
import random
import os

def verifica_permissao(aluno):
	if (aluno.uffmail is not None):
		raise ValueError("Aluno(a) " + aluno.nome + " já possui UFFMail:\n\n" + aluno.uffmail + "\n\nUse o recurso de redefinição de senha caso não consiga acessá-lo\nou entre em contato caso não tenha sido criado por você.")
	elif (aluno.ativo is False):
		raise ValueError("Aluno(a) " + aluno.nome + " está inativo.")
	return True

def gerar_opcoes(aluno, sufixo="@id.uff.br"):
	#Ex: Laura Azevedo Cunha
	nome_minuscula = aluno.nome.lower()
	nome_dividido = nome_minuscula.split(" ") 
	opcoes = []
	opcoes.append(nome_dividido[0] + "_" + nome_dividido[1] + sufixo) #laura_azevedo
	opcoes.append(nome_dividido[0] + nome_dividido[1][0] + nome_dividido[2][0] + sufixo) #lauraac
	opcoes.append(nome_dividido[0] + nome_dividido[2] + sufixo) #lauracunha
	opcoes.append(nome_dividido[0][0] + nome_dividido[2] + sufixo) #lcunha
	opcoes.append(nome_dividido[0][0] + nome_dividido[1] + nome_dividido[2] + sufixo) #lazevedocunha
	return opcoes

def cadastrar_uffmail(matricula, nome, uffmail, meio_envio):
	if (isinstance(meio_envio, Comunicador)):
		if ("@id.uff.br" in uffmail):
			print("\nBack-end do sistema UFFMail para cadastrar matrícula",matricula,"com UFFMail\n", uffmail)
			
			#Parte a seguir (da senha) """inspirada""" em http://stackoverflow.com/questions/7479442/high-quality-simple-random-password-generator
			tamanho_senha = 13
			caracteres = string.ascii_letters + string.digits + '!@#$%^&*()'
			random.seed(os.urandom(1024))
			senha = ''.join(random.choice(caracteres) for i in range(tamanho_senha))

			meio_envio.enviar_mensagem(nome, uffmail, senha)

			print("Fim do back-end")
			return True
		else:
			raise ValueError("UFFMail informado não é UFFMail")
	else:
		raise TypeError("Meio de envio não é subclasse de Comunicador")
