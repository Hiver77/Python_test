
class Hand():
    def __init__(self, cards):
        copy = cards[:] #Debido a problemas de memoria.
        copy.sort()
        self.cards = cards

    @property
    def _rank_validations_from_best_to_worst(self):
        return {
            ("Three of a Kind", self._three_of_a_kind),
            ("Two Pair", self._two_pair),
            ("Pair", self._pair),
            ("High Card", self._high_card)
        }

    def best_rank(self):
        for rank in self._rank_validations_from_best_to_worst:
            name, validator_func = rank
            if validator_func():
                return name

    def _three_of_a_kind(self):
        ranks_with_three_of_a_kind = self._ranks_with_count(3)
        return len(ranks_with_three_of_a_kind) == 1

    def _two_pair(self):
        ranks_with_pairs = self._ranks_with_count(2)
        return len(ranks_with_pairs) == 2

    def _pair(self):
        ranks_with_pairs = self._ranks_with_count(2)
        return len(ranks_with_pairs) == 1

    def _high_card(self):
        return True

    def _ranks_with_count(self, count):
        # Lista de comprehensión sobre un diccionario de comprenhensión
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == count
        }

    @property
    def _card_rank_counts(self):
        card_rank_counts = {}
        for card in self.cards:
            card_rank_counts.setdefault(card.rank,0) #setdefault: Asigna 0, si no existe un calor para el rank.
            card_rank_counts[card.rank] += 1

        return card_rank_counts

