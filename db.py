# SELECT * FROM users where id = 1
# INSERT INTO users (id, name, age) (1, "Rafael", 15)
# ORM - Object Relational Mapper

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, create_engine, delete
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()
# String de conexion
engine = create_engine("sqlite:///:memory:")

class Alumno(Base):
    __tablename__ = "alumnos"

    # id, nombres, apellidos, carnet
    # nullabl=True : Campo obligatorio
    id = Column(Integer, primary_key=True)
    nombres = Column(String, nullable=True)
    apellidos = Column(String, nullable=False)
    carnet = Column(Integer)

    #notas = relationship("Nota", back_populates="alumno")

    # IMPORTANTE no lleva parentesis al momento de llamarlo
    @hybrid_property
    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

alumno = Alumno(
    nombres = "Diana",
    apellidos = "Perez",
    carnet = 1234
)
print(alumno.nombres)
print(alumno.id)

session.add(alumno)


alumno2 = Alumno(
    nombres = "Milton",
    apellidos = "Juarez",
    carnet = 5678
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








