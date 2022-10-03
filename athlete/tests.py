from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
UserModel = get_user_model()

# Create your tests here.
class TestAthleteExerciseCreate(APITestCase):

    def auth(self):
        response = self.client.post(reverse('register'), {
            'username':'username', 'email': 'user@email.com', 'password':'Password@123','password2': 'Password@123',
            'first_name': 'first_name', 'last_name': 'last_name'
        })

        print(response.data)

        username = response.data['username']

        response = self.client.post(reverse('token_obtain_pair'),{'username':'username', 'password':'Password@123'})

        token = "Bearer {}".format(response.data['token']['access'])

        print(token)

        self.client.credentials(HTTP_AUTHORIZATION=token)
        
        return username
    
    def test_list_athlete_exercise(self):
        response = self.client.get(reverse("athlete_exercise-list"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_create_authenticated_athlete_exercise(self):
        username = self.auth()
        user = UserModel.objects.get(username=username)
        
        sample_equipment={ "name" : "equipment", "description": "equipment description"}
        response = self.client.post("/exercise/equipment/",sample_equipment)
        print(response.data)

        sample_exercise={ "name" : "exercise", "description": "exercise description", "calories_burnt": 10, "equipment": response.data['id']}
        response = self.client.post("/exercise/",sample_exercise)
        print(response.data)
        
        sample_athlete_exercise={ "athlete" : user.id, "exercise": response.data['id']}
        response = self.client.post("/athlete/exercise/",sample_athlete_exercise)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    

    def test_get_total_calories_consumed(self):
        username = self.auth()
        user = UserModel.objects.get(username=username)
        sample_equipment={ "name" : "equipment", "description": "equipment description"}
        response = self.client.post("/exercise/equipment/",sample_equipment)
        print(response.data)

        sample_exercise={ "name" : "exercise", "description": "exercise description", "calories_burnt": 10, "equipment": response.data['id']}
        response = self.client.post("/exercise/",sample_exercise)
        print(response.data)
        
        sample_athlete_exercise={ "athlete" : user.id, "exercise": response.data['id'], "exercise_date":'2022-10-03'}
        response = self.client.post("/athlete/exercise/",sample_athlete_exercise)

        start_date='2022-10-01'
        end_date='2022-10-10'
        
        response = self.client.get("/athlete/calories-consumed?start_date={}&end_date={}".format(start_date, end_date))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[2]['total_calories_burnt'], 10)
        