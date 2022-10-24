import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random
# cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha
co6 = "#0a64f5"   #azul                          
fundo = "#3b3b3b" # cinza

janela = Tk()
janela.configure(bg = fundo)
janela.geometry('300x300')
janela.resizable(width = False, height = False)
janela.title('Pedra Papel Tesoura')

frame_cima = Frame(janela, width = 292,height = 100, bg = fundo, relief = 'raised')
frame_cima.grid(row = 0, column = 1, padx = 4,pady = 4)

frame_baixo = Frame(janela,width = 300,height= 200, bg = co0)
frame_baixo.grid(row = 1, column = 1)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

linha_1 = Label(frame_cima,width = 145, text = "", anchor = 'center' , font= ('Ivy 1'), bg = fundo, fg = co0)
linha_1.place(x = 1, y = 1 )

linha_2 = Label(frame_cima,width = 145, text = "", anchor = 'center' , font= ('Ivy 1'), bg = fundo, fg = co0)
linha_2.place(x = 154 , y = 1 )

score_esq = Label(frame_cima,text='0',font='Ivy 35 bold', fg = co0, bg = fundo, relief = 'flat')
score_esq.place(x = 50, y = 15)

score_pontos = Label(frame_cima,text=' : ',font='Ivy 35 bold', fg = co0, bg = fundo, relief = 'flat')
score_pontos.place(x = 125, y = 10)

score_dir = Label(frame_cima,text='0',font='Ivy 35 bold', fg = co0, bg = fundo, relief = 'flat')
score_dir.place(x = 215, y = 15)

score_vc = Label(frame_cima,text='Você',font='Ivy 15 ', fg = co0, bg = fundo, relief = 'flat')
score_vc.place(x = 45, y = 75)

score_maq = Label(frame_cima,text='Máquina',font='Ivy 15 ', fg = co0, bg = fundo, relief = 'flat')
score_maq.place(x = 200, y = 75)

tesoura = Image.open('ppt/tesoura.png')
tesoura = tesoura.resize((60,60), Image.ANTIALIAS)
tesoura = ImageTk.PhotoImage(tesoura)

pedra = Image.open('ppt/pedra.png')
pedra = pedra.resize((60,60), Image.ANTIALIAS)
pedra = ImageTk.PhotoImage(pedra)

papel = Image.open('ppt/mao.png')
papel = papel.resize((60,60), Image.ANTIALIAS)
papel = ImageTk.PhotoImage(papel)

global voce, pc,rodadas, pontos_vc, pontos_pc

pontos_vc = 0
pontos_pc = 0
rodadas = 5

