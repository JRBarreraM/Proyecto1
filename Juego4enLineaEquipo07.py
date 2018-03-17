#
# Juego4enLineaEquipo07.py
#
# DESCRIPCION: algoritmo que permite a un usuario jugar al 4 en linea \
# contra una IA con 2 niveles de di cultad (facil y medio), a traves de la \
# terminal de la interfaz gra ca.
#
# Autores: 
#	Br. Jose Barrera y Alfredo Cruz.
#
# Ultima modificacion: 16/03/2018.

"""
   CONS					
   	nombreusuario : str  		#informacion proporcionada por el usuriario que el programa no modifica:
	nivel : int  			# su nombre, la dificultad, si desea abandonar una partida, si desea salir
	new : bool	  		# del programa, y por supuesto la jugada que hara en cada turno reflejada en
	seguir : bool  			# sus coordenadas  fila, columna.
	x : int  
	y : int  
   VAR
	A : array [0..6)x[0..7) of int  	# el tablero de juego
	G : array [0..4)	 		# tablero de resultados
	jugando : bool  			# en partida
	turno : int  				# contador de los turnos 
	juegauser : int				# a quien le toca jugar(True para user, False para IA)
	ganador : int  				# el primero en cumplir las condiciones victoria
	dentro : bool  				# dentro del programa
	movida : bool  				# permite reintentar hasta hacer una jugada
	i : int  				# fila de la jugada de la IA 
	j : int  				# columna de la jugada de la IA
	partida : int   			# numero de partidas jugadas en sesion actual
	bound : int  				# cota que permite que los ciclos terminen
"""	
	import pygame				
	import os				 
	# CONSTANTES:
	# Colores que seran usados en el juego
	NEGRO = (0, 0, 0)
	BLANCO = (255, 255, 255)
	ROJO = (255, 0, 0)
	AZUL = (0, 0, 255)
	VERDE = (0, 255, 0)
	AMARILLO = (255, 255, 000)

	# Valores necesarias para la pantalla
	ALTO = 720       # alto de la ventana
	ANCHO = 1280     # ancho de la ventana
	FPS = 30         # frames per second
	
#	Variables:
#	pantalla: object    // para el manejo de la interfaz gráfica
#	cuenta: object      // para el manejo del tiempo
#	evento: object      // para capturar los eventos producidos
#	jugando: bool       // dice si se continua en el juego

# Inicializar la pantalla del juego
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'                  # Centrar la ventana a la hora de abrirse
pantalla = pygame.display.set_mode((ANCHO, ALTO))       # Configurando la pantalla
pygame.display.set_caption("4 En Raya")                 # Coloca titulo a la pantalla
reloj = pygame.time.Clock()

# Loop del juego
	
	jugando,turno,dentro,ganador,juegauser=False,1,True,0,True	# Incializacion de las variables
	G=[0]*3								# Crear tablero de Victorias [0]Empate, [1]User, [2]IA
	G[0]=-1
	A=[[0]*6]*7							#Crear tablero de juego
	while dentro :									#en menu
		if not(jugando) :
			resultados(G)
			new=bool(input("Desea empezar una nueva partida?(False=no)"))
			if new :
				nombreusuario=str(input("Coloque su nombre, por favor:"))
				dificultad=int(input("Seleccione la dificultad:(1=basico,2=medio)"))
				A=[[0]*6]*7				#Crear tablero de juego
				dibujartableronuevo()
			else :
				dentro=False
				print("Hasta luego!")
	
		else :									#en partida
			if turno == 43 :
				jugando=False					# el tablero se encuentra lleno, se declara empate
				ganador=0
			elif turno < 43 :								
				if juegauser :						# juega=True representa al usuario
					seguir=bool(input("Desea seguir en esta partida?(False=no)"))	# en cada turno el usuario
					 if seguir :							# debe decidir si sigue 
						jugadaUser(A)
						victoria(A,i,j,jugando,ganador)				#la partida actual  
					  else :
						jugando = False
						ganador = 0
				elif not(juegauser) :
					if nivel == 1 :					# el nivel 1 hace un random de todas las
						movida = True  				# las coordenadas del tablero hasta 
						while movida:				# encontrar una jugada valida
							i = random.randrange(6)		
							j = random.randrange(7)
							if valida(A,i,j) :
								A[i][j] = 2
								movida = False		# momento en el que se rompe el ciclo
						victoria(A,i,j,jugando,ganador)  
					
					elif nivel == 2 :				# el nivel 2 presenta una sencilla IA
						if turno==1 or turno==2 :		# que lo hace apenas mas complejo
							if valida(A,5,3):		
								A[5][3]=2		# se le da una jugada inicial predefinida
								i,j=5,3 				
							elif not (valida(A,5,3)):		# y una jugada alternativa
								A[5][2]=2
								i,j=5,2  
							   
						elif turno > 2 :			# a partir de una jugada anterior
							IA(A,i,j)  			# decide que linea deberia jugar
							victoria(A,i,j,jugando,ganador)  
					 
				turno = turno + 1
				juegauser = not(juegauser)
		
	assert( dentro = False )

