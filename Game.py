import pygame as py
import threading
import random
import time 
from pygame import time as pytime  

global segundos
segundos = 0


class Boton(py.sprite.Sprite):

    def __init__(self,imagen1,imagen2,x,y):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
        
    def update(self,pantalla,cursor,Texto,x,y,valor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal
        
        pantalla.blit(self.imagen_actual,self.rect)
        pantalla.blit(Texto,(x,y))


class Cursor(py.Rect):

    def __init__(self):
        py.Rect.__init__(self,0,0,1,1)

    def update(self):
        self.left,self.top=py.mouse.get_pos()


def preguntas():
    pregunta1=["Nodo que no es raíz, ni terminal u hoja se le conoce como:","Interno","Medio","Externo","Descendente",1,"ARBOLES"]
    pregunta2=["Número de arcos que se recorren para llegar a un nodo, se conoce como:","Hermano","Niveles","Altura","Grado",2,"ARBOLES"]
    pregunta3=["¿Qué elementos crees que definen a un objeto?","Su cardinalidad y su tipo","Sus atributos y sus métodos","Establecen una comunicación","Interfaz y eventos asociados",2,"POO"]
    pregunta4=["¿Cómo se abre un archivo para leerlo?","f = open('archivo.txt','w')","f = open('read','archivo.txt')","f = open('archivo.txt', 'r')","f = open('archivo.txt','read')",3,"PYTHON"]
    pregunta5=["Cómo se inicializa una variable en java:","Int variable","Int variable=0;","variable=0","Inicializar variable en 0",2,"POO"]
    pregunta6=["Una definición de 'Clase' es...","Es similar al 'array'","Tipo particular de variable","Modelo en que creamos objetos","Categoria de datos ordenada",3,"POO"]
    pregunta7=["¿Quien es 'El Padre de la Computación'?","Blaise Pascal","Hollerith","Charles Babbage","Gottfried Leibniz",3,"PROGRAMACIÓN"]
    pregunta8=["¿Quién es el dueño y fundador de Microsoft?","Bill Gates","Mark Zuckenberg","Steve Jobs","Larry Page",1,"PROGRAMACIÓN"]
    pregunta9=["La combinación de constantes, variables, operadores, paréntesis. Es una…","Promedio","Constante","Variable","Expresión",4,"PROGRAMACIÓN"]
    pregunta10=["A que se le denomina condicional:","Decidir entre una opción u otra","Decidir si salir o entrar","Saber el proceso del programa","Proceso empleado para ordenar",1,"CONDICIONALES"]
    pregunta11=["Para que funciona el “IF”.","Expresar el caso contrario ","Para afirmar algo negativo","Evalua la expresión condicional","Ninguna de las anteriores",3,"CONDICIONALES"]
    pregunta12=["Los condicionales se trabajan con las sentencias…","WHERE AND WHILE","IF AND ELSE","FOR AND WHILE","SWITCH AND CASE",2,"CONDICIONALES"]
    pregunta13=["La forma correcta de escribir una función es","def nombrefuncion():","define nombrefuncion()","function nombrefuncion()","nombrefuncion: function()",1,"PYTHON"]
    pregunta14=["¿Cuál de ellos es un error?","xyz = 5,000,000","x,y,z = 1000, 3000, 7000","x y z = 1000 3000 7000","x_y_z = 5,000,000",3,"PYTHON"]
    pregunta15=["¿Qué significa instanciar una clase?","Duplicar una clase","Eliminar una clase","Crear un objeto por la clase","Conectar dos clases entre sí",3,"POO"]
 
    lista=[pregunta1,pregunta2,pregunta3,pregunta4,pregunta5,pregunta6,pregunta7,pregunta8,pregunta9,pregunta10,pregunta11,pregunta12,pregunta13,pregunta14,pregunta15]
    return lista

def worker():
    py.mixer_music.load("Medios/millonario.ogg")
    py.mixer_music.play(3000)
    py.mixer.music.set_volume(0.6) 

def ganancia():
    lista=[100,200,300,500,1000,2000,4000,8000,16000,32000,64000,125000,250000,500000,1000000]
    return lista

def crono():
    global segundos
    segundos = int(segundos)
    if segundos == 60:
        segundos = 0
        return crono()
    else:
        segundos += 1
        time.sleep(1)
        return crono()

def imagen_categorias(pantalla, cursor1,texto4):
    val="0"
    fondo = py.image.load("Medios/fondo2.jpg")
    pantalla.blit(fondo,(220,60))
    fuente2=py.font.SysFont("Fugaz One", 16, True, False)
    negro=(5,2,1)
    valor1=py.image.load("Medios/btnGen.png")
    valor2=py.image.load("Medios/btnGen2.png")
    boton5=Boton(valor1,valor2,310,400)
    Atext2 = fuente2.render("                CATEGORIAS ",1, negro) 
    Atext3 = fuente2.render("1.- Python.",1,negro) 
    Atext4 = fuente2.render("2.- POO.",1,negro)
    Atext5 = fuente2.render("3.- Programación(general).", 1, negro)
    Atext6 = fuente2.render("4.- Arboles.",1,negro)
    Atext7 = fuente2.render("5.- Condicionales.",1,negro)
    
    pantalla.blit(Atext2,(290,140))
    pantalla.blit(Atext3,(230,180))
    pantalla.blit(Atext4,(230,220))
    pantalla.blit(Atext5,(230,260))
    pantalla.blit(Atext6,(230,300))
    pantalla.blit(Atext7,(230,340))

    salir=False
    #LOOP PRINCIPAL
    while salir!=True:
        cursor1.update()
        boton5.update(pantalla,cursor1,texto4,345,415,"1")
        py.display.update()
        if val=="0":
            val="1"
            #audio("b") 
        for event in py.event.get():
        # si el evento es del tipo 
        # pygame.QUIT( cruz de la ventana)
            if event.type == py.QUIT:
                salir=True
                py.mixer.stop()
            if event.type == py.KEYDOWN:
                if event.unicode == "s":
                    salir=True
                    py.mixer.stop()
            if event.type == py.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton5.rect):
                    salir=True
                    py.mixer.stop()

