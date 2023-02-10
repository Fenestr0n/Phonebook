import model
import view

def run_app():
        num = view.display_menu()
        if num == 1:
            view.get_view()
        elif num == 2:
            model.writing_txt(view.add_user())
        