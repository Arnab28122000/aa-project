from fastapi import FastAPI
from aa_backend_service.routers import account_aggregator
from fastapi.middleware.cors import CORSMiddleware

from aa_backend_service.cron_job import create_cron_job
from aa_backend_service.services.aa import check_and_update_dummy_data, create_dummy_aa_data
from aa_backend_service.db import init_db

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "https://aa-ui.vercel.app",
    "https://setu-ui.dashtics.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(account_aggregator.router)

@app.on_event("startup")
def on_startup():
    # Initializing db and Create Tables
    init_db()
    # If no data is available adding past 7 days dummy time series data
    check_and_update_dummy_data()
    create_cron_job()

@app.get("/", include_in_schema=False)
async def root():
    return "Welcome to AA Metrics"

if __name__ == "__main__":
    create_cron_job()
    # create_dummy_aa_data()