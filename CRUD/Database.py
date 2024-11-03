from . import Operation

DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "judul":255*" ",
    "penulis":255*" ",
    "tahun":"yyyy"
}

def init_console():
    try:
        with open(DB_NAME, "r") as file:
            print("Database tersedia, init done!")
    except:
        print("Database tidak ditemukan!")
        Operation.create_first_data()