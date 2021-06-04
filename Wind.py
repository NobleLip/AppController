#!/usr/bin/python
import win32gui
import time
import datetime
import sqlite3
import os
#Conecta DB
conn = sqlite3.connect('AppValue.db')
c = conn.cursor()

#Apps a Serem Controladas
#Sempre Que Quiser Controlar a App Tenho que Adicionar Neste Array
Apps = ['YouTube', 'League of Legends','Naruto']

#Array de Controlo
Cont = {'YouTube':3600,
		'League of Legends': 3600,
		'Naruto':1}

Consola = {'YouTube':'brave.exe',
			'League of Legends':'LeagueClient.exe',
			'Naruto':'brave.exe'} 

# Retorna o Titulo da App a ser Ultilizada, talvez vá Filtrar
def GetNomeWindow():
	return win32gui.GetWindowText(win32gui.GetForegroundWindow())

#Retorna O Tempo Atual
def GetTime():
	return datetime.datetime.now()

#Reconhece a Applicação em Uso
def GetApp():
	App = GetNomeWindow()
	for i in Apps:
		if App.find(i) != -1:
			return i

#Controla Tempos nas Apps
def Controlador(App):
	if App != None:
		TempoDB = c.execute('''SELECT * FROM Apps WHERE App =?''', [App])
		for temp in TempoDB:
			Tempo = temp[1]
		#Validar
		if Cont[App] <= Tempo:
			os.system("TASKKILL /F /IM "+Consola[App])
#Adicionar DB
def AtualizaDB(Tempo, App):
	TempoDB = c.execute('''SELECT * FROM Apps WHERE App =?''', [App])
	#Soma Tempo da DB ao Tempo que foi usada a App
	for temp in TempoDB:
		Tempo = Tempo + temp[1]
	#Atualiza o Tempo
	c.execute('''UPDATE Apps SET App=?, Tempo=? WHERE App=?''', [App, Tempo, App])
	conn.commit()

#Atualiza os Valore Para o Dia Seguinte
def FimDoDia():
	for App in Apps:
			List = [App, 0, App]
			c.execute('''UPDATE Apps SET App=?, Tempo=? WHERE App=?''', List)
			conn.commit()

#Retorna o Dia
def GetDia():
	return datetime.datetime.now().date()

#Verifica DB
#Se Não Existir Cria
def VerificaDB():
	#Cria Se Não Existir
	try:
		c.execute('''CREATE TABLE Apps
            	 ([App] TEXT PRIMARY KEY,[Tempo] INTEGER)''')
		conn.commit()

		for App in Apps:
			List = [App, 0]
			c.execute('''INSERT INTO Apps (App,Tempo) VALUES (?,?)''', List)
			conn.commit()

		c.execute('''INSERT INTO Apps (App,Tempo) VALUES (?,?)''', ['Dia', GetDia()])
		conn.commit()

		print('DB Criada')
	except:
		print('Conexão Bem Sucedida')

#Update Dia
def UpdateDia():
	c.execute('''UPDATE Apps SET App=?, Tempo=? WHERE App=?''', ['Dia',GetDia(),'Dia'])
	conn.commit()

#Busca Dia na DB
def GetDiaDB():
	Data = c.execute('''SELECT * FROM Apps WHERE App="Dia"''')
	for dia in Data:
		Dia = dia[1]
	return Dia

#Verifica DB
VerificaDB()

#Começar o Ciclo
AppNow = GetApp()
TimeInit = GetTime()
Dia = str(GetDiaDB())

while True:
	if GetApp() != AppNow:
		
		#Mostrar Valores
		TimeFim = GetTime()
		TimeTotal = (TimeFim - TimeInit).total_seconds()
		
		#Add DB
		AtualizaDB(TimeTotal, AppNow)
		
		print(AppNow, TimeTotal)
		#Atualizar os Valores 
		TimeInit = TimeFim
		AppNow = GetApp()
		
	if Dia != str(GetDia()):
		FimDoDia()
		UpdateDia()
		Dia = str(GetDiaDB())

	Controlador(AppNow)
	time.sleep(1)