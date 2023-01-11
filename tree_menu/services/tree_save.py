from collections import defaultdict

from tree_menu.models import Item


class Tree:
    def __init__(self, menu_id):
        self.menu_id = menu_id
        self.i = 1
        self.tree = self.get_tree_map()
        self.passed_items = set()

    def get_tree_map(self):
        menu_items = Item.objects.filter(menu_id=self.menu_id)
        tree_map = defaultdict(list)
        for item in menu_items:
            tree_map[item.parent_id].append(item)
        return tree_map

    def set_keys(self, start=None):
        if not start:
            start = self.tree.pop(None)
        for item in start:
            self.passed_items.add(item)
            child_items = self.tree.get(item.id, None)
            item.left_key = self.i
            self.i = self.i + 1
            if child_items:
                self.set_keys(child_items)
            item.right_key = self.i
            self.i = self.i + 1
        Item.objects.bulk_update(self.passed_items, ["right_key", "left_key"])
