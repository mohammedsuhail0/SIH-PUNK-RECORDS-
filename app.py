import os
import uuid
import datetime
from typing import List, Optional, Dict, Any
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from pydantic import BaseModel, Field

app = FastAPI(
    title="ArogyaMitr Core Backend API",
    description="Decentralized Dual-Outlet Rural Healthcare Platform with Voice AI, Smart Dark Hub Fulfillment, and WhatsApp Delivery (SIH 2026 PS 26133)",
    version="3.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simulated UIDAI / ABDM Central Citizen Registry
AADHAAR_REGISTRY = {
    "918842194055": {
        "aadhaar": "9188-4219-4055",
        "name": "Baburao Madavi",
        "age": 54,
        "gender": "Male",
        "village": "Laheri Hamlet 3",
        "district": "Gadchiroli",
        "phone": "+91 98231 44012",
        "has_health_card": True,
        "abha_id": "91-8842-1940-5511",
        "photo_avatar": "👨‍🌾",
        "existing_conditions": ["Hypertension (Mild)"]
    },
    "914589204139": {
        "aadhaar": "9145-8920-4139",
        "name": "Sunita Madavi",
        "age": 24,
        "gender": "Female",
        "village": "Laheri Hamlet 2",
        "district": "Gadchiroli",
        "phone": "+91 94052 88910",
        "has_health_card": True,
        "abha_id": "91-4589-2041-3912",
        "photo_avatar": "🤰",
        "existing_conditions": ["Pregnancy 32 Weeks", "Anemia"]
    },
    "913321908744": {
        "aadhaar": "9133-2190-8744",
        "name": "Anandi Gawade",
        "age": 34,
        "gender": "Female",
        "village": "Allapalli",
        "district": "Gadchiroli",
        "phone": "+91 97631 22890",
        "has_health_card": False,
        "abha_id": None,
        "photo_avatar": "👩",
        "existing_conditions": []
    },
    "917765109234": {
        "aadhaar": "9177-6510-9234",
        "name": "Ramesh Atram",
        "age": 58,
        "gender": "Male",
        "village": "Bhamragad",
        "district": "Gadchiroli",
        "phone": "+91 99220 11456",
        "has_health_card": True,
        "abha_id": "91-7765-1092-3488",
        "photo_avatar": "👴",
        "existing_conditions": ["Cardiac Risk", "High BP"]
    }
}

# Live Operational In-Memory Database
DB = {
    "stats": {
        "today_triages": 32,
        "dispatched_prescriptions": 24,
        "lab_samples_processed": 18,
        "active_emergency_sos": 1,
        "dark_store_stock_index": "98% Optimal",
        "avg_delivery_time": "16 Mins"
    },
    "patients": [
        {
            "id": "P-101",
            "aadhaar": "9145-8920-4139",
            "abha_id": "91-4589-2041-3912",
            "has_card": True,
            "name": "Sunita Madavi",
            "age": 24,
            "gender": "Female",
            "village": "Laheri Hamlet 2",
            "district": "Gadchiroli",
            "phone": "+91 94052 88910",
            "symptoms": ["Pregnancy 32 Weeks", "Severe Fatigue", "Dizziness"],
            "condition": "High-Risk Maternal Anemia (Hb: 7.2 g/dL)",
            "risk_level": "High Risk",
            "vitals": {"bp": "95/60", "spo2": "97%", "pulse": 88, "temp": "98.6°F", "glucose": "105 mg/dL", "hb": "7.2 g/dL"},
            "timestamp": "2026-09-06T10:15:00Z",
            "status": "Doctor Consulted • Medicine Dispatched to Home",
            "blood_sample_drawn": True,
            "sample_id": "SMP-LAHERI-801"
        },
        {
            "id": "P-102",
            "aadhaar": "9177-6510-9234",
            "abha_id": "91-7765-1092-3488",
            "has_card": True,
            "name": "Ramesh Atram",
            "age": 58,
            "gender": "Male",
            "village": "Bhamragad Hamlet 4",
            "district": "Gadchiroli",
            "phone": "+91 99220 11456",
            "symptoms": ["Chest Heaviness", "High Blood Pressure", "Shortness of Breath"],
            "condition": "Hypertensive Crisis (BP: 175/105) with Cardiac Risk",
            "risk_level": "Emergency",
            "vitals": {"bp": "175/105", "spo2": "92%", "pulse": 104, "temp": "99.1°F", "glucose": "210 mg/dL", "hb": "13.8 g/dL"},
            "timestamp": "2026-09-06T11:00:00Z",
            "status": "108 Ambulance Dispatched",
            "blood_sample_drawn": False,
            "sample_id": None
        },
        {
            "id": "P-103",
            "aadhaar": "9133-2190-8744",
            "abha_id": None,
            "has_card": False,
            "name": "Anandi Gawade",
            "age": 34,
            "gender": "Female",
            "village": "Allapalli",
            "district": "Gadchiroli",
            "phone": "+91 97631 22890",
            "symptoms": ["High Fever", "Joint Pain", "Chills"],
            "condition": "Suspected Acute Plasmodium Vivax Malaria",
            "risk_level": "Moderate Risk",
            "vitals": {"bp": "120/80", "spo2": "98%", "pulse": 90, "temp": "103.2°F", "glucose": "115 mg/dL", "hb": "11.5 g/dL"},
            "timestamp": "2026-09-06T11:45:00Z",
            "status": "Blood Sample Queued for Dark Hub Lab",
            "blood_sample_drawn": True,
            "sample_id": "SMP-ALLAPALLI-803"
        }
    ],
    "clinic_samples": [
        {
            "sample_id": "SMP-LAHERI-801",
            "patient_id": "P-101",
            "patient_name": "Sunita Madavi",
            "village": "Laheri",
            "test_requested": "Complete Blood Count (CBC) & Hemoglobin",
            "draw_time": "10:20 AM",
            "storage": "Clinic Cold-Box (4°C)",
            "pickup_status": "Transported to Hub Lab",
            "result_status": "Report Ready (Hb: 7.2 g/dL)",
            "test_result": {"hb": "7.2 g/dL", "wbc": "8,200 /mcL", "platelets": "2.4 Lakhs", "findings": "Microcytic Hypochromic Anemia"}
        },
        {
            "sample_id": "SMP-ALLAPALLI-803",
            "patient_id": "P-103",
            "patient_name": "Anandi Gawade",
            "village": "Allapalli",
            "test_requested": "Rapid Malaria Antigen (RDT) & CBC",
            "draw_time": "11:50 AM",
            "storage": "Clinic Cold-Box (4°C)",
            "pickup_status": "Awaiting Hub Lab Processing",
            "result_status": "Pending Test Run",
            "test_result": None
        }
    ],
    "dark_store_inventory": [
        {"id": "MED-01", "name": "Polyvalent Anti-Snake Venom (ASV)", "category": "Critical Emergency", "stock": 36, "min": 10, "unit": "Vials", "cold_chain": "2°C - 8°C", "status": "Optimal"},
        {"id": "MED-02", "name": "Human Insulin (Regular 40 IU)", "category": "Chronic / Diabetes", "stock": 28, "min": 15, "unit": "Vials", "cold_chain": "2°C - 8°C", "status": "Optimal"},
        {"id": "MED-03", "name": "Oxytocin Injection (5 IU)", "category": "Maternal Emergency", "stock": 45, "min": 20, "unit": "Ampoules", "cold_chain": "2°C - 8°C", "status": "Optimal"},
        {"id": "MED-04", "name": "Artesunate + Lumefantrine (ACT)", "category": "Malaria Treatment", "stock": 190, "min": 50, "unit": "Blister Packs", "cold_chain": "Room Temp", "status": "Optimal"},
        {"id": "MED-05", "name": "Iron Folic Acid (IFA) 100mg", "category": "Maternal Nutrition", "stock": 540, "min": 100, "unit": "Strips", "cold_chain": "Room Temp", "status": "Optimal"},
        {"id": "MED-06", "name": "Amoxicillin + Clav 625mg", "category": "Antibiotic", "stock": 380, "min": 100, "unit": "Tablets", "cold_chain": "Room Temp", "status": "Optimal"},
        {"id": "TEST-01", "name": "Rapid Malaria Antigen (RDT) Kits", "category": "Diagnostic Testing", "stock": 240, "min": 50, "unit": "Kits", "cold_chain": "Room Temp", "status": "Optimal"},
        {"id": "TEST-02", "name": "CBC & Hematology Vials", "category": "Diagnostic Testing", "stock": 110, "min": 30, "unit": "Vials", "cold_chain": "Room Temp", "status": "Optimal"}
    ],
    "prescriptions": [
        {
            "rx_id": "RX-2026-801",
            "patient_id": "P-101",
            "patient_name": "Sunita Madavi",
            "doctor_name": "Dr. Vivek Deshmukh (MBBS, DGO)",
            "medicines": ["Iron Folic Acid (IFA) Tablets (100mg)", "Calcium + Vitamin D3 (500mg)", "Protein Supplement (Powder)"],
            "diagnostic_tests": ["Repeat Hb Test (Day 7)"],
            "target_hub": "Aheri Outskirts Diagnostic & Supply Hub",
            "destination_outlet": "🏠 Patient Doorstep Delivery (Laheri Hamlet 2)",
            "dosage_stickers": ["☀️ Morning (1 Tab After Food)", "🌙 Night (1 Tab After Food)"],
            "status": "Delivered to Doorstep (Runner: Sandeep K.)",
            "timestamp": "2026-09-06T10:30:00Z",
            "eta": "Delivered",
            "runner_name": "Sandeep Korwate (e-Bike #04)",
            "runner_phone": "+91 98221 55901"
        }
    ],
    "emergency_sos": [
        {
            "sos_id": "SOS-991",
            "patient_name": "Ramesh Atram",
            "village": "Bhamragad - Hamlet 4",
            "lat_long": "19.6542° N, 80.3541° E",
            "condition": "Severe Cardiac Chest Pain & BP Spike (175/105)",
            "assigned_ambulance": "108-MH-33-G-4412 (Aheri Base)",
            "eta": "11 Mins",
            "status": "En Route with Paramedic",
            "timestamp": "2026-09-06T11:05:00Z"
        }
    ],
    "whatsapp_messages": [
        {
            "patient_id": "P-101",
            "patient_name": "Sunita Madavi",
            "phone": "+91 94052 88910",
            "message_text": "नमस्कार Sunita Madavi जी, तुमचे आरोग्य तपासणी व रक्त अहवाल तयार आहेत. डॉक्टर विवेक देशमुख यांच्या सल्ल्यानुसार औषधे तुमच्या घरी 18 मिनिटांत पोहोचत आहेत. ☀️ सकाळी: 1 गोळी (IFA), 🌙 रात्री: 1 गोळी (Calcium).",
            "pdf_link": "/api/reports/download/P-101",
            "audio_link": "/audio/voice_report_mr.mp3",
            "tracking_link": "https://arogyamitr.gov.in/track/RX-2026-801",
            "sent_at": "10:32 AM"
        }
    ]
}

# --- Request & Response Models ---

class AadhaarAuthInput(BaseModel):
    aadhaar_number: str
    auth_method: str = "otp"  # "otp" or "face"
    otp_code: Optional[str] = "123456"

class TriageInput(BaseModel):
    name: str
    age: int
    gender: str
    village: str
    district: str = "Gadchiroli"
    phone: Optional[str] = "+91 98000 00000"
    aadhaar: Optional[str] = "9188-4219-4055"
    abha_id: Optional[str] = None
    has_card: bool = False
    systolic_bp: int
    diastolic_bp: int
    spo2: int
    pulse: int
    temp: float = 98.6
    blood_glucose: Optional[int] = 110
    hb_level: Optional[float] = 12.0
    symptoms: List[str]

class SampleDrawInput(BaseModel):
    patient_id: str
    patient_name: str
    village: str
    test_requested: str

class LabResultInput(BaseModel):
    sample_id: str
    test_result_text: str
    malaria_status: Optional[str] = "Negative"
    hb_value: Optional[float] = 12.5
    blood_sugar: Optional[int] = 110
    findings: str

class PrescriptionInput(BaseModel):
    patient_id: str
    patient_name: str
    doctor_name: str = "Dr. Vivek Deshmukh (Medical Officer)"
    medicines: List[str]
    diagnostic_tests: List[str] = []
    target_hub: str = "Aheri Outskirts Cluster Hub"
    destination_outlet: str = "🏠 Patient Doorstep Home Delivery"
    dosage_stickers: List[str] = ["☀️ Morning (1 Tab)", "🌙 Night (1 Tab)"]

class RunnerDispatchInput(BaseModel):
    rx_id: str
    runner_name: str = "Sandeep Korwate (e-Bike #04)"
    destination: str = "Patient Home Doorstep"

class SOSInput(BaseModel):
    patient_name: str
    village: str
    condition: str
    lat: float = 19.6542
    long: float = 80.3541

# --- API Endpoints ---

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "ArogyaMitr Core Backend API",
        "version": "3.0.0",
        "cloud": "Vercel Serverless Ready",
        "standards": ["ABDM FHIR R4", "Bhashini Voice AI", "UIDAI Aadhaar"]
    }

