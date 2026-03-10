from ex4.TournamentCard import TournamentCardClass


class TournamentPlatformClass():
    def __init__(self) -> None:
        self.cards: list = []
        self.matches_played: int = 0
        self.avg_rating: int = 0

    def register_card(self, card: TournamentCardClass) -> str:

        self.cards.append(card)
        return (f'card register: {card.name}')

    def create_match(self, card1_id: str, card2_id: str) -> dict:

        self.matches_played += 1

        return {
            'player_1': card1_id,
            'player_2': card2_id
        }

    def get_leaderboard(self) -> list:
        return (self.cards)

    def generate_tournament_report(self) -> dict:

        status: str = ''
        if self.matches_played > 0:
            status = 'active'
        else:
            status = 'inactive'

        for card in self.cards:
            self.avg_rating += card.rating
        self.avg_rating /= len(self.cards)

        return {
            'total_cards': len(self.cards),
            'matches_played': self.matches_played,
            'avg_rating': self.avg_rating,
            'platform_status': status
        }
