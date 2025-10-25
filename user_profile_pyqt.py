import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        
    def initializeUI(self):
        """Настройки графического интерфейса приложения."""
        self.setGeometry(50, 50, 250, 400)
        self.setWindowTitle("2.1 - User Profile GUI - PyQt6")
        self.setUpMainWindow()
        self.show()
        
    def createImageLabels(self):
        """Создаёт метки с изображениями."""
        try:
            # Фоновое изображение
            bg_label = QLabel(self)
            bg_pixmap = QPixmap("C:/Users/ilya1/Desktop/проекты py/images/skyblue.png")
            bg_label.setPixmap(bg_pixmap.scaled(250, 150, Qt.AspectRatioMode.IgnoreAspectRatio))
            bg_label.move(0, 0)
            
            # Изображение профиля
            profile_label = QLabel(self)
            profile_pixmap = QPixmap("C:/Users/ilya1/Desktop/проекты py/images/profile_image.png")
            profile_label.setPixmap(profile_pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio))
            profile_label.move(80, 20)
            
        except Exception as error:
            print(f"Image error: {error}")
            # Заглушки если изображения не найдены
            bg_label = QLabel(self)
            bg_label.setStyleSheet("background-color: lightblue;")
            bg_label.setFixedSize(250, 150)
            bg_label.move(0, 0)
            
            profile_label = QLabel(self)
            profile_label.setText("Фото профиля")
            profile_label.setStyleSheet("background-color: white; border: 1px solid black;")
            profile_label.setFixedSize(100, 100)
            profile_label.move(80, 20)
    
    def setUpMainWindow(self):
        """Создаёт метки, которые будут отображаться в окне."""
        self.createImageLabels()
        
        # Имя пользователя
        user_label = QLabel(self)
        user_label.setText("Иван Драго")
        user_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        user_label.move(60, 140)
        
        # Биография
        bio_label = QLabel(self)
        bio_label.setText("Биография")
        bio_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        bio_label.move(15, 170)
        
        about_label = QLabel(self)
        about_label.setText("Я инженер-программист с 10-летним опытом создания потрясающего кода.")
        about_label.setWordWrap(True)
        about_label.setFixedWidth(220)
        about_label.move(15, 190)
        
        # Умения
        skills_label = QLabel(self)
        skills_label.setText("Умения")
        skills_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        skills_label.move(15, 240)
        
        languages_label = QLabel(self)
        languages_label.setText("Python | PHP | SQL | JavaScript")
        languages_label.move(15, 260)
        
        # Опыт работы
        experience_label = QLabel(self)
        experience_label.setText("Опыт")
        experience_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        experience_label.move(15, 290)
        
        developer_label = QLabel(self)
        developer_label.setText("Python Разработчик")
        developer_label.move(15, 310)
        
        dev_dates_label = QLabel(self)
        dev_dates_label.setText("Март 2011 - настоящее время")
        dev_dates_label.setFont(QFont("Arial", 8))
        dev_dates_label.move(15, 330)
        
        driver_label = QLabel(self)
        driver_label.setText("Водитель доставки пиццы")
        driver_label.move(15, 350)
        
        driver_dates_label = QLabel(self)
        driver_dates_label.setText("Aug 2015 - Dec 2017")
        driver_dates_label.setFont(QFont("Arial", 8))
        driver_dates_label.move(15, 370)

# Запуск программы
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())