@app.get("/")
def get_dashboard():
    dashboard_path = os.path.join(os.path.dirname(__file__), "dashboard.html")
    return FileResponse(dashboard_path)

@app.post("/api/auth/aadhaar")
def authenticate_aadhaar(data: AadhaarAuthInput):
    clean_num = data.aadhaar_number.replace("-", "").replace(" ", "")
    
    if clean_num in AADHAAR_REGISTRY:
        record = AADHAAR_REGISTRY[clean_num]
        return {
            "status": "authenticated",
            "method": data.auth_method,
            "citizen": record,
            "has_existing_health_card": record["has_health_card"],
            "abha_id": record["abha_id"] if record["has_health_card"] else None,
            "message": f"Verified successfully via {data.auth_method.upper()}. Existing Health Card loaded." if record["has_health_card"] else f"Verified successfully via {data.auth_method.upper()}. Citizen profile active."
        }
    else:
        # Fallback profile for ad-hoc demo Aadhaar numbers
        formatted = f"{clean_num[:4]}-{clean_num[4:8]}-{clean_num[8:12]}" if len(clean_num) == 12 else clean_num
        new_record = {
            "aadhaar": formatted,
            "name": "Gram Citizen",
            "age": 42,
            "gender": "Male",
            "village": "Laheri Village",
            "district": "Gadchiroli",
            "phone": "+91 98000 12345",
            "has_health_card": False,
            "abha_id": None,
            "photo_avatar": "👤",
            "existing_conditions": []
        }
        return {
            "status": "authenticated",
            "method": data.auth_method,
            "citizen": new_record,
            "has_existing_health_card": False,
            "abha_id": None,
            "message": f"Aadhaar verified via {data.auth_method.upper()}. Immediate healthcare access enabled."
        }

