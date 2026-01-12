from PyQt6.QtWidgets import (
    QApplication, 
    QWidget, 
    QMainWindow, 
    QPushButton, 
    QLabel, 
    QVBoxLayout,
    QFileDialog,
    QStackedWidget)

from "." import (
    fromPDFToExcel, 
    fromPDFToWord)

import sys

def main():
    app = QApplication(sys.argv)
    
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Home")

            layout = QVBoxLayout()
            central_widget = QWidget(self)

            title = QLabel("From PDF to Office 365")
            button = QPushButton("Converti file")

            layout.addWidget(title)
            layout.addWidget(button)

            central_widget.setLayout(layout)
            self.setCentralWidget(central_widget)
    
    class ConvertFiles(QMainWindow):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("Seleziona file PDF")

            btn = QPushButton("Seleziona PDF")

            #apre il file pdf
            try:
                btn.clicked.connect(self.open_file())
            except Exception as error:
                return str(error)

            layout = QVBoxLayout(self)
            layout.addWidget(btn)
            
            self.label = QLabel("Nessun file selezionato")

        def open_file(self):
            file_path, _ = QFileDialog.getOpenFileName(
                self, "Seleziona PDF", "", "PDF files (*.pdf)"
            )
            if file_path:
                self.label.setText(file_path)

    home = MainWindow()
    convert = ConvertFiles()
    
    home.show()

    app.exec()


if __name__ == "__main__":
    main()