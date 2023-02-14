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
            elif num == 4:
                pass
            elif num == 5:
                break