@app.get("/api/stats")
def get_stats():
    return DB["stats"]

@app.get("/api/patients")
def list_patients():
    return DB["patients"]

@app.post("/api/triage")
def create_triage(data: TriageInput):
    risk_level = "Normal"
    reasons = []

    if data.systolic_bp >= 160 or data.diastolic_bp >= 100:
        risk_level = "Emergency"
        reasons.append(f"Hypertensive Crisis ({data.systolic_bp}/{data.diastolic_bp} mmHg)")
    elif data.systolic_bp >= 140 or data.diastolic_bp >= 90:
        risk_level = "High Risk"
        reasons.append(f"Stage 1 Hypertension ({data.systolic_bp}/{data.diastolic_bp})")

    if data.spo2 < 92:
        risk_level = "Emergency"
        reasons.append(f"Severe Hypoxia (SpO2: {data.spo2}%)")
    elif data.spo2 < 95:
        if risk_level != "Emergency": risk_level = "High Risk"
        reasons.append(f"Low Oxygenation (SpO2: {data.spo2}%)")

    if data.temp >= 102.5:
        if risk_level != "Emergency": risk_level = "High Risk"
        reasons.append(f"High Pyrexia/Fever ({data.temp}°F)")

    if data.hb_level and data.hb_level < 8.0:
        if risk_level != "Emergency": risk_level = "High Risk"
        reasons.append(f"Severe Anemia (Hb: {data.hb_level} g/dL)")

    if any(s.lower() in ["chest pain", "unconscious", "snake bite", "heavy bleeding", "breathlessness"] for s in data.symptoms):
        risk_level = "Emergency"
        reasons.append("Critical Red-Flag Symptom Flagged")

    p_id = f"P-{len(DB['patients']) + 101}"

    patient_record = {
        "id": p_id,
        "aadhaar": data.aadhaar,
        "abha_id": data.abha_id,
        "has_card": data.has_card,
        "name": data.name,
        "age": data.age,
        "gender": data.gender,
        "village": data.village,
        "district": data.district,
        "phone": data.phone,
        "symptoms": data.symptoms,
        "condition": ", ".join(reasons) if reasons else "Routine Primary Health Checkup",
        "risk_level": risk_level,
        "vitals": {
            "bp": f"{data.systolic_bp}/{data.diastolic_bp}",
            "spo2": f"{data.spo2}%",
            "pulse": data.pulse,
            "temp": f"{data.temp}°F",
            "glucose": f"{data.blood_glucose} mg/dL" if data.blood_glucose else "N/A",
            "hb": f"{data.hb_level} g/dL" if data.hb_level else "N/A"
        },
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "status": "Triage Recorded • Tele-Consult Queue Active",
        "blood_sample_drawn": False,
        "sample_id": None
    }

    DB["patients"].insert(0, patient_record)
    DB["stats"]["today_triages"] += 1
    return {"status": "success", "patient": patient_record, "risk_assessment": {"level": risk_level, "flags": reasons}}

