import PySimpleGUI as sg
from tela.abstract_tela import AbstractTela


class TelaProduto(AbstractTela):
    def __init__(self, controlador_produto):
        self.__controle = controlador_produto
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel("Reddit")
        menu_def = [
            ['File', ['Open', 'Save', 'Exit', 'Properties']]
        ]

    def mostra_opcoes(self):
        layout = [
            [sg.Text('O que você deseja?')],

            [sg.Button("Adicionar produto")],
            [sg.Button("Listar produtos")],

            [sg.Cancel("Voltar")]

        ]

        self.__window = sg.Window("Produtos").Layout(layout)
        return self.open()

    def open(self):
        button, values = self.__window.Read()
        return button, values
        if Button == "Listar produtos":
            controlador.controlador_produto.lista()
            dados_obj = values['lb_produtos'][0]




    def close(self):
        self.__window.Close()

    def requisita_dados_cadastro(self):
        layout = [
            # [sg.Menu(menu_def, tearoff=True)]
            [sg.Text('Código: ', size=(20, 1)), sg.InputText()],
            [sg.Text("Nome: ", size=(20, 1)), sg.InputText()],
            [sg.Text("Valor: ", size=(20, 1)), sg.InputText()],
            [sg.Text("Quantidade", size=(20, 2)), sg.InputText()],

            [sg.Submit("Salvar"), sg.Cancel("Cancelar")]]

        self.__window = sg.Window("Cadastro de produto").Layout(layout)


        return self.open()
        self.close()

    def mostra_dados_cadastrados(self, dados):
        layout = [
            [sg.Text("Produtos cadastrados: ")],
            [sg.Listbox(values=dados, size=(30, 5), key='lb_produtos')],
            [sg.Button("Alterar produto"), sg.Button("Remover produto"), sg.Cancel("Voltar")]]

        self.__window = sg.Window("Produtos").Layout(layout)
        return self.open()


    def requisita_dado_remover(self):
        print("------REMOVER PRODUTO------")
        codigo = self.le_numero_inteiro("Digite o codigo do produto que deseja remover: ", [])
        return codigo

    def requisita_dado_atualizar(self):
        layout = [
            [sg.Text('Código: ', size=(20, 1)), sg.InputText(key='codigo')],
            [sg.Text("Nome: ", size=(20, 1)), sg.InputText(key='nome')],
            [sg.Text("Valor: ", size=(20, 1)), sg.InputText(key='valor')],
            [sg.Text("Quantidade", size=(20, 2)), sg.InputText(key='quantidade')],

            [sg.Submit("Salvar Alteração"), sg.Cancel("Cancelar")]]

        self.__window = sg.Window("Atualização de produto").Layout(layout)

        #codigo = self.le_numero_inteiro("Digite o codigo do produto que deseja atualizar: ", [])
        return self.open()

    def atualiza_produto(self):
        nome = self.verifica_palavra("Digite o novo nome: ")

        valor = self.verifica_float("Digite o novo valor: ")

        quantidade = self.le_numero_inteiro("Digite a nova quantidade: ", [])
        return {"nome": nome, "valor": valor, "quantidade": quantidade}

    def avisos(self, opcao: str):
        dicionario = {
            "produto_ja_cadastrado": "Produto já cadastrado!",
            "produto_adicionado": "Produto adicionado ao carrinho!",
            "produto_cadastrado": "Produto cadastrado com sucesso!",
            "atualiza_produto": "Produto alterado com sucesso!",
            "remove_produto": "Produto removido do estoque!",
            "codigo_invalido": "Digite um código válido!",
            "operacao_cancelada": "Operação cancelada!",
            "campo_vazio": "Preencha todos os campos!"
        }

        sg.Popup(dicionario[opcao])