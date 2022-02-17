def get_data(isbn):
    import requests
    isbn = str(isbn)

    payload = {
        'kl': '',
        'al': '',
        'priority': '1',
        'uid': '',
        'dist': '2',
        'lok': 'all',
        'liczba': '5',
        'pubyearh': '',
        'pubyearl': '',
        'lang': 'pl',
        'bib': 'UJ',
        'si': '1',
        'qt': 'F',
        'di': 'i' + isbn,
        'pp': '1',
        'detail': '3',
        'pm': 'm',
        'st1': 'ie' + isbn,
    }

    r = requests.get('https://karo.umk.pl/K_3.02/Exec/z2w_f.pl', params=payload)
    html = r.text
    print(r.url)
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, 'lxml')
    soup.find('table', {'class': 'fulltbl'})
    table_data = [[cell.text for cell in row("td")]
                  for row in soup("tr")]
    table_size = len(table_data)
    table_data_clean = []
    # junk off
    for i in range(table_size):
        try:
            int(table_data[i][0])
            table_data_clean.append(table_data[i])
        except:
            pass

    print(table_data_clean)

    # check if data is present
    table_data_trimmed = []
    if not table_data_clean:
        return 'No_Data'
    else:
        # trim data
        for i in range(len(table_data_clean)):
            if int(table_data_clean[i][0]) == 20:
                # ISBN
                table_data_trimmed.append(table_data_clean[i])
            if int(table_data_clean[i][0]) == 245:
                # TITLE
                table_data_trimmed.append(table_data_clean[i])
            if int(table_data_clean[i][0]) == 260:
                # PUBLISHER
                table_data_trimmed.append(table_data_clean[i])
            if int(table_data_clean[i][0]) == 700:
                # AUTHORS
                for j in range(len(table_data_clean)):
                    if int(table_data_clean[i][0]) == 700:
                        table_data_trimmed.append(table_data_clean[i])
            if int(table_data_clean[i][0] == 388):
                # TIME OF CREATION
                table_data_trimmed.append(table_data_clean[i])
    return table_data_trimmed


print(get_data(9788381181341))
