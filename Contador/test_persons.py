from Person import Worker

def test_worker_creation():
    worker = Worker()
    assert worker.name is not None, "El nombre del trabajador no se ha generado."
    assert worker.dni is not None, "La dirección del cliente no se ha generado."