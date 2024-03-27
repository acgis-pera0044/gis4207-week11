import geom_obj03 as go

def test_get_stop_id_to_da_data():
    stops_workspace = go.stops_workspace
    stop_name = go.stop_name
    stop_id_fc = go.stop_id_fc
    dissemination_area_fc = go.dissemination_area_fc
    da_population_field = go.da_population_field
    expected = '1708'
    actual = go.get_stop_id_to_da_data()[1][0]
    assert expected == actual
