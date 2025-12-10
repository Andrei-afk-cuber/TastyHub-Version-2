import customtkinter as ctk

from app.windows.admin.admin_frames import MainFrame
from app.classes import User
from app.windows.user.user_frames import AddRecipeFrame
from app.config import ICON_PATH, night_theme, day_theme

# Основное окно приложения
class MainApp(ctk.CTk):
    def __init__(self, language, user=User(4, 'admin', '0000'), theme=day_theme):
        super().__init__()
        self.user = user
        self.theme = theme
        self.language = language

        self.geometry(f"1280x720+100+100")   # Standard size 600x400
        self.title(f"TastyHub {self.language['administrator']}")
        self.iconbitmap(ICON_PATH)
        self.resizable(False, False)
        self.configure(fg_color=theme['frame_background_color'])

        # Создаем основное окно
        self.main_frame = MainFrame(self)
        self.main_frame.pack(fill="both", expand=True)
        self.frames = {}

    # Открываем основной фрейм
    def open_main_frame(self):
        self.destroy_all_frames()
        self.main_frame = MainFrame(self)
        self.main_frame.pack(fill="both", expand=True)

    # Метод открытия фрейма для редактирования рецепта
    def open_edit_recipe_frame(self, recipe):
        # Закрываем фрейм профиля пользователя
        self.main_frame.destroy()
        # Открываем фрейм редактирования рецепта
        self.edit_recipe_frame = AddRecipeFrame(self, recipe, admin=True)
        self.frames['edit_recipe_frame'] = self.edit_recipe_frame
        self.edit_recipe_frame.pack(fill="both", expand=True)

    # Функция удаления всех фреймов
    def destroy_all_frames(self):
        # Удаляем все фреймы, которые есть в словаре
        for frame_name, frame in self.frames.items():
            frame.destroy()
        self.frames = {}

if __name__ == '__main__':
    MainApp().mainloop()