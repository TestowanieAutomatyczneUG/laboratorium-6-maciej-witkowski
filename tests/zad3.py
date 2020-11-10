import unittest
import json
from src.zad3 import statement

with open('../src/json/invoice.json', 'r') as f:
    invoice_data = json.load(f)

with open('../src/json/plays.json', 'r') as f:
    plays_data = json.load(f)


class StatementTest(unittest.TestCase):
    def test_data_from_json(self):
        self.assertEqual(
            statement(invoice_data, plays_data),
            "Statement for BigCo\n"
            " Hamlet: $650.00 (55 seats)\n"
            " As You Like It: $580.00 (35 seats)\n"
            " Othello: $500.00 (40 seats)\n"
            "Amount owed is $1,730.00\n"
            "You earned 47 credits\n"
        )

    def test_no_performances_no_plays(self):
        self.assertEqual(
            statement({"customer": "BigCo", "performances": []}, {}),
            "Statement for BigCo\n"
            "Amount owed is $0.00\n"
            "You earned 0 credits\n"
        )

    def test_audience_on_tragedy_greater_than_30(self):
        self.assertEqual(
            statement({"customer": "BigCo", "performances": [{"playID": "hamlet", "audience": 55}]}, {"hamlet": {"name": "Hamlet", "type": "tragedy"}}),
            "Statement for BigCo\n"
            " Hamlet: $650.00 (55 seats)\n"
            "Amount owed is $650.00\n"
            "You earned 25 credits\n"
        )

    def test_audience_on_tragedy_less_than_or_equal_30(self):
        self.assertEqual(
            statement({"customer": "BigCo", "performances": [{"playID": "othello", "audience": 23}]}, {"othello": {"name": "Othello", "type": "tragedy"}}),
            "Statement for BigCo\n"
            " Othello: $400.00 (23 seats)\n"
            "Amount owed is $400.00\n"
            "You earned 0 credits\n"
        )

    def test_audience_on_comedy_greater_than_20(self):
        self.assertEqual(
            statement({"customer": "BigCo", "performances": [{"playID": "as-like", "audience": 35}]}, {"as-like": {"name": "As You Like It", "type": "comedy"}}),
            "Statement for BigCo\n"
            " As You Like It: $580.00 (35 seats)\n"
            "Amount owed is $580.00\n"
            "You earned 12 credits\n"
        )

    def test_audience_on_comedy_less_than_or_equal_20(self):
        self.assertEqual(
            statement({"customer": "BigCo", "performances": [{"playID": "as-like", "audience": 13}]}, {"as-like": {"name": "As You Like It", "type": "comedy"}}),
            "Statement for BigCo\n"
            " As You Like It: $339.00 (13 seats)\n"
            "Amount owed is $339.00\n"
            "You earned 2 credits\n"
        )

    def test_different_type(self):
        self.assertRaises(
            ValueError,
            statement,
            {"customer": "Teatr Polski", "performances": [{"playID": "lalka", "audience": 2115}]},
            {"lalka": {"name": "lalka", "type": "tragicomedy"}}
        )

    def test_empty_data(self):
        self.assertRaises(KeyError, statement, {}, {})

    def test_no_performances_property(self):
        self.assertRaises(KeyError, statement, {"customer": "BigCo"}, {})

    def test_no_playID_property(self):
        self.assertRaises(
            KeyError,
            statement,
            {"customer": "BigCo", "performances": [{"audience": 55}]},
            {"hamlet": {"name": "Hamlet", "type": "tragedy"}}
        )

    def test_no_audience_property(self):
        self.assertRaises(
            KeyError,
            statement,
            {"customer": "BigCo", "performances": [{"playID": "hamlet"}]},
            {"hamlet": {"name": "Hamlet", "type": "tragedy"}}
        )

    def test_no_play_that_match_performance(self):
        self.assertRaises(
            KeyError,
            statement,
            {"customer": "BigCo", "performances": [{"playID": "hamlet", "audience": 55}]},
            {"as-like": {"name": "As You Like It", "type": "comedy"}}
        )

    def test_no_name_property(self):
        self.assertRaises(
            KeyError,
            statement,
            {"customer": "BigCo", "performances": [{"playID": "as-like", "audience": 13}]},
            {"as-like": {"type": "comedy"}}
        )

    def test_no_type_property(self):
        self.assertRaises(
            KeyError,
            statement,
            {"customer": "BigCo", "performances": [{"playID": "as-like", "audience": 13}]},
            {"as-like": {"name": "As You Like It"}}
        )
