from Entity import Entity,TypeEntity,FakeEntity
def main():
    worker = Entity("david","Calle Macarena","698023",TypeEntity.WORKER)
    clients = FakeEntity.get_n("Persona",TypeEntity.WORKER,5)
    a = 1


if __name__ == "__main__":
    main()