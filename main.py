

if __name__ == '__main__':
    import folium
    dir(folium)
    map = folium.Map(location=(35.61, -82.44))
    map.save('data/map1.html')

    import csv

    with open("data/volcanoes.tsv") as fd:
        rd = csv.reader(fd, delimiter="\t", quotechar='"')
        for row in rd:
            print(row)