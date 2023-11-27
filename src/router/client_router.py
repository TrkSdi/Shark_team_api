
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from models.client import Client
from config.connexion import ENGINE
from schema.client_schema import Client_schema, Client_schema_optionnel
from fastapi.encoders import jsonable_encoder
from config.connexion import get_db

router = APIRouter()

# creation d'une route pour remplire la Bdd table client
@router.post("/inscription/",tags=["Client"], summary="",description="")
async def ajout_client(client : Client_schema):
    with Session(ENGINE) as session:
        personne = Client(**client.dict())
        session.add_all([personne])
        session.commit()

# creation d'une route pour modifier la Bdd table client
@router.get("/information_client/{id}",tags=["Client"], summary="",description="")
async def suppression_client(id : int):
    with Session(ENGINE) as session:
        client_db = session.query(Client).filter(Client.id_client == id).first()
        if client_db:
            return {"info client" : client_db}

# creation d'une route pour effacer la Bdd table client
@router.delete("/information_client/{id}",tags=["Client"], summary="",description="")
async def affiche_client(id : int):
    with Session(ENGINE) as session:
        client_db = session.query(Client).filter(Client.id_client == id).first()
        if client_db:
            session.delete(client_db)
            session.commit()
            return {"personne supprimée" : client_db}

# creation d'une route pour modifier la Bdd table client
@router.patch("/modification_client/{id}",response_model=Client_schema,tags=["Client"], summary="",description="")
async def modif_client(id : int, client_update : Client_schema_optionnel):
    with Session(ENGINE) as session:
        client_db = session.query(Client).filter(Client.id_client == id).first()
        if client_db:
            for cle,valeur in client_update.dict(exclude_unset=True).items():
                setattr(client_db, cle, valeur)
            session.commit()
            session.refresh(client_db)
        return Client_schema.from_orm(client_db)

"""
Vu avec Robin, ne fonctionne pas : pbe de dict sur stored_client_model
Code Robin en deuxième partie, non utilisé, on est passé en query

# creation d'une route pour modifier la Bdd table client
@router.patch("/modification/{id}",response_model=Client_schema)
async def modif_client(id : int, client : Client_schema_optionnel, bdd : Session = Depends(get_db)):
    stmt = select(Client).where(Client.id_client == id)
    stored_client_data = bdd.scalars(stmt).one() # recuperation des données via id
    stored_client_model = Client(**stored_client_data.dict()) # on transforme les données client en Client pour exploitation 
    update_data = client.dict(exclude_unset=True) # transforme données de la requète en dictionnaire
    update_client =stored_client_model.copy(update=update_data) # application de la mise à jour partielle à l'objet existant
    Session.commit(update_client) # on commit pour "fermer l'enveloppe"
    Session.refresh(update_client) # mise à jour BdD avec la version mise à jour
    return update_client # retour au client de l'objet mis à jour

@router.patch("/{id_client}", response_model=Client_schema, status_code=200)
def update_client(id_client: int, client: Client_schema_optionnel, db : Session = Depends(get_db)):
    stmt = select(Client).where(Client.id_client == id_client)
    result = db.scalars(stmt).first()
    for key, value in client.dict().items():
        setattr(result, key, value)
    db.commit()
    return result
"""