@app.post("/api/clinic/draw-sample")
def draw_clinic_sample(data: SampleDrawInput):
    sample_id = f"SMP-{data.village.upper()[:4]}-{len(DB['clinic_samples']) + 801}"
    record = {
        "sample_id": sample_id,
        "patient_id": data.patient_id,
        "patient_name": data.patient_name,
        "village": data.village,
        "test_requested": data.test_requested,
        "draw_time": datetime.datetime.now().strftime("%I:%M %p"),
        "storage": "Clinic Cold-Box (4°C)",
        "pickup_status": "Queued for Daily Batch Transport to Dark Hub",
        "result_status": "Pending Test Run at Hub",
        "test_result": None
    }
    DB["clinic_samples"].insert(0, record)
    
    # Update patient record
    for p in DB["patients"]:
        if p["id"] == data.patient_id:
            p["blood_sample_drawn"] = True
            p["sample_id"] = sample_id
            p["status"] = f"Blood Sample #{sample_id} Collected in Clinic Cold-Box"
            break

    return {"status": "success", "sample": record}

@app.get("/api/lab/samples")
def list_lab_samples():
    return DB["clinic_samples"]

@app.post("/api/lab/submit-result")
def submit_lab_result(data: LabResultInput):
    for sample in DB["clinic_samples"]:
        if sample["sample_id"] == data.sample_id:
            sample["result_status"] = "Verified Digital Report Ready"
            sample["pickup_status"] = "Testing Completed at Hub"
            sample["test_result"] = {
                "malaria": data.malaria_status,
                "hb": f"{data.hb_value} g/dL",
                "sugar": f"{data.blood_sugar} mg/dL",
                "findings": data.findings
            }
            DB["stats"]["lab_samples_processed"] += 1
            
            # Send automated WhatsApp Notification to patient
            for p in DB["patients"]:
                if p["id"] == sample["patient_id"]:
                    p["status"] = "Diagnostic Lab Report Published to Cloud & WhatsApp"
                    whatsapp_payload = {
                        "patient_id": p["id"],
                        "patient_name": p["name"],
                        "phone": p.get("phone", "+91 98000 00000"),
                        "message_text": f"नमस्कार {p['name']} जी, तुमचा लॅब रिपोर्ट तयार आहे: मलेरिया: {data.malaria_status}, Hb: {data.hb_value} g/dL. निष्कर्ष: {data.findings}.",
                        "pdf_link": f"/api/reports/download/{p['id']}",
                        "audio_link": "/audio/voice_report_mr.mp3",
                        "tracking_link": f"https://arogyamitr.gov.in/report/{sample['sample_id']}",
                        "sent_at": datetime.datetime.now().strftime("%I:%M %p")
                    }
                    DB["whatsapp_messages"].insert(0, whatsapp_payload)
                    break
            
            return {"status": "success", "sample": sample}
            
    raise HTTPException(status_code=404, detail="Sample ID not found")

