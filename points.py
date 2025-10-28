
def sort_by_point(competitors): #sorterar spelarna efter poäng
    point_sort = dict(sorted(competitors.items(), key=lambda x: x[1], reverse=True))
    point_str = '\n'
    for name, score in point_sort.items():
        point_str += f"{name}: {score}\n"
    return point_str

def sort_by_name(competitors):
    name_sort = dict(sorted(competitors.items()))# sorterar i alfabetisk ordning
    name_str = '\n'
    for name, score in name_sort.items(): #lägger till namn och poäng i tom sträng
        name_str += f"{name}: {score}\n"
    return name_str


