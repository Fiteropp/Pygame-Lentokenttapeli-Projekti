from scenes.gameplay_scene import GameScene
from scenes.menu_scene import MenuScene
from assets import Assets
from models.db_connector import DBConnector
import ui
import scenes
import controller
import eventmanager
import model
import view


def main():

    ev_manager = eventmanager.EventManager()

    assets = Assets(ev_manager)
    game_model = model.Engine(ev_manager)
    ui_manager = ui.UIManager(ev_manager)
    scene_manager = scenes.SceneManager(ev_manager)
    graphics = view.Graphics(ev_manager, game_model, scene_manager)
    keyboard = controller.Keyboard(ev_manager, game_model)
    test_db_connector = DBConnector(ev_manager)

    scene_manager.register("menu", MenuScene(ev_manager, ui_manager, assets))
    scene_manager.register("game", GameScene(ev_manager, ui_manager, assets))

    game_model.run()

if __name__ == "__main__":
    main()
