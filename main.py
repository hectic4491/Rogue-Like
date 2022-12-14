import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:

# screen size
    screen_width = 80
    screen_height = 50

# player position
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

# defining the font that will be read from
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

# builds the window, called "context"
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:

# builds the console, which is what we draw to
        root_console = tcod.Console(screen_width, screen_height, order="F")

        # Game Loop (i.e. updates every cycle)
        while True:

            #drawing to the console
            root_console.print(x=player_x, y=player_y, string="@")

            # update screen
            context.present(root_console)

            root_console.clear()

            # event handler
            for event in tcod.event.wait():
                
                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()

if __name__ == "__main__":
    main()