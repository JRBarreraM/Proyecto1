# Juego4enLineaEquipo07.py
#
# DESCRIPCION: algoritmo que permite a un usuario jugar al 4 en linea \
# contra una IA con 2 niveles de dificultad (fácil, jugadas random y medio,\
# jugadas controladas por la IA), a traves de la terminal de la interfaz grafica.
#
# Autores: 
#	Br. Jose Barrera y Br. Alfredo Cruz.
#
# Ultima modificacion: 06/04/2018.

"""
   CONSTANTES Logicas	#informacion proporcionada por el usuriario que el programa no modifica:		
   	nombreusuario : str	# nombre del usuario que esta jugando la partida
	nivel : int  		# la dificultad escogida nivel1=Facil y nivel2=Medio, si desea salir
	partida : int	  	# si se escoge 0 se inicia una partida, 1 se carga una, 2 se cierra el juego.
	seguir : bool  		# si se desea o no rendirse en la partida actual.
	guardar : bool		# si se desea o no guardar el estado actual de la partida en curso.
	x : int				# Almacena la fila jugada por el usuario
	y : int				# Almacena la columna jugada por el usuario
  
   VARIABLES Logicas
	tabl : list			# el tablero logico del juego
	tabv : list		 	# tablero de victorias globales del juego
	jugando : bool  	# controla si se esta en partida o en el menu
	turno : int  		# contador de los turnos de la partida
	juegauser : int		# a quien le toca jugar(True para user, False para IA)
	ganador : int  		# el primero en cumplir las condiciones victoria
	dentro : bool  		# controla si esta dentro del programa
	movida : bool  		# permite al nivel1 reintentar hasta hacer una jugada
	i : int  			# fila de la jugada de la IA
	j : int  			# columna de la jugada de la IA
	Ruser : list		# Almacena los resultados de jugadaUser()
	Rvictoria : list	# Almacena los resultados de Rvictoria()
	RIA : list			# Almacena los resultados de IA()
	bound : int  		# cota que permite que los ciclos terminen
"""	
import pygame				
import os		
import random	 
# CONSTANTES Graficas:
# Colores que seran usados en el juego
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AMARILLO = (255, 255, 000)

# Valores necesarios para la pantalla
ALTO = 720       # alto de la ventana
ANCHO = 1280     # ancho de la ventana
FPS = 30         # frames per second

# Inicializar la pantalla del juego
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'                  # Centrar la ventana a la hora de abrirse
pantalla = pygame.display.set_mode((ANCHO, ALTO))       # Configurando la pantalla
pygame.display.set_caption("4 En Raya")                 # Coloca titulo a la pantalla

# Lista de subprogramas (funciones) que usa el esqueleto principal:

def resultados(tabv=list,ganador=int,juegauser=bool) -> bool:
	#Pre: ganador==0 \/ ganador==1 \/ ganador==2
	#Post: True
	
	if ganador==0:
		tabv[0][0]=tabv[0][0]+1
		juegauser = False
	elif ganador==1:
		tabv[0][1]=tabv[0][1]+1
		juegauser = True
	elif ganador==2:
		tabv[0][2]=tabv[0][2]+1
		juegauser = False
	print("Este el tablero de victorias")
	print("Empates/Jugador/IA")
	print(tabv)
	return juegauser	


def valida( tabl = list, i=int, j=int ):
	# Pre: True 
	# Post: valida=((tabl[i][j]=0)andi=5)\/((tabl[i][j]=0)andi<5andtabl[i-1][j]!=0)
	# VAR:
		#valida : bool  
	
	if 0 <= i < 6 and 0 <= j < 7: 
		if tabl[i][j]==0:
			if i==5:
				valida=True
			elif i<5 and tabl[i+1][j]!=0:
				valida=True
			elif i<5 and tabl[i+1][j]==0:
				valida=False
			
		else:
			valida=False
		
	elif i < 0 or i > 5 or j < 0 or j > 6:
		valida=False
	
	return valida

