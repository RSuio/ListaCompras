import mysql.connector
import fpdf



class Database:
    def __init__(self):
        self.connection = mysql.connector.connect()
        self.cursor = self.connection.cursor()
        

    def adicionar_compras(self, compras):
        sql = 'INSERT INTO compras (nome, preco, quantidade) VALUES (%s, %s, %s)'
        val = (compras.nome, compras.preco, compras.quantidade)
        self.cursor.execute(sql,val)
        self.connection.commit()
        
    
    def alterar_compras(self,compras_id,compras):
        sql = 'UPDATE compras SET nome = %s, preco = %s, quantidade = %s WHERE id = %s'
        val = (compras.nome, compras.preco, compras.quantidade, compras_id)
        self.cursor.execute(sql,val)
        self.connection.commit()
        
    def retornar_compras(self):
        self.cursor.execute('SELECT * FROM compras')
        return self.cursor.fetchall()
    
    def apagar_todas_compras(self):
        self.cursor.execute("DELETE FROM compras")
        self.connection.commit()
        
    def deletar_compra(self,compra_id):
        sql = 'DELETE FROM compras WHERE id = %s'
        val = (compra_id,)
        self.cursor.execute(sql,val)
        self.connection.commit()
        
    
class Compras:
    def __init__(self,nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def __str__(self):
        return f'Nome:{self.nome}, Preço:{self.preco}, Quantidade:{self.quantidade}'
    

class Relatorio:
    def __init__(self,compras):
        self.compras = compras
        
    def gerar_pdf(self,nome_arquivo):
        pdf = fpdf.FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        pdf.cell(200, 10, txt="Relatório de Compras", ln=True, align='C')
        for compras in self.compras:
            pdf.cell(200, 10, txt=f"ID:{compras[0]} | Nome:{compras[1]} | Preço:{compras[2]} | Quantidade:{compras[3]}", ln=True)
            
        pdf.output(f'relatorios/{nome_arquivo}')
        
        
        
        

        
