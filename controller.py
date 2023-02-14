import model
import view


def run_app():
        while True:
            num = view.display_menu()
            if num == 1:
                model.reading_db()
            elif num == 2:
                user_info = view.add_user()
                model.writing_db(user_info)
            elif num == 3:
                model.writing_txt()
                view.export()
            elif num == 4:
                model.writing_csv()
                view.export()
            elif num == 5:
                model.logger("Выход из программы")
                break

