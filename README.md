# AppController

This is a Old Mini project that i was working on for some hours, the purpose of this project was to stop me from playing and watching youtube soo mutch and consequently work more.

To make this program work without any visual console i used pyinstaller :

* pyinstaller --noconsole wind.py

Since for a long time i'm using linux ,this project is just reminder of the old projects that i was working on!


## How To Use

For it to work you have to insert the task's that you whant to be controlled , like:
```
Apps = ['YouTube', 'League of Legends','Naruto', 'Name that Appears on the Windows TaskBar']

#Array de Controlo
Cont = {'YouTube':3600,
		'League of Legends': 3600,
		'Naruto':1
    'Name that Appears on the Windows TaskBar': Time in secs that u whant to use it daily}

Consola = {'YouTube':'brave.exe',
			'League of Legends':'LeagueClient.exe',
			'Naruto':'brave.exe',
      'Name that Appears on the Windows TaskBar':'The Name of the .exe file that makes the program that you are using work'} 
```

After this , its a simple procedure:
* pyinstaller --noconsole wind.py

**Run the .exe File and its Done.**
