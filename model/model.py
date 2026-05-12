import networkx as nx

from UI.controller import Controller
from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._allBorders = None
        self._idMapBo = {}



    def buildGraph(self, year):
            self._graph.clear()
            self._allBorders = DAO.getAllBorders(year)

            for b in self._allBorders:

                self._idMapBo[b.state1ab] = b.state1nm

                self._graph.add_node(b.state1ab)
                self._graph.add_node(b.state2ab)

                if b.conttype == 1:
                    self._graph.add_edge(b.state1ab, b.state2ab)

    def getCompConn(self):
        return nx.number_connected_components(self._graph)

    def getNumNeightbours(self):
        countries = []

        for n in self._graph.nodes:
            neigh = len(list(self._graph.neighbors(n)))
            name = self._idMapBo.get(n, n)
            countries.append((name, neigh))
        order_countries = sorted(countries, key=lambda x: x[0])
        return order_countries

    def get_numNodi(self):
        return len(self._graph.nodes)

    def get_numArchi(self):
        return len(self._graph.edges)

