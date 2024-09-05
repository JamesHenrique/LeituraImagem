from main import main
import customtkinter as ct
from customtkinter import filedialog
import webbrowser


#funçao para abir arquivo
def openFile():
    
    file = filedialog.askdirectory()
    main(file)

#função para criar botão e abrir site
def abrir_site():
    webbrowser.open("https://www.ilovepdf.com/pt/pdf_para_jpg")


app = ct.CTk()
app.geometry("500x400")
app.title("Extração de imagem para texto ")


label1 = ct.CTkLabel(app, text='\n\n\n')
label1.pack()

label = ct.CTkLabel(app, text='*Verifique antes se os pdfs contém imagens\n\n\nAcesse o site clicando no botão para converter pdf->jpg')
label.pack()

botao = ct.CTkButton(app, text="Ir para o site", command=abrir_site)
botao.pack(pady=20)

label2 = ct.CTkLabel(app, text='*Após baixar Extrair a pasta com as imagens\n\n\n Clique no botão para escolher a pasta das imagens\n ')
label2.pack()

btn = ct.CTkButton(app,text='ESCOLHA A PASTA',width=25, height=25, command=openFile)
btn.pack()

app.mainloop()