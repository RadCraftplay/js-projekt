from src.ui import SetupRoutesForm, FindRoutesForm, CloseReason

if __name__ == '__main__':
    setupForm = SetupRoutesForm()
    setupForm.show()

    if setupForm.close_reason == CloseReason.OK:
        findForm = FindRoutesForm(setupForm.list_of_connections)
        findForm.show()
