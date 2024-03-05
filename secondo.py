# In una stanza entrano, uno dopo l'altro, 10 persone, rispettivamente:
# antonio, marco, andrea, luigi, tony, bruno, laura, anita, annarita, lucia
# le prime due vanno via dopo un pochino di tempo ma entrano altre tre persone
# john, alice, mary
# altre due vanno via, sempre in ordine di ingresso (primo entrato, primo a uscire)
# stampare l'elenco delle persone presenti


stanza = []
stanza.append("antonio")
stanza.append("marco")
stanza.append("andrea")
stanza.append("luigi")
stanza.append("tony")
stanza.append("bruno")
stanza.append("laura")
stanza.append("anita")
stanza.append("annarita")
stanza.append("lucia")

stanza = stanza[2:]

stanza.append("john")
stanza.append("alice")
stanza.append("mary")

stanza = stanza[2:]

print(stanza)

stanza.sort()

print(stanza)

### Seconda versione
stanza = [
    "antonio",
    "marco",
    "andrea",
    "luigi",
    "tony",
    "bruno",
    "laura",
    "anita",
    "annarita",
    "lucia",
]
stanza = stanza[2:]
stanza.extend(["john", "alice", "mary"])
stanza = stanza[2:]
print(stanza)
stanza.sort()
print(stanza)


