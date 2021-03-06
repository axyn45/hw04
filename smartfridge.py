class SmartFridge:
    """"
    >>> fridgey = SmartFridge()
    >>> fridgey.add_item('Mayo', 1)
    'I now have 1 Mayo'
    >>> fridgey.add_item('Mayo', 2)
    'I now have 3 Mayo'
    >>> fridgey.use_item('Mayo', 2.5)
    'I have 0.5 Mayo left'
    >>> fridgey.use_item('Mayo', 0.5)
    'Uh oh, buy more Mayo!'
    """

    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        "*** YOUR CODE HERE ***"
        if item not in self.items:
            self.items[item]=quantity
        else:
            self.items[item]+=quantity
        return 'I now have '+str(self.items[item])+' '+item

    def use_item(self, item, quantity):
        "*** YOUR CODE HERE ***"
        if(self.items[item-quantity]<=0):
            return 'Uh no, buy more '+item+'!'
        self.items[item]-=quantity
        return 'I have '+str(self.items[item])+' '+item+' left'

fridgey = SmartFridge()
print(fridgey.add_item('Mayo', 1))
print(fridgey.add_item('Mayo', 2))