import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QBrush, QColor

class MatrixWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.matrix = self.generate_random_matrix(15, 10)
        self.frame_pos = (0, 0)
        self.square_size = 100
        self.padding = 5
        self.initUI()

        self.column_counter_label = QLabel("Столбцы: 0/5", self)
        self.column_counter_label.move(10, 0)
        self.column_counter_label.show()

    def generate_random_matrix(self, red_count, yellow_count):
        colors = ['red'] * red_count + ['yellow'] * yellow_count
        random.shuffle(colors)
        return [colors[i:i+5] for i in range(0, 25, 5)]

    def initUI(self):
        self.setWindowTitle('Квадротека')
        self.setFixedSize((self.square_size + self.padding) * 5 - self.padding, (self.square_size + self.padding) * 5 - self.padding)

    def paintEvent(self, event):
        painter = QPainter(self)
        for row in range(5):
            for col in range(5):
                color = QColor(self.matrix[row][col])
                rect = QRect(col * (self.square_size + self.padding),
                             row * (self.square_size + self.padding),
                             self.square_size, self.square_size)
                painter.fillRect(rect, QBrush(color))
                if self.is_within_frame(row, col):
                    painter.setPen(QColor('black'))
                    painter.drawRect(rect)

    def is_within_frame(self, row, column):
        fr, fc = self.frame_pos
        return fr <= row < fr + 3 and fc <= column < fc + 3
    
    def check_victory(self):
        self.update_column_counter()
        red_columns = 0
        yellow_columns = 0
        for col in range(5):
            column_colors = [self.matrix[row][col] for row in range(5)]
            if all(color == 'red' for color in column_colors):
                red_columns += 1
            elif all(color == 'yellow' for color in column_colors):
                yellow_columns += 1

        if red_columns == 3 and yellow_columns == 2:
            return True
        else:
            return False

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Left:
            self.move_frame(0, -1)
        elif key == Qt.Key_Right:
            self.move_frame(0, 1)
        elif key == Qt.Key_Up:
            self.move_frame(-1, 0)
        elif key == Qt.Key_Down:
            self.move_frame(1, 0)
        elif key == Qt.Key_Z:
            self.rotate_frame(clockwise=False)
        elif key == Qt.Key_X:
            self.rotate_frame(clockwise=True)

    def move_frame(self, dx, dy):
        x, y = self.frame_pos
        new_x = min(max(x + dx, 0), 2)
        new_y = min(max(y + dy, 0), 2)
        self.frame_pos = (new_x, new_y)
        self.update()
        if self.check_victory():
            self.handle_victory()

    def rotate_frame(self, clockwise):
        fr, fc = self.frame_pos
        section = [row[fc:fc+3] for row in self.matrix[fr:fr+3]]
        if clockwise:
            section = [list(x)[::-1] for x in zip(*section)]
        else:
            section = list(zip(*[row[::-1] for row in section]))
        
        for r, row in enumerate(section):
            for c, val in enumerate(row):
                self.matrix[fr+r][fc+c] = val
        self.update()
        if self.check_victory():
            self.handle_victory()

    def handle_victory(self):
        QMessageBox.information(self, "Победа", "Вы собрали 5 одинаковых столбцов!")

    def update_column_counter(self):
        red_columns, yellow_columns = self.count_columns()
        total_columns = red_columns + yellow_columns
        self.column_counter_label.setText(f"Столбцы: {total_columns}/5")

    def count_columns(self):
        red_columns = 0
        yellow_columns = 0
        for col in range(5):
            column_colors = [self.matrix[row][col] for row in range(5)]
            if all(color == 'red' for color in column_colors):
                red_columns += 1
            elif all(color == 'yellow' for color in column_colors):
                yellow_columns += 1
        return red_columns, yellow_columns

def main():
    app = QApplication(sys.argv)
    ex = MatrixWindow()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()