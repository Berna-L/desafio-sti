from aluno import Aluno

if __name__ == "__main__":
	aluno = None
	while(aluno is None):
		print("Digite a matricula:")
		mat = input()
		try:
			aluno = Aluno.matricula_para_aluno(mat) 
		except ValueError as e:
			print(e)
