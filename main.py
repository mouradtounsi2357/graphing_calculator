import pygame,math,sys
from Fonction_de_R_dans_R import fonction

# initiation pygame -----------------------------------------------$
pygame.init()
new_space=50
width,height=400,400+new_space
display=pygame.display.set_mode((width,height))
pygame.display.set_caption("Calculatrice graphique")
clock=pygame.time.Clock()
fps=30

# classes -----------------------------------------------------------$

class Fonction():
    def __init__(self):
        self.int_x=(-5,5)
        self.int_y=(-5,5)
        self.trace=False
        self.points=[]
        self.fonction_text_syntax=''
        self.is_correct=False
        self.init_points()
        self.chek=False

        self.logo_ER=pygame.image.load("images/warning.png")
        self.warning=False

        self.mous_in=False
        self.zoom_OK=False
        self.zoom=1
        self.zoom_mnx=0

        self.up=False
        self.down=False
        self.left=False
        self.right=False
        self.speed=0.2

        self.center=(0,0)

        self.font=pygame.font.Font(None,18)
        self.text_coord=''
    
    def update(self):
        self.speed=0.08*((self.int_x[1]-self.int_x[0])/2)
        if self.up == True:
            self.int_y=(self.int_y[0]+self.speed,self.int_y[1]+self.speed)
            self.trace=True
        if self.down == True:
            self.int_y=(self.int_y[0]-self.speed,self.int_y[1]-self.speed)
            self.trace=True
        if self.left == True:
            self.int_x=(self.int_x[0]-self.speed,self.int_x[1]-self.speed)
            self.trace=True
        if self.right == True:
            self.int_x=(self.int_x[0]+self.speed,self.int_x[1]+self.speed)
            self.trace=True


        if self.mous_in == True and self.zoom_OK == True:
            self.trace=True
            self.int_x=(self.int_x[0]-self.zoom,self.int_x[1]+self.zoom)
            self.zoom_OK=False
            self.zoom=1
            

        if self.trace :
            self.trace=False
            self.correction()
            self.reinit_points()
            self.center=(float(0),float(0))
            
            
            for i in range(0,len(self.points),1):
                output=fonction((self.fonction_text_syntax),self.points[i][0],False)
                self.points[i]=(self.points[i][0],output)
                
                if output == "Error":
                    self.warning=True
            
            if self.warning == True:
                self.warning=False
                self.draw_warning()
            else:
                self.translate()
                self.unit_homothesie()
                self.project()
                arrier_sup_tach()

                pygame.draw.line(display,(200,200,200),(self.center[0],height),(self.center[0],0),1)
                pygame.draw.line(display,(200,200,200),(0,self.center[1]),(width,self.center[1]),1)

                self.draw_line()
                self.draw_point()
                
                self.draw_number()

                pygame.draw.line(display,(0,200,0),(width/2,180),(width/2,width-180),1)
                pygame.draw.line(display,(0,200,0),(180,width/2),(width-180,width/2),1)

    def draw_number(self):
        k=str("%.2f" % float((self.int_x[1]+self.int_x[0])/2))
        l=str("%.2f" % float((self.int_y[1]+self.int_y[0])/2))
        self.text_coord='( '+k+' , '+l+' )'
        self.coord_rend=self.font.render(self.text_coord,True,(200,200,00))
        display.blit(self.coord_rend,(int(width/2)+5,int(width/2)+5))
        
        k=str("%.2f"%self.int_x[0])
        self.coord_rend=self.font.render(k,True,(00,200,00))
        display.blit(self.coord_rend,(0,max(0,min(width-self.coord_rend.get_height(),self.center[1]))))

        k=str("%.2f"%self.int_x[1])
        self.coord_rend=self.font.render(k,True,(00,200,00))
        display.blit(self.coord_rend,(width-self.coord_rend.get_width(),max(0,min(width-10,self.center[1]))))
        
        k=str("%.2f"%self.int_y[1])
        self.coord_rend=self.font.render(k,True,(00,200,00))
        display.blit(self.coord_rend,(max(0,min(self.center[0]+5,width-self.coord_rend.get_width())),0))

        k=str("%.2f"%self.int_y[0])
        self.coord_rend=self.font.render(k,True,(00,200,00))
        display.blit(self.coord_rend,(max(0,min(self.center[0]+5,width-self.coord_rend.get_width())),width-self.coord_rend.get_height()))

    def translate(self):
        tmp1=(self.int_x[1]+self.int_x[0])/2
        tmp2=(self.int_y[1]+self.int_y[0])/2
        self.center=(self.center[0]-tmp1,self.center[1]-tmp2)
        for i in range(0,len(self.points),1):
            if self.points[i][1] != "nan":
                self.points[i]=(self.points[i][0]-tmp1,self.points[i][1]-tmp2)

    def unit_homothesie(self):
        self.center=(self.center[0]/((self.int_x[1]-self.int_x[0])/2),self.center[1]/((self.int_x[1]-self.int_x[0])/2))
        for i in range(0,len(self.points),1):
            if self.points[i][1] != "nan":
                self.points[i]=(self.points[i][0]/((self.int_x[1]-self.int_x[0])/2),self.points[i][1]/((self.int_x[1]-self.int_x[0])/2))
                
    def project(self):
        self.center=(int((width/2)*(self.center[0])+(width/2)),int((-width/2)*(self.center[1])+(width/2)))
        for i in range(0,len(self.points),1):
            if self.points[i][1] != "nan":
                self.points[i]=(int((width/2)*(self.points[i][0])+(width/2)),int((-width/2)*(self.points[i][1])+(width/2)))

    def draw_warning(self):
        arrier_sup_tach_war()
        display.blit(self.logo_ER,((width-self.logo_ER.get_width()+40)/2,60))
    
    def draw_point(self):
        for i in range(0,len(self.points),1):
            if self.points[i][1] != "nan":
                if math.sqrt((self.points[i][0])**2+(self.points[i][1])**2) <= 2*width:
                    pygame.draw.rect(display,(200,0,0),(self.points[i][0],self.points[i][1],1,1))
                
    
    def draw_line(self):
        for i in range(0,len(self.points)-1,1):
            if self.points[i][1] != "nan" and self.points[i+1][1] !="nan":
                if math.sqrt((self.points[i+1][0])**2+(self.points[i+1][1])**2) <= 2*width and math.sqrt((self.points[i][0])**2+(self.points[i][1])**2) <= 2*width :
                    pygame.draw.line(display,(200,0,0),self.points[i],self.points[i+1],2)
                
    def correction(self):
        tb=[]
        s=self.fonction_text_syntax
        for i in range(0,len(self.fonction_text_syntax)-1,1):
            if s[i] == '*' and s[i+1] == '*':
                tb.append(i)
        s_=''
        for i in range(0,len(s),1):
            var_bool=False
            for j in range(0,len(tb),1):
                if i == tb[j]:
                    s_+='^'
                    var_bool=True
                if i == tb[j]+1:
                    var_bool=True
            if var_bool == False:
                s_+=s[i]
        self.fonction_text_syntax=s_
    
    def init_points(self):
        self.nbp=80
        for i in range(0,self.nbp+1,1):
            self.points.append((self.int_x[0]+i*((self.int_x[1]-self.int_x[0])/self.nbp),"nan"))
        
    
    def reinit_points(self):
        for i in range(0,self.nbp+1,1):
            self.points[i]=(self.int_x[0]+i*((self.int_x[1]-self.int_x[0])/self.nbp),"nan")


