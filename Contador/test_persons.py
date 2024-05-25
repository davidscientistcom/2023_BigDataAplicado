from Entity import Entity,TypeEntity

def test_worker_creation():
    worker = Entity("david","Calle Macarena","698023",TypeEntity.WORKER)
    assert worker.name is not None, "El nombre del trabajador no se ha generado."
    assert worker.dni is not None, "La dirección del cliente no se ha generado."