# Aqui termina el esqueleto del programa, de aqui en adelante se colocan
# todos los procedimientos que llama.

def resultados(G=array of array) -> array of array
	#Pre: ganador==0 \/ ganador==1 \/ ganador==2
	#Post: G[0]+G[1]+G[2]= partida-1
	
	if ganador==0:
		G[0]=G[0]+1
		juegauser = False
	elif ganador==1:
		G[1]=G[1]+1
		juegauser = True
	elif ganador==2:
		G[2]=G[2]+1
		juegauser = True
	print(G)
	return(G)

def jugadaUser( A = array of array ) -> array of array
	# Pre: True 
	# Post:  (valida(x,y)=True => A[x][y] = 1]) 
		
	while True :
		x=int(input("Ingrese la fila donde desea jugar:"))
		y=int(input("Ingrese la columna donde desea jugar:"))
		if valida(A,x,y):
			A[x][y] = 1
			#Dibujar circulo rojo en la posicion correspodiente
			break
		else not valida(i,j):					#se pide al usuario que intente otra jugada
			print("Jugada no valida,intenta otra vez")
	return A

# Esta es la funcion valida una de las funciones mas importantes del programa, sin importar
# si la coordenada esta o no en el tablero (la matriz A), nos dice si la jugada es valida
def valida( A = array of array, i=int, j=int ) -> bool
	# Pre: True 
	# Post: valida=((A[i][j]=0)andi=5)\/((A[i][j]=0)andi<5andA[i-1][j]!=0)
	# VAR:
		#valida : bool  
	
	if 0 <= i < 6 and 0 <= j < 7: 
		if A[i][j]==0:
			if i==5:
				valida=True
			elif i<5 and A[i+1][j]!=0:
				valida=True
			elif i<5 and A[i+1][j]==0:
				valida=False
			
		else A[i][j]!=0:
			valida=False
		
	elif i < 0 or i > 5 or j < 0 or j > 6:
		valida=False
	
	return valida
		
def victoria( A= array of array, i=int, j= int, jugando, ganador) -> (bool, int)
	# Pre: True  
	# Post:  (ganador=0 and jugando=1) \/ ((ganador=1 \/ ganador=2)and(jugando=0))

	victoriahorizontal(A,i,j)  

	if jugando:
		victoriavertical(A,i,j)
		if jugando:
			victoriadiagonalprincipal(A,i,j)
			if jugando:
				victoriadiagonalsecundaria(A,i,j)
	
	return jugando, ganador

