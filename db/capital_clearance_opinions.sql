create table capital_clearance_opinions (
  ccm_id uuid primary key default gen_random_uuid(),
  deal_id text not null,
  snapshot_id uuid not null references decision_snapshots(snapshot_id),
  clearance_status text not null
    check (clearance_status in ('CLEARED','CONDITIONAL','NOT_CLEARED')),
  conditions jsonb,
  accepted_risks jsonb,
  unresolved_constraints jsonb,
  deployed_capital_amount numeric not null,
  engine_version_hash text not null,
  issued_at timestamp with time zone default now()
);

