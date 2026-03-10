from ex0.Card import CardClass
from ex2.Combatable import CombatableClass
from ex4.Rankable import RankableClass


class TournamentCardClass(CardClass, CombatableClass, RankableClass):
    def __init__(
            self, name: str, cost: int, rarity: str,  card_id: str,
            rating: int) -> None:
        super().__init__(name, cost, rarity)
        self.wins: int = 0
        self.losses: int = 0
        self.rating = rating
        self.card_id = card_id

    def play(self, game_state: dict) -> dict:

        game_state = {
            "played": self.name
        }
        return (game_state)

    def attack(self, target) -> dict:

        won = self.rating > target.rating

        if won:
            self.rating += 16
            target.rating -= 16
            self.wins += 1
            target.losses += 1
            winner = self.name
            loser = target.name
        else:
            target.rating += 16
            self.rating -= 16
            target.wins += 1
            self.losses += 1
            winner = target.name
            loser = self.name

        return {
            'winner': winner,
            'loser': loser,
            'winner_rating': self.calculate_rating() if won
            else target.calculate_rating(),
            'loser_rating': target.calculate_rating() if won
            else self.calculate_rating()
        }

    def calculate_rating(self) -> int:
        return (self.rating)

    def get_tournament_stats(self) -> dict:
        return {
            'player': self.name,
            'rating': self.rating,
            'wins': self.wins,
            'losses': self.losses,
        }

    def defend(self, incoming_damage: int) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        pass

    def update_wins(self, wins: int) -> None:
        pass

    def update_losses(self, losses: int) -> None:
        pass

    def get_rank_info(self) -> dict:
        pass