#Aqui se verifican las distintas condiciones para que un jugador gane el juego formando 4 en raya.
def victoriadiagonalprincipal( A= array of array, i=int, j= int, jugando, ganador ) -> (bool, int)
	#Pre: N = 6 and M = 7  
	# Post:  (ganador=0 /\ jugando=False) \/ ((ganador=1 \/ ganador=2)/\(jugando=False)) 
	#VAR
    	#ganador : int  
		#jugando : bool  
		#i : int  
		#j : int  

	jugando = True

	i=0
	#cota= 6-i
	while i < 3:
		j=0
		#cota= 4-j
		while j < 4 and jugando==True:
			#Conexion diagonal principal
			if A[i][j]==A[i+1][j+1]==A[i+2][j+2]==A[i+3][j+3]==1:
				ganador=1
				jugando=False
				A[i][j],A[i+1][j+1],A[i+2][j+2],A[i+3][j+3]=3,3,3,3
				#Dibujar circulo amarillo en las posiciones correspodientes
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
			
			elif A[i][j]==A[i+1][j+1]==A[i+2][j+2]==A[i+3][j+3]==2:
				ganador=2
				jugando=False
				A[i][j],A[i+1][j+1],A[i+2][j+2],A[i+3][j+3]=3,3,3,3
				#Dibujar circulo amarillo en las posiciones correspodientes
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
			j=j+1
		i=i+1
	return jugando, ganador 

def victoriahorizontal( A= array of array, i=int, j= int, jugando, ganador ) -> (bool,int)
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
		while j<4 and jugando=True:
			#Conexion horizontal
			if A[i][j]==A[i][j+1]==A[i][j+2]==A[i][j+3]==1:
				ganador=1
				jugando=False
				A[i][j],A[i+1][j+1],A[i+2][j+2],A[i+3][j+3]=3,3,3,3
				#Dibujar circulo amarillo en las posiciones correspodientes
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)

			elif A[i][j]==A[i][j+1]==A[i][j+2]==A[i][j+3]==2:
				ganador=2
				jugando=False
				A[i][j],A[i+1][j+1],A[i+2][j+2],A[i+3][j+3]=3,3,3,3
				#Dibujar circulo amarillo en las posiciones correspodientes
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
			j=j+1
		i=i+1
	return jugando, ganador


def victoriavertical( A= array of array, i=int, j= int, jugando, ganador ) -> (bool,int)
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
		while j < 7 and jugando=1:
			if A[i][j]==A[i+1][j]==A[i+2][j]==A[i+3][j]==1:
				ganador=1
				jugando=0
				A[i][j],A[i+1][j+1],A[i+2][j+2],A[i+3][j+3]=3,3,3,3
				#Dibujar circulo amarillo en las posiciones correspodientes
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
			elif A[i][j]==A[i+1][j]==A[i+2][j]==A[i+3][j]==2:
				ganador=2
				jugando=False
				A[i][j],A[i+1][j+1],A[i+2][j+2],A[i+3][j+3]=3,3,3,3
				#Dibujar circulo amarillo en las posiciones correspodientes
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
			j=j+1
		i=i+1
	return jugando, ganador

def victoriadiagonalsecundaria( A= array of array, i=int, j= int, jugando, ganador) -> (bool,int)
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
		while j < 7 and jugando=True:
			#Conexion diagonal secundaria
			if j>2 and A[i][j]==A[i+1][j-1]==A[i+2][j-2]==A[i+3][j-3]==1:
				ganador=1
				jugando=False
				A[i][j],A[i+1][j+1],A[i+2][j+2],A[i+3][j+3]=3,3,3,3
				#Dibujar circulo amarillo en las posiciones correspodientes
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)

			elif j>2 and A[i][j]==A[i+1][j-1]==A[i+2][j-2]==A[i+3][j-3]==2:
				ganador=2
				jugando=False
				A[i][j],A[i+1][j+1],A[i+2][j+2],A[i+3][j+3]=3,3,3,3
				#Dibujar circulo amarillo en las posiciones correspodientes
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
				#pygame.draw.circle(pantalla, AMARILLO, evento.pos, 30, 0)
			j=j+1
		i=i+1
	return jugando, ganador

# Aqui culminan las verificaciones de las posibilidades de ganar el juego con un 4 en raya.