def imagen_instrucciones(pantalla, cursor1, texto4):
    fondo = py.image.load("Medios/Fondo2.jpg")
    val="0"
    pantalla.blit(fondo,(220,60))
    fuente2=py.font.SysFont("Fugaz One", 16, True, False)
    negro=(5,2,1)
    valor1=py.image.load("Medios/btnGen.png")
    valor2=py.image.load("Medios/btnGen2.png")
    boton5=Boton(valor1,valor2,310,420)
    Atext1 = fuente2.render("              INSTRUCCIONES",1, negro)
    Atext2 = fuente2.render("1.- Este es un juego de preguntas, donde",1, negro) 
    Atext3 = fuente2.render("    tendras que elegir entre cuatro opciones",1,negro) 
    Atext4 = fuente2.render("    o falso y verdadero.",1,negro)
    Atext5 = fuente2.render("2.- Para llegar al final, debes contestar",1,negro)
    Atext6 = fuente2.render("    quince preguntas seguidas sin equivocarte.", 1, negro)
    Atext7 = fuente2.render("4. Atravez de cada tres preguntas el dinero", 1, negro)
    Atext8 = fuente2.render("   obtenido quedara asegurado", 1, negro)
    
    pantalla.blit(Atext1,(290,100))
    pantalla.blit(Atext2,(230,140))
    pantalla.blit(Atext3,(230,180))
    pantalla.blit(Atext4,(230,220))
    pantalla.blit(Atext5,(230,260))
    pantalla.blit(Atext6,(230,300))
    pantalla.blit(Atext7,(230,340))
    pantalla.blit(Atext8,(230,380))
    salir=False
    
    while salir!=True:
        cursor1.update()
        boton5.update(pantalla,cursor1,texto4,345,435,"1")
        py.display.update()
        if val=="0":
            val="1"
        for event in py.event.get():
            if event.type == py.QUIT:
                salir=True
                py.mixer.stop()
            if event.type == py.KEYDOWN:
                if event.unicode == "s":
                    salir=True
                    py.mixer.stop()
            if event.type == py.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton5.rect):
                    salir=True
                    py.mixer.stop()

