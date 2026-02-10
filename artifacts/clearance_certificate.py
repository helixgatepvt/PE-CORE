def generate_clearance_certificate(clearance):
    return {
        "title": "Capital Clearance Opinion & Deployment Readiness Certification",
        "status": clearance["clearance_status"],
        "conditions": clearance.get("conditions", []),
        "issued_at": clearance.get("issued_at")
    }

