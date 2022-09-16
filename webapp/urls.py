from django.urls import path

from webapp.views import index_view, get_token_view, math_action

app_name = 'webapp'

urlpatterns = [
    path('', index_view),
    path('get_token/', get_token_view, name='get_token_view'),
    path('add/', math_action, name='add'),
    path('subtract/', math_action, name='subtract'),
    path('multiply/', math_action, name='multiply'),
    path('divide/', math_action, name='divide'),
]