def jugadaUser( tabl = list ):
	# Pre: True 
	# Post:  (valida(x,y)=True => tabl[x][y] = 1])
	# VAR:
		# JugadaCorrecta : bool
		# x : int
		# y : int
	
	JugadaCorrecta=False
	
	while not(JugadaCorrecta) :
		try:	
			x=int(input("Ingrese la fila donde desea jugar:"))
			y=int(input("Ingrese la columna donde desea jugar:"))
			assert(valida(tabl,x,y))
			break
		except:
			print("Jugada no valida,intenta otra vez")
		
	tabl[x][y] = 1
	pygame.draw.circle(pantalla,ROJO , (201 + y*142, 134 + x*88), 30, 0)
	#Dibujar circulo rojo en la posicion correspodiente	

	return tabl,x,y


def victoria(tabl=list,i=int,j= int,jugando=bool,ganador=int):
	# Pre: True  
	# Post:  (ganador=0 and jugando=1) \/ ((ganador=1 \/ ganador=2)and(jugando=0))
	# VAR:
		# Rvictoria : list
	Rvictoria=victoriahorizontal(tabl,i,j,jugando,ganador)
	jugando=Rvictoria[0]
	ganador=Rvictoria[1]
	if jugando:
		Rvictoria=victoriavertical(tabl,i,j,jugando,ganador)
		jugando=Rvictoria[0]
		ganador=Rvictoria[1]
		if jugando:
			Rvictoria=victoriadiagonalprincipal(tabl,i,j,jugando,ganador)
			jugando=Rvictoria[0]
			ganador=Rvictoria[1]
			if jugando:
				Rvictoria=victoriadiagonalsecundaria(tabl,i,j,jugando,ganador) 
				jugando=Rvictoria[0]
				ganador=Rvictoria[1]

	return jugando, ganador

#Aqui se verifican las distintas condiciones para que un jugador gane el juego formando 4 en raya.
def victoriadiagonalprincipal( tabl= list, i=int, j= int, jugando=bool, ganador=int ):
	#Pre: N = 6 and M = 7  
	# Post:  (ganador=0 /\ jugando=False) \/ ((ganador=1 \/ ganador=2)/\(jugando=False)) 
	#VAR
    		#ganador : int  
		#jugando : bool   

	jugando = True
	i=0
	#cota= 6-i
	while i < 3:
		j=0
		#cota= 4-j
		while j < 4 and jugando==True:
			#Conexion diagonal principal
			if tabl[i][j]==tabl[i+1][j+1]==tabl[i+2][j+2]==tabl[i+3][j+3]==1:
				ganador=1
				jugando=False
				tabl[i][j],tabl[i+1][j+1],tabl[i+2][j+2],tabl[i+3][j+3]=3,3,3,3
				#Dibujar circulo amarillo en las posiciones correspodientes
				pygame.draw.circle(pantalla, AMARILLO,(201 + j*142, 134 + i*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + (j+1)*142, 134 + (i+1)*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + (j+2)*142, 134 + (i+2)*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + (j+3)*142, 134 + (i+3)*88), 20, 0)
			
			elif tabl[i][j]==tabl[i+1][j+1]==tabl[i+2][j+2]==tabl[i+3][j+3]==2:
				ganador=2
				jugando=False
				tabl[i][j],tabl[i+1][j+1],tabl[i+2][j+2],tabl[i+3][j+3]=3,3,3,3
				#Dibujar circulo amarillo en las posiciones correspodientes
				pygame.draw.circle(pantalla, AMARILLO,(201 + j*142, 134 + i*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + (j+1)*142, 134 + (i+1)*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + (j+2)*142, 134 + (i+2)*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + (j+3)*142, 134 + (i+3)*88), 20, 0)
			j=j+1
		i=i+1
	return jugando, ganador 

