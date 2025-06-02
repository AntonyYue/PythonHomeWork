import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_normal_item_degrades(self):
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)

    def test_normal_item_degrades_twice_after_expiry(self):
        items = [Item("Normal Item", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_quality_never_negative(self):
        items = [Item("Normal Item", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_increases_quality(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_aged_brie_does_not_exceed_50(self):
        items = [Item("Aged Brie", 2, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_backstage_passes_increase_1(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_backstage_passes_increase_2(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(27, items[0].quality)

    def test_backstage_passes_increase_3(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 45)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(48, items[0].quality)

    def test_backstage_passes_drop_to_zero(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_conjured_degrades_twice(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)  # -2

    def test_conjured_degrades_four_after_expiry(self):
        items = [Item("Conjured Mana Cake", 0, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)  # -4

    def test_conjured_quality_never_negative(self):
        items = [Item("Conjured Mana Cake", 0, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_illegal_name_becomes_fixme(self):
        items = [Item("f234", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fixme", items[0].name)

    def test_invalid_quality_below_zero(self):
        items = [Item("Aged Brie", 2, -5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreaterEqual(items[0].quality, 0)

    def test_invalid_quality_above_50_gets_capped(self):
        items = [Item("Aged Brie", 5, 55)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertLessEqual(items[0].quality, 50)

    def test_invalid_sell_in_type(self):
        items = [Item("Aged Brie", "not-an-int", 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertIsInstance(items[0].sell_in, int)

