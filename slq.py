from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
engine = create_engine('sqlite://')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Consulta todos os usuários
users = session.query(User).all()

# Insere um novo usuário
new_user = User(name='John Doe', email='john@example.com')
session.add(new_user)
session.commit()

# Atualiza um usuário existente
user = session.query(User).get(1)
user.name = 'Jane Doe'
session.commit()

# Exclui um usuário
user = session.query(User).get(2)
session.delete(user)
session.commit()
