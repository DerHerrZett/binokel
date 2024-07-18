from typing import List
import random

from binokel import card, player, table


def get_shuffled_deck(with_sevens=False):
    cards = []
    for rank in card.CardRank:
        for suit in card.CardSuit:
            current_card = card.Card(suit=suit, rank=rank)
            cards += [current_card, current_card]
    random.shuffle(cards)
    return cards


def init_table(players: List[str]):
    player_list = [player.Player(name=player_name) for player_name in players]
    return table.Table(players=player_list)


def start_new_round(table: table.Table):
    deck = get_shuffled_deck()

    number_of_cards = 12

    for player in table.players:
        player.cards = []
        for _ in range(number_of_cards):
            player.cards.append(deck.pop())
        player.cards = sorted(player.cards, key=lambda x: (x.suit.name, x.value))
