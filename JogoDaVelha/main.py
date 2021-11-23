import sys
from jogo_velha_uic import jogo_velha
from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    velha_game = jogo_velha()
    velha_game.show()
    sys.exit(app.exec())