def victoriahorizontal( tabl= list, i=int, j= int, jugando=bool, ganador=int ):
	#Pre: N = 6 and M = 7         
	# Post:  (ganador=0 /\ jugando=False) \/ ((ganador=1 \/ ganador=2)/\(jugando=False))
	#VAR
    	#ganador : int  
		#jugando : bool  
		#i : int  
		#j : int  

	jugando,i = True,0

	#cota=6-i
	while i<6:
		j=0
		#cota=4-j}
		while j<4 and jugando==True:
			#Conexion horizontal
			if tabl[i][j]==tabl[i][j+1]==tabl[i][j+2]==tabl[i][j+3]==1:
				ganador=1
				jugando=False
				tabl[i][j],tabl[i][j+1],tabl[i][j+2],tabl[i][j+3]=3,3,3,3
				#Dibujar circulo amarillo en las posiciones correspodientes
				pygame.draw.circle(pantalla, AMARILLO, (201 + j*142, 134 + i*88) , 20, 0)
				pygame.draw.circle(pantalla, AMARILLO, (201 + (j+1)*142, 134 + i*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,((201 + (j+2)*142, 134 + i*88)) , 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + (j+3)*142, 134 + i*88) , 20, 0)

			elif tabl[i][j]==tabl[i][j+1]==tabl[i][j+2]==tabl[i][j+3]==2:
				ganador=2
				jugando=False
				tabl[i][j],tabl[i][j+1],tabl[i][j+2],tabl[i][j]=3,3,3,3
				#Dibujar circulo amarillo en las posiciones correspodientes
				pygame.draw.circle(pantalla, AMARILLO,(201 + j*142, 134 + i*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + (j+1)*142, 134 + i*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + (j+2)*142, 134 + i*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + (j+3)*142, 134 + i*88), 20, 0)
			j=j+1
		i=i+1
	return jugando, ganador

def victoriavertical( tabl= list, i=int, j= int, jugando=bool, ganador=int ):
	#Pre: N = 6 and M = 7       
	# Post: (ganador=0 /\ jugando=False) \/ ((ganador=1 \/ ganador=2)/\(jugando=False))
	#VAR 
		#jugando : bool  
		#i : int  
		#j : int  

	jugando, i = True,0

	#cota= 3-i
	while i < 3:
		j=0
		#cota= 7-j
		while j < 7 and jugando==1:
			if tabl[i][j]==tabl[i+1][j]==tabl[i+2][j]==tabl[i+3][j]==1:
				ganador=1
				jugando=False
				tabl[i][j],tabl[i+1][j],tabl[i+2][j],tabl[i+3][j]=3,3,3,3
				#Dibujar circulo amarillo en las posiciones correspodientes
				pygame.draw.circle(pantalla, AMARILLO,(201 + j*142, 134 + i*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + j*142, 134 + (i+1)*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + j*142, 134 + (i+2)*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + j*142, 134 + (i+3)*88), 20, 0)
			elif tabl[i][j]==tabl[i+1][j]==tabl[i+2][j]==tabl[i+3][j]==2:
				ganador=2
				jugando=False
				tabl[i][j],tabl[i+1][j+1],tabl[i+2][j+2],tabl[i+3][j+3]=3,3,3,3
				#Dibujar circulo amarillo en las posiciones correspodientes
				pygame.draw.circle(pantalla, AMARILLO,(201 + j*142, 134 + i*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + j*142, 134 + (i+1)*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + j*142, 134 + (i+2)*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + j*142, 134 + (i+3)*88), 20, 0)
			j=j+1
		i=i+1
	return jugando, ganador

