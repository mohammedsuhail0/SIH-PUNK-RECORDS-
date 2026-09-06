import os
import uuid
import datetime
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel

app = FastAPI(
    title="ArogyaMitr API — SIH 2026",
    description="Decentralized Dual-Outlet Rural Healthcare Platform (PS 26133)",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB = {
    "stats": {
        "today_triages": 28,
        "dispatched_prescriptions": 19,
        "active_emergency_sos": 1,
        "dark_store_stock_index": "96% Optimal",
        "avg_delivery_time": "18 Mins"
    },
    "patients": [
        {
            "id": "P-101",
            "abha_id": "91-4589-2041-3912",
            "name": "Sunita Madavi",
            "age": 24,
            "gender": "Female",
            "village": "Laheri",
            "district": "Gadchiroli",
            "symptoms": ["Pregnancy 32 Weeks", "Severe Fatigue", "Dizziness"],
            "condition": "High-Risk Pregnancy (Severe Anemia, Hb: 7.2 g/dL)",
            "risk_level": "High Risk",
            "vitals": {"bp": "95/60", "spo2": "97%", "pulse": 88, "temp": "98.6°F", "glucose": "105 mg/dL"},
            "timestamp": "2026-09-03T10:15:00Z",
            "status": "Doctor Consulted • Medicine Dispatched"
        },
        {
            "id": "P-102",
            "abha_id": "91-8842-1940-5511",
            "name": "Ramesh Atram",
            "age": 58,
            "gender": "Male",
            "village": "Bhamragad",
            "district": "Gadchiroli",
            "symptoms": ["Chest Heaviness", "High Blood Pressure", "Shortness of Breath"],
            "condition": "Hypertensive Crisis (BP: 175/105) with Cardiac Risk",
            "risk_level": "Emergency",
            "vitals": {"bp": "175/105", "spo2": "92%", "pulse": 104, "temp": "99.1°F", "glucose": "210 mg/dL"},
            "timestamp": "2026-09-03T11:00:00Z",
            "status": "108 Ambulance Dispatched"
        },
        {
            "id": "P-103",
            "abha_id": "91-3321-9087-4420",
            "name": "Anandi Gawade",
            "age": 34,
            "gender": "Female",
            "village": "Allapalli",
            "district": "Gadchiroli",
            "symptoms": ["High Fever", "Joint Pain", "Chills"],
            "condition": "Suspected Acute Plasmodium Vivax Malaria",
            "risk_level": "Moderate Risk",
            "vitals": {"bp": "120/80", "spo2": "98%", "pulse": 90, "temp": "103.2°F", "glucose": "115 mg/dL"},
            "timestamp": "2026-09-03T11:45:00Z",
            "status": "Diagnostic Blood Test Ordered at Hub"
        }
    ],
    "dark_store_inventory": [
        {"id": "MED-01", "name": "Oxytocin Injection (5 IU)", "category": "Maternal Emergency", "stock": 48, "min": 20, "unit": "Ampoules", "cold_chain": "2°C - 8°C", "status": "Adequate"},
        {"id": "MED-02", "name": "Human Insulin (Regular 40 IU)", "category": "Chronic / Diabetes", "stock": 25, "min": 15, "unit": "Vials", "cold_chain": "2°C - 8°C", "status": "Adequate"},
        {"id": "MED-03", "name": "Polyvalent Anti-Snake Venom (ASV)", "category": "Critical Emergency", "stock": 32, "min": 10, "unit": "Vials", "cold_chain": "2°C - 8°C", "status": "Adequate"},
        {"id": "MED-04", "name": "Amoxicillin + Clav 625mg", "category": "Antibiotic", "stock": 420, "min": 100, "unit": "Tablets", "cold_chain": "Room Temp", "status": "Adequate"},
        {"id": "MED-05", "name": "Artesunate + Lumefantrine (ACT)", "category": "Malaria Treatment", "stock": 180, "min": 50, "unit": "Courses", "cold_chain": "Room Temp", "status": "Adequate"},
        {"id": "TEST-01", "name": "Rapid Malaria Antigen (RDT) Kits", "category": "Diagnostic Testing", "stock": 210, "min": 50, "unit": "Kits", "cold_chain": "Room Temp", "status": "Adequate"},
        {"id": "TEST-02", "name": "Complete Blood Count (CBC) Vials", "category": "Diagnostic Testing", "stock": 95, "min": 30, "unit": "Vials", "cold_chain": "Room Temp", "status": "Adequate"}
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
            "destination_outlet": "Laheri Village Care Point",
            "status": "Dispatched (Runner ETA: 12 Mins)",
            "timestamp": "2026-09-03T10:30:00Z"
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
            "timestamp": "2026-09-03T11:05:00Z"
        }
    ]
}

class TriageInput(BaseModel):
    name: str
    age: int
    gender: str
    village: str
    district: str = "Gadchiroli"
    systolic_bp: int
    diastolic_bp: int
    spo2: int
    pulse: int
    temp: float = 98.6
    blood_glucose: Optional[int] = 110
    symptoms: List[str]

class PrescriptionInput(BaseModel):
    patient_id: str
    patient_name: str
    doctor_name: str = "Dr. Priya Kulkarni (Medical Officer)"
    medicines: List[str]
    diagnostic_tests: List[str] = []
    target_hub: str = "Aheri Outskirts Cluster Hub"
    destination_outlet: str = "Gram Care Point"

