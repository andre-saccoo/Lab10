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
        tratte = grafo.edges( data=True )
        self._view.lista_visualizzazione.controls.append(ft.Row(controls=[ft.Text("numero di edge:"),ft.Text(str(self._model.get_num_edges()))]))
        self._view.lista_visualizzazione.controls.append(ft.Row(controls=[ft.Text("numero di nodi:"),ft.Text(str(self._model.get_num_nodes()))]))

        '''
            STAMPA PER RIGHE NORMALE
            for partenza,arrivo,guadagno in tratte:
            guadagno=guadagno["weight"]
            stampa = f"{partenza.nome}  |  {arrivo.nome}  |  {guadagno}"
            self._view.lista_visualizzazione.controls.append(ft.Text(stampa))
            self._view.page.update()'''

        #formattazione in tabella
        rows = []
        for partenza, arrivo, data in tratte:
            peso = data["weight"]
            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(partenza.nome)),
                        ft.DataCell(ft.Text(arrivo.nome)),
                        ft.DataCell(ft.Text(str(peso))),
                    ]
                )
            )

        table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Partenza")),
                ft.DataColumn(ft.Text("Arrivo")),
                ft.DataColumn(ft.Text("Guadagno")),
            ],
            rows=rows
        )
        self._view.lista_visualizzazione.controls.append(table)
        self._view.page.update()