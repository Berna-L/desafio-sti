def verifica_permissao(aluno):
	if (aluno.uffmail is not None):
		raise ValueError("Aluno(a) " + aluno.nome + " já possui UFFMail:\n\n" + aluno.uffmail + "\n\nUse o recurso de redefinição de senha caso não consiga acessá-lo\nou entre em contato caso não tenha sido criado por você.")
	elif (aluno.ativo is False):
		raise ValueError("Aluno(a) " + aluno.nome + " está inativo.")
	return true

def gerar_opcoes(aluno):
	if (verifica_permissao):
		nome_dividido = aluno.nome.split(" ")