def iniciar_jogo(i):
    global rodadas, pontos_vc, pontos_pc
    if rodadas > 0:
        print(rodadas)
        alter = ['pedra','papel', 'tesoura']
        pc = random.choice(alter)
                       
        vc = i
        if vc == 'pedra' and pc == 'pedra':
            print('empate')
            empate = Label(frame_baixo,text = 'Empate',width = 8,anchor = 'center', bg = co3, fg = co1, font= ('Ivy 11 bold'), relief = 'flat')
            empate.place(x = 130, y = 8)
            linha_1['bg'] = co3
            linha_2['bg'] = co3
        elif vc == 'papel' and pc == 'papel':
            print('empate')
            empate = Label(frame_baixo,text = 'Empate',width = 8,anchor = 'center', bg = co3, fg = co1, font= ('Ivy 11 bold'), relief = 'flat')
            empate.place(x = 130, y = 8)      
            linha_1['bg'] = co3
            linha_2['bg'] = co3     
                  
        elif vc == 'tesoura' and pc == 'tesoura':
            print('empate')
            empate = Label(frame_baixo,text = 'Empate',width = 8,anchor = 'center', bg = co3, fg = co1, font= ('Ivy 11 bold'), relief = 'flat')
            empate.place(x = 130, y = 8)        
            linha_1['bg'] = co3
            linha_2['bg'] = co3
            
        elif vc == 'pedra' and pc == 'tesoura':
            print('vitoria')
            vitoria = Label(frame_baixo,text = 'Vítoria',width = 8,anchor = 'center', bg = co3, fg = co1, font= ('Ivy 11 bold'), relief = 'flat')
            vitoria.place(x = 135, y = 8)
            linha_1['bg'] = co6
            linha_2['bg'] = co5 
                   
        elif vc == 'papel' and pc == 'pedra':
            print('vitoria')
            vitoria = Label(frame_baixo,text = 'Vítoria',width = 8,anchor = 'center', bg = co3, fg = co1, font= ('Ivy 11 bold'), relief = 'flat')
            vitoria.place(x = 135, y = 8)
            linha_1['bg'] = co6
            linha_2['bg'] = co5 
                    
        elif vc == 'tesoura' and pc == 'papel':            
            print('vitoria')
            vitoria = Label(frame_baixo,text = 'Vítoria',width = 8,anchor = 'center', bg = co3, fg = co1, font= ('Ivy 11 bold'), relief = 'flat')
            vitoria.place(x = 135, y = 8)            
            linha_1['bg'] = co6
            linha_2['bg'] = co5 
                    
        elif vc == 'tesoura' and pc == 'pedra':
            print('Derrota')
            vitoria = Label(frame_baixo,text = 'Derrota',width = 8,anchor = 'center', bg = co3, fg = co1, font= ('Ivy 11 bold'), relief = 'flat')
            vitoria.place(x = 133, y = 8)
            linha_1['bg'] = co5
            linha_2['bg'] = co6         
        
        elif vc == 'papel' and pc == 'tesoura':
            print('Derrota')
            vitoria = Label(frame_baixo,text = 'Derrota',width = 8,anchor = 'center', bg = co3, fg = co1, font= ('Ivy 11 bold'), relief = 'flat')
            vitoria.place(x = 133, y = 8)
            linha_1['bg'] = co5
            linha_2['bg'] = co6  
        
        elif vc == 'pedra' and pc == 'papel':            
            print('Derrota')
            vitoria = Label(frame_baixo,text = 'Derrota',width = 8,anchor = 'center', bg = co3, fg = co1, font= ('Ivy 11 bold'), relief = 'flat')
            vitoria.place(x = 133, y = 8)              
            linha_1['bg'] = co5
            linha_2['bg'] = co6              
            
            
                                           
        print(vc , pc)
        
    
    
    
    
    
    
    
    else:
        end_game()
        
        
        
        
        
        
def jogando():
    global papel, tesoura, pedra, b_tesoura, b_papel, b_pedra
    tesoura = Image.open('ppt/tesoura.png')
    tesoura = tesoura.resize((60,60),Image.ANTIALIAS)
    tesoura = ImageTk.PhotoImage(tesoura)
    pedra = Image.open('ppt/pedra.png')
    pedra = pedra.resize((60,60),Image.ANTIALIAS)
    pedra = ImageTk.PhotoImage(pedra)
    papel = Image.open('ppt/mao.png')
    papel = papel.resize((60,60),Image.ANTIALIAS)
    papel = ImageTk.PhotoImage(papel) 
    b_tesoura = Button(frame_baixo,command = lambda: iniciar_jogo('tesoura'), width = 60, image = tesoura, compound = CENTER, bg = co0, fg = co0,font =('Ivy 10 bold'),anchor = CENTER, relief = 'flat')
    b_tesoura.place(x = 20, y = 50)
    b_pedra = Button(frame_baixo,command = lambda: iniciar_jogo('pedra'), width = 60, image = pedra, compound = CENTER, bg = co0, fg = co0,font =('Ivy 10 bold'),anchor = CENTER, relief = 'flat')
    b_pedra.place(x = 120, y = 50)
    b_papel = Button(frame_baixo,command = lambda: iniciar_jogo('papel'), width = 60, image = papel, compound = CENTER, bg = co0, fg = co0,font =('Ivy 10 bold'),anchor = CENTER, relief = 'flat')
    b_papel.place(x = 210, y = 50)
                   
        
        
def end_game():
    pass
    
    



b_jogar = Button(frame_baixo, width = 15,command = jogando, text = 'Jogar', compound = CENTER, bg = fundo, fg = co0,font =('Ivy 10 bold'),anchor = CENTER, relief = SOLID)
b_jogar.place(x = 100, y = 145) 





janela.mainloop()