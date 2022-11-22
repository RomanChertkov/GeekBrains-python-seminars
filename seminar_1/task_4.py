"""
Программа принимает на вход координаты двух точек
и находит расстояние между ними в 2D пространстве.
"""

def points_distance(point_a: tuple, point_b: tuple) -> float:
    """Calculate 2 points_distance"""
    return round(
            ((point_a[0]-point_b[0])**2+(point_a[1]-point_b[1])**2)**(0.5), 3
        )

def input_point(point_name: str) -> tuple:
    """Define point coords"""
    return (
        int(input(f"Введите координату X точки {point_name}\n")),
        int(input(f"Введите координату Y точки {point_name}\n"))
    )

first_point = input_point("A")
second_point = input_point("B")

print(
    "Растояние между точками",
    points_distance(first_point, second_point)
)
