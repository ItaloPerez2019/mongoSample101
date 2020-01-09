from data.owners import Owner
import services.data_service as svc



active_account: Owner  = None


def reload_account():
    global active_account
    if not active_account:
        return

    # TODO: pull owner account from the database.
    pass
