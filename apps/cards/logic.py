from .constants import LIMIT_AMOUNT_OPERATION
from .serializers import CardSerializer
from .models import Card, Operation
from django.utils import timezone


class CardLogic:

    def get_card(self, number, brand_name):
        try:
            card = Card.objects.get(
                number=number,
                brand__name=brand_name
            )
        except Card.DoesNotExist:
            return
        return card

    def get_cards(self):
        cards = Card.objects.all().select_related('cardholder', 'brand')
        data = CardSerializer(cards).data
        return data

    def get_card_info_by_number(self, number, brand_name):
        card = self.get_card(number, brand_name)
        if card is None:
            raise Card.DoesNotExist
        data = CardSerializer(card).data
        return data

    def get_cards_by_person_id(self, person_id):
        card = Card.objects.filter(cardholder_id=person_id)
        data = CardSerializer(card, many=True).data
        return data

    def is_card_valid_to_operate(self, card):
        now = timezone.now().date()
        expires = card.expires.date()
        is_valid = expires > now
        return is_valid

    def validate_cards(self, card1, card2):
        differente_numbers = card1.number != card2.number
        different_brands = card1.brand_id != card2.brand_id
        return differente_numbers and different_brands


class OperationLogic:

    def get_operation_info_by_id(self, operation_id):
        operation = Operation.objects.filter(
            id=operation_id
        ).select_related(
            'card__brand'
        )
        if operation is None:
            return

        card = operation.card
        brand = card.brand
        data = {
            'amount': operation.amount,
            'card': {
                'number': card.number,
                'brand_name': brand.name,
                'rate': card.rate
            }
        }
        return data

    def validate_operation(self, amount):
        is_valid = amount <= LIMIT_AMOUNT_OPERATION
        return is_valid
