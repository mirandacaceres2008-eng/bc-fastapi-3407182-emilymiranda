from fastapi import FastAPI

# ============================================
# CONFIGURACIÓN DEL SPA
# ============================================

GREETINGS: dict[str, str] = {
    "es": "¡Bienvenido/a a nuestro spa, {name}!",
    "en": "Welcome to our spa, {name}!",
    "fr": "Bienvenue à notre spa, {name}!",
    "de": "Willkommen in unserem Spa, {name}!",
    "it": "Benvenuto/a alla nostra spa, {name}!",
    "pt": "Bem-vindo ao nosso spa, {name}!",
}

SUPPORTED_LANGUAGES = list(GREETINGS.keys())

# ============================================
# 1. CREAR APP FASTAPI
# ============================================

app = FastAPI(
    title="Spa & Bienestar API",
    description="API para gestión de clientes y servicios de spa",
    version="1.0.0"
)

# ============================================
# 2. ENDPOINT RAÍZ
# ============================================

@app.get("/")
async def root():
    return {
        "name": "Spa & Bienestar API",
        "version": "1.0.0",
        "docs": "/docs",
        "languages": SUPPORTED_LANGUAGES
    }

# ============================================
# 3. BIENVENIDA PERSONALIZADA
# ============================================

@app.get("/spa/{name}")
async def greet(
    name: str,
    language: str = "es"
):

    template = GREETINGS.get(language, GREETINGS["es"])
    message = template.format(name=name)

    return {
        "greeting": message,
        "language": language,
        "name": name
    }

# ============================================
# 4. MENSAJE FORMAL SPA
# ============================================

@app.get("/spa/{name}/vip")
async def greet_vip(
    name: str,
    title: str = "Cliente VIP"
):

    return {
        "greeting": f"Estimado/a {title} {name}, disfrute su experiencia de spa.",
        "title": title,
        "name": name
    }

# ============================================
# 5. SERVICIO SEGÚN HORA
# ============================================

def get_day_period(hour: int):

    if 5 <= hour < 12:
        return "Buenos días en el spa", "morning"
    elif 12 <= hour < 18:
        return "Buenas tardes de relajación", "afternoon"
    else:
        return "Buenas noches de descanso", "night"


@app.get("/spa/{name}/time-based")
async def time_based(
    name: str,
    hour: int
):

    greeting, period = get_day_period(hour)

    return {
        "greeting": f"{greeting}, {name}!",
        "hour": hour,
        "period": period
    }

# ============================================
# 6. HEALTH CHECK
# ============================================

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "spa-bienestar-api",
        "version": "1.0.0"
    }