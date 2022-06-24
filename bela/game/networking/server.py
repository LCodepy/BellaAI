import pickle
import socket
import time
import random
from _thread import start_new_thread

from bela.game.networking.commands import Commands
from ..main.bela import Bela
from ..utils.log import Log


class Server:

    def __init__(self):

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((socket.gethostname(), 22222))

        self.socket.listen()

        self.buffer = 4096

        self.games = {}
        self.client_id = 0
        self.current_game_id = 0

        while True:

            connection, address = self.socket.accept()
            Log.i("SERVER", "Client connected from " + str(address))

            player_id = 0

            self.current_game_id = self.client_id // 4
            self.client_id += 1

            if self.client_id % 4 == 1:
                self.games[self.current_game_id] = Bela(self.current_game_id)
                Log.i("SERVER", "Starting new game | id:" + str(self.current_game_id))
            else:
                player_id = (self.client_id - 1) % 4

            Log.i("SERVER", "New player joined | id:" + str(player_id) + "  | address:" + str(address))
            start_new_thread(self.client, (connection, player_id, self.current_game_id))

    def client(self, connection, player_id, game_id):
        connection.send(pickle.dumps([player_id, game_id]))
        nickname = pickle.loads(connection.recv(self.buffer))

        while True:

            try:
                data = pickle.loads(connection.recv(self.buffer))

                if game_id not in self.games:
                    break

                game = self.games[game_id]
                game.set_nickname(player_id, nickname)

                # Check commands
                if Commands.equals(data, Commands.READY_UP):
                    game.ready_up_player(player_id, True)

                self.games[game_id] = game

                connection.sendall(
                    pickle.dumps(
                        {
                            "game": game,
                        }
                    )
                )

            except (socket.error, EOFError, ):
                Log.i("SERVER", f"Player {player_id} from game {game_id} disconnected.")
                break

        connection.close()


if __name__ == "__main__":
    server = Server()
