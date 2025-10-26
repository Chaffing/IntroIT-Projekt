
def sort_by_point(competitors): #sorterar spelarna efter poäng
    return dict(sorted(competitors.items(), key=lambda x: x[1], reverse=True))

def sort_by_name(competitors):
    name_sort = dict(sorted(competitors.items()))# sorterar i alfabetisk ordning
    name_str = ''
    for name, score in name_sort.items(): #lägger till namn och poäng i tom sträng
        name_str += f"{name}: {score}\n"
    return name_str