def imagen_perdiste(pantalla, cursor1, contT):
    contT = str(contT)

    fondo = py.image.load("Medios/fondPerd.jpg")
    pantalla.blit(fondo,(220,30)) 
    val="0"

    valor1 = py.image.load("Medios/btnPerd1.png") 
    valor2 = py.image.load("Medios/btnPerd2.png")

    fuente1 = py.font.SysFont("Comic Sans MS", 18, True, False)
    fuente2 = py.font.SysFont("Comic Sans MS", 22, True, False)
    blanco = (255,255,255)
    negro=(5,2,1)

    jboton1 = Boton(valor1, valor2, 265, 330)
    jboton2 = Boton(valor1, valor2, 481, 329)
    
    Atext = fuente2.render("= "+contT, 1, negro)
    Atext1 = fuente1.render("REINTENTAR", 1, blanco)
    Atext2 = fuente1.render("SALIR", 1, blanco)

    pantalla.blit(Atext,(360, 185))
    salir = False

    while salir != True:
        cursor1.update()
        jboton1.update(pantalla,cursor1,Atext1,282,350,"1")
        jboton2.update(pantalla,cursor1,Atext2,530,350,"1")
        py.display.update()
        if val=="0":
            val="1"
        for event in py.event.get():
            if event.type == py.QUIT:
                salir=True
                py.mixer.stop()
            if event.type == py.KEYDOWN:
                if event.unicode == "s":
                    salir=True
                    py.mixer.stop()
            if event.type == py.MOUSEBUTTONDOWN:
                if cursor1.colliderect(jboton2.rect):
                    salir=True
                    py.mixer.stop()
                if cursor1.colliderect(jboton1.rect):
                    py.mixer.stop()
                    imagen_jugar(pantalla,cursor1)

