import model
import view


def run_app():
        while True:
            num = view.display_menu()
            if num == 1:
                view.get_view()
            elif num == 2:
                user_info = view.add_user()
                model.writing_txt(user_info)
                model.writing_csv(user_info)
            elif num == 3:
                pass
            elif num == 4:
                break