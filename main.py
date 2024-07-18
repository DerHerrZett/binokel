from binokel import preparation
from binokel import card


table = preparation.init_table(["Alice", "Bob", "Charlie"])
preparation.start_new_round(table=table)

for player in table.players:
    print(player.name)
    player.show_cards()
