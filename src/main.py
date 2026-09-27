import controller
import eventmanager
import model
import view


def main():

    ev_manager = eventmanager.EventManager()
    game_model = model.Engine(ev_manager)
    keyboard = controller.Keyboard(ev_manager, game_model)
    graphics = view.Graphics(ev_manager, game_model)
    game_model.run()


if __name__ == "__main__":
    main()