def victoriadiagonalsecundaria( tabl= list, i=int, j= int, jugando=bool, ganador=int):
	#Pre: N = 6 and M = 7        
	# Post:  (ganador=0 /\ jugando=False) \/ ((ganador=1 \/ ganador=2)/\(jugando=False))
	#VAR 
	#jugando : bool  
	#i : int  
	#j : int  

	jugando, i = True, 0

	#cota=3-i
	while i < 3:
		j=0
		#cota=7-j
		while j < 7 and jugando==True:
			#Conexion diagonal secundaria
			if j>2 and tabl[i][j]==tabl[i+1][j-1]==tabl[i+2][j-2]==tabl[i+3][j-3]==1:
				ganador=1
				jugando=False
				tabl[i][j],tabl[i+1][j-1],tabl[i+2][j-2],tabl[i+3][j-3]=3,3,3,3
				#Dibujar circulo amarillo en las posiciones correspodientes
				pygame.draw.circle(pantalla, AMARILLO,(201 + j*142, 134 + i*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + (j-1)*142, 134 + (i+1)*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + (j-2)*142, 134 + (i+2)*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + (j-3)*142, 134 + (i+3)*88), 20, 0)

			elif j>2 and tabl[i][j]==tabl[i+1][j-1]==tabl[i+2][j-2]==tabl[i+3][j-3]==2:
				ganador=2
				jugando=False
				tabl[i][j],tabl[i+1][j-1],tabl[i+2][j+2],tabl[i+3][j-3]=3,3,3,3
				#Dibujar circulo amarillo en las posiciones correspodientes
				pygame.draw.circle(pantalla, AMARILLO,(201 + j*142, 134 + i*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + (j-1)*142, 134 + (i+1)*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + (j-2)*142, 134 + (i+2)*88), 20, 0)
				pygame.draw.circle(pantalla, AMARILLO,(201 + (j-3)*142, 134 + (i+3)*88), 20, 0)
			j=j+1
		i=i+1
	return jugando, ganador

# Aqui culminan las verificaciones de las posibilidades de ganar el juego con un 4 en raya.

