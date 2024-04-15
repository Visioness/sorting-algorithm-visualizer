from app import VisualizerApp
from visualizers import Visualize


app = VisualizerApp()

screen = app.create_screen()
Visualize.get_screen(screen)
app.setup()
