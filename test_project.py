import pytest
from unittest.mock import MagicMock
from project import create_screen, setup, check_click, button_clicked, start_visualize

# Mocking a screen
@pytest.fixture
def mocked_screen():
    return MagicMock()

def test_create_screen():
    # Test that create_screen() function creates a screen object
    screen = create_screen()
    assert screen is not None

def test_setup(mocked_screen):
    # Test that setup() function sets up the menu correctly
    setup(mocked_screen)
    
    # Assert that screen.onscreenclick() is called with check_click function
    mocked_screen.onscreenclick.assert_called_once_with(check_click)

def test_button_clicked():
    # Test button_clicked function with known coordinates
    assert button_clicked(-350, 0, 0) is True
    assert button_clicked(-350, -200, 3) is True
    assert button_clicked(-350, 0, 1) is False
    assert button_clicked(-350, -200, 2) is False
    assert button_clicked(350, -200, 5) is True