def IA( tabl=list, i=int, j=int ):
	#Pre: 0<=i<6 and 0<=j<7
	#Post: 0<=i<6 and 0<=j<7

	#VAR:						# para esta version de la IA solo nos interesan las jugadas
	#z:int  					# que puede hacer a partir de la anterior, por lo que
	#max:int  					# la vi (vertical inferior queda descartada), y tiende a
	#hi,hd,vs,dps,dss: int  			# escoger jugadas horizontales.

	hi,hd,vs,dps,dpi,dss,dsi=0,0,0,0,0,0,0
								
	z=1					# aqui cuenta las 3 proximas posibles jugadas para armar una
	#cota= 4-z				# linea horizontal hacia la izquierda de su posicion
	while z<4 and valida(tabl,i,j-z): 	
		hi= hi+1		
		z = z+1

	z=1				    	# aqui cuenta las 3 proximas posibles jugadas para armar una
	#cota= 4-z				# linea horizontal hacia la derecha de su posicion
	while z<4 and valida(tabl,i,j+z):
		hd = hd+1
		z = z+1

	
	if valida(tabl,i-1,j):		# aqui solo se cuenta si la proxima posible jugada para armar una
		vs = vs+1		    	# linea vertical, justo arriba de su posicion

	z=1				        # aqui cuenta las 3 proximas posibles jugadas para armar una	
	#cota= 4-z				# linea diagonal principal superior (raro pero posible)
	while z<4 and valida(tabl,i-z,j-z):	 
		dps = dps+1
		z = z+1


	z=1				        # aqui cuenta las 3 proximas posibles jugadas para armar una	
	#cota= 4-z				# linea diagonal principal inferior (raro pero posible)                
	while z<4 and valida(tabl,i+z,j+z):	 
		dpi = dpi+1
		z = z+1
	

	z=1	     			    # aqui cuenta las 3 proximas posibles jugadas para armar una
	#cota= 4-z			    # linea diagonal secundaria superior (raro pero posible)
	while z<4 and valida(tabl,i-z,j+z):
		dss = dss+1
		z = z+1

	
	z=1					# aqui cuenta las 3 proximas posibles jugadas para armar una
	#cota=4-z				# diagonal secundaria inferior (raro pero posible)
	while z<4 and valida(tabl,i+z,j-z):
		dsi = dsi+1
		z = z+1
	
	z=0
	Max=max(hi,hd,vs,dps,dpi,dss,dsi)  	# buscamos la jugada mas "favorable"
	if Max==0:			# si la pieza se encuentra rodeada, se busca un nuevo
		i,j = 5,6			# lugar donde jugar.
		#cota = i
		while 0 <= i < 6 and z==0:
		#cota = j
			while 0 <= j < 7 and z==0:
				if valida(tabl,i,j):
					tabl[i][j]=2
					pygame.draw.circle(pantalla,AZUL, (201 + j*142, 134 + i*88), 30, 0)
					z=1
				j=j-1
			i=i-1
			
	elif Max==hi:			# la ejecutamos
		tabl[i][j-1]=2
		#Dibujar circulo azul en la posicion correspodiente
		pygame.draw.circle(pantalla,AZUL, (201 + (j-1)*142, 134 + i*88), 30, 0)
		i=i
		j=j-1
	elif Max==hd:
		tabl[i][j+1]=2
		#Dibujar circulo azul en la posicion correspodiente
		pygame.draw.circle(pantalla,AZUL, (201 + (j+1)*142, 134 + i*88), 30, 0)
		i=i
		j=j+1
	elif Max==vs:
		tabl[i-1][j]=2
		#Dibujar circulo azul en la posicion correspodiente
		pygame.draw.circle(pantalla,AZUL, (201 + j*142, 134 + (i-1)*88), 30, 0)
		i=i-1
		j=j
	elif Max==dps:
		tabl[i-1][j-1]=2
		#Dibujar circulo azul en la posicion correspodiente
		pygame.draw.circle(pantalla,AZUL, (201 + (j-1)*142, 134 + (i-1)*88), 30, 0)
		i=i-1
		j=j-1
	elif Max==dpi:
		tabl[i+1][j+1]=2
		#Dibujar circulo azul en la posicion correspodiente
		pygame.draw.circle(pantalla,AZUL, (201 + (j+1)*142, 134 + (i+1)*88), 30, 0)
		i=i+1
		j=j+1
	elif Max==dss:
		tabl[i-1][j+1]=2
		#Dibujar circulo azul en la posicion correspodiente
		pygame.draw.circle(pantalla,AZUL, (201 + (j+1)*142, 134 + (i-1)*88), 30, 0)
		i=i-1
		j=j+1
	elif Max==dsi:				
		tabl[i+1][j-1]=2
		#Dibujar circulo azul en la posicion correspodiente
		pygame.draw.circle(pantalla,AZUL, (201 + (j-1)*142, 134 + (i+1)*88), 30, 0)
		i=i+1
		j=j-1	
	return tabl,i,j
	
#Clase que nos almacenar los valores de juego

class valoresdejuego:
	nombreusuario="EAS"				#nombre del jugador
	turno=1							#turno de la partida en curso
	nivel=2							#deficultad de la IA
	tabl=[[0]*7 for i in range(6)]		#tablero de juego
	i=5								#fila de la ultima jugada de la IA
	j=3								#columna de la ultima jugada de la IA
	tabv=[[0,0,0]]					#tablero de victorias globales
anterior=valoresdejuego()			#estructura donde guardamos los datos de la partida

# Descripcion: Funcion que cada turno actualiza los valores de las variables de juego. 
# Parametros:
def actualizacion(estructura=valoresdejuego,nombreusuario=str,turno=int,nivel=int,A=list,i=int,j=int,G=list):
		anterior.nombreusuario=nombreusuario
		anterior.turno=turno
		anterior.nivel=nivel
		anterior.tabl=tabl
		anterior.i=i
		anterior.j=j
		anterior.tabv=tabv
		return anterior

