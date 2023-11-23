# Week3 - SQL and Python - Homework 3

from typing import Optional, List

# One line of FastAPI imports here later &#x1f448;
from fastapi import FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


# 1. Create POST (PUT) API - only meant to create `hero` for the first time
@app.put("/heroes/")  # Decorator in FastAPi telling HTTP method and path
def create_hero(
    hero: Hero,
):  # Takes a single parameter which is a string representing the hero's name
    with Session(engine) as session:  # Creates a new db session
        session.add(hero)  # Adds hero object to the session
        session.commit()  # Commits the session to the db
        print("Hero added")  # Prints a message to the console
        return hero  # Returns the hero object


class HeroUpdate(SQLModel):  # HeroUpdae is a DTO
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None


# Patch API
@app.patch("/hero/", response_model=Hero)
def change_secret_name(hero_update: HeroUpdate):
    with Session(engine) as session:
        db_hero = session.exec(
            select(Hero).where(Hero.name == hero_update.name)
        ).first()
        if not db_hero:
            raise HTTPException(status_code=404, detail="Hero not found")
        hero_data = HeroUpdate.dict(exclude_unset=True)
        for key, value in hero_data.items():
            setattr(db_hero, key, value)
        session.add(db_hero)
        session.commit()
        session.refresh(db_hero)
        return db_hero


# 2. Create GET `hero` API by name
@app.get(
    "/heroes/{name}", response_model=Hero
)  # {name} is a path parameter, represents the name of the hero we want to get
def get_hero(
    name: str,
):  # Takes a single parameter which is a string representing the hero's name
    with Session(engine) as session:  # Creates a new db session
        statement = select(Hero).where(
            Hero.name == name
        )  # Creates a SQL statement to select the hero by name
        hero = session.exec(
            statement
        ).first()  # Executes the SQL statement and returns the first result
        print(hero)  # Prints the hero to the console
        return hero  # Returns the hero object


# 3. Create GET all `hero` API
@app.get(
    "/heroes/", response_model=List[Hero]
)  # Decorator in FastAPi telling HTTP method and path
def get_heroes():  # No parameters - GET request to retrieve all heroes
    with Session(engine) as session:  # Creates a new db session
        statement = select(Hero)  # Creates a SQL statement to select all heroes
        heroes = session.exec(
            statement
        ).all()  # Executes the SQL statement and returns all results
        print(heroes)  # Prints a list of all heroes to the console
        return heroes  # Returns a list of all heroes


# hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
# hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
# hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)


# engine = create_engine("sqlite:///database.db")


# SQLModel.metadata.create_all(engine)

# with Session(engine) as session:
#     session.add(hero_1)
#     session.add(hero_2)
#     session.add(hero_3)
#     session.commit()

# with Session(engine) as session:
#     statement = select(Hero).where(Hero.name == "Spider-Boy")
#     heroes = session.exec(statement).all() #returns list of all records that match
#     print(heroes)
#     print(type(heroes))
#     hero = session.exec(statement).first() #returns only first record
#     print(hero)
