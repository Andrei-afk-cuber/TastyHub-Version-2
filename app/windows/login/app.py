import customtkinter as tk
from app.windows.login.frames import MainFrame, RegistrationFrame
from app.config import ICON_PATH

# Main app window
class LoginMainApp(tk.CTk):
    def __init__(self, user_program_class, admin_program_class):
        super().__init__()

        self.user_program_class = user_program_class
        self.admin_program_class = admin_program_class

        self.geometry(f"600x400+550+250")   # Standard size 600x400
        self.title("Авторизация")
        self.iconbitmap(ICON_PATH)
        # Create the main frame
        self.main_frame = MainFrame(self)
        self.main_frame.pack(fill="both", expand=True)
        self.frames = {}

    # Change geometry method
    def change_geometry(self, new_geometry):
        # Change the window geometry
        self.geometry(new_geometry)

    # Change title method
    def change_title(self, new_title):
        # Change the window title
        self.title(new_title)

    # Open register frame method
    def open_register_frame(self):
        # Уничтожаем основной фрейм и отрисовываем фрейм регистрации
        self.main_frame.destroy()
        # Запускаем фрейм регистрации
        self.register_frame = RegistrationFrame(self)
        self.frames['register_frame'] = self.register_frame
        self.register_frame.pack(expand=True, fill="both")

    # Открываем основной фрейм
    def open_main_frame(self):
        self.destroy_all_frames()
        self.change_title("Авторизация")
        self.main_frame = MainFrame(self)
        self.main_frame.pack(fill="both", expand=True)

    def open_main_program(self, user):
        self.destroy()
        if user.admin():
            self.main_program = self.admin_program_class(user)
        else:
            self.main_program = self.user_program_class(user)

        self.main_program.mainloop()

    def destroy_all_frames(self):
        # Удаляем все фреймы, которые есть в словаре
        for frame_name, frame in self.frames.items():
            frame.destroy()
        self.frames = {}

if __name__ == '__main__':
    app = LoginMainApp()
    app.mainloop()