# Descripcion: Funcion que lee el archivo de guardado y almacena su informacion
#			en una lista para posteriormente sobreescribir las variables de juego. 
# Parametros:
def CargarJuego(archivo=str):
	with open(archivo,'r+') as f:
		oldcontenido = f.readlines()
		contenido = [oldcontenido[i].rstrip() for i in range(7)]
	f.closed
	return contenido
# Descripcion: Funcion que escibe en el archivo de guardado los valores actuales
#			de las variables de juego(nombre,turno,nivel,A,i,j). 
# Parametros:
def GuardarJuego(archivo=str, estructura=valoresdejuego):#no tiene salida
	with open(archivo,'w') as f:
		f.write(anterior.nombreusuario+"\n")
		f.write(str(anterior.turno)+"\n")
		f.write(str(anterior.nivel)+"\n")
		f.write(str(anterior.tabl)+"\n")
		f.write(str(anterior.i)+"\n")
		f.write(str(anterior.j)+"\n")
		f.write(str(anterior.tabv))
	f.closed

#Funciones referentes a la parte grafica 
def dibujartableronuevo(tabl=list):        #->void
	assert(True)
	#Postcondicion:se dibuja en una ventana grafica un tablero con filas y columnas de color verde
	#Cuadrado exterior
	pygame.draw.line(pantalla, VERDE, (130, 90), (130, 620))
	pygame.draw.line(pantalla, VERDE, (1120, 90), (1120, 620))
	pygame.draw.line(pantalla, VERDE, (130, 90), (1120, 90))
	pygame.draw.line(pantalla, VERDE, (130, 620), (1120, 620))

    # Filas
	pygame.draw.line(pantalla, VERDE, (130, 178), (1120, 178))
	pygame.draw.line(pantalla, VERDE, (130, 266), (1120, 266))
	pygame.draw.line(pantalla, VERDE, (130, 354), (1120, 354))
	pygame.draw.line(pantalla, VERDE, (130, 442), (1120, 442))
	pygame.draw.line(pantalla, VERDE, (130, 530), (1120, 530))

    # Columnas
	pygame.draw.line(pantalla, VERDE, (272, 90), (272, 620))
	pygame.draw.line(pantalla, VERDE, (414, 90), (414, 620))
	pygame.draw.line(pantalla, VERDE, (556, 90), (556, 620))
	pygame.draw.line(pantalla, VERDE, (698, 90), (698, 620))
	pygame.draw.line(pantalla, VERDE, (840, 90), (840, 620))
	pygame.draw.line(pantalla, VERDE, (982, 90), (982, 620))

	#Numeros Guia
	fuente = pygame.font.Font(None, 75)
	I = fuente.render("0", True, VERDE)
	pantalla.blit(I, [90, 90])
	pantalla.blit(I, [170, 40])
	II = fuente.render("1", True, VERDE)
	pantalla.blit(II, [90, 190])
	pantalla.blit(II, [330, 40])
	III = fuente.render("2", True, VERDE)
	pantalla.blit(III, [90, 280])
	pantalla.blit(III, [470, 40])
	IV = fuente.render("3", True, VERDE)
	pantalla.blit(IV, [90, 380])
	pantalla.blit(IV, [610, 40])
	V = fuente.render("4", True, VERDE)
	pantalla.blit(V, [90, 470])
	pantalla.blit(V, [750, 40])
	VI = fuente.render("5", True, VERDE)
	pantalla.blit(VI, [90, 570])
	pantalla.blit(VI, [900, 40])
	VII = fuente.render("6", True, VERDE)
	pantalla.blit(VII, [1050, 40])	

	for i in range(0,6):
		for j in range(0,7):
			if tabl[i][j] != 0:
				pygame.draw.circle(pantalla, NEGRO, (201 + j*142, 134 + i*88), 30, 0)
	pygame.display.flip()

