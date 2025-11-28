from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None


    def costruisci_grafo(self, threshold):
        """ Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con guadagno medio per spedizione >= threshold (euro) """
        self.G = nx.Graph()
        lista_oggetti_hub=DAO.get_hub()
        self._dizionario_hub={}
        for hub in lista_oggetti_hub:
            self._dizionario_hub[hub.id]=hub
        self.G.add_nodes_from(lista_oggetti_hub)
        self._edges=DAO.get_tratta()
        for oggetto_tratta in self._edges:
            if oggetto_tratta.guadagno_medio >= threshold:
                hub_A=self._dizionario_hub[oggetto_tratta.id_hub_A]
                hub_B = self._dizionario_hub[oggetto_tratta.id_hub_B]
                self.G.add_edge( hub_A, hub_B,weight=oggetto_tratta.guadagno_medio)
        return self.G



    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        return self.G.number_of_edges()





    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        return self._edges