def imagen_jugar(pantalla, cursor1):
    reloj1 = py.time.Clock()
    precio = ""
    precio2 = 0 #Ganancia inicial
    cont1 = 0 #Posicion inicial del vector de Ganancias
    contT = 0

    gan = ganancia()
    lista = preguntas()
    temp = 15 #Cantidad de preguntas

    fondo = py.image.load("Medios/fondPreg.jpg")
    pantalla.blit(fondo,(0,0))
      
    fuente1 = py.font.SysFont("Comic Sans MS", 16, True, False)
    fuente2 = py.font.SysFont("Comic Sans MS", 13, True, False)
    fuente3 = py.font.SysFont("Comic Sans MS", 18, True, False)
    negro = (5,2,1)

    valor1 = py.image.load("Medios/btnGen.png")
    valor2 = py.image.load("Medios/btnGen2.png")
    valor3 = py.image.load("Medios/salida.png")
    valor4 = py.image.load("Medios/salida2.png")
    
    jboton1 = Boton(valor1,valor2,116,306) #Pocisionamiento de botones
    jboton2 = Boton(valor1,valor2,554,306)
    jboton3 = Boton(valor1,valor2,111,400)
    jboton4 = Boton(valor1,valor2,554,400)
    jboton5 = Boton(valor3,valor4,720,90)

    hilo = threading.Thread(target = crono, args=())
    hilo.start()
    reloj1.tick(20)

    salir = False

    while salir!=True:
        global segundos
        for event in py.event.get():
            if event.type == py.QUIT:
                salir=True
            if event.type == py.KEYDOWN:
                if event.unicode == "s":
                    salir=True
        if temp==1:
            salir=True
                        
        aleatorio = random.choice(range(temp))
        temp=temp-1
        preg=lista.pop(aleatorio)
        cursor1.update()
        pantalla.blit(fondo,(0,0))

        Atext =  fuente1.render(preg[0], 1, negro)
        Atext1 = fuente2.render(preg[1], 1, negro)
        Atext2 = fuente2.render(preg[2], 1, negro) 
        Atext3 = fuente2.render(preg[3], 1, negro)
        Atext4 = fuente2.render(preg[4], 1, negro)
        Atext5 = fuente1.render(preg[6], 1, negro)
        Atext6 = fuente1.render("",1,negro)

        precio= "= "+str(precio2) # Cantidad de monedas
        precio_cont = fuente3.render(precio, 1, negro)
        pantalla.blit(precio_cont,(80,90))

        pantalla.blit(Atext,(140,240))
        pantalla.blit(Atext5,(215,150))

        jboton1.update(pantalla,cursor1,Atext1,405,330,"1")
        jboton2.update(pantalla,cursor1,Atext2,450,430,"1")
        jboton3.update(pantalla,cursor1,Atext3,65,508,"1")
        jboton4.update(pantalla,cursor1,Atext4,450,508,"1")
        jboton5.update(pantalla,cursor1,Atext6,30,90,"1")
        py.display.update()

        salir2 = False
        resp = False
        py.time.set_timer(1,0)

        while salir2!=True:
            for event2 in py.event.get():
                if event2.type == py.QUIT:
                    salir2 = True
                    py.mixer.stop()
                if event2.type == py.KEYDOWN:
                    if event2.unicode == "s":
                        salir2=True
                        py.mixer.stop()
                    if event2.unicode == "a":
                        salir2=True
                        py.mixer.stop()
                        if preg[5]==1:
                            resp= True
                            sound = py.mixer.Sound("Medios/acertas.ogg")
                            sound.play()
                            pytime.wait(1000)
                        else:
                            resp= False
                            sound = py.mixer.Sound("Medios/perdistes.ogg")
                            sound.play()
                    if event2.unicode == "b":
                        salir2=True
                        py.mixer.stop()
                        if preg[5]==2:
                            resp= True
                            sound = py.mixer.Sound("Medios/acertas.ogg")
                            sound.play()
                            pytime.wait(1000)
                        else:
                            resp= False
                            sound = py.mixer.Sound("Medios/perdistes.ogg")
                            sound.play()
                    if event2.unicode == "c":
                        salir2=True
                        py.mixer.stop()
                        if preg[5]==3:
                            resp= True
                            sound = py.mixer.Sound("Medios/acertas.ogg")
                            sound.play()
                            pytime.wait(1000)
                        else:
                            resp= False
                            sound = py.mixer.Sound("Medios/perdistes.ogg")
                            sound.play()
                    if event2.unicode == "d":
                        salir2=True
                        py.mixer.stop()
                        if preg[5]==4:
                            resp= True
                            sound = py.mixer.Sound("Medios/acertas.ogg")
                            sound.play()
                            pytime.wait(1000)
                        else:
                            resp= False
                            sound = py.mixer.Sound("Medios/perdistes.ogg")
                            sound.play()
                if event2.type == py.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(jboton1.rect):
                        salir2=True
                        py.mixer.stop()
                        if preg[5]==1:
                            resp= True
                            sound = py.mixer.Sound("Medios/acertas.ogg")
                            sound.play()
                            pytime.wait(1000)
                        else:
                            resp= False
                            sound = py.mixer.Sound("Medios/perdistes.ogg")
                            sound.play()
                    if cursor1.colliderect(jboton2.rect):
                        salir2=True
                        py.mixer.stop()
                        if preg[5]==2:
                            resp= True
                            sound = py.mixer.Sound("Medios/acertas.ogg")
                            sound.play()
                            pytime.wait(1000)
                        else:
                            resp= False
                            sound = py.mixer.Sound("Medios/perdistes.ogg")
                            sound.play() 
                    if cursor1.colliderect(jboton3.rect):
                        salir2=True
                        py.mixer.stop()
                        if preg[5]==3:
                            resp= True
                            sound = py.mixer.Sound("Medios/acertas.ogg")
                            sound.play()
                            pytime.wait(1000)
                        else:
                            resp= False
                            sound = py.mixer.Sound("Medios/perdistes.ogg")
                            sound.play()
                    if cursor1.colliderect(jboton4.rect):
                        salir2=True
                        py.mixer.stop()
                        if preg[5]==4:
                            resp= True
                            sound = py.mixer.Sound("Medios/acertas.ogg")
                            sound.play()
                            pytime.wait(1000)
                        else:
                            resp= False
                            sound = py.mixer.Sound("Medios/perdistes.ogg")
                            sound.play()
                    if cursor1.colliderect(jboton5.rect):
                        salir2=True
                        py.mixer.stop()
            
            cursor1.update()
            pantalla.blit(fondo,(0,0))
            pantalla.blit(precio_cont,(80,100))
            pantalla.blit(Atext,(140,240))
            pantalla.blit(Atext5,(385,160))

            jboton1.update(pantalla,cursor1,Atext1,124,320,"1")
            jboton2.update(pantalla,cursor1,Atext2,560,320,"1")
            jboton3.update(pantalla,cursor1,Atext3,118,420,"1")
            jboton4.update(pantalla,cursor1,Atext4,560,420,"1")
            jboton5.update(pantalla,cursor1,Atext6,30,90,"1")

            segundos = str(segundos)
            cronometro = fuente3.render("= "+segundos,1,negro)
            pantalla.blit(cronometro,(80,35))            
            
            py.display.update()

        if resp == True:
            precio2 = gan[cont1]
            cont1 = cont1+1
            contT = precio2 
        else: 
            segundos = 0
            salir = True
            imagen_perdiste(pantalla,cursor1, contT)
            

