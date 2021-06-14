import pytest
from rest_framework.permissions import AllowAny
from rest_framework.test import APIRequestFactory
from rest_framework.views import APIView

from games.tests.factories import DesignerFactory, GameFactory, GameDesignersFactory


@pytest.fixture
def APIrequest():
    return APIRequestFactory()


@pytest.fixture
def designer_conf():
    return DesignerFactory()


@pytest.fixture
def game_conf():
    return GameFactory()


@pytest.fixture
def game_designers():
    return GameDesignersFactory


@pytest.fixture(autouse=True)
def disable_authentication(monkeypatch, request):
    """
    Use `use_auth` marker to enable authentication for the test.
    See https://pytest.readthedocs.io/en/latest/example/markers.html
    """
    if "use_auth" not in request.keywords:
        monkeypatch.setattr(APIView, "permission_classes", (AllowAny,))
