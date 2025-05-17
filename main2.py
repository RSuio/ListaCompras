import os
from main import Database, compras, Relatorio


def main():
    if not os.path.exists('relatorios'):
        os.makedirs('relatorios')


    db = Database()
    
    while True:
        print("1. Adicionar Compra")
        print("2. Alterar Compra")
        print("3. Listar Compras")
        print("4. Apagar Todas As Compras")
        print("5. Deletar uma compra")
        print("6. Gerar Relatório em PDF")
        print("7. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        
        if escolha == '1':
            nome = input("Nome: ")
            preco = input("Preço: ")
            quantidade = input("Quantidade: ")
            compra = compras(nome,preco,quantidade)
            db.adicionar_compras(compra)
            
        elif escolha == '2':
            compras_name = input("ID da compra a alterar: ")
            nome = input("Nome: ")
            preco = input("Preço: ")
            quantidade = input("Quantidade: ")
            compra = compras(nome, preco, quantidade)
            db.alterar_compras(compras_name, compra)
            
        
        elif escolha == '3':
            compra = db.retornar_compras()
            for i in compra:
                print(i)
                
                
        elif escolha == '4':
            db.apagar_todas_compras()
            
        
        elif escolha == '5':
            compras_name = input("ID da Compra a deletar: ")
            db.deletar_compra(compras_name)
            
        elif escolha == '6':
            compra = db.retornar_compras()
            relatorio = Relatorio(compra)
            relatorio.gerar_pdf("relatorio_contatos.pdf")
            
            
        elif escolha == '7':
            break
        
        
        else:
            print("Opção inválida. Tente novamente.")
            
            
if __name__ == "__main__":
    main()