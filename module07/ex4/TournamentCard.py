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
        self.target = target
        self.winner: str = ''
        self.loser: str = ''
        self.winner_rating: int = 0
        self.loser_rating: int = 0
        if self.rating > target.rating:
            self.winner = self.name
            self.rating += 16
            self.winner_rating = self.rating
            self.loser = target.name
            target.rating -= 16
            self.loser_rating = target.rating
            self.wins += 1
            target.losses += 1
        else:
            self.winner = target.name
            target.rating += 16
            self.winner_rating = target.rating
            self.loser = self.name
            self.rating -= 16
            self.loser_rating = self.rating
            target.wins += 1
            self.losses += 1
        return {
            'winner': self.winner,
            'loser': self.loser,
            'winner_rating': self.winner_rating,
            'loser_rating': self.loser_rating
        }

    def calculate_rating(self) -> int:
        return (self.winner_rating + self.loser_rating)

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
