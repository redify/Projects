"""
Manage video rentals and controls when videos are checked out, due to return, 
overdue fees and for added complexity create a summary of those accounts which are overdue for contact.
"""

import Store

the_store = Store.store()

the_store.createAccount('bob')
the_store.createAccount('timmy')
the_store.createAccount('greg')

the_store.createMovie('timbucktoo')
the_store.createMovie('star trek 3')
the_store.createMovie('villia')

the_store.checkMovie('timmy', 'villia')

the_store.dumpAccountInfo('timmy')