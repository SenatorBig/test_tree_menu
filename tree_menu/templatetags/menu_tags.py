from django import template

from tree_menu.models import Item

register = template.Library()


@register.inclusion_tag("tags/draw_menu.html", takes_context=True)
def draw_menu(context, menu_name):
    request = context["request"]
    levels = request.resolver_match.kwargs
    all_items = Item.objects.filter(menu__name=menu_name).order_by("left_key")
    items = []
    current_item = None
    if levels:
        for item in all_items:
            if item.name == levels["name"]:
                current_item = item
                break
        if current_item:
            for item in all_items:
                if item.right_key > current_item.left_key and item.level <= current_item.level + 1:
                    items.append(item)
    else:
        for item in all_items:
            if item.level == 0:
                items.append(item)
    return {"items": items}


@register.filter(name='times')
def times(number):
    return range(number)
