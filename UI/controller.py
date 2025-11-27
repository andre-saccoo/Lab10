import flet as ft
from UI.view import View
from Model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """

        self._view.lista_visualizzazione.clean()
        grafo=self._model.costruisci_grafo(float(self._view.guadagno_medio_minimo.value))
        tratte = grafo.edges()
        self._view.lista_visualizzazione.controls.append(ft.Text(self._model.get_num_edges())) #stampo il numero di tratte
        self._view.lista_visualizzazione.controls.append(ft.Text(self._model.get_num_edges()))
        nome_partenza=''
        nome_arrivo=''
        for tratta in tratte:
            for hub in grafo.nodes():
                print(hub)
                if tratta[0]== hub.id:
                    nome_partenza=hub.nome
                if tratta[1]== hub.id:
                    nome_arrivo=hub.nome
            self._view.lista_visualizzazione.controls.append(ft.Text(nome_partenza,nome_arrivo,tratta))
            self._view.page.update()