@app.get("/api/inventory")
def get_inventory():
    return {
        "temperature": "4.2°C (Optimal Solar Cold-Chain Active)",
        "solar_power_status": "100% Battery Backup",
        "items": DB["dark_store_inventory"]
    }

@app.post("/api/prescriptions")
def issue_prescription(data: PrescriptionInput):
    rx_id = f"RX-2026-{len(DB['prescriptions']) + 801}"
    record = {
        "rx_id": rx_id,
        "patient_id": data.patient_id,
        "patient_name": data.patient_name,
        "doctor_name": data.doctor_name,
        "medicines": data.medicines,
        "diagnostic_tests": data.diagnostic_tests,
        "target_hub": data.target_hub,
        "destination_outlet": data.destination_outlet,
        "dosage_stickers": data.dosage_stickers,
        "status": "Pre-Stickered at Hub • Ready for Doorstep Dispatch",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "eta": "16 Mins",
        "runner_name": "Sandeep Korwate (e-Bike #04)",
        "runner_phone": "+91 98221 55901"
    }
    DB["prescriptions"].insert(0, record)
    DB["stats"]["dispatched_prescriptions"] += 1
    
    # Update patient status
    for p in DB["patients"]:
        if p["id"] == data.patient_id:
            p["status"] = f"Prescription #{rx_id} Pre-Stickered & Dispatched to Home"
            break

    # Automated WhatsApp Notification
    whatsapp_payload = {
        "patient_id": data.patient_id,
        "patient_name": data.patient_name,
        "phone": "+91 94052 88910",
        "message_text": f"नमस्कार {data.patient_name} जी, डॉ. {data.doctor_name} यांनी लिहिलेली औषधे डार्क स्टोअरमधून रवाना झाली आहेत. ☀️ सकाळी: 1 गोळी, 🌙 रात्री: 1 गोळी. रनर ETA: 16 मिनिटे.",
        "pdf_link": f"/api/reports/download/{data.patient_id}",
        "audio_link": "/audio/voice_report_mr.mp3",
        "tracking_link": f"https://arogyamitr.gov.in/track/{rx_id}",
        "sent_at": datetime.datetime.now().strftime("%I:%M %p")
    }
    DB["whatsapp_messages"].insert(0, whatsapp_payload)

    return {"status": "success", "prescription": record}

