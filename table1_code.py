def create_table():
    # Tablonun sütun başlıklarını tanımlama
    headers = ["~k", "Classical Algorithm", "Smart Algorithm"]
    
    # Tablonun verilerini tanımlama
    data = [
        ["1", "1 × 1 = 1", "1"],
        ["10", "136", "29"],
        ["10^2", "136,567", "3653"],
        ["10^3", "112,464,651", "333,385"],
        ["...", "...", "..."],
        ["10^10", "1.1 × 10^26", "3.3 × 10^19"]
    ]
    
    # Sütun genişliklerini ayarlama
    col_widths = [12, 25, 20]
    
    # Başlıkları yazdırma
    header_row = "|".join(header.center(width) for header, width in zip(headers, col_widths))
    print("-" * len(header_row))
    print(header_row)
    print("-" * len(header_row))
    
    # Verileri yazdırma
    for row in data:
        row_str = "|".join(cell.center(width) for cell, width in zip(row, col_widths))
        print(row_str)
    print("-" * len(header_row))

# Tabloyu oluşturma
create_table()