class SOSInput(BaseModel):
    patient_name: str
    village: str
    condition: str
    lat: float = 19.6542
    long: float = 80.3541

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
        risk_level = "Moderate Risk"
        reasons.append(f"Stage 1 Hypertension ({data.systolic_bp}/{data.diastolic_bp})")

    if data.spo2 < 92:
        risk_level = "Emergency"
        reasons.append(f"Severe Hypoxia (SpO2: {data.spo2}%)")
    elif data.spo2 < 95:
        if risk_level != "Emergency": risk_level = "Moderate Risk"
        reasons.append(f"Low Oxygenation (SpO2: {data.spo2}%)")

    if data.temp >= 102.5:
        if risk_level != "Emergency": risk_level = "Moderate Risk"
        reasons.append(f"High Pyrexia/Fever ({data.temp}°F)")

    if any(s.lower() in ["chest pain", "unconscious", "snake bite", "heavy bleeding", "breathlessness"] for s in data.symptoms):
        risk_level = "Emergency"
        reasons.append("Critical Red-Flag Symptom Flagged")

    p_id = f"P-{len(DB['patients']) + 101}"
    rand_uuid = uuid.uuid4().int
    abha_id = f"91-{str(rand_uuid)[:4]}-{str(rand_uuid)[4:8]}-{str(rand_uuid)[8:12]}"

    patient_record = {
        "id": p_id,
        "abha_id": abha_id,
        "name": data.name,
        "age": data.age,
        "gender": data.gender,
        "village": data.village,
        "district": data.district,
        "symptoms": data.symptoms,
        "condition": ", ".join(reasons) if reasons else "Routine Primary Health Checkup",
        "risk_level": risk_level,
        "vitals": {
            "bp": f"{data.systolic_bp}/{data.diastolic_bp}",
            "spo2": f"{data.spo2}%",
            "pulse": data.pulse,
            "temp": f"{data.temp}°F",
            "glucose": f"{data.blood_glucose} mg/dL" if data.blood_glucose else "N/A"
        },
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "status": "Triage Recorded • Awaiting Doctor / Dispatch"
    }

    DB["patients"].insert(0, patient_record)
    DB["stats"]["today_triages"] += 1
    return {"status": "success", "patient": patient_record, "risk_assessment": {"level": risk_level, "flags": reasons}}

@app.get("/api/inventory")
def get_inventory():
    return {
        "temperature": "4.2°C (Optimal Cold-Chain Active)",
        "solar_power_status": "100% Battery Backup",
        "items": DB["dark_store_inventory"]
    }

@app.get("/api/prescriptions")
def get_prescriptions():
    return DB["prescriptions"]

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
        "status": "Order Received at Hub • Packing in Progress (ETA: 18 Mins)",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }
    DB["prescriptions"].insert(0, record)
    DB["stats"]["dispatched_prescriptions"] += 1
    
    for p in DB["patients"]:
        if p["id"] == data.patient_id:
            p["status"] = f"Prescription #{rx_id} Dispatched from Outskirts Hub"
            break

    return {"status": "success", "prescription": record}

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
        "assigned_ambulance": "108-MH-33-EMS (Cluster Fast Responder)",
        "eta": "8 Mins",
        "status": "🚨 HIGH PRIORITY — Ambulance Dispatched",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }
    DB["emergency_sos"].insert(0, record)
    DB["stats"]["active_emergency_sos"] += 1
    return {"status": "success", "sos": record}

@app.get("/api/fhir/{patient_id}")
def export_fhir(patient_id: str):
    p = next((x for x in DB["patients"] if x["id"] == patient_id), None)
    if not p:
        raise HTTPException(status_code=404, detail="Patient not found")

    fhir_doc = {
        "resourceType": "Bundle",
        "id": f"bundle-{p['id']}",
        "type": "document",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "identifier": {
            "system": "https://healthid.abdm.gov.in",
            "value": p["abha_id"]
        },
        "entry": [
            {
                "fullUrl": f"urn:uuid:{p['id']}-patient",
                "resource": {
                    "resourceType": "Patient",
                    "id": p["id"],
                    "identifier": [{"system": "https://healthid.abdm.gov.in", "value": p["abha_id"]}],
                    "name": [{"use": "official", "text": p["name"]}],
                    "gender": p["gender"].lower(),
                    "address": [{"city": p["village"], "state": "Maharashtra", "country": "IND"}]
                }
            },
            {
                "fullUrl": f"urn:uuid:{p['id']}-condition",
                "resource": {
                    "resourceType": "Condition",
                    "clinicalStatus": {"text": "Active"},
                    "verificationStatus": {"text": "Confirmed"},
                    "code": {"text": p["condition"]},
                    "subject": {"reference": f"Patient/{p['id']}"}
                }
            },
            {
                "fullUrl": f"urn:uuid:{p['id']}-vitals",
                "resource": {
                    "resourceType": "Observation",
                    "status": "final",
                    "code": {"text": "Frontline Vital Signs"},
                    "component": [
                        {"code": {"text": "Blood Pressure"}, "valueString": p["vitals"]["bp"]},
                        {"code": {"text": "Pulse Oximetry"}, "valueString": p["vitals"]["spo2"]},
                        {"code": {"text": "Body Temperature"}, "valueString": p["vitals"]["temp"]}
                    ]
                }
            }
        ]
    }
    return fhir_doc
