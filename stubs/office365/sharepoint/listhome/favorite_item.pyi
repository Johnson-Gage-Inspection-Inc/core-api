from office365.sharepoint.listhome.item import ListHomeItem as ListHomeItem

class FavoriteListHomeItem(ListHomeItem):
    @property
    def entity_type_name(self): ...