def cargarTablero(tabl=list): #-> 'void':
	for i in range(0,6):
		for j in range(0,7):
			if tabl[i][j] == 1:
				pygame.draw.circle(pantalla,ROJO , (201 + j*142, 134 + i*88), 30, 0)
			elif tabl[i][j] == 2:
				pygame.draw.circle(pantalla,AZUL, (201 + j*142, 134 + i*88), 30, 0)

	pygame.display.flip()    

# Incializacion de las variables del juego:
dentro=True				# Para entrar en el loop del juego
jugando=False				# Para entra primero al menu
ganador=0				# Se supone un empate por defecto
juegauser=True				# El primer turno corresponde al jugador por defecto
tabv=[[0,0,0]]				# Crear tablero de Victorias [0]Empate, [1]User, [2]IA
tabv[0][0]=-1				# Corrije el error de leer que la partida a terminado en empate
i,j=5,3					# Jugada Predeterminada de la IA en su primer turno
tabl=[[0]*7 for i in range(6)]		# Crear tablero de juego logico.

#Loop del juego

while dentro :							# Dentro del juego
	if not(jugando) :					# en menu
		juegauser=resultados(tabv,ganador,juegauser)	# Comienza la partida el ganador de la anterior
		while True: 					# Se permite al usuario introducir nuevos datos correctos
			try: 
				partida=int(input("Desea empezar o cargar una partida?(0=Nueva,1=Cargar,No=2)"))
				assert( partida==0 or partida==2 or partida==1 )
				break
			except:
				print("Partida solo puede valer 0, 1 o 2")
		dibujartableronuevo(tabl)				#Limpiamos el tablero grafico

		if partida==0:		#Inicializamos las varibles de juego con las de la partida guardada
			tabl=[[0]*7 for i in range(6)]			# Crear nuevo tablero de juego logico.
			jugando=True					# Salir del menu entrar en partida
			turno=1						# Se empieza el primer turno
			
			while True: # Se permite al usuario introducir nuevamente su nombre
				try: 
					nombreusuario=str(input("Coloque su nombre, por favor:"))
					assert( len(nombreusuario)>0 )
					break
				except:
					print("Coloque al menos un caracter")
			
			while True: # Se permite al usuario escoger nuevamente el nivel 
				try: 
					nivel=int(input("Seleccione el nivel:(1=basico,2=medio)"))
					assert( nivel==1 or nivel==2 )
					break
				except:
					print("Escoja entre el nivel 1 o 2")
			
		elif partida==1:       # Sobreescribimos las variables de juego con las de la partida guardada
			contenido=CargarJuego("guardado.txt")	# Leemos el archivo donde guardamos la partida
			nombreusuario = contenido[0]		# Nombre del jugador
			turno = int(contenido[1])		# Turno de la partida
			nivel = int(contenido[2])		# Dificultad de la IA
			tabl = eval(contenido[3])			# Tablero de juego
			i = int(contenido[4])			# Fila de la ultima jugada de la IA
			j = int(contenido[5])			# Columna de la ultima jugada de la IA
			tabv = eval(contenido[6])			# Tablero global de victorias
			dibujartableronuevo(tabl)			# Dibujamos un tablero grafico nuevo
			cargarTablero(tabl)			# Dibujamos las jugadas cargadas del tablero
			jugando=True				# Salir del Menu entrar en partida
			jugadaUser=True				# El jugador debe empezar en su turno
		
		elif partida==2:	# El jugador decide que quiere salir del juego
			dentro=False	# Salimos del loop del juego
			print("Hasta luego!")	# Nos depedimos del usuario
			pygame.quit()		# Cerramos la interfaz grafica
	
	elif jugando :					#en partida
		if turno >= 43 :			# el tablero se encuentra lleno, se declara empate
			jugando=False
			ganador=0
		elif turno < 43 :			# el tablero aun no ha llenado se sigue jugando					
			if juegauser :			# Turno del usuario
				guardar=bool(input("Desea guardar su partida?(Si=Enter)(No=Else)"))
				if not(guardar): #escribimos en alrchivo de guardado las variales de juego actuales
					actualizacion(anterior,nombreusuario,turno,nivel,tabl,i,j,tabv) #actuliza las variables de juego
					GuardarJuego("guardado.txt",anterior)	# guarda el estado del juego en el archivo
				seguir=bool(input("Desea seguir en esta partida?(Si=Enter)(No=Else)")) # en cada turno
				if not(seguir):	
					Ruser=jugadaUser(tabl)	# Almacenamos los cambios tras la jugada del usuario.
					tabl=Ruser[0]		# Reescribimos la matriz con la jugada
					x=Ruser[1]		# Guardamos la fila de la jugada
					y=Ruser[2]		# Guardamos la columna de la jugada
					Rvictoria=victoria(tabl,x,y,jugando,ganador)   # Almacenamos los cambios de jugando y ganador
					jugando=Rvictoria[0]				# Sobreescribimos jugando y ganador
					ganador=Rvictoria[1]				# Si la funcion victoria no encuentra
											# 4 en raya no deberian cambiar.
				else:
					jugando = False				# Se va al menu
					ganador = 2				# Se declara ganador a la maquina

			elif not(juegauser) :					# turno de la maquina
				if nivel == 1 :					# el nivel 1 hace un random de todas las
					movida = True  				# las coordenadas del tablero hasta 
					while movida:				# encontrar una jugada valida
						i = random.randrange(6)	
						j = random.randrange(7)
						if valida(tabl,i,j) :		# si la jugada es valida la ejecuta
							tabl[i][j] = 2
							pygame.draw.circle(pantalla,AZUL, (201 + j*142, 134 + i*88), 30, 0)
							movida = False		# se rompe el ciclo
					Rvictoria=victoria(tabl,i,j,jugando,ganador)   # Almacenamos los cambios de jugando y ganador
					jugando=Rvictoria[0]				# Sobreescribimos jugando y ganador
					ganador=Rvictoria[1]				# Si la funcion victoria no encuentra
											# 4 en raya no deberian cambiar.

				elif nivel == 2 :				# el nivel 2 presenta una sencilla IA
					if turno==1 or turno==2 :		# si esta en su primer turno
						if valida(tabl,5,3):		# y es valida la jugada predefinida
							tabl[5][3]=2		# fila 5 columna 3, la ejecuta
							i,j=5,3 		# se guarda la jugada
							pygame.draw.circle(pantalla,AZUL, (201 + j*142, 134 + i*88), 30, 0)   
						elif not (valida(tabl,5,3)):	# si no era valida la predefinida
							tabl[5][2]=2		# siempre podra ejecutar esta
							i,j=5,2			# se guarda la jugada
							pygame.draw.circle(pantalla,AZUL, (201 + j*142, 134 + i*88), 30, 0)   
					elif turno > 2 :			# a partir de una jugada anterior
						RIA=IA(tabl,i,j)			# Almacenamos los cambios del tablero, y la jugada
						A=RIA[0]			# Sobreescribimos el tablero y la jugada
						i=RIA[1]
						j=RIA[2]
					Rvictoria=victoria(tabl,i,j,jugando,ganador)   # Almacenamos los cambios de jugando y ganador
					jugando=Rvictoria[0]				# Sobreescribimos jugando y ganador
					ganador=Rvictoria[1]				# Si la funcion victoria no encuentra
											# 4 en raya no deberian cambiar.

			turno = turno + 1		# contamos el siguiente turno
			juegauser = not(juegauser)	# se pasa el turno al rival
			pygame.display.flip() 		# se recarga el tablero

assert( dentro==False )

# Aqui termina el el loop del juego.
#cerrar el programa
pygame.quit()