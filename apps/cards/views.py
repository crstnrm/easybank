from decimal import Decimal

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import TemplateView

from .logic import CardLogic, OperationLogic


class CardsTemplateView(TemplateView):
    template_name = 'cards.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GetCardsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logic = CardLogic()
        return Response(logic.get_cards())


class GetCardByNumberAndBrandNameView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = request.GET.dict()
        number = data.get('number')
        brand_name = data.get('brand_name')
        logic = CardLogic()
        return Response(logic.get_card_info_by_number(
            number=number,
            brand_name=brand_name
        ))


class GetCardsByPersonIdView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, person_id):
        logic = CardLogic()
        return Response(logic.get_cards_by_person_id(
            person_id=person_id
        ))


class ValidateCardOperationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = request.GET.dict()
        number = data.get('number')
        brand_name = data.get('brand_name')
        logic = CardLogic()
        card = logic.get_card(number, brand_name)
        if card is None:
            error_message = 'Card does not exists.'
            return Response(
                error_message,
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            logic.is_card_valid_to_operate(card)
        )


class GetOperationByIdView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, operation_id):
        logic = OperationLogic()
        return Response(
            logic.get_operation_info_by_id(operation_id=operation_id)
        )


class ValidateOperationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = request.GET.dict()
        amount = Decimal(data.get('amount'))
        logic = OperationLogic()
        return Response(
            logic.validate_operation(amount)
        )
