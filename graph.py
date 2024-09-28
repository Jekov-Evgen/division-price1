import matplotlib.pyplot as plt

class DivisionChart:
    def draw(self, end, div):
        if div > end:
            div = max(1, end // 10) 

        graph_points = []
        y_values = []

        for i in range(0, end, div):
            y_values.append(i)
            graph_points.append(0)

        if end not in y_values:
            y_values.append(end)
            graph_points.append(0)

        plt.plot(graph_points, y_values, color='blue', marker='o', linestyle='-')
        
        plt.xlim(-1, 1)
        plt.title("Vertical Division Chart")
        plt.xlabel("X = 0") 
        plt.ylabel("Y Values")

        plt.grid(True)
        plt.show()