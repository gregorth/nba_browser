from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from rest_framework import status
from model_mommy import mommy


from .models import Player

class EndpointTest(APITestCase):
    def test_get_players(self):
        mommy.make(Player, _quantity=10)

        resp = self.client.get(reverse('player-list'), {}, format='json')

        self.assertEqual(resp.status_code, status.HTTP_200_OK)

