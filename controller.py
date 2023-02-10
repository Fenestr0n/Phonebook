import model
import view

def run_app():
        num = view.display_menu()
        if num == 1:
            view.get_view()
        