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
        self._view.lista_visualizzazione.controls.append(ft.Row(controls=[ft.Text("numero di edge:"),ft.Text(str(self._model.get_num_edges()))]))
        self._view.lista_visualizzazione.controls.append(ft.Row(controls=[ft.Text("numero di nodi:"),ft.Text(str(self._model.get_num_nodes()))]))
        for tratta in tratte:
            self._view.lista_visualizzazione.controls.append(ft.Text(tratta))
            self._view.page.update()