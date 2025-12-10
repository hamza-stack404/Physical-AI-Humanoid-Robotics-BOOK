import logging
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware # Import CORSMiddleware

# Import routers
from backend.app.api import chatbot, personalization, translation, auth, user

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Embodied Intelligence Book API",
    description="API for the Embodied Intelligence book, including RAG chatbot, personalization, and translation services.",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json"
)

# Add CORS middleware to allow requests from the Docusaurus frontend
origins = [
    "http://localhost:3000",  # Docusaurus development server
    # Add your deployed Docusaurus frontend URL here for production
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(user.router, prefix="/api/v1/user", tags=["User Profile"])
app.include_router(chatbot.router, prefix="/api/v1/chatbot", tags=["Chatbot"])
app.include_router(personalization.router, prefix="/api/v1/content", tags=["Personalization"])
app.include_router(translation.router, prefix="/api/v1/content", tags=["Translation"])


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Outgoing Response: {request.method} {request.url} - Status: {response.status_code}")
    return response

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>Embodied Intelligence Book API</title>
        </head>
        <body>
            <h1>Welcome to the Embodied Intelligence Book API!</h1>
            <p>Visit <a href="/docs">/docs</a> for API documentation.</p>
        </body>
    </html>
    """

@app.get("/health", response_class=HTMLResponse, tags=["Monitoring"])
async def health_check():
    logger.info("Health check endpoint accessed.")
    return "OK"