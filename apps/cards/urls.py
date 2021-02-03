from django.conf.urls import url
from . import views


app_name = 'cards'

urlpatterns = [
    url(r'^$', views.CardsTemplateView.as_view(), name='cards-home'),
    url(r'^cards$', views.GetCardsView.as_view(), name='cards'),
    url(r'^find_card$', views.GetCardByNumberAndBrandNameView.as_view(), name='find-cards'),
    url(r'^find_card_by_person$', views.GetCardsByPersonIdView.as_view(), name='find-card-by-person'),
    url(r'^validate_card_operation$', views.ValidateCardOperationView.as_view(), name='validate-card'),
    url(r'^find_operation_by_id$', views.GetOperationByIdView.as_view(), name='find-opertation-by-id'),
    url(r'^validate_operation$', views.ValidateOperationView.as_view(), name='validate-operation')
]
