from enum import Enum

from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox

from src import *
from src.graphs import Generators, NodePair
from src.explorers import BfsExplorer


class CloseReason(Enum):
    CLOSE = 0,
    OK = 1,
    EDIT = 2


class SetupRoutesForm(object):
    def __init__(self, connection_list=None):
        if connection_list is None:
            connection_list = []

        self.list_of_connections = connection_list
        self.close_reason = CloseReason.CLOSE

        self._window = Tk()
        self._window.title("Konfiguracja połączeń")
        self._window.resizable(width=False, height=False)

        # Inner grid
        self._mainframe = ttk.Frame(self._window)
        self._mainframe.grid(column=0, row=0, sticky=(N, W, E, S), padx=5, pady=5)

        # Label over ComboBoxes
        Label(self._mainframe, text="Miasta:").grid(row=0, column=0, columnspan=2)

        # ComboBoxes
        self._city_a = Combobox(self._mainframe)
        self._city_b = Combobox(self._mainframe)

        self._city_a.grid(row=1, column=0)
        self._city_b.grid(row=1, column=1)

        self._city_a['state'] = 'readonly'
        self._city_b['state'] = 'readonly'

        self._city_a['values'] = sorted(data.cities)
        self._city_b['values'] = sorted(data.cities)

        self._city_a.set(self._city_a['values'][1])
        self._city_b.set(self._city_a['values'][2])

        # List of connected cities
        self._connections_frame = Frame(self._mainframe)
        self._connections_frame.grid(row=2, column=0, columnspan=2)

        self._connection_list = Listbox(self._connections_frame, width=45, listvariable=self.list_of_connections)
        self._connection_list.grid(row=0, column=0, sticky=(W, E))

        self._connection_list_scrollbar = Scrollbar(self._connections_frame, orient=VERTICAL)
        self._connection_list_scrollbar.grid(row=0, column=1, sticky=(N, S))

        self._connection_list.configure(yscrollcommand=self._connection_list_scrollbar.set)
        self._connection_list_scrollbar.config(command=self._connection_list.yview)

        # Conenct and disconnect buttons
        self._connect = Button(self._mainframe, text="Połącz", command=self.add_connection)
        self._connect.grid(row=3, column=0)

        self._disconnect = Button(self._mainframe, text="Rozłącz", command=self.remove_connection)
        self._disconnect.grid(row=3, column=1)

        # Confirm button
        Label(self._mainframe, text=" ").grid(row=4, column=0, columnspan=2)
        self._confirm = Button(self._mainframe, text="Zatwierdź", command=self.confirm_action)
        self._confirm.grid(row=7, column=0, columnspan=2)

        # Add existing connections
        add_connection = lambda c: self._connection_list.insert(0, c)
        for connection in reversed(self.list_of_connections):
            add_connection(connection)

    def add_connection(self):
        """
        Runs when user presses connect button
        """
        pair = NodePair(self._city_a.get(), self._city_b.get())
        inverse_pair = NodePair(pair.b, pair.a)

        if pair.a == pair.b:
            messagebox.showwarning("Nie można dodać połączenia!", "Nie można połączyć miasta z samym sobą!")
            return

        if pair in self.list_of_connections or inverse_pair in self.list_of_connections:
            messagebox.showwarning("Nie można dodać połączenia!", "Miasta są już połączone!")
            return

        # Should be one list instead of two
        # but listbox works very strangely
        self.list_of_connections.insert(0, pair)
        self._connection_list.insert(0, pair)

    def remove_connection(self):
        """
        Runs when user presses disconnect button
        """
        selected = self._connection_list.curselection()
        if len(selected) != 1:
            return

        self.list_of_connections.pop(selected[0])
        self._connection_list.delete(selected[0])

    def confirm_action(self):
        self.close_reason = CloseReason.OK
        self._window.destroy()

    def show(self):
        self._window.mainloop()


class FindRoutesForm(object):
    def __init__(self, list_of_connections):
        adjacency_lists = Generators.generate_adjacency_lists(list_of_connections)
        adjacency_matrix = Generators.generate_adjacency_matrix(list_of_connections)
        list_based_graph = graphs.ListDefinedGraph(adjacency_lists)
        matrix_based_graph = graphs.MatrixDefinedGraph(adjacency_matrix)
        self._list_explorer = BfsExplorer(list_based_graph)
        self._matrix_explorer = BfsExplorer(matrix_based_graph)
        self.close_reason = CloseReason.CLOSE
        self.list_of_connections = list_of_connections

        self._window = Tk()
        self._window.title("Wyszukiwanie połączeń")
        self._window.resizable(width=False, height=False)

        # Inner grid
        self._mainframe = ttk.Frame(self._window)
        self._mainframe.grid(column=0, row=0, sticky=(N, W, E, S), padx=5, pady=5)

        # Labels over ComboBoxes
        Label(self._mainframe, text="Z miasta:").grid(row=0, column=0)
        Label(self._mainframe, text="Do miasta:").grid(row=0, column=1)

        # ComboBoxes
        self._city_from = Combobox(self._mainframe)
        self._city_to = Combobox(self._mainframe)

        self._city_from.grid(row=1, column=0)
        self._city_to.grid(row=1, column=1)

        self._city_from['state'] = 'readonly'
        self._city_to['state'] = 'readonly'

        self._city_from['values'] = sorted(data.cities)
        self._city_to['values'] = sorted(data.cities)

        self._city_from.set(self._city_from['values'][1])
        self._city_to.set(self._city_from['values'][2])

        # Labels
        Label(self._mainframe, text=" ").grid(row=2, column=0, columnspan=2)
        Label(self._mainframe, text="Reprezentacja:").grid(row=3, column=0)

        # Graph representation
        self._representation = Combobox(self._mainframe)
        self._representation.grid(row=3, column=1)
        self._representation['state'] = 'readonly'
        self._representation['values'] = ["Macierz sąsiedztwa", "Listy sąsiedztwa"]
        self._representation.set(self._representation['values'][0])

        # Confirm button
        Label(self._mainframe, text=" ").grid(row=4, column=0, columnspan=2)
        self._search = Button(self._mainframe, text="Szukaj", command=self.search)
        self._search.grid(row=5, column=0)

        # Edit connections button
        self._edit = Button(self._mainframe, text="Edytuj poł.", command=self.edit)
        self._edit.grid(row=5, column=1)

    def search(self):
        """
        Runs when user presses search button
        """
        explorer = self._matrix_explorer if self._representation.get() == "Macierz sąsiedztwa" else self._list_explorer
        path = explorer.find_path_cities(self._city_from.get(), self._city_to.get())

        if not path:
            messagebox.showwarning("Nie udało się znaleźć połączenia", "Brak połączenia na tej trasie")
        else:
            messagebox.showinfo("Znaleziono połączenie!", utils.print_path(path))

    def edit(self):
        """
        Runs when user presses edit button
        """

        # Workaround - I had couple of problems with multiple windows,
        # so I am just closing the window and reopening configuration dialog
        self.close_reason = CloseReason.EDIT
        self._window.destroy()

    def show(self):
        self._window.mainloop()
