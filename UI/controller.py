import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        txtYear = self._view._txtAnno.value

        if txtYear == "":
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(
                ft.Text(f"Attenzione, inserire un valore  nel campo anno.", color="red")
            )
            self._view.update_page()
            return

        try:
            year = int(txtYear)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(
                ft.Text(f"Attenzione, inserire un valore numerico nel campo anno.", color="red")
            )
            self._view.update_page()
            return

        self._model.buildGraph(year)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo è costituito da {self._model.get_numNodi()} nodi"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo è costituito da {self._model.get_numArchi()} archi"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo è ha {self._model.getCompConn()} componenti connesse"))
        for c in self._model.getNumNeightbours():
            self._view._txt_result.controls.append(
                ft.Text(f"{c[0]} -- {c[1]} vicini")
            )
        self._view.update_page()


