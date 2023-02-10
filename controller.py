import model
import view


def run_app():
        while True:
            num = view.display_menu()
            if num == 1:
                view.get_view()
            elif num == 2:
                model.writing_txt(view.add_user())
                model.writing_csv(view.add_user())
            elif num == 3:
                pass
            elif num == 4:
                break