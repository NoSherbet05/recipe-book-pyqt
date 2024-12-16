from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from Program_form_main import Ui_MainWindow
from recipe_widget import recipe_form
import sys
import sqlite3



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.showing_recipes = []

    def set_recipes(self, recipes):
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # for recipe in recipes:
        #     self.showing_recipes.append(RecipeBase(recipe, self.scrollAreaWidgetContents))
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        # self.recipesLayout.addWidget(self.scrollArea)
        self.scrollArea

# class RecipeForm(recipe_form):
#     def __init__(self, parent=None):
#         self.setupUi(self)

# class RecipeWidget()


class RecipeBase(QWidget):
    def __init__(self, recipe, parent):
        super(QWidget, self).__init__()
        self.gridLayoutWidget = QtWidgets.QWidget(parent=parent)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 631, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.recipeBase = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.recipeBase.setContentsMargins(0, 0, 0, 0)
        self.recipeBase.setObjectName("recipeBase")
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(recipe["label"])
        self.recipeBase.addWidget(self.label_2, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.recipeBase.addWidget(self.frame, 0, 1, 3, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setObjectName(recipe["description"])
        self.recipeBase.addWidget(self.label, 1, 0, 2, 1)

    # def add_recipe(self, parent):


dummy_data = [{"rec_id": 123, "label": "agfe ", "description": "adfasf ", "time": "123:123", "servings": "1"}]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MW = MainWindow()
    MW.set_recipes(dummy_data)
    # RF = RecipeForm()
    # recipe_form.setupUi(RF,MW)
    MW.show()
    sys.exit(app.exec())