def IA( A=array of array, i=int, j=int )
	#Pre: 0<=i<6 and 0<=j<7
	#Post: 0<=i<6 and 0<=j<7

	#VAR:						# para esta version de la IA solo nos interesan las jugadas
	#z:int  					# que puede hacer a partir de la anterior, por lo que
	#max:int  					# la vi (vertical inferior queda descartada), y tiende a
	#hi,hd,vs,dps,dss: int  			# escoger jugadas horizontales.

	hi,hd,vs,dps,dpi,dss,dsi=0,0,0,0,0,0,0
								
	z=1					# aqui cuenta las 3 proximas posibles jugadas para armar una
	#cota= 4-z				# linea horizontal hacia la izquierda de su posicion
	while z<4 and valida(i,j-z): 	
		hi= hi+1		
		z=z+1

	z=1				    	# aqui cuenta las 3 proximas posibles jugadas para armar una
	#cota= 4-z				# linea horizontal hacia la derecha de su posicion
	while z<4 and valida(i,j+z):
		hd= hd+1
		z=z+1

	
	if valida(1+i,j):			# aqui solo se cuenta si la proxima posible jugada para armar una
		vs = vs+1		    	# linea vertical, justo arriba de su posicion

	z=1				        # aqui cuenta las 3 proximas posibles jugadas para armar una	
	#cota= 4-z				# linea diagonal principal superior (raro pero posible)
	while z<4 and valida(i-z,j-z):	 
		dps= dps+1
		z=z+1


	z=1				        # aqui cuenta las 3 proximas posibles jugadas para armar una	
	#cota= 4-z				# linea diagonal principal inferior (raro pero posible)                
	while z<4 and valida(i+z,j+z):	 
		dpi= dpi+1
		z=z+1
	

	z=1	     			    # aqui cuenta las 3 proximas posibles jugadas para armar una
	#cota= 4-z			    # linea diagonal secundaria superior (raro pero posible)
	while z<4 and valida(i-z,j+z):
		dss= dss+1
		z=z+1

	
	z=1					# aqui cuenta las 3 proximas posibles jugadas para armar una
	#cota=4-z				# diagonal secundaria inferior (raro pero posible)
	while z<4 and valida(i+z,j-z):
		dsi= dsi+1
		z=z+1
	

	max=max(hi,hd,vs,dps,dpi,dss,dsi)  	# buscamos la jugada mas "favorable"
		if max==0:			# si la pieza se encuentra rodeada, se busca un nuevo
			i,j=5,6			# lugar donde jugar.
			#cota=i
			while 0 <= i < 6:
			#cota= j
				while 0 <= j < 7:
					if valida(i,j):
						A[i][j]=2
					j=j-1
				i=i-1
			
		elif max==hi:			# la ejecutamos
			A[i][j-1]=2
			#Dibujar circulo azul en la posicion correspodiente
			#pygame.draw.circle(pantalla, AZUL, evento.pos, 30, 0)
		elif max==hd:
			A[i][j+1]=2
			#Dibujar circulo azul en la posicion correspodiente
			#pygame.draw.circle(pantalla, AZUL, evento.pos, 30, 0)
		elif max==vs:
			A[i+1][j]=2
			#Dibujar circulo azul en la posicion correspodiente
			#pygame.draw.circle(pantalla, AZUL, evento.pos, 30, 0)
		elif max==dps:
			A[i][j+1]=2
			#Dibujar circulo azul en la posicion correspodiente
			#pygame.draw.circle(pantalla, AZUL, evento.pos, 30, 0)
		elif max==dpi:
			A[i][j+1]=2
			#Dibujar circulo azul en la posicion correspodiente
			#pygame.draw.circle(pantalla, AZUL, evento.pos, 30, 0)
		elif max==dss:
			A[i][j+1]=2
			#Dibujar circulo azul en la posicion correspodiente
			#pygame.draw.circle(pantalla, AZUL, evento.pos, 30, 0)
		elif max==dsi:				
			A[i][j+1]=2
			#Dibujar circulo azul en la posicion correspodiente
			#pygame.draw.circle(pantalla, AZUL, evento.pos, 30, 0)
	return (A,i,j)

#Funciones referentes a la parte grafica 
def dibujartableronuevo():
	# Cuadrado exterior
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

        pygame.display.flip()

# Cerrar el juego
pygame.quit()
