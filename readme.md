Jag kom på med ett system i draw.io och orkade inte ändra det.
Resultatet blev ett väldigt scuffed inventory där items måste använda sig själva
och om det finns flera olika items med samma namn finns det chans att inventoryt tar bort fel object.
Men programmet följer min draw.io sketch ganska bra.

Inventoryt hanterar att ta in och ta bort items samt kunna skicka en lista om allting som finns i det.
Ett enskillt item kan användas, säljas och inspekteras.

Om jag hadde skrivit inventoryt mer i min stil så hadde jag nog gjort liknande saker:

item.id = plats i inventoryts lista

inventory.add_item(item):
(om det finns plats i inventoryt)
(lägg till itemet i listan)
(item.id = len(list)) <-- itemet är nyligast så det borde vara i sista sloten i listan. Om listan har 2 saker så är itemet på plats 2 och har då id:t 2
detta kanske är fel skrivit men någonting liknande.

inventory_useItem(item)
itemId = item.id
list[itemId] borde vara itemet eftersom id:t är samma som dens plats i listan
item.use() <-- effekt
self.remove_item(itemId) <-- tar bort saken på den platsen så de borde vara itemet
item.destroy() <-- jag vet inte om man måste förgöra saker i python så att det inte finns en massa items i voiden som inte finns i några inventoryn

skrev detta on the fly men det känns någorlunda rätt.