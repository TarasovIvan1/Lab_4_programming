Добавочка

''Лабораторная №4''
import pygame
from pygame.draw import *
from random import randint,choice


pygame.init()

FPS = 30 #кол-во обновлений в секунду
width, hight = 1200,900 # ширина и высота
screen = pygame.display.set_mode((width,hight)) # Вывод экрана

# Задание цветов для шаров
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
GREEN = (0,255,0)
MAGENTA = (255,0,255)
CYAN = (0,255,255)
BLACK = (0,0,0)
COLORS = [RED,BLUE,YELLOW,GREEN,MAGENTA,CYAN]


num_balls = 10 #Количество шаров на экране 

balls = []  #Массив с шарами

font = pygame.font.SysFont('arial', 30) # Для вывода очков 


score = 0  #Переменная 

def new_ball(): #Для задания всех параметров для нового шара
    
    x = randint(100,1100)
    y = randint(100,900)
    r = randint(10,100)
    color = choice(COLORS)
    dx,dy = randint(-5,5),randint(-5,5)  
    return [x,y,r,color,dx,dy]

def draw_ball(ball): # Для вывода шара по ранее заданным параметрам
    
    circle(screen,ball[3],(ball[0],ball[1]),ball[2])

def move_ball(ball): #Для перемещения шаров с помощью смещения
    
    ball[0] += ball[4] 
    ball[1] += ball[5]
    if ball[0] - ball[2] < 0 or ball[0] + ball[2] > width: #Если координата x касается левой или правой стороны
        ball[4] = -ball[4]
    if ball[1] - ball[2] < 0 or ball[1] + ball[2] > hight: #Если координата y касается нижней или верхней стороны
        ball[5] = -ball[5]

def check_click(event,ball):#проверка, что клик был внутри шара
    
    distance = ((event.pos[0] - ball[0])**2 + (event.pos[1] - ball[1])**2)**0.5  
    return distance < ball[2]


# Начало работы программы

text_pos = (10, 10) # координаты вывода текста


for I in range(num_balls):  #Задание нужного количества шаров
    balls.append(new_ball())

pygame.display.update()

clock = pygame.time.Clock()

finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                if check_click(event,ball):
                    score += 1
                    print(f"{score}")
                    balls.remove(ball) #удаление шара, на который нажали
                    balls.append(new_ball()) #Добавление нового шара

    screen.fill(BLACK)
    for ball in balls:
        draw_ball(ball) #Вывод шаров
        move_ball(ball) #Движение шара
    
        

    show_score = font.render(f'{score}', True, (255, 255, 255)) #Вывод обновлённого счёта
    screen.blit(show_score, text_pos) #Вывод счёта
    pygame.display.update() #обновление дисплея
    pygame.display.update()
    


pygame.quit()
