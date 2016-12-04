from aluno import Aluno
import gerador_uffmail as gerador

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
		lista = gerador.gerar_opcoes(aluno)