from aluno import Aluno
import gerador_uffmail as gerador
from comunicador_email import Comunicador_email as cemail
from comunicador_sms import Comunicador_sms as csms

if __name__ == "__main__":
	aluno = None
	while(aluno is None):
		print("Digite a matricula:")
		mat = input()
		print()
		try:
			aluno = Aluno.matricula_para_aluno(mat) 
		except ValueError as e:
			print(e)
	try:
		gerador.verifica_permissao(aluno)
	except ValueError as e:
		print(e)
	else:
		opcoes = gerador.gerar_opcoes(aluno)
		escolha = None
		while (escolha is None):
			contador = 0
			print("Essas são as opções geradas para você:")
			for opcao in opcoes:
				contador = contador + 1
				print(contador, "-", opcao)
			print("\nEscolha uma opção, de 1 a 5:")
			numero = int(input())
			if (1 <= numero <= 5):
				escolha = opcoes[numero - 1]
			else:
				print("\nEscolha de 1 a 5!\n")
		meio_envio = None
		while(meio_envio is None):
			print("Como deseja receber a senha?")
			print("1 - Telefone:", aluno.telefone)
			print("2 - E-mail:", aluno.email)
			print("\nEscolha uma opção, 1 ou 2:")
			numero = int(input())
			if (numero == 1):
				meio_envio = csms(aluno.telefone)
			elif (numero == 2):
				meio_envio = cemail(aluno.email)
			else:
				print("\nEscolha 1 ou 2!\n")
		gerador.cadastrar_uffmail(aluno.matricula, aluno.nome, escolha, meio_envio)
		print("Senha enviada à opção escolhida.")
		aluno.uffmail = escolha
		aluno.salvar_em_csv()