@app.post("/api/dispatch/runner")
def dispatch_runner(data: RunnerDispatchInput):
    for rx in DB["prescriptions"]:
        if rx["rx_id"] == data.rx_id:
            rx["status"] = f"Out for Home Delivery with Runner {data.runner_name}"
            rx["eta"] = "12 Mins"
            return {"status": "success", "prescription": rx}
    raise HTTPException(status_code=404, detail="Rx not found")

@app.get("/api/whatsapp/latest")
def get_latest_whatsapp():
    return DB["whatsapp_messages"][0] if DB["whatsapp_messages"] else None

@app.get("/api/sos")
def list_sos():
    return DB["emergency_sos"]

@app.post("/api/sos")
def trigger_sos(data: SOSInput):
    sos_id = f"SOS-{len(DB['emergency_sos']) + 991}"
    record = {
        "sos_id": sos_id,
        "patient_name": data.patient_name,
        "village": data.village,
        "lat_long": f"{data.lat}° N, {data.long}° E",
        "condition": data.condition,
        "assigned_ambulance": "108-MH-33-G-4412 (Aheri Cluster Base)",
        "eta": "9 Mins",
        "status": "En Route with Paramedic & Oxygen",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }
    DB["emergency_sos"].insert(0, record)
    DB["stats"]["active_emergency_sos"] += 1
    return {"status": "success", "sos": record}

