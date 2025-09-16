from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers (we will create teacher_router.py & student_router.py later)
try:
    from api.teacher_router import router as teacher_router
    from api.student_router import router as student_router
except ImportError:
    teacher_router = None
    student_router = None

# Create FastAPI app
app = FastAPI(title="Face Recognition Attendance System")

# CORS middleware (allows frontend/mobile apps to call your backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # in production, restrict to frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check route (test if server is running)
@app.get("/ping")
async def health_check():
    return {"status": "ok", "message": "Server is running 🚀"}

# Include routers only if they exist
if teacher_router:
    app.include_router(teacher_router, prefix="/teacher", tags=["Teacher"])

if student_router:
    app.include_router(student_router, prefix="/student", tags=["Student"])