def main():
    py.init() # Inicializa el modulo
    pytime.wait(500)
    t = threading.Thread(target=worker, name='audio')
    t.start()
    val="0"
        
    pantalla=py.display.set_mode((833,499))
    py.display.set_caption("¡Programando tu Cerebro!") # Titulo de la Ventana
    
    fondo = py.image.load("Medios/Fondo.jpg")
    #py.display.set_icon(icon)
    valor1=py.image.load("Medios/btnGen.png")
    valor2=py.image.load("Medios/btnGen.png")
    valor3=py.image.load("Medios/btnGen.png")
    valor4=py.image.load("Medios/btnGen.png")
    valor5=py.image.load("Medios/btnGen2.png")
    valor6=py.image.load("Medios/btnGen2.png")
    valor7=py.image.load("Medios/btnGen2.png")
    valor8=py.image.load("Medios/btngen2.png")

    boton1=Boton(valor1,valor5,120,265)
    boton2=Boton(valor2,valor6,530,265)
    boton3=Boton(valor4,valor8,530,390)
    boton4=Boton(valor3,valor7,120,390)
    cursor1=Cursor()
    
    fuente1=py.font.SysFont("Comic Sans MS", 24, True, False)
    blanco=(255,255,255)

    texto1 = fuente1.render("         Jugar", 1, blanco)
    texto2 = fuente1.render("    Instrucciones", 1, blanco)
    texto3 = fuente1.render("        Categorias", 1, blanco)
    texto4 = fuente1.render("         Salir", 1, blanco)
    texto5 = fuente1.render("    Salir", 1, blanco) # Para boton "instrucciones" y "Categorias"
    salir=False
        
    while salir!=True:
        pantalla.blit(fondo,(0,0))
        cursor1.update()
        boton1.update(pantalla,cursor1,texto1,100,275,"1")
        boton2.update(pantalla,cursor1,texto2,524,275,"2")
        boton3.update(pantalla,cursor1,texto4,505,400,"3")
        boton4.update(pantalla,cursor1,texto3,85,400,"4")
        py.display.update() # Actualizo el display
            
        for event in py.event.get():
            if event.type == py.QUIT:
                salir=True
                py.mixer.stop()
            if event.type == py.KEYDOWN:
                if event.unicode == "s":
                    py.quit()
                    py.mixer.stop()
                if event.unicode == "j":
                    py.mixer.stop()
                    imagen_jugar(pantalla,cursor1)
                if event.unicode == "a":
                    py.mixer.stop()
                    imagen_categorias(pantalla,cursor1,texto5)
                if event.unicode == "i":
                    py.mixer.stop()
                    imagen_instrucciones(pantalla,cursor1,texto5)
            if event.type == py.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton3.rect):
                    py.mixer.stop()
                    py.quit()   
            if event.type == py.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton2.rect):
                    py.mixer.stop()
                    imagen_instrucciones(pantalla,cursor1,texto5)
            if event.type == py.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton4.rect):
                    py.mixer.stop()
                    imagen_categorias(pantalla,cursor1,texto5)
            if event.type == py.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    py.mixer.stop()
                    imagen_jugar(pantalla,cursor1)
            
        if val=="0":
            val="1"

    py.quit()
        
main() 