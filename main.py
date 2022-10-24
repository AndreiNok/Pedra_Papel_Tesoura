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

esc_vc = Label(frame_baixo,text = '',width = 8,anchor = 'center', bg = co0, fg = co1, font= ('Ivy 11 bold'), relief = 'flat')
esc_vc.place(x = 15, y = 8)
esc_pc = Label(frame_baixo,text = '',width = 8,anchor = 'center', bg = co0, fg = co1, font= ('Ivy 11 bold'), relief = 'flat')
esc_pc.place(x = 210, y = 8)



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
    global vitoria1, vitoria2, vitoria3
    global empate1, empate2, empate3
    global derrota1, derrota2, derrota3
    if rodadas > 0:
        print(rodadas)
        alter = ['pedra','papel', 'tesoura']
        pc = random.choice(alter)
                       
        vc = i
        esc_pc['text'] = pc
        esc_vc ['text'] = vc
        
        if vc == 'pedra' and pc == 'pedra':

            linha_1['bg'] = co3
            linha_2['bg'] = co3
        elif vc == 'papel' and pc == 'papel':
     
            linha_1['bg'] = co3
            linha_2['bg'] = co3     
                  
        elif vc == 'tesoura' and pc == 'tesoura':
     
            linha_1['bg'] = co3
            linha_2['bg'] = co3
            
        elif vc == 'pedra' and pc == 'tesoura':


            linha_1['bg'] = co6
            linha_2['bg'] = co5 
            pontos_vc +=1       
        elif vc == 'papel' and pc == 'pedra':

            linha_1['bg'] = co6
            linha_2['bg'] = co5 
            pontos_vc +=1         
        elif vc == 'tesoura' and pc == 'papel':            
          
            linha_1['bg'] = co6
            linha_2['bg'] = co5 
            pontos_vc +=1         
        elif vc == 'tesoura' and pc == 'pedra':


            linha_1['bg'] = co5
            linha_2['bg'] = co6         
            pontos_pc += 1
        elif vc == 'papel' and pc == 'tesoura':


            linha_1['bg'] = co5
            linha_2['bg'] = co6  
            pontos_pc += 1
        elif vc == 'pedra' and pc == 'papel':            
             
            linha_1['bg'] = co5
            linha_2['bg'] = co6              
            pontos_pc += 1
        score_esq['text'] = pontos_vc
        score_dir['text'] = pontos_pc
        rodadas -= 1
    else:
        score_esq['text'] = pontos_vc
        score_dir['text'] = pontos_pc
        end_game()
        
        
        
        
        
        
def jogando():
    global papel, tesoura, pedra, b_tesoura, b_papel, b_pedra
    b_jogar.destroy()
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
    global rodadas, pontos_vc, pontos_pc, vencedor
    pontos_pc = 0
    pontos_vc = 0
    rodadas = 5
    
    b_tesoura.destroy()
    b_papel.destroy()
    b_pedra.destroy()
    esc_vc.destroy() 
    esc_pc.destroy()

    player_vc = int(score_esq['text'])
    player_pc = int(score_dir['text'])
    
    if player_vc > player_pc:
        vencedor = Label(frame_baixo,text = 'Parabens você venceu!!!!',width = 25,anchor = 'center', bg = co6, fg = co1, font= ('Ivy 12 bold'), relief = 'flat')
        vencedor.place(x = 20, y = 50)
    elif player_vc < player_pc:
        vencedor = Label(frame_baixo,text = 'Que pena, você perdeu...',width = 25,anchor = 'center', bg = co5, fg = co1, font= ('Ivy 12 bold'), relief = 'flat')
        vencedor.place(x = 20, y = 50)
    else:
        vencedor = Label(frame_baixo,text = 'O jogo terminou empatado...',width = 25,anchor = 'center', bg = co3, fg = co1, font= ('Ivy 12 bold'), relief = 'flat')
        vencedor.place(x = 20, y = 50)        

    def jogar_novamente():
        score_dir['text'] = '0'
        score_esq['text'] = '0'
        
        vencedor.destroy()
        
        b_jogarnovamente.destroy()
       
        jogando()
    
    b_jogarnovamente = Button(frame_baixo, width = 15,command = jogar_novamente, text = 'Jogar', compound = CENTER, bg = fundo, fg = co0,font =('Ivy 10 bold'),anchor = CENTER, relief = SOLID)
    b_jogarnovamente.place(x = 100, y = 145) 


b_jogar = Button(frame_baixo, width = 15,command = jogando, text = 'Jogar', compound = CENTER, bg = fundo, fg = co0,font =('Ivy 10 bold'),anchor = CENTER, relief = SOLID)
b_jogar.place(x = 100, y = 145) 





janela.mainloop()