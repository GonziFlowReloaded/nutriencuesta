from locust import HttpUser, task, between
import random

class MyUser(HttpUser):
    wait_time = between(1, 3)  # Tiempo de espera entre las solicitudes
    host = "http://localhost:8000"  # Cambia esto por el host de tu aplicación

    @task
    def submit_form(self):
        # Genera valores aleatorios para cada campo
        birth_year = random.randint(1, 60)
        gender = random.choice(["Male", "Female", "Other"])
        textura = random.choice(["Esponjoso", "Cremoso", "Aireado", "Compacto"])
        consistencia = random.randint(1, 5)
        satisfactionRange = random.randint(1, 5)
        satisfactionRange_4 = random.randint(1, 5)
        satisfactionRange_5 = random.randint(1, 5)
        humedad = random.choice(["Alta", "Media", "Baja"])
        sabores = random.choice(["Dulce", "Salado", "Amargo", "Acido"])
        respuesta7 = random.choice(["Sí", "No"])

        # Simula una solicitud POST al endpoint /submit con datos válidos
        response = self.client.post("/submit", data={
            "birth_year": birth_year,
            "gender": gender,
            "textura": textura,
            "consistencia": consistencia,
            "satisfactionRange": satisfactionRange,
            "satisfactionRange_4": satisfactionRange_4,
            "satisfactionRange_5": satisfactionRange_5,
            "humedad": humedad,
            "sabores": sabores,
            "respuesta7": respuesta7
        })
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)

    @task
    def download_csv(self):
        # Simula una solicitud GET al endpoint /download_csv
        response = self.client.get("/download_csv")
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