@app.get("/api/fhir/patient/{patient_id}")
def export_fhir_r4(patient_id: str):
    patient = next((p for p in DB["patients"] if p["id"] == patient_id), None)
    if not patient:
        patient = DB["patients"][0]

    fhir_bundle = {
        "resourceType": "Bundle",
        "id": f"arogyamitr-bundle-{patient['id']}",
        "type": "document",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "identifier": {
            "system": "https://healthid.abdm.gov.in",
            "value": patient.get("abha_id") or f"AADHAAR-{patient.get('aadhaar')}"
        },
        "entry": [
            {
                "fullUrl": f"urn:uuid:patient-{patient['id']}",
                "resource": {
                    "resourceType": "Patient",
                    "id": patient["id"],
                    "identifier": [
                        {"system": "https://uidai.gov.in", "value": patient.get("aadhaar")},
                        {"system": "https://healthid.abdm.gov.in", "value": patient.get("abha_id")}
                    ],
                    "name": [{"text": patient["name"]}],
                    "gender": patient["gender"].lower(),
                    "address": [{"city": patient["village"], "district": patient["district"], "state": "Maharashtra"}]
                }
            },
            {
                "fullUrl": f"urn:uuid:encounter-{patient['id']}",
                "resource": {
                    "resourceType": "Encounter",
                    "status": "finished",
                    "class": {"code": "AMB", "display": "Rural Care Point Tele-Triage"},
                    "subject": {"reference": f"Patient/{patient['id']}"},
                    "reasonCode": [{"text": ", ".join(patient["symptoms"])}]
                }
            },
            {
                "fullUrl": f"urn:uuid:observation-vitals-{patient['id']}",
                "resource": {
                    "resourceType": "Observation",
                    "status": "final",
                    "category": [{"coding": [{"system": "http://terminology.hl7.org/CodeSystem/observation-category", "code": "vital-signs"}]}],
                    "code": {"text": "Clinical Vitals Telemetry"},
                    "subject": {"reference": f"Patient/{patient['id']}"},
                    "component": [
                        {"code": {"text": "Blood Pressure"}, "valueString": patient["vitals"]["bp"]},
                        {"code": {"text": "Oxygen Saturation SpO2"}, "valueString": patient["vitals"]["spo2"]},
                        {"code": {"text": "Body Temperature"}, "valueString": patient["vitals"]["temp"]},
                        {"code": {"text": "Hemoglobin"}, "valueString": patient["vitals"].get("hb", "N/A")}
                    ]
                }
            }
        ]
    }
    return JSONResponse(content=fhir_bundle)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
