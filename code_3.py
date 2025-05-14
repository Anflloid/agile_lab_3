zadachi = [
    {"id": 1, "nazva": "Zrobyty holovnu storinku", "status": "To Do"},
    {"id": 2, "nazva": "Dodaty knopku 'Kupyty'", "status": "To Do"},
    {"id": 3, "nazva": "Vypravyty pomylku zi vkhodom", "status": "To Do\n"}
]

def onovity_zadachu(id_zadachi, novyi_status):
    for zadacha in zadachi:
        if zadacha["id"] == id_zadachi:
            zadacha["status"] = novyi_status
            print(f"Zadacha '{zadacha['nazva']}' teper: {novyi_status}")
            return
    print("Zadachu ne znaydeno")

def pokazaty_zadachi():
    print("\nSpysok zadach:")
    for zadacha in zadachi:
        print(f"{zadacha['id']}. {zadacha['nazva']} - {zadacha['status']}")

pokazaty_zadachi()
onovity_zadachu(1, "In Progress")
onovity_zadachu(3, "Done")
pokazaty_zadachi()
