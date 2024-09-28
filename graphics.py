from tkinter import ttk
from tkinter import *
from graph import DivisionChart

class MainWindow:
    def run(self):
        self.root = Tk()
        self.root.title("Цена деления")
        
        frm = ttk.Frame(self.root, padding=10)
        frm.grid
        
        ttk.Label(text="Введите значения нижнего штриха: ", font="30").grid(row=0, column=0, pady=10, padx=10)
        
        self.bottom_stroke = ttk.Entry(width=100)
        self.bottom_stroke.grid(row=1, column=0, pady=10, padx=10)
        
        ttk.Label(text="Введите значения верхнего штриха: ", font="30").grid(row=2, column=0, pady=10, padx=10)
        
        self.top_stroke = ttk.Entry(width=100)
        self.top_stroke.grid(row=3, column=0, pady=10, padx=10)
        
        ttk.Label(text="Введите количество поделов: ", font="30").grid(row=4, column=0, pady=10, padx=10)
        
        self.sections = ttk.Entry(width=100)
        self.sections.grid(row=5, column=0, pady=10, padx=10)
        
        ttk.Label(text="Введите единицу измирения", font="30").grid(row=6, column=0, pady=10, padx=10)
        
        self.unit_of_measurement = ttk.Entry(width=100)
        self.unit_of_measurement.grid(row=7, column=0, pady=10, padx=10)
        
        ttk.Button(text="Узнать цену поделов", width=100, command=self.calculation).grid(row=8, column=0, pady=10, padx=10)
        
        self.root.mainloop()
        
    def calculation(self):
        try:
            self.top = int(self.top_stroke.get())
            bottom = int(self.bottom_stroke.get())
            self.div = int(self.sections.get())
            unit = self.unit_of_measurement.get()
            
            if self.div <= 0:
                raise ValueError
        except ValueError:
            popup_error = Toplevel(self.root)
            popup_error.title("ОШИБКА!")
            Label(popup_error, text="Можно вводить только числа и поделы должны быть больше 0", font="30").grid(row=0, column=0, pady=10, padx=10)
            Button(popup_error, text="OK", width=40, command=popup_error.destroy).grid(row=1, column=0, pady=10, padx=10)
            
        the_price_is_fair = (self.top - bottom) / self.div
        
        result_popup_window = Toplevel()
        
        Label(result_popup_window, text=f"Цена вашего подела равна: {the_price_is_fair} {unit}", font="30").grid(row=0, column=0, pady=10, padx=10)
        Button(result_popup_window, text="ВЫЙТИ", command=result_popup_window.destroy, width=40).grid(row=1, column=0, pady=10, padx=10)
        Button(result_popup_window, text="ПОЛУЧИТЬ ПРЕДСТАВЛЕНИЕ ГРАФИКОМ", width=40, command=self.call_graph).grid(row=2, column=0, pady=10, padx=10)
        
    def call_graph(self):
        go_graph = DivisionChart()
        go_graph.draw(self.top, self.div)