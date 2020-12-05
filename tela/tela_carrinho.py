from tela.abstract_tela import AbstractTela
import PySimpleGUI as sg

class TelaCarrinho(AbstractTela):

    def __init__(self, controlador_carrinho):
        self.__controlador = controlador_carrinho
        self.__window = None

    def mostra_opcoes(self, produtos, produto_novo):
        layout = [
            [sg.Text("Lista de produtos")],
            [sg.Listbox(values=produtos, size=(30, 5)), sg.Listbox(values=produto_novo, size=(30,5))],
            [sg.Button("Finalizar compra")],
            [sg.Button("Adicionar ao carrinho"), sg.Button("Atualizar quantidade"), sg.Button("Remover do carrinho")],
            [sg.Button("Limpar carrinho"), sg.Cancel("Voltar")]]

        self.__controlador.lista()
        self.__window = sg.Window("Realizar Compra").Layout(layout)
        return self.open()

        #opcao = self.le_numero_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 5, 6, 7, 0])
        #return opcao

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def requisita_dados_adicionar(self):
        layout = [
            [sg.Text("Digite a quantidade do produto: ")],
            [sg.InputText()],
            [sg.Submit("Salvar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window("Quantidade de produto").Layout(layout)
        return self.open()

    def mostra_produtos_adicionados(self, codigo: int, nome: str, valor: float, quantidade: int):
        print("-----------------------------------")
        print("Codigo: ", codigo)
        print("Nome: ", nome)
        print("Valor: ", valor)
        print("Quantidade: ", quantidade)
        print("-----------------------------------")

    def requisita_dado_remover(self):
        print("------REMOVER PRODUTO DO CARRINHO------")
        codigo = self.le_numero_inteiro("Digite o codigo do produto: ", [])
        return {"codigo": codigo}

    def requisita_dado_atualizar(self):
        print("------ATUALIZAR QUANTIDADE DO PRODUTO------")
        codigo = self.le_numero_inteiro("Digite o codigo do produto que deseja atualizar a quantidade: ", [])
        quantidade = self.le_numero_inteiro("Digite a quantidade do produto que deseja atualizar: ", [])
        return {"codigo": codigo, "quantidade": quantidade}

    def avisos(self, opcao: str):
        dicionario = {
            "produto_removido": "Produto removido com sucesso",
            "compra_cancelada": "Compra cancelada!",
            "produto_adicionado": "Produto adicionado",
            "carrinho_vazio": "O carrinho está vazio",
            "quantidade_insuficiente": "Quantidade insuficiente no estoque!",
            "limpa_carrinho": "O carrinho foi esvaziado",
            "campo_vazio": "Digite um valor"
        }

        sg.Popup(dicionario[opcao])