import csv
import shutil

def salvar_linha(linha_nova, chave_a_comparar, campos, nome_arquivo_csv):
	salvo = False
	with open(nome_arquivo_csv, 'r', newline='') as arquivo_csv:
		leitor = csv.DictReader(arquivo_csv)
		with open(nome_arquivo_csv + ".temp", 'w', newline='') as arquivo_csv_escrita:
			escritor = csv.DictWriter(arquivo_csv_escrita, fieldnames=campos)
			escritor.writeheader()
			for linha in leitor:
				if (str(linha_nova[chave_a_comparar]) == linha[chave_a_comparar]):
					escritor.writerow(linha_nova)
					salvo = True
				else:
					escritor.writerow(linha)
			if (not salvo):
				escritor.writerow(linha_nova) #Se não foi salvo, salvar no fim
	shutil.move(nome_arquivo_csv + ".temp", nome_arquivo_csv)

def get_linha(valor, chave, nome_arquivo_csv):
		with open(nome_arquivo_csv, newline='') as arquivo_csv:
			dict = csv.DictReader(arquivo_csv)
			for linha in dict:
				# contador = contador + 1
				if (str(valor) == linha[chave]):
					return linha
			raise ValueError()