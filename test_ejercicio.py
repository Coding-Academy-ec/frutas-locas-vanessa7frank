import ejercicio

def test_frutas():
    frutas = ejercicio.frutas
    assert frutas["manzana"] == "roja"
    assert frutas["banana"] == "amarilla"
    assert frutas["pera"] == "verde"
    assert frutas["naranja"] == "naranja"
    assert frutas.get("uva") is None

test_frutas()