class Input():
    def __init__(self):
        self.text_tab=[]
        self.text_str=''
        self.text_red=[]
        self.curseur=0
        self.font=pygame.font.Font(None,32)
        self.text_str_surface=self.font.render(self.text_str,True,(255,255,255))
        self.text_str_surface_pos=(100,height-new_space)

        self.aff_av_curseur=[]
        self.aff_av_CS=self.font.render(self.text_str,True,(255,255,255))

        
class Image_f():
    def __init__(self):
        self.pos=(0,height-new_space)
        self.image=pygame.image.load("images/fonction_image.png")
        self.w_h=(self.image.get_width(),self.image.get_height())
        self.k=(new_space)/self.image.get_height()
        self.image=pygame.transform.scale(self.image,(int(self.k*self.w_h[0]),int(self.k*self.w_h[1])))
        self.w_h=(self.image.get_width(),self.image.get_height())

class Bouton():
    def __init__(self):
        self .pos=(0,0)
        self.d_image=pygame.image.load("images/graph.png")
        self.k=new_space/self.d_image.get_height()
        self.d_image=pygame.transform.scale(self.d_image,(int(self.k*self.d_image.get_width()),int(self.k*self.d_image.get_height())))
        self.w_h=(self.d_image.get_width(),self.d_image.get_height())

        self.S=[]
        self.S.append(pygame.image.load("images/1.png"))
        self.S.append(pygame.image.load("images/2.png"))
        self.S.append(pygame.image.load("images/3.png"))
        self.S.append(pygame.image.load("images/4.png"))
        for i in range(0,4,1):
            self.S[i]=pygame.transform.scale(self.S[i],(int(self.k*self.S[i].get_width()),int(self.k*self.S[i].get_height())))

        self.selected=False
        self.clicked=False
        self.enter=False
        self.dt=0
    
    def draw(self):
        if (self.selected and self.clicked) or (self.selected==False and self.clicked==False) :
            display.blit(self.d_image,self.pos)
        elif self.selected :
            self.dt=(self.dt+(0.4))%4
            display.blit(self.S[int(self.dt)],self.pos)


