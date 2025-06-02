# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):
    VALID_ITEM_NAMES = [
        "Aged Brie",
        "Backstage passes to a TAFKAL80ETC concert",
        "Sulfuras, Hand of Ragnaros",
        "Conjured Mana Cake"
    ]

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self._validate_item(item)

            if item.name == "Sulfuras, Hand of Ragnaros":
                continue  # Sulfuras never changes

            if item.name == "Aged Brie":
                self._update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._update_backstage(item)
            elif "Conjured" in item.name:
                self._update_conjured(item)
            else:
                self._update_normal(item)

            item.sell_in -= 1

            if item.sell_in < 0:
                if item.name == "Aged Brie":
                    self._increase_quality(item)
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = 0
                elif "Conjured" in item.name:
                    self._decrease_quality(item, 2)
                else:
                    self._decrease_quality(item)

    def _validate_item(self, item):
        if item.name not in self.VALID_ITEM_NAMES and not item.name.startswith("Conjured"):
            item.name = "fixme"

        if not isinstance(item.quality, int) or item.quality < 0:
            item.quality = 0
        elif item.name != "Sulfuras, Hand of Ragnaros":
            item.quality = min(item.quality, 50)

        if not isinstance(item.sell_in, int):
            item.sell_in = 0

    def _increase_quality(self, item, step=1):
        if item.quality < 50:
            item.quality = min(50, item.quality + step)

    def _decrease_quality(self, item, step=1):
        if item.quality > 0:
            item.quality = max(0, item.quality - step)

    def _update_aged_brie(self, item):
        self._increase_quality(item)

    def _update_backstage(self, item):
        self._increase_quality(item)
        if item.sell_in < 11:
            self._increase_quality(item)
        if item.sell_in < 6:
            self._increase_quality(item)

    def _update_conjured(self, item):
        self._decrease_quality(item, step=2)

    def _update_normal(self, item):
        self._decrease_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)