import unittest
from fastapi.testclient import TestClient
from main import app
from config.connexion import get_db


class BaseTestFastAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)


class TestClients(BaseTestFastAPI):
    def test_get_client_by_id(self):
        """Tester la recherche par ID client"""
        test_response = self.client.get("/information_client/1")
        expected_response = {
            "info client": {
                "email_client": "marie.dubois@example.com",
                "telephone_client": "+33 6 12 34 56 78",
                "prenom_client": "Marie",
                "adresse_livraison_client": "12 Rue des Fleurs, 75001 Paris",
                "nom_client": "Dubois",
                "id_client": 1,
                "preferences_client": "Produits bio",
                "adresse_facturation_client": "12 Rue des Fleurs, 75001 Paris",
            }
        }

        self.assertEqual(test_response.status_code, 200)
        self.assertEqual(test_response.json(), expected_response)


# class TestCommentaires(BaseTestFastAPI):
#     def test_get_comment(self):
#         """Test pour vérifier la route pour chercher un commentaire par ID"""

#         test_response = self.client.get("/commentaires/1")

#         expected_response = {
#             "id_commentaire": 1,
#             "date_publication_commentaire": "2023-11-13T00:00:00",
#             "contenu_commentaire": "Une lecture agréable et légère. Idéal pour se détendre après une journée chargée.",
#             "titre_commentaire": "Agréable",
#             "id_client": 15,
#             "id_ouvrage": 15,
#         }

#         self.assertEqual(test_response.status_code, 200)
#         self.assertEqual(test_response.json(), expected_response)

#     def test_update_comment(self):
#         """Test pour vérifier la mise à jour d'un commentaire (UPDATE/patch)."""
#         test_response = self.client.patch(
#             "/commentaires/10",
#             json={
#                 "contenu_commentaire": "Updated Content",
#                 "titre_commentaire": "Updated Title",
#             },
#         )
#         expected_response = {
#             "id_commentaire": 10,
#             "date_publication_commentaire": "2023-11-28T00:00:00",
#             "contenu_commentaire": "Updated Content",
#             "titre_commentaire": "Updated Title",
#             "id_client": 6,
#             "id_ouvrage": 1,
#         }
#         self.assertEqual(test_response.status_code, 200)
#         self.assertEqual(test_response.json(), expected_response)

#     def test_add_comment(self):
#         """Test pour vérifier l'ajoute d'un commentaire."""
#         comment_data = {
#             "date_publication_commentaire": "2023-11-28T14:21:20.833Z",
#             "contenu_commentaire": "New Comment Content",
#             "titre_commentaire": "New Comment Title",
#             "id_client": 1,
#             "id_ouvrage": 10,
#         }
#         expected_response = {
#             "id_commentaire": 16,
#             "date_publication_commentaire": "2023-11-28T00:00:00",
#             "contenu_commentaire": "New Comment Content",
#             "titre_commentaire": "New Comment Title",
#             "id_client": 1,
#             "id_ouvrage": 10,
#         }
#         response = self.client.post("/commentaires", json=comment_data)
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(response.json(), expected_response)

#     def test_delete_comment(self):
#         """Test pour vérifier la route pour supprimer un commentaire"""
#         test_response = self.client.delete("/commentaires/15")
#         expected_response = "Commentaire supprimé."
#         self.assertEqual(test_response.status_code, 201)
#         self.assertEqual(test_response.json(), expected_response)


if __name__ == "__main__":
    unittest.main()
