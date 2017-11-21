from unittest import TestCase

import vcr

import lykkex.lykkex as lykkex


class TestLykkex(TestCase):
    @vcr.use_cassette('vcr_cassetes/is_alive.yml')
    def test_is_alive_returns_a_dict_with_a_field_for_possible_issues(self):
        response = lykkex.is_alive()
        self.assertTrue("IssueIndicators" in response.keys())

    @vcr.use_cassette('vcr_cassetes/order_books.yml')
    def test_get_order_books_retrieves_a_list_of_order_books(self):
        list_of_order_books = lykkex.get_order_books()
        self.assertIsInstance(list_of_order_books, list)

    @vcr.use_cassette('vcr_cassetes/order_book.yml')
    def test_get_order_book_fetches_the_correct_order_book(self):
        asset_pair_id = 'AUDUSD'
        order_book = lykkex.get_order_book(asset_pair_id)
        self.assertIsInstance(order_book, list)

        for entry in order_book:
            self.assertEqual(entry["AssetPair"], asset_pair_id)
