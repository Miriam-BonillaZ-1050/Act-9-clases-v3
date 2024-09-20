print("Actividad 9 clase humano")
print("Miriam Bonilla, Mat: 22308051281050")

#Zona de clases
class humano1050:
    #Zona de atributos
    edad=0
    fecha_nac=" "
    genero=" "
    estatura=0
    color_cabello=" "
    
    #Zona de funciones
    def correr1050(self,n):
        print(f"{n} Esta corriendo")
    def comer1050(self,n):
        print(f"{n} Esta comiendo")
    def dormir1050(self,n):
        print(f"{n} Esta durmiendo") 
    def jugar1050(self,n):
        print(f"{n} Esta jugando")   
        
#Zona de creacion de objetos
miriam=humano1050()
beom=humano1050()

#Zona de usando objetos
miriam.edad=17
miriam.fecha_nac="14/09/07"
miriam.genero="Femenino"
miriam.estatura=1.67
miriam.color_cabello="Negro"
print("Resultado para Miriam")
print(f"Edad: {miriam.edad}")
print(f"Fecha de nacimiento: {miriam.fecha_nac}")
print(f"Genero: {miriam.genero}")
print(f"Estatura: {miriam.estatura}")
print(f"Color de cabello: {miriam.color_cabello}")
miriam.correr1050("Miriam")
miriam.comer1050("Miriam")
miriam.dormir1050("Miriam")
miriam.jugar1050("Miriam")

print("")
beom.edad=23
beom.fecha_nac="13/03/01"
beom.genero="Maculino"
beom.estatura=1.81
beom.color_cabello="Rubio"
print("Resultado para Beomgyu")
print(f"Edad: {beom.edad}")
print(f"Fecha de nacimiento: {beom.fecha_nac}")
print(f"Genero: {beom.genero}")
print(f"Estatura: {beom.estatura}")
print(f"Color de cabello: {beom.color_cabello}")
beom.correr1050("Beomgyu")
beom.comer1050("Beomgyu")
beom.dormir1050("Beomgyu")
beom.jugar1050("Beomgyu")