import geom_obj03 as go
import os
import csv

def test_get_stop_id_to_da_data():
    stops_workspace = go.stops_workspace
    stop_name = go.stop_name
    stop_id_fc = go.stop_id_fc
    dissemination_area_fc = go.dissemination_area_fc
    da_population_field = go.da_population_field
    expected = ('1708', 837, 32171, 115926)
    actual = go.get_stop_id_to_da_data()['CH080'][0]
    assert expected == actual

def test_write_report():
    stops_workspace = go.stops_workspace
    stop_name = go.stop_name
    stop_id_fc = go.stop_id_fc
    dissemination_area_fc = go.dissemination_area_fc
    da_population_field = go.da_population_field
    out_csv = r'C:\acgis\gis4207_prog\data\Ottawa\test_geom_obj03.csv'
    go.write_report(out_csv)
    expected = True
    actual = os.path.exists(out_csv)
    assert expected == actual
    expected = ['CH080', '1708', '837', '27.751324120559666', '232']
    with open(out_csv) as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            actual = row
            break
    assert expected == actual

