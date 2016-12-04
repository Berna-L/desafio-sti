import csv

def csv_para_lista(nome_arquivo_csv):
	with open(nome_arquivo_csv, newline='') as arquivo_csv:
		return csv.DictReader(arquivo_csv)