from src.ui import SetupRoutesForm, FindRoutesForm, CloseReason

if __name__ == '__main__':
    setupForm = SetupRoutesForm()
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
