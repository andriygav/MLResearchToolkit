import pytest

from ml_research_toolkit.notifications import TelegramClient

def test_raise_token():
    with pytest.raises(ValueError):
        notificator = TelegramClient(token=None)