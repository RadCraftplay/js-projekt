from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox

from src import *


class Generators(object):
    @staticmethod
    def get_adjacency_lists(list_of_node_pairs):
        adjacency_lists = [[] for _ in data.cities]

        for pair in list_of_node_pairs:
            a, b = pair.to_graph_node_ids()
            adjacency_lists[a].append(b)

        return adjacency_lists

    @staticmethod
    def get_adjacency_matrix(list_of_node_pairs):
        adjacency_matrix = [[0 for _ in data.cities] for _ in data.cities]

        for pair in list_of_node_pairs:
            a, b = pair.to_graph_node_ids()
            adjacency_matrix[a][b] = 1

        return adjacency_matrix


class NodePair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def to_graph_node_ids(self):
        a_id = utils.get_node_id_of_city_by_name(self.a)
        b_id = utils.get_node_id_of_city_by_name(self.b)
        return a_id, b_id

    def __str__(self):
        return "{0} <=> {1}".format(self.a, self.b)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b


# List of connections
list_of_connections = []


def add_connection():
    pair = NodePair(city_a.get(), city_b.get())
    inverse_pair = NodePair(pair.b, pair.a)

    if pair.a == pair.b:
        messagebox.showwarning("Nie można dodać połączenia!", "Nie można połączyć miasta z samym sobą!")
        return

    if pair in list_of_connections or inverse_pair in list_of_connections:
        messagebox.showwarning("Nie można dodać połączenia!", "Miasta są już połączone!")
        return

    # Should be one list instead of two
    # but listbox works very strangely
    list_of_connections.insert(0, pair)
    connection_list.insert(0, pair)


def remove_connection():
    selected = connection_list.curselection()
    if len(selected) != 1:
        return

    list_of_connections.pop(selected[0])
    connection_list.delete(selected[0])


def confirm_action():
    adjacency_lists = Generators.get_adjacency_lists(list_of_connections)
    adjacency_matrix = Generators.get_adjacency_matrix(list_of_connections)
    gl = graphs.ListDefinedGraph(adjacency_lists)
    gm = graphs.MatrixDefinedGraph(adjacency_matrix)
    lex = explorers.BfsExplorer(gl)
    mex = explorers.BfsExplorer(gm)
    gliwice = utils.get_node_id_of_city_by_name("Gliwice")
    breslau = utils.get_node_id_of_city_by_name("Wrocław")
    path_l = lex.find_path(gliwice, breslau)
    path_m = mex.find_path(gliwice, breslau)
    messagebox.showinfo("Lista: trasa", utils.print_path(path_l))
    messagebox.showinfo("Macierz: trasa", utils.print_path(path_m))


window = Tk()
window.title("Konfiguracja połączeń")
window.resizable(width=False, height=False)

# Tworzenie siatki na przyciski
mainframe = ttk.Frame(window)
# Umieszczenie siatki w oknie
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Tworzenie siatki na przyciski
mainframe = ttk.Frame(window)
# Umieszczenie siatki w oknie
mainframe.grid(column=0, row=0, sticky=(N, W, E, S), padx=5, pady=5)

#Label over ComboBoxes
Label(mainframe, text="Miasta:").grid(row=0, column=0, columnspan=2)

# ComboBoxes
city_a = Combobox(mainframe)
city_b = Combobox(mainframe)

city_a.grid(row=1, column=0)
city_b.grid(row=1, column=1)

city_a['state'] = 'readonly'
city_b['state'] = 'readonly'

city_a['values'] = sorted(data.cities)
city_b['values'] = sorted(data.cities)

city_a.set(city_a['values'][1])
city_b.set(city_a['values'][2])

# List of connected cities
connections_frame = Frame(mainframe)
connections_frame.grid(row=2, column=0, columnspan=2)

connection_list = Listbox(connections_frame, width=45, listvariable=list_of_connections)
connection_list.grid(row=0, column=0, sticky=(W, E))

connection_list_scrollbar = Scrollbar(connections_frame, orient=VERTICAL)
connection_list_scrollbar.grid(row=0, column=1, sticky=(N, S))

connection_list.configure(yscrollcommand=connection_list_scrollbar.set)
connection_list_scrollbar.config(command=connection_list.yview)

# Conenct and disconnect buttons
connect = Button(mainframe, text="Połącz", command=add_connection)
connect.grid(row=3, column=0)

disconnect = Button(mainframe, text="Rozłącz", command=remove_connection)
disconnect.grid(row=3, column=1)

# PLabels
Label(mainframe, text=" ").grid(row=4, column=0, columnspan=2)
Label(mainframe, text="Reprezentacja:").grid(row=5, column=0)

# Graph representation
representation = Combobox(mainframe)
representation.grid(row=5, column=1)
representation['state'] = 'readonly'
representation['values'] = ["Macierz sąsiedztwa", "Listy sąsiedztwa"]
representation.set(representation['values'][0])

# Confirm button
Label(mainframe, text=" ").grid(row=6, column=0, columnspan=2)
confirm = Button(mainframe, text="Zatwierdź", command=confirm_action)
confirm.grid(row=7, column=0, columnspan=2)

if __name__ == '__main__':
    window.mainloop()
    pass
