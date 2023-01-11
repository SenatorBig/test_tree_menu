from django.forms import ModelForm
from tree_menu.models import Item
from tree_menu.services.tree_save import Tree


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "menu", "parent"]

    def _save_m2m(self):
        parent = self.cleaned_data["parent"]
        if parent:
            self.cleaned_data["level"] = parent.level + 1
        instance = super(ItemForm, self)._save_m2m()
        menu_id = self.cleaned_data["menu"].id
        tree = Tree(menu_id)
        tree.set_keys()
        return instance
