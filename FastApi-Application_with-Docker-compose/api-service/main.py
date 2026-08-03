from fastapi import FastAPI

app = FastAPI(title="Portfolio API Service")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Portfolio Backend API!"}

@app.get("/api/services")
def get_services():
    return [
        {
            "title": "Web Development (Dynamic)",
            "desc": "We build responsive, modern websites tailored to your business needs (fetched dynamically from API-Service)."
        },
        {
            "title": "Graphic Design (Dynamic)",
            "desc": "Creative designs for logos, branding, and marketing materials (fetched dynamically from API-Service)."
        },
        {
            "title": "Digital Marketing (Dynamic)",
            "desc": "Boost your online presence with SEO, social media, and ad campaigns (fetched dynamically from API-Service)."
        },
        {
            "title": "Consulting (Dynamic)",
            "desc": "Expert advice to help streamline your business processes and strategy (fetched dynamically from API-Service)."
        },
        {
            "title": "Docker Training (New)",
            "desc": "Learn how Docker and Docker Compose work in microservices architectures!"
        }
    ]