# fonctions --------------------------------------------$
def arrier_inf_tach():
    pygame.draw.rect(display,(100,100,100),(0,height-new_space,width,new_space))

def arrier_sup_tach():
    pygame.draw.rect(display,(0,0,40),(0,0,width,height-new_space))

def arrier_sup_tach_war():
    pygame.draw.rect(display,(200,100,0),(0,0,width,height-new_space))
    

# classe des variables ---------------------------------$
class Variable():
    def __init__(self):
        self.fonction=Fonction()
        self.input_=Input()
        self.image_f=Image_f()
        self.bouton=Bouton()
# declaration des variables ----------------------------$
VAR=Variable()

# setup ------------------------------------------------$
VAR.input_.text_str_surface_pos=(VAR.image_f.image.get_width()+10,VAR.input_.text_str_surface_pos[1]+int(new_space/3))
VAR.bouton.pos=(width-VAR.bouton.w_h[0],height-VAR.bouton.w_h[1])
arrier_sup_tach()
pygame.draw.line(display,(200,200,200),(width/2,0),(width/2,width),1)
pygame.draw.line(display,(200,200,200),(0,width/2),(width,width/2),1)


while 1:
    # input et logique ------------------------------------$
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if VAR.input_.curseur > 0:
                    VAR.input_.curseur-=1
            elif event.key == pygame.K_RIGHT:
                if VAR.input_.curseur < len(VAR.input_.text_tab):
                    VAR.input_.curseur+=1
            elif event.key == pygame.K_BACKSPACE:
                if VAR.input_.curseur > 0:
                    l=[]
                    for i in range(0,len(VAR.input_.text_tab),1):
                        if i != (VAR.input_.curseur-1):
                            l.append(VAR.input_.text_tab[i])
                    VAR.input_.text_tab=[]
                    for i in range(0,len(l),1):
                        VAR.input_.text_tab.append(l[i])
                    VAR.input_.curseur-=1
            elif event.key == pygame.K_DELETE:
                if VAR.input_.curseur >= 0:
                    l=[]
                    for i in range(0,len(VAR.input_.text_tab),1):
                        if i != (VAR.input_.curseur):
                            l.append(VAR.input_.text_tab[i])
                    VAR.input_.text_tab=[]
                    for i in range(0,len(l),1):
                        VAR.input_.text_tab.append(l[i])
                    
            elif event.key == pygame.K_END :
                VAR.input_.curseur=len(VAR.input_.text_tab)
            elif event.key == pygame.K_HOME:
                VAR.input_.curseur=0
            elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                VAR.bouton.enter=True
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                pass
            elif event.key == pygame.K_INSERT:
                VAR.input_.text_tab=[]
                VAR.input_.curseur=0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pass
            else:
                VAR.input_.text_tab.insert(VAR.input_.curseur,event.unicode)
                VAR.input_.curseur+=1
            
            if event.key == pygame.K_UP :
                if pygame.mouse.get_focused():
                    VAR.fonction.up=True
            if event.key == pygame.K_DOWN :
                if pygame.mouse.get_focused():
                    VAR.fonction.down=True
            if event.key == pygame.K_LEFT :
                if pygame.mouse.get_focused():
                    VAR.fonction.left=True
            if event.key == pygame.K_RIGHT :
                if pygame.mouse.get_focused():
                    VAR.fonction.right=True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or pygame.mouse.get_focused() == 0:
                VAR.fonction.up=False
            if event.key == pygame.K_DOWN or pygame.mouse.get_focused() == 0:
                VAR.fonction.down=False
            if event.key == pygame.K_LEFT or pygame.mouse.get_focused() == 0:
                VAR.fonction.left=False
            if event.key == pygame.K_RIGHT or pygame.mouse.get_focused() == 0:
                VAR.fonction.right=False
                
        if event.type  == pygame.MOUSEBUTTONDOWN:
            if VAR.bouton.selected == True and pygame.mouse.get_pressed()[0]:
                VAR.bouton.clicked=True
            if event.button == 4:
                # zoom out
                if VAR.fonction.zoom_mnx > -6:
                    VAR.fonction.zoom_mnx-=1
                    VAR.fonction.zoom_OK=True
                    VAR.fonction.zoom=((VAR.fonction.int_x[1]-VAR.fonction.int_x[0])/2)/2
                
            if event.button == 5:
                # zoom in
                if VAR.fonction.zoom_mnx < 20:
                    VAR.fonction.zoom_mnx+=1
                    VAR.fonction.zoom_OK=True
                    VAR.fonction.zoom=-((VAR.fonction.int_x[1]-VAR.fonction.int_x[0])/2)/3
                
    # mouse position ------------------------------------$
    mouse_pos=pygame.mouse.get_pos()

    # mise ajour ----------------------------------------$
    # input text organisation ---------------------------$
    VAR.input_.text_str=''.join(VAR.input_.text_tab)
    VAR.input_.text_red=[]
    VAR.input_.aff_av_curseur=[]
    

    if VAR.input_.curseur < 10:
        for i in range(0,min(len(VAR.input_.text_str),20)):
            VAR.input_.text_red.append(VAR.input_.text_str[i])

            if i < VAR.input_.curseur :
                VAR.input_.aff_av_curseur.append(VAR.input_.text_str[i])
            
    elif VAR.input_.curseur > len(VAR.input_.text_str)-10:
        for i in range(max(0,len(VAR.input_.text_str)-20),len(VAR.input_.text_str)):
            VAR.input_.text_red.append(VAR.input_.text_str[i])

            if i < VAR.input_.curseur :
                VAR.input_.aff_av_curseur.append(VAR.input_.text_str[i])
            
    else:
        for i in range(max(0,VAR.input_.curseur-10),min(len(VAR.input_.text_str),VAR.input_.curseur+10)):
            VAR.input_.text_red.append(VAR.input_.text_str[i])

            if i < VAR.input_.curseur :
                VAR.input_.aff_av_curseur.append(VAR.input_.text_str[i])
            
    VAR.input_.text_red=''.join(VAR.input_.text_red)
    VAR.input_.aff_av_curseur=''.join(VAR.input_.aff_av_curseur)
    
    # boutton -------------------------------------------$
    # selection du bouton -------------------------------$
    if pygame.mouse.get_focused() and mouse_pos[0]> width-VAR.bouton.w_h[0] and mouse_pos[1] > height-new_space:
        VAR.bouton.selected=True
    else:
        VAR.bouton.selected=False
    # action du bouton ----------------------------------$
    if VAR.bouton.selected and VAR.bouton.clicked or VAR.bouton.enter:
        VAR.bouton.clicked=False
        VAR.bouton.enter=False
        VAR.fonction.fonction_text_syntax=''+VAR.input_.text_str
        VAR.fonction.trace=True

    # mouse in graph ------------------------------------$
    if mouse_pos[1]<width and pygame.mouse.get_focused() == 1:
        VAR.fonction.mous_in=True
    else:
        VAR.fonction.mous_in=False
        

    # fonction organisation -----------------------------$
    VAR.fonction.update()

    # dessiner ------------------------------------------$
    
    # dessiner la partie superieur ----------------------$
    
    
    # dessiner sur une nouvelle surface -----------------$
    VAR.input_.text_str_surface=VAR.input_.font.render(VAR.input_.text_red,True,(0,0,0))
    VAR.input_.aff_av_CS=VAR.input_.font.render(VAR.input_.aff_av_curseur,True,(0,0,0))

    # dessiner la partie inferieur ----------------------$
    # arrier -------------------------------------------$
    arrier_inf_tach()
    
    # afficher le text ---------------------------------$
    display.blit(VAR.input_.text_str_surface,VAR.input_.text_str_surface_pos)
    # dessiner le curseur ------------------------------$
    pygame.draw.rect(display,(0xFF,0x97,00),(VAR.input_.text_str_surface_pos[0]+VAR.input_.aff_av_CS.get_width(),VAR.input_.text_str_surface_pos[1],10,20),1)
    # dessiner un cadre noire --------------------------$
    pygame.draw.rect(display,(0,0,0),(VAR.image_f.w_h[0],height-new_space,width-(VAR.image_f.w_h[0]+VAR.bouton.w_h[0])-1,new_space),3)
    # dessiner le bord ---------------------------------$
    pygame.draw.rect(display,(255,0,0),(VAR.input_.text_str_surface_pos[0]-5,VAR.input_.text_str_surface_pos[1]-10,min(width-(VAR.image_f.w_h[0]+VAR.bouton.w_h[0]+18),max(100,VAR.input_.text_str_surface.get_width()+20)),37),2)
    
    # dessiner l'image f(x) ----------------------------$
    display.blit(VAR.image_f.image,VAR.image_f.pos)

    # afficher le bouton sur l'ecran -------------------$
    VAR.bouton.draw()

    #mise a jour de lecran ------------------------------$
    pygame.display.flip()
    clock.tick(fps)