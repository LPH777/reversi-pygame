import pygame
import sys
import numpy as np
from pygamewrapper import PyGameWrapper
from reversi_board import ReversiBoard

class Reversi(PyGameWrapper):
    """
        game_state:
            -1: dark side
            0: no piece
            1: light side
    """
    def __init__(self, width=600, height=600):
        screen_dim = (width, height)
        side_length = min(width, height)
        top_left = (0, 0)
        self.board = ReversiBoard(side_length, top_left)

        actions = self.board.enum
        super().__init__(width, height, actions=actions)

        self.BG_COLOR = (255, 255, 255)

    def _handle_player_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEMOTION:
                # TODO
                # show available or not
                label = self.pos2label(event.pos)
                if self._is_available(label):
                    self.board.update(label, 2)
                # self.board.update()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # TODO
                # edit status
                pos = event.pos
                print (pos)
                # self.board.update()

    def pos2label(self, pos):
        # TODO
        return ('1A')


    def get_available_actions(self):
        # TODO
        return self.actions

    def _is_available(self, label):
        # TODO
        return True

    def get_game_state(self):
        return self.board.status

    def get_actions(self):
        return self.actions

    def init(self):
        init_status = [('4D', 1), ('4E', -1), ('5D', -1), ('5E', 1)]
        for s in init_status:
            self.board.update(*s)

        self.board.draw_board(self.screen)
        self.board.draw_pieces(self.screen)

    def game_over(self):
        # TODO
        return False

    def step(self, dt):
        self._handle_player_events()
        self.board.draw_pieces(self.screen)

if __name__ == '__main__':
    pygame.init()
    game = Reversi(width=600, height=600)
    game.screen = pygame.display.set_mode(game.get_screen_dims(), 0, 32)
    game.clock = pygame.time.Clock()
    game.rng = np.random.RandomState(24)
    game.init()

    while True:
        dt = game.clock.tick_busy_loop(30)
        game.step(dt)
        pygame.display.update()