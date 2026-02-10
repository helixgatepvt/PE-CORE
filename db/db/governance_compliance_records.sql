create table governance_compliance_records (
  compliance_id uuid primary key default gen_random_uuid(),
  mandate_id uuid not null references governance_mandates(mandate_id),
  snapshot_id uuid not null references decision_snapshots(snapshot_id),
  compliance_status text not null
    check (compliance_status in ('COMPLIANT','NON_COMPLIANT')),
  violations jsonb,
  evaluated_at timestamp with time zone default now()
);
