# SELECT * FROM users where id = 1
# INSERT INTO users (id, name, age) (1, "Rafael", 15)
# ORM - Object Relational Mapper

from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, create_engine, delete, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()
# String de conexion
engine = create_engine("sqlite:///:memory:")


class Alumno(Base):
    __tablename__ = "alumnos"

    # id, nombres, apellidos, carnet
    # nullable=False : Campo obligatorio
    id = Column(Integer, primary_key=True)
    nombres = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    genero = Column(String)
    # unique=True hace la campo unico, no se puede repetir
    carnet = Column(Integer, unique=True)

    # back_populates="alumno" hace referencia a:
    # alumno = relationship("Alumno", back_populates="notas") de la clase "Nota"
    # El primer parametro hace referencia al nombre de la clase que se quiere relacionar
    notas = relationship("Nota", back_populates="alumno")

    # IMPORTANTE no lleva parentesis al momento de llamarlo
    @hybrid_property
    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"


class Nota(Base):
    __tablename__ = "notas"

    id = Column(Integer, primary_key=True)
    curso = Column(String, nullable=False)
    # Campo relacionada con la tabla "alumnos" especificamente en el campo "id"
    alumno_id = Column(Integer, ForeignKey("alumnos.id"))
    # El primer parametro hace referencia al nombre de la clase que se quiere relacionar
    alumno = relationship("Alumno", back_populates="notas")



if __name__ == "__main__":
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    alumno = Alumno(
        nombres="Diana",
        apellidos="Perez",
        carnet=1234
    )
    print(alumno.nombres)
    print(alumno.id)

    session.add(alumno)


    alumno2 = Alumno(
        nombres="Milton",
        apellidos="Juarez",
        carnet=5678
    )
    session.add(alumno2)
    session.commit()

    # IMPORTANTE no lleva parentesis al final
    print(alumno2.nombre_completo)

    # Devuelve la informacion más reciente
    session.refresh(alumno2)
    print(alumno2.id)


    alumno_db = session.query(Alumno).where(Alumno.nombres == "Diana").first()
    print(alumno_db.apellidos)
    print(alumno_db.id)

    # Devulve una lista con toda la información
    alumnos = session.query(Alumno).all()
    print(alumnos)

    print(alumnos[1].id)
    print(alumnos[1].nombres)

    cantidad_alumnos = session.query(Alumno).count()
    print(f"La cantidad de alumnos es: {cantidad_alumnos}")

    # El session.query devuelve la informacion de la base
    # de datos y la manera en la que la devuelve
    # depende de lo último que se coloque:

    # un .count() de vuelve la cantidad

    # un .all() devuelve todo lo que coincida

    # un .first() devuelve el primero que encuentre
    #   con las carácteristicas que se le indica


    # Actualizar informacion
    alumno_db.nombres = "Dianah"
    session.add(alumno_db)
    session.commit()

    # Borrar informacion
    borrado = delete(Alumno).where(Alumno.id == 1)
    session.execute(borrado)
    session.commit()

    alumno_borrado = session.query(Alumno).where(Alumno.id == 1).first()
    print(alumno_borrado)


    nota = Nota(
        curso = "Matematicas",

        # Esto no es posible en otras bases de datos
        # No se deberia poder guardar un alumnos que no exista
        # Recordad que alumno_id es una llave relacionada con otra tabla
        alumno_id = 2
    )
    session.add(nota)
    session.commit()

    nota_db = session.query(Nota).first()
    print(nota_db.alumno.nombres)

    session.refresh(alumno2)
    print(alumno2.notas)
    print(alumno2.notas[0].curso)


