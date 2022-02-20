import yaml

from errors import TooManyMatchesError, ItemNotExistError, ItemAlreadyExistsError
from item import Item
from shopping_cart import ShoppingCart


class Store:
    def __init__(self, path):
        with open(path) as inventory:
            items_raw = yaml.load(inventory, Loader=yaml.FullLoader)['items']
        self._items = self._convert_to_item_objects(items_raw)
        self._shopping_cart = ShoppingCart()

    @staticmethod
    def _convert_to_item_objects(items_raw):
        return [Item(item['name'],
                     int(item['price']),
                     item['hashtags'],
                     item['description'])
                for item in items_raw]

    def get_items(self) -> list:
        return self._items

    """Search items by name that are not in the shopping cart by name and sorts them"""
    def search_by_name(self, item_name: str) -> list:
        itemAndCount = []
        for i in self._items:
            # Checks if the item isn't in the shopping cart and the item name contains the item name that we search
            if i not in self._shopping_cart.cart and item_name in i.name:
                itemAndCount.append((i, i.name, sum(self.cart_hashtags().count(idx) for idx in i.hashtags)))
        # Sorting the array first by the name and then by the hashtags count
        itemAndCount = sorted(itemAndCount, key=lambda x: x[1])
        itemAndCount = sorted(itemAndCount, key=lambda x: x[2], reverse=True)
        return [row[0] for row in itemAndCount]
    pass

    """Search items by hashtags that are not in the shopping cart by name and sorts them"""
    def search_by_hashtag(self, hashtag: str) -> list:
        itemAndCount = []
        for i in self._items:
            # Checks if the item isn't in the shopping cart and the item name contains the item name that we search
            if i not in self._shopping_cart.cart and hashtag in i.hashtags:
                itemAndCount.append((i, i.name, sum(self.cart_hashtags().count(idx) for idx in i.hashtags)))
        # Sorting the array first by the name and then by the hashtags count
        itemAndCount = sorted(itemAndCount, key=lambda x: x[1])
        itemAndCount = sorted(itemAndCount, key=lambda x: x[2],  reverse=True)
        return [row[0] for row in itemAndCount]
    pass

    """Adds an item to the shopping cart"""
    def add_item(self, item_name: str):
        counter = 0
        # Checks if the item already in the shopping cart
        for item in self._items:
            if item_name in item.name:
                search = item
                counter += 1
        if counter > 1:
            raise TooManyMatchesError
            return
        if counter == 0:
            raise ItemNotExistError
            return
        if search in self._shopping_cart.cart:
            raise ItemAlreadyExistsError
            return
        self._shopping_cart.add_item(search)
        pass

    """Removes an item from the shopping cart"""
    def remove_item(self, item_name: str):
        counter = 0
        # Checks if the item is indeed in the shopping cart
        for item in self._items:
            if item_name in item.name:
                search = item
                counter += 1
        if counter > 1:
            raise TooManyMatchesError
            return
        if counter == 0:
            raise ItemNotExistError
            return
        self._shopping_cart.remove_item(search.name)
        pass

    """Return the subtotal cost of the shopping cart"""
    def checkout(self) -> int:
        return self._shopping_cart.get_subtotal()
        pass

    """Return a list with hashtags of the items that are in the shopping cart"""
    def cart_hashtags(self) -> list:
        hashtags = []
        for item in self._shopping_cart.cart:
            hashtags += item.hashtags
        return hashtags


# <html>
#   <body>
#       <script>
# 		<!--
# 		function checkSubmit(id) {
# 		var myform = document.getElementById(id);
# 		var val = myform['iagree'].checked;
# 		if (val == True) {
# 		alert("Must check I agree");
# 		return false;
# 		}
# 		return true;
# 		}
# 		-->
#       </script>
#   <form id="myform" action="/play" onsubmit=“return checkSubmit(‘myform’);”>
#    <input type='checkbox' name="iagree" value="yes">I Agree<br>
#    <input type='text' name='register'>
#    <input type='submit'>
#   </form>
#   </body>
# </html>


#
# var globalCounter = 1;
# var timerId = window.setInterval(updateTimer, 1000);
# function updateTimer(){
# alert("Counting!");
# if (globalCounter > 10){
# window.clearInterval(timerId);
# }
# }
#
