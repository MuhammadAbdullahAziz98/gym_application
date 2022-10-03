from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.
class TestAthleteExerciseCreate(APITestCase):

    def auth(self):
        response = self.client.post(reverse('register'), {
            'username':'username', 'email': 'user@email.com', 'password':'Password@123','password2': 'Password@123',
            'first_name': 'first_name', 'last_name': 'last_name'
        })

        print(response.data)

        
        response = self.client.post(reverse('token_obtain_pair'),{'username':'username', 'password':'Password@123'})

        token = "Bearer {}".format(response.data['token']['access'])

        print(token)

        self.client.credentials(HTTP_AUTHORIZATION=token)
        
    def test_list_exercise(self):
        response = self.client.post(reverse("exercise-list"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_authenticated_exercise(self):
        self.auth()
        
        sample_equipment={ "name" : "equipment", "description": "equipment description"}
        response = self.client.post("/exercise/equipment/",sample_equipment)
        print(response.data)

        sample_exercise={ "name" : "exercise", "description": "exercise description", "calories_burnt": 10, "equipment": response.data['id']}
        response = self.client.post("/exercise/",sample_exercise)
        print(response.data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
