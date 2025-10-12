from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Relative imports within the same package
from .api.certificates import router as certificates_router

app = FastAPI(title="Hacktoberfest Certificate Generator")

# Include routers
app.include_router(certificates_router, prefix="/certificates", tags=["certificates"])

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to Hacktoberfest Certificate Generator API 🚀"}

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
