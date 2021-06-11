from src.data import initial_connections
from src.graphs import NodePair
from src.ui import SetupRoutesForm, FindRoutesForm, CloseReason

if __name__ == '__main__':
    # Transform list of tuples into list of nodes
    # Can't do nodes in data module (circular reference)
    connections = list(map(lambda city_tuple: NodePair(city_tuple[0], city_tuple[1]), initial_connections))

    setupForm = SetupRoutesForm(connections)
    setupForm.show()

    while setupForm.close_reason == CloseReason.OK:
        findForm = FindRoutesForm(setupForm.list_of_connections)
        findForm.show()

        # WORKAROUND - problems with opening sub-dialogs
        if findForm.close_reason != CloseReason.EDIT:
            break

        setupForm = SetupRoutesForm(findForm.list_of_connections)
        setupForm.show()

        if setupForm.close_reason == CloseReason.CLOSE:
            setupForm.list_of_connections = findForm.list_of_connections
            setupForm.close_reason = CloseReason.OK
